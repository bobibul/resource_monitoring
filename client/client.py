import sys
import psutil
from py3nvml import py3nvml
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer, QTime, QDateTime, Signal, QObject
from PySide6.QtNetwork import QTcpSocket
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QIcon
import subprocess
from ui_clientwindow import Ui_ClientWindow
import json
from concurrent.futures import ThreadPoolExecutor
import logging
import struct

# 로그 레벨 설정
logging.basicConfig(level=logging.ERROR)

class ClientWindow(QMainWindow):
    connectionResult = Signal(bool, str)  # 연결 결과를 전달할 시그널

    def __init__(self):
        super().__init__()
        self.ui = Ui_ClientWindow()
        self.setWindowIcon(QIcon('client_icon.ico'))
        self.ui.setupUi(self)  # UI 설정

        self.tcpSocket = QTcpSocket(self)
        self.timer = QTimer(self)
        self.timer.setInterval(1000)  # 1초 간격으로 업데이트
        self.timeValue = QTime(0, 0, 0)

        self.ui.connect.clicked.connect(self.connectToServer)
        self.ui.onButton.clicked.connect(self.sendOnMessage)
        self.ui.offButton.clicked.connect(self.sendOffMessage)
        self.ui.programSearchButton.clicked.connect(self.openFileDialog)
        self.timer.timeout.connect(self.updateDisplay)

        self.ui.onButton.setEnabled(True)
        self.ui.offButton.setEnabled(False)

        self.computing_resources = [0] * 7  # CPU, GPU0, GPU1, GPU2, Memory, Time, program_name

        self.connecting_state = False

        self.executor = ThreadPoolExecutor(max_workers=3)

        self.loadSettings()  # 설정 로드 및 UI 초기화
        self.gpuSetting()
        self.progressBarSetting()

    def openFileDialog(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(
            None, 
            "Select Program", 
            "", 
            "Executable Files (*.exe);;All Files (*)"
        )
        if file_path:
            self.ui.program_path.setText(file_path)

    def loadSettings(self):
        try:
            with open('_internal/config.json', 'r') as f:
                config = json.load(f)
                self.ui.client_name.setText(config.get("client_name", ""))
                self.ui.IP_address.setText(config.get("server_address", ""))
                self.ui.program_path.setText(config.get("program_path", ""))
                self.ui.server_port.setText(str(config.get("port_number", 0)))
                self.ui.start_time.setText(config.get("start_time", ""))
                self.ui.end_time.setText(config.get("end_time", ""))
                self.ui.current_state.append("설정이 로드되었습니다.")
        except FileNotFoundError:
            self.ui.current_state.append("설정 파일을 찾을 수 없습니다. 기본 설정을 사용합니다.")

    def saveSettings(self):
        config = {
            "client_name": self.ui.client_name.text(),
            "server_address": self.ui.IP_address.text(),
            "program_path": self.ui.program_path.text(),
            "port_number": int(self.ui.server_port.text()),
            "start_time": self.ui.start_time.text(),
            "end_time": self.ui.end_time.text()
        }
        with open('_internal/config.json', 'w') as f:
            json.dump(config, f, indent=4)


    def connectToServer(self):
        serverAddress = self.ui.IP_address.text()
        port = int(self.ui.server_port.text())
        self.tcpSocket.connectToHost(serverAddress, port)
        if self.tcpSocket.waitForConnected(3000):
            self.ui.current_state.append("서버에 연결되었습니다.")
            self.tcpSocket.readyRead.connect(self.receiveMessage)
            
        else:
            error_message = "서버에 연결하지 못했습니다: " + self.tcpSocket.errorString()
            self.ui.current_state.append(error_message)
 

    def sendOnMessage(self):
        self.timer.start()
        self.ui.onButton.setEnabled(False)
        self.ui.offButton.setEnabled(True)
        self.startKakaoTalk()

        currentTime = QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")
        self.ui.current_state.append(currentTime + " 장치 켜짐")
        self.ui.start_time.setText(currentTime)

        # JSON 파일에 변경된 정보 저장
        self.saveSettings()

    def sendOffMessage(self):
        self.timer.stop()
        self.timeValue.setHMS(0, 0, 0)

        self.offKakaoTalk()

        timeText = self.timeValue.toString("HH:mm:ss")
        self.ui.current_time.setText(timeText)

        self.ui.onButton.setEnabled(True)
        self.ui.offButton.setEnabled(False)

        currentTime = QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")
        self.ui.current_state.append(currentTime + " 장치 꺼짐")
        self.ui.end_time.setText(currentTime)

        # JSON 파일에 변경된 정보 저장
        self.saveSettings()

    def receiveMessage(self):
        print("receiveMessage")
        while self.tcpSocket.bytesAvailable():
            data = self.tcpSocket.readAll().data()
            message = data.decode('utf-8')
            self.ui.current_state.append(f"서버에서 수신한 메시지: {message}")

            if message == "on":
                self.sendOnMessage()
            elif message == "off":
                self.sendOffMessage()

    def updateDisplay(self):
        self.timeValue = self.timeValue.addSecs(1)
        self.computing_resources[5] = self.QTimeToDouble(self.timeValue)
        timeText = self.timeValue.toString("HH:mm:ss")

        # CPU, GPU, 메모리 사용량 업데이트
        self.executor.submit(self.getCPUUsage)
        self.executor.submit(self.getGPUUsage)
        self.executor.submit(self.getMemoryUsage)

        # UI 업데이트 최소화
        self.ui.current_time.setText(timeText)
        self.ui.cpu_usage.setText(f"{self.computing_resources[0]:.1f}")
        self.ui.gpu0_usage.setText(f"{self.computing_resources[1]:.1f}")
        self.ui.gpu1_usage.setText(f"{self.computing_resources[2]:.1f}")
        self.ui.gpu2_usage.setText(f"{self.computing_resources[3]:.1f}")
        self.ui.memory_usage_per.setText(f"{self.computing_resources[4]:.1f}")

        # ProgressBar 업데이트
        self.progressBarSetting()

        # 리소스 전송
        self.sendComputingResource()

    def gpuSetting(self):
        py3nvml.nvmlInit()
        device_count = py3nvml.nvmlDeviceGetCount()
        if device_count > 0:
            for i in range(device_count):
                handle = py3nvml.nvmlDeviceGetHandleByIndex(i)
                name = py3nvml.nvmlDeviceGetName(handle)
                self.ui.current_state.append(f"GPU {i} name: {name}")
                if i == 0:
                    self.ui.gpu0_name.setText(name)
                elif i == 1:
                    self.ui.cpu_name_6.setText(name)
                elif i == 2:
                    self.ui.cpu_name_12.setText(name)
        else:
            self.ui.current_state.append("No GPU found")
        py3nvml.nvmlShutdown()

    def getCPUUsage(self):
        self.computing_resources[0] = psutil.cpu_percent(interval=1)

    def getGPUUsage(self):
        try:
            py3nvml.nvmlInit()
            device_count = py3nvml.nvmlDeviceGetCount()
            for i in range(device_count):
                handle = py3nvml.nvmlDeviceGetHandleByIndex(i)
                utilization = py3nvml.nvmlDeviceGetUtilizationRates(handle)
                self.computing_resources[i + 1] = utilization.gpu
        except Exception as e:
            logging.error(f"Error getting GPU usage: {e}")
        finally:
            py3nvml.nvmlShutdown()

    def getMemoryUsage(self):
        memory_info = psutil.virtual_memory()
        self.computing_resources[4] = memory_info.percent

    def sendComputingResource(self):
        # 모든 값을 문자열로 변환하고 콤마로 구분
        data_string = ','.join(str(value) for value in self.computing_resources)
        data_string += '\n'

        # 문자열을 UTF-8로 인코딩하여 전송
        data = data_string.encode('utf-8')
        self.tcpSocket.write(data)
        self.tcpSocket.flush()

    def progressBarSetting(self):
        self.ui.cpu_progressBar.setValue(self.computing_resources[0])
        self.ui.gpu0_progressBar.setValue(self.computing_resources[1])
        self.ui.gpu1_progressBar.setValue(self.computing_resources[2])
        self.ui.gpu2_progressBar.setValue(self.computing_resources[3])
        self.ui.memory_progressBar.setValue(self.computing_resources[4])
        self.computing_resources[6] = self.ui.client_name.text()

    def QTimeToDouble(self, time):
        return time.hour() * 3600 + time.minute() * 60 + time.second() + time.msec() / 1000.0

    def startKakaoTalk(self):
        kakaotalkFilePath = self.ui.program_path.text()
        subprocess.Popen([kakaotalkFilePath], creationflags=subprocess.CREATE_NO_WINDOW)

    def offKakaoTalk(self):
        program_name = self.ui.program_path.text().split('/')[-1] 
        subprocess.run(["taskkill", "/F", "/IM", program_name], creationflags=subprocess.CREATE_NO_WINDOW)

    def closeEvent(self, event):
        self.saveSettings()  # 프로그램 종료 시 설정 저장
        super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('client_icon.ico'))
    window = ClientWindow()
    window.show()
    sys.exit(app.exec())
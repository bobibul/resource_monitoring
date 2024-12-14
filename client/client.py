import sys
import psutil
from py3nvml import py3nvml
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer, QTime, QDateTime
from PySide6.QtNetwork import QTcpSocket
from PySide6.QtGui import QIcon
from ui_clientwindow import Ui_ClientWindow
from concurrent.futures import ThreadPoolExecutor
import json
import atexit
import os


class ClientWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ClientWindow()
        self.ui.setupUi(self)  # UI 설정

        self.tcpSocket = QTcpSocket(self)
        self.timer = QTimer(self)
        self.timer.setInterval(1000)  # 1초 간격으로 업데이트
        self.timeValue = QTime(0, 0, 0)

        self.ui.connect.clicked.connect(self.connectToServer)
        self.timer.timeout.connect(self.updateDisplay) # 1초마다 디스플레이 업데이트, 서버 연결 상태 시 리소스 전송

        self.computing_resources = [0] * 9  # elapsed_time, cpu, memory, gpu0, gpu1, gpu2, gpu3, gpu4, gpu5

        self.connecting_state = False
        self.connectToServer()

        self.executor = ThreadPoolExecutor(max_workers=3)

        self.loadSettings()  # 설정 로드 및 UI 초기화
        self.gpuSetting() # gpu 이름 및 nvml 시작하기
        self.progressBarSetting() # progressBar 연동되는거 설정
        self.timer_start() # 타이머 시작

        atexit.register(self.saveSettings) # 프로그램 종료 시 호출

    def loadSettings(self):
        try:
            with open('config.json', 'r') as f:
                config = json.load(f)
                self.ui.client_name.setText(config.get("client_name", ""))
                self.ui.IP_address.setText(config.get("server_address", ""))
                self.ui.current_state.append("설정이 로드되었습니다.")
        except FileNotFoundError:
            self.ui.current_state.append("설정 파일을 찾을 수 없습니다. 기본 설정을 사용합니다.")

    def saveSettings(self):
        config = {
            "client_name": self.ui.client_name.text(),
            "server_address": self.ui.IP_address.text(),
        }
        with open('config.json', 'w') as f:
            json.dump(config, f, indent=4)


    def connectToServer(self):
        serverAddress = self.ui.IP_address.text()
        port = 8095
        self.tcpSocket.connectToHost(serverAddress, port)
        if self.tcpSocket.waitForConnected(500):
            self.ui.current_state.append("서버에 연결되었습니다.")
            self.tcpSocket.readyRead.connect(self.receiveMessage)
            self.connecting_state = True
            
        else:
            error_message = "서버에 연결하지 못했습니다: " + self.tcpSocket.errorString()
            self.ui.current_state.append(error_message)
 

    def timer_start(self):
        self.timer.start()
        currentTime = QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")
        self.ui.current_state.append(currentTime + " 장치 켜짐")
        self.ui.start_time.setText(currentTime)


    def receiveMessage(self):
        print("receiveMessage")
        while self.tcpSocket.bytesAvailable():
            data = self.tcpSocket.readAll().data()
            message = data.decode('utf-8')
            self.ui.current_state.append(f"서버에서 수신한 메시지: {message}")

            if message == "off":
                # print("off_system")
                os.system("shutdown /s /t 1")

    def updateDisplay(self):
        self.timeValue = self.timeValue.addSecs(1)
        self.computing_resources[0] = self.QTimeToDouble(self.timeValue)

        # CPU, GPU, 메모리 사용량 업데이트
        self.executor.submit(self.getCPUUsage)
        self.executor.submit(self.getGPUUsage)
        self.executor.submit(self.getMemoryUsage)

        # UI 업데이트 최소화
        self.ui.current_time.setText(self.timeValue.toString("HH:mm:ss"))
        self.ui.cpu_usage.setText(f"{self.computing_resources[1]:.1f}")
        self.ui.mem_usage.setText(f"{self.computing_resources[2]:.1f}")
        self.ui.gpu_usage_0.setText(f"{self.computing_resources[3]:.1f}")
        self.ui.gpu_usage_1.setText(f"{self.computing_resources[4]:.1f}")
        self.ui.gpu_usage_2.setText(f"{self.computing_resources[5]:.1f}")
        self.ui.gpu_usage_3.setText(f"{self.computing_resources[6]:.1f}")
        self.ui.gpu_usage_4.setText(f"{self.computing_resources[7]:.1f}")
        self.ui.gpu_usage_5.setText(f"{self.computing_resources[8]:.1f}")
        
        # ProgressBar 업데이트
        self.progressBarSetting()

        if(self.connecting_state) : self.sendComputingResource()

    def gpuSetting(self):
        py3nvml.nvmlInit()
        device_count = py3nvml.nvmlDeviceGetCount()
        if device_count > 0:
            for i in range(device_count):
                handle = py3nvml.nvmlDeviceGetHandleByIndex(i)
                name = py3nvml.nvmlDeviceGetName(handle)
                gpu_label = getattr(self.ui, f"gpu_name_{i}")
                gpu_label.setText(name)
                self.ui.current_state.append(f"GPU {i} name: {name}")

        else:   
            self.ui.current_state.append("No GPU found")

    def getCPUUsage(self):
        self.computing_resources[1] = psutil.cpu_percent(interval=1)

    def getGPUUsage(self):
            device_count = py3nvml.nvmlDeviceGetCount()
            for i in range(device_count):
                handle = py3nvml.nvmlDeviceGetHandleByIndex(i)
                utilization = py3nvml.nvmlDeviceGetUtilizationRates(handle)
                self.computing_resources[i + 3] = utilization.gpu

    def getMemoryUsage(self):
        memory_info = psutil.virtual_memory()
        self.computing_resources[2] = memory_info.percent

    def sendComputingResource(self):
        # 모든 값을 문자열로 변환하고 콤마로 구분
        data_string = ','.join(str(value) for value in self.computing_resources)
        data_string += '\n'

        # 문자열을 UTF-8로 인코딩하여 전송
        data = data_string.encode('utf-8')
        self.tcpSocket.write(data)
        self.tcpSocket.flush()

    def progressBarSetting(self):
        self.ui.cpu_progressBar.setValue(self.computing_resources[1])
        self.ui.memory_progressbar.setValue(self.computing_resources[2])

        self.ui.gpu_progressbar_0.setValue(self.computing_resources[3])
        self.ui.gpu_progressbar_1.setValue(self.computing_resources[4])
        self.ui.gpu_progressbar_2.setValue(self.computing_resources[5])
        self.ui.gpu_progressbar_3.setValue(self.computing_resources[6])
        self.ui.gpu_progressbar_4.setValue(self.computing_resources[7])
        self.ui.gpu_progressbar_5.setValue(self.computing_resources[8])
        

    def QTimeToDouble(self, time):
        return time.hour() * 3600 + time.minute() * 60 + time.second() + time.msec() / 1000.0
    



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('client_icon.ico'))
    window = ClientWindow()
    window.show()
    sys.exit(app.exec())
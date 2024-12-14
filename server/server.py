
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTime, QTimer
from PySide6.QtNetwork import QTcpServer, QHostAddress
from PySide6.QtWidgets import (QApplication, QMainWindow)
from ui_serverwindow import Ui_ServerWindow

import socket
import subprocess
import ctypes
import sys
import json

class Device:
    def __init__(self):
        self.on_state = True
        self.data_list = ["0", "0", "0", "0", "0", "0", "0", "0", "0"] 
        # Elapsed_time, cpu, mem, gpu0, gpu1, gpu2, gpu3, gpu4, gpu5

        self.ipLabel = None
        self.elapsedTimeLabel = None

        self.cpuLabel = None
        self.memoryLabel = None

        self.gpu0Label = None
        self.gpu1Label = None
        self.gpu2Label = None
        self.gpu3Label = None
        self.gpu4Label = None
        self.gpu5Label = None

        self.onOffButton = None
        self.clientSocket = None
        self.ip_address = None

    def update(self, data):
        values = data.split(',')
        for i, val in enumerate(values):
            self.data_list[i] = val



class ServerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ServerWindow()
        self.ui.setupUi(self)

        server_ip = self.server_ip = self.get_local_ip()
        self.ui.serverIPLabel.setText(f"Server IP: {server_ip}")

        # 서버 설정
        self.tcpServer = QTcpServer(self)
        self.devices = {}
        self.buffers = {}

        self.startServer()

        # QTimer 설정
        self.timer = QTimer(self)
        self.timer.setInterval(1000)  # 1초 간격으로 설정
        self.timer.timeout.connect(self.update_window)  
        self.timer.start()  # 타이머 시작

    def get_local_ip(self):
        # 임의의 외부 주소로 소켓을 연결하여 로컬 IP 주소를 가져옵니다.
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # 연결할 필요는 없지만, 외부 주소로 소켓을 설정하여 로컬 IP를 알아냅니다.
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
        finally:
            s.close()
        return local_ip
    

    def startServer(self):
        if self.tcpServer.listen(QHostAddress.Any, 8095):
            self.ui.textEdit.append("Server started")
        else:
            self.ui.textEdit.append("Server start failed")
        self.tcpServer.newConnection.connect(self.clientConnect)

    def clientConnect(self):
        clientSocket = self.tcpServer.nextPendingConnection()
        client_ip = clientSocket.peerAddress().toString().split(":")[-1]

        self.buffers[client_ip] = ""
        self.ui.textEdit.append(f"Connected: {client_ip}")

        clientSocket.readyRead.connect(self.update_status)
        clientSocket.disconnected.connect(self.clientDisconnected)

        if client_ip not in self.devices:
            self.devices[client_ip] = Device()
            self.devices[client_ip].ip_address = client_ip
            self.devices[client_ip].clientSocket = clientSocket
            self.ui.addDeviceWidget(client_ip, self.devices[client_ip])
            self.devices[client_ip].onOffButton.clicked.connect(lambda : self.sendMessageToClient(client_ip))

    def clientDisconnected(self):
        clientSocket = self.sender()
        client_ip = clientSocket.peerAddress().toString().split(":")[-1]
        self.clear_layout(self.devices[client_ip].layout)
        self.removeLine(self.devices[client_ip])
        self.ui.verticalLayout_2.removeWidget(self.devices[client_ip].line)
        self.ui.verticalLayout_2.update()

        self.ui.textEdit.append(f"disConnected: {client_ip}")

        del self.devices[client_ip]

    def removeLine(self, device):
        # line 위젯을 레이아웃에서 제거
        self.ui.verticalLayout_2.removeWidget(device.line)
        # line 위젯을 메모리에서 삭제
        device.line.deleteLater()
    

    
    def clear_layout(self, layout):
        """특정 행 레이아웃의 모든 요소를 삭제합니다."""
        
        while layout.count():
            # 아이템 제거
            item = layout.takeAt(0)

            # 위젯이 있으면 삭제
            if item.widget():
                layout.removeWidget(item.widget())
                #item.widget().deleteLater()

            # 하위 레이아웃이 있으면 재귀적으로 삭제
            if item.layout():
                self.clear_layout(item.layout())

        # 최종적으로 레이아웃에서 모든 참조 해제
        layout.deleteLater()
        

    def update_status(self):
        clientSocket = self.sender()
        client_ip = clientSocket.peerAddress().toString().split(":")[-1]

        raw_data = clientSocket.readAll().data().decode('utf-8')
        self.buffers[client_ip] += raw_data


        if '\n' in self.buffers[client_ip]:
            data = self.buffers[client_ip].split('\n')[0]
            self.devices[client_ip].update(data)
            self.buffers[client_ip] = self.buffers[client_ip].split('\n')[1]


    def update_window(self):
        for client_ip, device in self.devices.items():
            self.updateDeviceWidget(device)

    def strToTime(self, time):
        return QTime(0, 0, float(time)).toString("hh:mm:ss")

    def updateDeviceWidget(self, device):
        device.elapsedTimeLabel.setText(self.strToTime(device.data_list[0]))
        device.cpuLabel.setText(device.data_list[1] + "%")
        device.memoryLabel.setText(device.data_list[2] + "%")
        device.gpu0Label.setText(device.data_list[3] + "%")
        device.gpu1Label.setText(device.data_list[4] + "%")
        device.gpu2Label.setText(device.data_list[5] + "%")
        device.gpu3Label.setText(device.data_list[6] + "%")
        device.gpu4Label.setText(device.data_list[7] + "%")
        device.gpu5Label.setText(device.data_list[8] + "%")

    def sendMessageToClient(self, client_ip):
        clientSocket = self.devices[client_ip].clientSocket
        data = "off".encode('utf-8')
        clientSocket.write(data)
        clientSocket.flush()

def open_firewall_port(port, protocol='TCP'):
    try:
        # 인바운드 규칙 추가
        subprocess.run(
            ["netsh", "advfirewall", "firewall", "add", "rule",
             f"name=Open Port {port}", f"dir=in", f"action=allow",
             f"protocol={protocol}", f"localport={port}"],
            check=True,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        print(f"Port {port} opened successfully for {protocol} traffic.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to open port {port}: {e}")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if __name__ == "__main__":
    if is_admin():
        open_firewall_port(8095, 'TCP')
        app = QApplication(sys.argv)
        window = ServerWindow()
        window.show()
        sys.exit(app.exec())
    else:
        print("Re-launching as admin...")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

    
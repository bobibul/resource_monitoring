import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QScrollArea
from PySide6.QtCore import QTime, QTimer
from PySide6.QtNetwork import QTcpServer, QTcpSocket, QHostAddress
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QScrollArea, QSizePolicy,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)
from PySide6.QtWidgets import QLabel, QPushButton, QHBoxLayout, QWidget, QFrame
from PySide6.QtGui import QFont
import socket
import subprocess
import ctypes
import sys

class Device:
    def __init__(self):
        self.data_list = ["0", "0", "0", "0", "0", "0", ""] # CPU, GPU0, GPU1, GPU2, Memory, Elapsed Time, Program

        self.ipLabel = None
        self.programLabel = None
        self.cpuLabel = None
        self.gpu0Label = None
        self.gpu1Label = None
        self.gpu2Label = None
        self.memoryLabel = None
        self.elapsedTimeLabel = None
        self.onOffButton = None
        self.clientSocket = None

        self.ip_address = None

    def update(self, data):
        values = data.split(',')
        for i, val in enumerate(values):
            self.data_list[i] = val

        self.program_name = values[6]


class ServerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('server_icon.png'))
        self.setWindowTitle("Server Window")

        self.resize(1300, 800)
        self.setStyleSheet("background-color: rgb(75, 75, 75);")

        # UI 설정
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.verticalLayout = QVBoxLayout(self.centralwidget)

        # 열 이름 설정
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setMaximumHeight(50)
        self.scrollArea.setMinimumWidth(900)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea.setWidgetResizable(True)

        self.columnLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        # 열 이름 추가
        self.addColumnNames()

        # 스크롤 영역 설정
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea.setWidgetResizable(True)
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setAlignment(Qt.AlignTop)
        self.verticalLayout.addWidget(self.scrollArea)

        # 텍스트 에디트
        self.textEdit = QTextEdit(self.centralwidget)
        self.verticalLayout.addWidget(self.textEdit)
        self.textEdit.setStyleSheet("color: white;")
        self.textEdit.setMaximumSize(QSize(16777215, 100))

        # 서버 IP 주소 및 포트 번호 표시
        server_ip = self.get_local_ip()
        self.serverIPLabel = QLabel(f"Server IP: {server_ip}", self.centralwidget)
        self.serverIPLabel.setStyleSheet("color: white;")
        self.verticalLayout.addWidget(self.serverIPLabel)
        

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
    
    def addColumnNames(self):
        from PySide6.QtWidgets import QLabel
        from PySide6.QtGui import QFont

        # 폰트 설정
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)

        # 스타일 시트 설정 (폰트 색상 변경)
        style_sheet = "color: white;"

        # 열 이름 리스트
        column_names = ["IP", "Program", "CPU", "GPU0", "GPU1", "GPU2", "Memory", "Elapsed Time", "On/Off"]

        for name in column_names:
            label = QLabel(name)
            label.setFont(font)
            label.setStyleSheet(style_sheet)
            label.setAlignment(Qt.AlignCenter)
            self.columnLayout.addWidget(label)

        # 열 이름 사이에 구분선 추가
        for i in range(len(column_names) - 1):
            separator = QFrame()
            separator.setFrameShape(QFrame.VLine)
            separator.setFrameShadow(QFrame.Sunken)
            self.columnLayout.insertWidget(2 * i + 1, separator)

    def startServer(self):
        if self.tcpServer.listen(QHostAddress.Any, 8095):
            self.textEdit.append("Server started")
        else:
            self.textEdit.append("Server start failed")
        self.tcpServer.newConnection.connect(self.clientConnect)

    def clientConnect(self):
        clientSocket = self.tcpServer.nextPendingConnection()
        client_ip = clientSocket.peerAddress().toString().split(":")[-1]

        self.buffers[client_ip] = ""

        self.textEdit.append(f"Connected: {client_ip}")

        clientSocket.readyRead.connect(self.update_status)
        clientSocket.disconnected.connect(self.clientDisconnected)

        if client_ip not in self.devices:
            self.devices[client_ip] = Device()
            self.devices[client_ip].ip_address = client_ip
            self.devices[client_ip].clientSocket = clientSocket
            self.addDeviceWidget(client_ip, self.devices[client_ip])

    def clientDisconnected(self):
        clientSocket = self.sender()
        client_ip = clientSocket.peerAddress().toString()
        if client_ip in self.devices:
            del self.devices[client_ip]

        if clientSocket:
            clientSocket.deleteLater()

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
        device.cpuLabel.setText(device.data_list[0] + "%")
        device.gpu0Label.setText(device.data_list[1] + "%")
        device.gpu1Label.setText(device.data_list[2] + "%")
        device.gpu2Label.setText(device.data_list[3] + "%")
        device.memoryLabel.setText(device.data_list[4] + "%")
        device.elapsedTimeLabel.setText(self.strToTime(device.data_list[5]))
        device.programLabel.setText(device.data_list[6])

    def sendMessageToClient(self, clientSocket):
        data = "off".encode('utf-8')
        clientSocket.write(data)
        clientSocket.flush()

    def addDeviceWidget(self, ip="192.168.1.1", device = Device()):
        font = QFont()
        font.setPointSize(12)  # 폰트 크기 설정

        # 스타일 시트 설정 (폰트 색상 변경)
        style_sheet = "color: white;"

        # 새로운 위젯 컨테이너
        deviceWidget = QWidget(self.scrollAreaWidgetContents)
        deviceWidget.setMaximumHeight(50)
        deviceWidget.setMinimumWidth(1000)
        layout = QHBoxLayout(deviceWidget)


        def addSeparator():
            separator = QFrame(deviceWidget)
            separator.setFrameShape(QFrame.VLine)
            separator.setFrameShadow(QFrame.Sunken)
            layout.addWidget(separator)

        # IP 주소
        device.ipLabel = QLabel(str(ip), deviceWidget)
        device.ipLabel.setFont(font)
        device.ipLabel.setStyleSheet(style_sheet)
        device.ipLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(device.ipLabel)

        addSeparator()

        # 실행 중 프로그램
        device.programLabel = QLabel(f"program_name", deviceWidget)
        device.programLabel.setFont(font)
        device.programLabel.setStyleSheet(style_sheet)
        device.programLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(device.programLabel)

        addSeparator()

        # CPU 사용량
        device.cpuLabel = QLabel("0%", deviceWidget)
        device.cpuLabel.setFont(font)
        device.cpuLabel.setStyleSheet(style_sheet)
        device.cpuLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(device.cpuLabel)

        addSeparator()

        # GPU0 사용량
        device.gpu0Label = QLabel("0%", deviceWidget)
        device.gpu0Label.setFont(font)
        device.gpu0Label.setStyleSheet(style_sheet)
        device.gpu0Label.setAlignment(Qt.AlignCenter)
        layout.addWidget(device.gpu0Label)

        addSeparator()

        # GPU1 사용량
        device.gpu1Label = QLabel("0%", deviceWidget)
        device.gpu1Label.setFont(font)
        device.gpu1Label.setStyleSheet(style_sheet)
        device.gpu1Label.setAlignment(Qt.AlignCenter)
        layout.addWidget(device.gpu1Label)

        addSeparator()

        # GPU2 사용량
        device.gpu2Label = QLabel("0%", deviceWidget)
        device.gpu2Label.setFont(font)
        device.gpu2Label.setStyleSheet(style_sheet)
        device.gpu2Label.setAlignment(Qt.AlignCenter)
        layout.addWidget(device.gpu2Label)

        addSeparator()

        # 메모리 사용량
        device.memoryLabel = QLabel("0%", deviceWidget)
        device.memoryLabel.setFont(font)
        device.memoryLabel.setStyleSheet(style_sheet)
        device.memoryLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(device.memoryLabel)

        addSeparator()

        # 경과된 시간
        device.elapsedTimeLabel = QLabel("00:00:00", deviceWidget)
        device.elapsedTimeLabel.setFont(font)
        device.elapsedTimeLabel.setStyleSheet(style_sheet)
        device.elapsedTimeLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(device.elapsedTimeLabel)

        addSeparator()

        # On/Off 버튼
        device.onOffButton = QPushButton("Off", deviceWidget)
        device.onOffButton.setFont(font)
        device.onOffButton.setStyleSheet(style_sheet)
        device.onOffButton.clicked.connect(lambda: self.sendMessageToClient(device.clientSocket))
        layout.addWidget(device.onOffButton)


        # 스크롤 영역의 맨 위에 위젯 추가
        self.verticalLayout_2.insertWidget(0, deviceWidget)

        # 행 구분선 추가
        line = QFrame(self.scrollAreaWidgetContents)
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet("background-color: rgb(200, 200, 200);")
        line.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_2.insertWidget(1, line)

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

    
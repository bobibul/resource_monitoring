from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QScrollArea
from PySide6.QtCore import QTime, QTimer
from PySide6.QtNetwork import QTcpServer, QTcpSocket, QHostAddress
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import QSize, QTime, Qt
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QScrollArea, QSizePolicy,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)
from PySide6.QtWidgets import QLabel, QPushButton, QHBoxLayout, QWidget, QFrame
from PySide6.QtGui import QFont

class Ui_ServerWindow:
    def setupUi(self, MainWindow):
        MainWindow.setWindowIcon(QIcon('server_icon.png'))
        MainWindow.setWindowTitle("Server Window")

        MainWindow.resize(1300, 800)
        MainWindow.setStyleSheet("background-color: rgb(75, 75, 75);")

        # UI 설정
        self.centralwidget = QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
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
        self.serverIPLabel = QLabel(self.centralwidget)
        self.serverIPLabel.setStyleSheet("color: white;")
        self.verticalLayout.addWidget(self.serverIPLabel)

        self.startServerButton = QPushButton("서버 시작", self.centralwidget)
        self.startServerButton.setFont(QFont())
        self.startServerButton.setStyleSheet("color: white;")
        self.verticalLayout.addWidget(self.startServerButton)

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
        column_names = ["IP", "Elapsed Time", "CPU", "Memory", "GPU0", "GPU1", "GPU2", "GPU3", "GPU4", "GPU5", "On/Off"]

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

    def addDeviceWidget(self, ip="192.168.1.1", device=None):
        font = QFont()
        font.setPointSize(17)  # 폰트 크기 설정

        # 스타일 시트 설정 (폰트 색상 변경)
        style_sheet = "color: white;"

        # 새로운 위젯 컨테이너
        device.deviceWidget = QWidget(self.scrollAreaWidgetContents)
        device.deviceWidget.setMaximumHeight(50)
        device.deviceWidget.setMinimumWidth(1000)
        
        device.layout = QHBoxLayout(device.deviceWidget)
        def addSeparator():
            separator = QFrame(device.deviceWidget)
            separator.setFrameShape(QFrame.VLine)
            separator.setFrameShadow(QFrame.Sunken)
            device.layout.addWidget(separator)

        # IP 주소
        device.ipLabel = QLabel(str(ip), device.deviceWidget)
        ip_font = QFont()
        ip_font.setPointSize(11)
        device.ipLabel.setFont(ip_font)
        device.ipLabel.setStyleSheet(style_sheet)
        device.ipLabel.setAlignment(Qt.AlignCenter)
        device.layout.addWidget(device.ipLabel)

        addSeparator()

        # 경과된 시간
        device.elapsedTimeLabel = QLabel("00:00:00", device.deviceWidget)
        ip_font = QFont()
        ip_font.setPointSize(12)
        device.elapsedTimeLabel.setFont(ip_font)
        device.elapsedTimeLabel.setStyleSheet(style_sheet)
        device.elapsedTimeLabel.setAlignment(Qt.AlignCenter)
        device.layout.addWidget(device.elapsedTimeLabel)

        addSeparator()

        # CPU 사용량
        device.cpuLabel = QLabel("0%", device.deviceWidget)
        device.cpuLabel.setFont(font)
        device.cpuLabel.setStyleSheet(style_sheet)
        device.cpuLabel.setAlignment(Qt.AlignCenter)
        device.layout.addWidget(device.cpuLabel)

        addSeparator()

        # 메모리 사용량
        device.memoryLabel = QLabel("0%", device.deviceWidget)
        device.memoryLabel.setFont(font)
        device.memoryLabel.setStyleSheet(style_sheet)
        device.memoryLabel.setAlignment(Qt.AlignCenter)
        device.layout.addWidget(device.memoryLabel)

        addSeparator()

        # GPU0 사용량
        device.gpu0Label = QLabel("0%", device.deviceWidget)
        device.gpu0Label.setFont(font)
        device.gpu0Label.setStyleSheet(style_sheet)
        device.gpu0Label.setAlignment(Qt.AlignCenter)
        device.layout.addWidget(device.gpu0Label)

        addSeparator()

        # GPU1 사용량
        device.gpu1Label = QLabel("0%", device.deviceWidget)
        device.gpu1Label.setFont(font)
        device.gpu1Label.setStyleSheet(style_sheet)
        device.gpu1Label.setAlignment(Qt.AlignCenter)
        device.layout.addWidget(device.gpu1Label)

        addSeparator()

        # GPU2 사용량
        device.gpu2Label = QLabel("0%", device.deviceWidget)
        device.gpu2Label.setFont(font)
        device.gpu2Label.setStyleSheet(style_sheet)
        device.gpu2Label.setAlignment(Qt.AlignCenter)
        device.layout.addWidget(device.gpu2Label)

        addSeparator()

        # GPU3 사용량
        device.gpu3Label = QLabel("0%", device.deviceWidget)
        device.gpu3Label.setFont(font)
        device.gpu3Label.setStyleSheet(style_sheet)
        device.gpu3Label.setAlignment(Qt.AlignCenter)
        device.layout.addWidget(device.gpu3Label)

        addSeparator()

        # GPU4 사용량
        device.gpu4Label = QLabel("0%", device.deviceWidget)
        device.gpu4Label.setFont(font)
        device.gpu4Label.setStyleSheet(style_sheet)
        device.gpu4Label.setAlignment(Qt.AlignCenter)
        device.layout.addWidget(device.gpu4Label)

        addSeparator()

        # GPU5 사용량
        device.gpu5Label = QLabel("0%", device.deviceWidget)
        device.gpu5Label.setFont(font)
        device.gpu5Label.setStyleSheet(style_sheet)
        device.gpu5Label.setAlignment(Qt.AlignCenter)
        device.layout.addWidget(device.gpu5Label)

        addSeparator()

        # On/Off 버튼

        style_sheet = "color: red; background-color: white"
        device.onOffButton = QPushButton("Off", device.deviceWidget)
        device.onOffButton.setFont(font)
        device.onOffButton.setStyleSheet(style_sheet)
        device.layout.addWidget(device.onOffButton)

        # 스크롤 영역의 맨 위에 위젯 추가
        self.verticalLayout_2.insertWidget(0, device.deviceWidget)

        # 행 구분선 추가
        device.line = QFrame(self.scrollAreaWidgetContents)
        device.line.setFrameShape(QFrame.HLine)
        device.line.setStyleSheet("background-color: rgb(200, 200, 200);")
        device.line.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_2.insertWidget(1, device.line)
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clientwindowrkAEZy.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QWidget)

class Ui_ClientWindow(object):
    def setupUi(self, ClientWindow):
        if not ClientWindow.objectName():
            ClientWindow.setObjectName(u"ClientWindow")
        ClientWindow.resize(800, 550)
        ClientWindow.setMinimumSize(QSize(650, 550))
        ClientWindow.setMaximumSize(QSize(800, 550))
        ClientWindow.setStyleSheet(u"background-color:rgb(55, 55, 55);")
        ClientWindow.setWindowIcon(QIcon('client_icon.ico')) # 아이콘 설정


        self.centralwidget = QWidget(ClientWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.current_state = QTextEdit(self.centralwidget)
        self.current_state.setObjectName(u"current_state")
        self.current_state.setGeometry(QRect(20, 460, 431, 71))
        self.current_state.setStyleSheet(u"color:rgb(255, 255, 255)")
        self.current_state.setReadOnly(True)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 20, 761, 431))
        self.frame.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(30, 30, 351, 71))
        self.frame_2.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.cpu_name = QLabel(self.frame_2)
        self.cpu_name.setObjectName(u"cpu_name")
        self.cpu_name.setGeometry(QRect(20, 10, 41, 21))
        font = QFont()
        font.setFamilies([u"\ub9d1\uc740 \uace0\ub515"])
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.cpu_name.setFont(font)
        self.cpu_name.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")
        self.cpu_usage = QLabel(self.frame_2)
        self.cpu_usage.setObjectName(u"cpu_usage")
        self.cpu_usage.setGeometry(QRect(200, 20, 91, 51))
        self.cpu_usage.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpu_usage.setStyleSheet(u"font: 700 25pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpu_usage.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(170, 110, 91, 31))
        self.label_10.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(30, 140, 131, 31))
        self.label_11.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.memory_usage = QLabel(self.frame_2)
        self.memory_usage.setObjectName(u"memory_usage")
        self.memory_usage.setGeometry(QRect(170, 140, 91, 31))
        self.memory_usage.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.cpu_progressBar = QProgressBar(self.frame_2)
        self.cpu_progressBar.setObjectName(u"cpu_progressBar")
        self.cpu_progressBar.setGeometry(QRect(20, 40, 171, 21))
        self.cpu_progressBar.setStyleSheet(u"QProgressBar{\n"
"	background-color : rgb(200, 200, 200);\n"
"	border-style:solid;\n"
"	border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(6, 160, 191, 255), stop:1 rgba(255, 255, 255, 255));\n"
"		\n"
"}")
        self.cpu_progressBar.setValue(24)
        self.cpu_progressBar.setTextVisible(False)
        self.cpu_name_2 = QLabel(self.frame_2)
        self.cpu_name_2.setObjectName(u"cpu_name_2")
        self.cpu_name_2.setGeometry(QRect(300, 40, 21, 21))
        self.cpu_name_2.setFont(font)
        self.cpu_name_2.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(390, 30, 351, 71))
        self.frame_5.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.cpu_name_7 = QLabel(self.frame_5)
        self.cpu_name_7.setObjectName(u"cpu_name_7")
        self.cpu_name_7.setGeometry(QRect(20, 10, 51, 21))
        self.cpu_name_7.setFont(font)
        self.cpu_name_7.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")
        self.label_16 = QLabel(self.frame_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(170, 110, 91, 31))
        self.label_16.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_17 = QLabel(self.frame_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(30, 140, 131, 31))
        self.label_17.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.memory_usage_3 = QLabel(self.frame_5)
        self.memory_usage_3.setObjectName(u"memory_usage_3")
        self.memory_usage_3.setGeometry(QRect(170, 140, 91, 31))
        self.memory_usage_3.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.gpu_progressbar_2 = QProgressBar(self.frame_5)
        self.gpu_progressbar_2.setObjectName(u"gpu_progressbar_2")
        self.gpu_progressbar_2.setGeometry(QRect(20, 40, 171, 21))
        self.gpu_progressbar_2.setStyleSheet(u"QProgressBar{\n"
"	background-color : rgb(200, 200, 200);\n"
"	border-style:solid;\n"
"	border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(210, 0, 238, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	\n"
"	\n"
"		\n"
"}")
        self.gpu_progressbar_2.setValue(24)
        self.gpu_progressbar_2.setTextVisible(False)
        self.cpu_name_8 = QLabel(self.frame_5)
        self.cpu_name_8.setObjectName(u"cpu_name_8")
        self.cpu_name_8.setGeometry(QRect(300, 40, 21, 21))
        self.cpu_name_8.setFont(font)
        self.cpu_name_8.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")
        self.gpu_name_2 = QLabel(self.frame_5)
        self.gpu_name_2.setObjectName(u"gpu_name_2")
        self.gpu_name_2.setGeometry(QRect(70, 10, 171, 21))
        font1 = QFont()
        font1.setFamilies([u"\ub9d1\uc740 \uace0\ub515"])
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setItalic(False)
        self.gpu_name_2.setFont(font1)
        self.gpu_name_2.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(155, 155, 155)")
        self.gpu_usage_2 = QLabel(self.frame_5)
        self.gpu_usage_2.setObjectName(u"gpu_usage_2")
        self.gpu_usage_2.setGeometry(QRect(210, 30, 81, 31))
        self.gpu_usage_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu_usage_2.setStyleSheet(u"font: 700 25pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu_usage_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(230, 370, 401, 51))
        self.frame_8.setStyleSheet(u"background-color:rgb(50, 50, 50);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.gpu0_usage_6 = QLabel(self.frame_8)
        self.gpu0_usage_6.setObjectName(u"gpu0_usage_6")
        self.gpu0_usage_6.setGeometry(QRect(210, 80, 91, 31))
        self.gpu0_usage_6.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_24 = QLabel(self.frame_8)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(170, 80, 81, 31))
        self.label_24.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_25 = QLabel(self.frame_8)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(170, 110, 91, 31))
        self.label_25.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_26 = QLabel(self.frame_8)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(30, 140, 131, 31))
        self.label_26.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.memory_usage_6 = QLabel(self.frame_8)
        self.memory_usage_6.setObjectName(u"memory_usage_6")
        self.memory_usage_6.setGeometry(QRect(170, 140, 91, 31))
        self.memory_usage_6.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.current_time = QLabel(self.frame_8)
        self.current_time.setObjectName(u"current_time")
        self.current_time.setGeometry(QRect(210, 20, 171, 31))
        font2 = QFont()
        font2.setFamilies([u"\ub9d1\uc740 \uace0\ub515"])
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setItalic(False)
        self.current_time.setFont(font2)
        self.current_time.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.current_time.setStyleSheet(u"font: 700 18pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color:rgb(255, 255, 255)")
        self.current_time.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.cpu_name_16 = QLabel(self.frame_8)
        self.cpu_name_16.setObjectName(u"cpu_name_16")
        self.cpu_name_16.setGeometry(QRect(100, 0, 71, 21))
        self.cpu_name_16.setFont(font1)
        self.cpu_name_16.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(155, 155, 155)")
        self.start_time = QLabel(self.frame_8)
        self.start_time.setObjectName(u"start_time")
        self.start_time.setGeometry(QRect(10, 20, 251, 31))
        self.start_time.setFont(font2)
        self.start_time.setStyleSheet(u"font: 700 18pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(200, 200, 200)")
        self.cpu_name_27 = QLabel(self.frame_8)
        self.cpu_name_27.setObjectName(u"cpu_name_27")
        self.cpu_name_27.setGeometry(QRect(290, 0, 81, 21))
        self.cpu_name_27.setFont(font1)
        self.cpu_name_27.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(155, 155, 155)")
        self.frame_10 = QFrame(self.frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(640, 370, 111, 51))
        self.frame_10.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.gpu0_usage_9 = QLabel(self.frame_10)
        self.gpu0_usage_9.setObjectName(u"gpu0_usage_9")
        self.gpu0_usage_9.setGeometry(QRect(210, 80, 91, 31))
        self.gpu0_usage_9.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_33 = QLabel(self.frame_10)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(170, 80, 81, 31))
        self.label_33.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_34 = QLabel(self.frame_10)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(170, 110, 91, 31))
        self.label_34.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_35 = QLabel(self.frame_10)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(30, 140, 131, 31))
        self.label_35.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.memory_usage_9 = QLabel(self.frame_10)
        self.memory_usage_9.setObjectName(u"memory_usage_9")
        self.memory_usage_9.setGeometry(QRect(170, 140, 91, 31))
        self.memory_usage_9.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.cpu_name_24 = QLabel(self.frame_10)
        self.cpu_name_24.setObjectName(u"cpu_name_24")
        self.cpu_name_24.setGeometry(QRect(280, 30, 21, 21))
        self.cpu_name_24.setFont(font)
        self.cpu_name_24.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")
        self.cpu_usage_8 = QLabel(self.frame_10)
        self.cpu_usage_8.setObjectName(u"cpu_usage_8")
        self.cpu_usage_8.setGeometry(QRect(210, 20, 61, 51))
        self.cpu_usage_8.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpu_usage_8.setStyleSheet(u"font: 700 40pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpu_usage_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.connect = QPushButton(self.frame_10)
        self.connect.setObjectName(u"connect")
        self.connect.setGeometry(QRect(10, 10, 91, 31))
        self.connect.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(52, 52, 52);")
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(30, 110, 351, 71))
        self.frame_6.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.cpu_name_9 = QLabel(self.frame_6)
        self.cpu_name_9.setObjectName(u"cpu_name_9")
        self.cpu_name_9.setGeometry(QRect(20, 10, 51, 21))
        self.cpu_name_9.setFont(font)
        self.cpu_name_9.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")
        self.label_18 = QLabel(self.frame_6)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(170, 110, 91, 31))
        self.label_18.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_19 = QLabel(self.frame_6)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(30, 140, 131, 31))
        self.label_19.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.memory_usage_4 = QLabel(self.frame_6)
        self.memory_usage_4.setObjectName(u"memory_usage_4")
        self.memory_usage_4.setGeometry(QRect(170, 140, 91, 31))
        self.memory_usage_4.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.memory_progressbar = QProgressBar(self.frame_6)
        self.memory_progressbar.setObjectName(u"memory_progressbar")
        self.memory_progressbar.setGeometry(QRect(20, 40, 171, 21))
        self.memory_progressbar.setStyleSheet(u"QProgressBar{\n"
"	background-color : rgb(200, 200, 200);\n"
"	border-style:solid;\n"
"	border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 208, 149, 255), stop:1 rgba(255, 255, 255, 255));\n"
"		\n"
"}")
        self.memory_progressbar.setValue(24)
        self.memory_progressbar.setTextVisible(False)
        self.cpu_name_10 = QLabel(self.frame_6)
        self.cpu_name_10.setObjectName(u"cpu_name_10")
        self.cpu_name_10.setGeometry(QRect(300, 40, 21, 21))
        self.cpu_name_10.setFont(font)
        self.cpu_name_10.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")
        self.mem_usage = QLabel(self.frame_6)
        self.mem_usage.setObjectName(u"mem_usage")
        self.mem_usage.setGeometry(QRect(210, 30, 81, 31))
        self.mem_usage.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.mem_usage.setStyleSheet(u"font: 700 25pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.mem_usage.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.frame_11 = QFrame(self.frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(30, 190, 351, 71))
        self.frame_11.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.cpu_name_15 = QLabel(self.frame_11)
        self.cpu_name_15.setObjectName(u"cpu_name_15")
        self.cpu_name_15.setGeometry(QRect(20, 10, 51, 21))
        self.cpu_name_15.setFont(font)
        self.cpu_name_15.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")
        self.label_27 = QLabel(self.frame_11)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(170, 110, 91, 31))
        self.label_27.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_28 = QLabel(self.frame_11)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(30, 140, 131, 31))
        self.label_28.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.memory_usage_10 = QLabel(self.frame_11)
        self.memory_usage_10.setObjectName(u"memory_usage_10")
        self.memory_usage_10.setGeometry(QRect(170, 140, 91, 31))
        self.memory_usage_10.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.gpu_progressbar_0 = QProgressBar(self.frame_11)
        self.gpu_progressbar_0.setObjectName(u"gpu_progressbar_0")
        self.gpu_progressbar_0.setGeometry(QRect(20, 40, 171, 21))
        self.gpu_progressbar_0.setStyleSheet(u"QProgressBar{\n"
"	background-color : rgb(200, 200, 200);\n"
"	border-style:solid;\n"
"	border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(210, 0, 238, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	\n"
"	\n"
"		\n"
"}")
        self.gpu_progressbar_0.setValue(24)
        self.gpu_progressbar_0.setTextVisible(False)
        self.cpu_name_17 = QLabel(self.frame_11)
        self.cpu_name_17.setObjectName(u"cpu_name_17")
        self.cpu_name_17.setGeometry(QRect(300, 40, 21, 21))
        self.cpu_name_17.setFont(font)
        self.cpu_name_17.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")
        self.gpu_name_0 = QLabel(self.frame_11)
        self.gpu_name_0.setObjectName(u"gpu_name_0")
        self.gpu_name_0.setGeometry(QRect(70, 10, 171, 21))
        self.gpu_name_0.setFont(font1)
        self.gpu_name_0.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(155, 155, 155)")
        self.gpu_usage_0 = QLabel(self.frame_11)
        self.gpu_usage_0.setObjectName(u"gpu_usage_0")
        self.gpu_usage_0.setGeometry(QRect(210, 30, 81, 31))
        self.gpu_usage_0.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu_usage_0.setStyleSheet(u"font: 700 25pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu_usage_0.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.frame_13 = QFrame(self.frame)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(390, 190, 351, 71))
        self.frame_13.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.cpu_name_18 = QLabel(self.frame_13)
        self.cpu_name_18.setObjectName(u"cpu_name_18")
        self.cpu_name_18.setGeometry(QRect(20, 10, 51, 21))
        self.cpu_name_18.setFont(font)
        self.cpu_name_18.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")
        self.label_29 = QLabel(self.frame_13)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(170, 110, 91, 31))
        self.label_29.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_36 = QLabel(self.frame_13)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(30, 140, 131, 31))
        self.label_36.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.memory_usage_11 = QLabel(self.frame_13)
        self.memory_usage_11.setObjectName(u"memory_usage_11")
        self.memory_usage_11.setGeometry(QRect(170, 140, 91, 31))
        self.memory_usage_11.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.gpu_progressbar_4 = QProgressBar(self.frame_13)
        self.gpu_progressbar_4.setObjectName(u"gpu_progressbar_4")
        self.gpu_progressbar_4.setGeometry(QRect(20, 40, 171, 21))
        self.gpu_progressbar_4.setStyleSheet(u"QProgressBar{\n"
"	background-color : rgb(200, 200, 200);\n"
"	border-style:solid;\n"
"	border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(210, 0, 238, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	\n"
"	\n"
"		\n"
"}")
        self.gpu_progressbar_4.setValue(24)
        self.gpu_progressbar_4.setTextVisible(False)
        self.cpu_name_19 = QLabel(self.frame_13)
        self.cpu_name_19.setObjectName(u"cpu_name_19")
        self.cpu_name_19.setGeometry(QRect(300, 40, 21, 21))
        self.cpu_name_19.setFont(font)
        self.cpu_name_19.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")
        self.gpu_name_4 = QLabel(self.frame_13)
        self.gpu_name_4.setObjectName(u"gpu_name_4")
        self.gpu_name_4.setGeometry(QRect(70, 10, 171, 21))
        self.gpu_name_4.setFont(font1)
        self.gpu_name_4.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(155, 155, 155)")
        self.gpu_usage_4 = QLabel(self.frame_13)
        self.gpu_usage_4.setObjectName(u"gpu_usage_4")
        self.gpu_usage_4.setGeometry(QRect(210, 30, 81, 31))
        self.gpu_usage_4.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu_usage_4.setStyleSheet(u"font: 700 25pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu_usage_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(390, 110, 351, 71))
        self.frame_7.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.cpu_name_13 = QLabel(self.frame_7)
        self.cpu_name_13.setObjectName(u"cpu_name_13")
        self.cpu_name_13.setGeometry(QRect(20, 10, 51, 21))
        self.cpu_name_13.setFont(font)
        self.cpu_name_13.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")
        self.label_22 = QLabel(self.frame_7)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(170, 110, 91, 31))
        self.label_22.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_23 = QLabel(self.frame_7)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(30, 140, 131, 31))
        self.label_23.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.memory_usage_5 = QLabel(self.frame_7)
        self.memory_usage_5.setObjectName(u"memory_usage_5")
        self.memory_usage_5.setGeometry(QRect(170, 140, 91, 31))
        self.memory_usage_5.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.gpu_progressbar_3 = QProgressBar(self.frame_7)
        self.gpu_progressbar_3.setObjectName(u"gpu_progressbar_3")
        self.gpu_progressbar_3.setGeometry(QRect(20, 40, 171, 21))
        self.gpu_progressbar_3.setStyleSheet(u"QProgressBar{\n"
"	background-color : rgb(200, 200, 200);\n"
"	border-style:solid;\n"
"	border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(210, 0, 238, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	\n"
"	\n"
"		\n"
"}")
        self.gpu_progressbar_3.setValue(24)
        self.gpu_progressbar_3.setTextVisible(False)
        self.cpu_name_14 = QLabel(self.frame_7)
        self.cpu_name_14.setObjectName(u"cpu_name_14")
        self.cpu_name_14.setGeometry(QRect(300, 40, 21, 21))
        self.cpu_name_14.setFont(font)
        self.cpu_name_14.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")
        self.gpu_name_3 = QLabel(self.frame_7)
        self.gpu_name_3.setObjectName(u"gpu_name_3")
        self.gpu_name_3.setGeometry(QRect(70, 10, 171, 21))
        self.gpu_name_3.setFont(font1)
        self.gpu_name_3.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(155, 155, 155)")
        self.gpu_usage_3 = QLabel(self.frame_7)
        self.gpu_usage_3.setObjectName(u"gpu_usage_3")
        self.gpu_usage_3.setGeometry(QRect(210, 30, 81, 31))
        self.gpu_usage_3.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu_usage_3.setStyleSheet(u"font: 700 25pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu_usage_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.frame_14 = QFrame(self.frame)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(30, 270, 351, 71))
        self.frame_14.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.cpu_name_20 = QLabel(self.frame_14)
        self.cpu_name_20.setObjectName(u"cpu_name_20")
        self.cpu_name_20.setGeometry(QRect(20, 10, 51, 21))
        self.cpu_name_20.setFont(font)
        self.cpu_name_20.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")
        self.label_37 = QLabel(self.frame_14)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(170, 110, 91, 31))
        self.label_37.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_38 = QLabel(self.frame_14)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(30, 140, 131, 31))
        self.label_38.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.memory_usage_13 = QLabel(self.frame_14)
        self.memory_usage_13.setObjectName(u"memory_usage_13")
        self.memory_usage_13.setGeometry(QRect(170, 140, 91, 31))
        self.memory_usage_13.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.gpu_progressbar_1 = QProgressBar(self.frame_14)
        self.gpu_progressbar_1.setObjectName(u"gpu_progressbar_1")
        self.gpu_progressbar_1.setGeometry(QRect(20, 40, 171, 21))
        self.gpu_progressbar_1.setStyleSheet(u"QProgressBar{\n"
"	background-color : rgb(200, 200, 200);\n"
"	border-style:solid;\n"
"	border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(210, 0, 238, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	\n"
"	\n"
"		\n"
"}")
        self.gpu_progressbar_1.setValue(24)
        self.gpu_progressbar_1.setTextVisible(False)
        self.cpu_name_21 = QLabel(self.frame_14)
        self.cpu_name_21.setObjectName(u"cpu_name_21")
        self.cpu_name_21.setGeometry(QRect(300, 40, 21, 21))
        self.cpu_name_21.setFont(font)
        self.cpu_name_21.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")
        self.gpu_name_1 = QLabel(self.frame_14)
        self.gpu_name_1.setObjectName(u"gpu_name_1")
        self.gpu_name_1.setGeometry(QRect(70, 10, 171, 21))
        self.gpu_name_1.setFont(font1)
        self.gpu_name_1.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(155, 155, 155)")
        self.gpu_usage_1 = QLabel(self.frame_14)
        self.gpu_usage_1.setObjectName(u"gpu_usage_1")
        self.gpu_usage_1.setGeometry(QRect(210, 30, 81, 31))
        self.gpu_usage_1.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu_usage_1.setStyleSheet(u"font: 700 25pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu_usage_1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.frame_15 = QFrame(self.frame)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(390, 270, 351, 71))
        self.frame_15.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.cpu_name_23 = QLabel(self.frame_15)
        self.cpu_name_23.setObjectName(u"cpu_name_23")
        self.cpu_name_23.setGeometry(QRect(20, 10, 51, 21))
        self.cpu_name_23.setFont(font)
        self.cpu_name_23.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")
        self.label_39 = QLabel(self.frame_15)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(170, 110, 91, 31))
        self.label_39.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_40 = QLabel(self.frame_15)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(30, 140, 131, 31))
        self.label_40.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.memory_usage_14 = QLabel(self.frame_15)
        self.memory_usage_14.setObjectName(u"memory_usage_14")
        self.memory_usage_14.setGeometry(QRect(170, 140, 91, 31))
        self.memory_usage_14.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.gpu_progressbar_5 = QProgressBar(self.frame_15)
        self.gpu_progressbar_5.setObjectName(u"gpu_progressbar_5")
        self.gpu_progressbar_5.setGeometry(QRect(20, 40, 171, 21))
        self.gpu_progressbar_5.setStyleSheet(u"QProgressBar{\n"
"	background-color : rgb(200, 200, 200);\n"
"	border-style:solid;\n"
"	border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(210, 0, 238, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	\n"
"	\n"
"		\n"
"}")
        self.gpu_progressbar_5.setValue(24)
        self.gpu_progressbar_5.setTextVisible(False)
        self.cpu_name_28 = QLabel(self.frame_15)
        self.cpu_name_28.setObjectName(u"cpu_name_28")
        self.cpu_name_28.setGeometry(QRect(300, 40, 21, 21))
        self.cpu_name_28.setFont(font)
        self.cpu_name_28.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")
        self.gpu_name_5 = QLabel(self.frame_15)
        self.gpu_name_5.setObjectName(u"gpu_name_5")
        self.gpu_name_5.setGeometry(QRect(70, 10, 171, 21))
        self.gpu_name_5.setFont(font1)
        self.gpu_name_5.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(155, 155, 155)")
        self.gpu_usage_5 = QLabel(self.frame_15)
        self.gpu_usage_5.setObjectName(u"gpu_usage_5")
        self.gpu_usage_5.setGeometry(QRect(210, 30, 81, 31))
        self.gpu_usage_5.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu_usage_5.setStyleSheet(u"font: 700 25pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu_usage_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.frame_9 = QFrame(self.centralwidget)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(630, 470, 151, 61))
        self.frame_9.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.gpu0_usage_8 = QLabel(self.frame_9)
        self.gpu0_usage_8.setObjectName(u"gpu0_usage_8")
        self.gpu0_usage_8.setGeometry(QRect(210, 80, 91, 31))
        self.gpu0_usage_8.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_30 = QLabel(self.frame_9)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(170, 80, 81, 31))
        self.label_30.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_31 = QLabel(self.frame_9)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(170, 110, 91, 31))
        self.label_31.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_32 = QLabel(self.frame_9)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(30, 140, 131, 31))
        self.label_32.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.memory_usage_8 = QLabel(self.frame_9)
        self.memory_usage_8.setObjectName(u"memory_usage_8")
        self.memory_usage_8.setGeometry(QRect(170, 140, 91, 31))
        self.memory_usage_8.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.cpu_name_22 = QLabel(self.frame_9)
        self.cpu_name_22.setObjectName(u"cpu_name_22")
        self.cpu_name_22.setGeometry(QRect(280, 30, 21, 21))
        self.cpu_name_22.setFont(font)
        self.cpu_name_22.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")
        self.cpu_name_25 = QLabel(self.frame_9)
        self.cpu_name_25.setObjectName(u"cpu_name_25")
        self.cpu_name_25.setGeometry(QRect(10, 0, 141, 31))
        self.cpu_name_25.setFont(font)
        self.cpu_name_25.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")
        self.IP_address = QLineEdit(self.frame_9)
        self.IP_address.setObjectName(u"IP_address")
        self.IP_address.setGeometry(QRect(10, 30, 131, 22))
        self.IP_address.setStyleSheet(u"background-color: rgb(238, 238, 238);\n"
"font: 10pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.IP_address.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_12 = QFrame(self.centralwidget)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(460, 470, 161, 61))
        self.frame_12.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.gpu0_usage_12 = QLabel(self.frame_12)
        self.gpu0_usage_12.setObjectName(u"gpu0_usage_12")
        self.gpu0_usage_12.setGeometry(QRect(210, 80, 91, 31))
        self.gpu0_usage_12.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_42 = QLabel(self.frame_12)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(170, 80, 81, 31))
        self.label_42.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_43 = QLabel(self.frame_12)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(170, 110, 91, 31))
        self.label_43.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_44 = QLabel(self.frame_12)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(30, 140, 131, 31))
        self.label_44.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.memory_usage_12 = QLabel(self.frame_12)
        self.memory_usage_12.setObjectName(u"memory_usage_12")
        self.memory_usage_12.setGeometry(QRect(170, 140, 91, 31))
        self.memory_usage_12.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.cpu_name_32 = QLabel(self.frame_12)
        self.cpu_name_32.setObjectName(u"cpu_name_32")
        self.cpu_name_32.setGeometry(QRect(280, 30, 21, 21))
        self.cpu_name_32.setFont(font)
        self.cpu_name_32.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")
        self.client_name = QLineEdit(self.frame_12)
        self.client_name.setObjectName(u"client_name")
        self.client_name.setGeometry(QRect(10, 31, 141, 21))
        self.client_name.setStyleSheet(u"background-color: rgb(238, 238, 238);\n"
"font: 10pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.client_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cpu_name_29 = QLabel(self.frame_12)
        self.cpu_name_29.setObjectName(u"cpu_name_29")
        self.cpu_name_29.setGeometry(QRect(57, 0, 51, 31))
        self.cpu_name_29.setFont(font)
        self.cpu_name_29.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")
        self.cpu_name_29.setAlignment(Qt.AlignmentFlag.AlignCenter)
        ClientWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(ClientWindow)
        self.statusbar.setObjectName(u"statusbar")
        ClientWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ClientWindow)

        QMetaObject.connectSlotsByName(ClientWindow)
    # setupUi

    def retranslateUi(self, ClientWindow):
        ClientWindow.setWindowTitle(QCoreApplication.translate("ClientWindow", u"ClientWindow", None))
        self.cpu_name.setText(QCoreApplication.translate("ClientWindow", u"CPU", None))
        self.cpu_usage.setText(QCoreApplication.translate("ClientWindow", u"0.0", None))
        self.label_10.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_11.setText(QCoreApplication.translate("ClientWindow", u"MEMORY:", None))
        self.memory_usage.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.cpu_name_2.setText(QCoreApplication.translate("ClientWindow", u"%", None))
        self.cpu_name_7.setText(QCoreApplication.translate("ClientWindow", u"GPU2", None))
        self.label_16.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_17.setText(QCoreApplication.translate("ClientWindow", u"MEMORY:", None))
        self.memory_usage_3.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.cpu_name_8.setText(QCoreApplication.translate("ClientWindow", u"%", None))
        self.gpu_name_2.setText(QCoreApplication.translate("ClientWindow", u"devicename", None))
        self.gpu_usage_2.setText(QCoreApplication.translate("ClientWindow", u"0.0", None))
        self.gpu0_usage_6.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_24.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_25.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_26.setText(QCoreApplication.translate("ClientWindow", u"MEMORY:", None))
        self.memory_usage_6.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.current_time.setText(QCoreApplication.translate("ClientWindow", u"00:00:00", None))
        self.cpu_name_16.setText(QCoreApplication.translate("ClientWindow", u"start time", None))
        self.start_time.setText(QCoreApplication.translate("ClientWindow", u"2024-10-11 00:00:00", None))
        self.cpu_name_27.setText(QCoreApplication.translate("ClientWindow", u"elapsed time", None))
        self.gpu0_usage_9.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_33.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_34.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_35.setText(QCoreApplication.translate("ClientWindow", u"MEMORY:", None))
        self.memory_usage_9.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.cpu_name_24.setText(QCoreApplication.translate("ClientWindow", u"%", None))
        self.cpu_usage_8.setText(QCoreApplication.translate("ClientWindow", u"0", None))
        self.connect.setText(QCoreApplication.translate("ClientWindow", u"CONNECT", None))
        self.cpu_name_9.setText(QCoreApplication.translate("ClientWindow", u"MEM", None))
        self.label_18.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_19.setText(QCoreApplication.translate("ClientWindow", u"MEMORY:", None))
        self.memory_usage_4.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.cpu_name_10.setText(QCoreApplication.translate("ClientWindow", u"%", None))
        self.mem_usage.setText(QCoreApplication.translate("ClientWindow", u"0.0", None))
        self.cpu_name_15.setText(QCoreApplication.translate("ClientWindow", u"GPU0", None))
        self.label_27.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_28.setText(QCoreApplication.translate("ClientWindow", u"MEMORY:", None))
        self.memory_usage_10.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.cpu_name_17.setText(QCoreApplication.translate("ClientWindow", u"%", None))
        self.gpu_name_0.setText(QCoreApplication.translate("ClientWindow", u"devicename", None))
        self.gpu_usage_0.setText(QCoreApplication.translate("ClientWindow", u"0.0", None))
        self.cpu_name_18.setText(QCoreApplication.translate("ClientWindow", u"GPU4", None))
        self.label_29.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_36.setText(QCoreApplication.translate("ClientWindow", u"MEMORY:", None))
        self.memory_usage_11.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.cpu_name_19.setText(QCoreApplication.translate("ClientWindow", u"%", None))
        self.gpu_name_4.setText(QCoreApplication.translate("ClientWindow", u"devicename", None))
        self.gpu_usage_4.setText(QCoreApplication.translate("ClientWindow", u"0.0", None))
        self.cpu_name_13.setText(QCoreApplication.translate("ClientWindow", u"GPU3", None))
        self.label_22.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_23.setText(QCoreApplication.translate("ClientWindow", u"MEMORY:", None))
        self.memory_usage_5.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.cpu_name_14.setText(QCoreApplication.translate("ClientWindow", u"%", None))
        self.gpu_name_3.setText(QCoreApplication.translate("ClientWindow", u"devicename", None))
        self.gpu_usage_3.setText(QCoreApplication.translate("ClientWindow", u"0.0", None))
        self.cpu_name_20.setText(QCoreApplication.translate("ClientWindow", u"GPU1", None))
        self.label_37.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_38.setText(QCoreApplication.translate("ClientWindow", u"MEMORY:", None))
        self.memory_usage_13.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.cpu_name_21.setText(QCoreApplication.translate("ClientWindow", u"%", None))
        self.gpu_name_1.setText(QCoreApplication.translate("ClientWindow", u"devicename", None))
        self.gpu_usage_1.setText(QCoreApplication.translate("ClientWindow", u"0.0", None))
        self.cpu_name_23.setText(QCoreApplication.translate("ClientWindow", u"GPU5", None))
        self.label_39.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_40.setText(QCoreApplication.translate("ClientWindow", u"MEMORY:", None))
        self.memory_usage_14.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.cpu_name_28.setText(QCoreApplication.translate("ClientWindow", u"%", None))
        self.gpu_name_5.setText(QCoreApplication.translate("ClientWindow", u"devicename", None))
        self.gpu_usage_5.setText(QCoreApplication.translate("ClientWindow", u"0.0", None))
        self.gpu0_usage_8.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_30.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_31.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_32.setText(QCoreApplication.translate("ClientWindow", u"MEMORY:", None))
        self.memory_usage_8.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.cpu_name_22.setText(QCoreApplication.translate("ClientWindow", u"%", None))
        self.cpu_name_25.setText(QCoreApplication.translate("ClientWindow", u"server IP address", None))
        self.IP_address.setText(QCoreApplication.translate("ClientWindow", u"127.0.0.1", None))
        self.gpu0_usage_12.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_42.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_43.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_44.setText(QCoreApplication.translate("ClientWindow", u"MEMORY:", None))
        self.memory_usage_12.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.cpu_name_32.setText(QCoreApplication.translate("ClientWindow", u"%", None))
        self.client_name.setText(QCoreApplication.translate("ClientWindow", u"client1", None))
        self.cpu_name_29.setText(QCoreApplication.translate("ClientWindow", u"name", None))
    # retranslateUi


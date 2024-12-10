# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clientwindowPHrDso.ui'
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
        ClientWindow.resize(930, 500)
        ClientWindow.setMinimumSize(QSize(930, 500))
        ClientWindow.setMaximumSize(QSize(930, 500))
        ClientWindow.setStyleSheet(u"background-color:rgb(55, 55, 55);")
        self.centralwidget = QWidget(ClientWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.current_state = QTextEdit(self.centralwidget)
        self.current_state.setObjectName(u"current_state")
        self.current_state.setGeometry(QRect(30, 400, 451, 71))
        self.current_state.setStyleSheet(u"color:rgb(255, 255, 255)")
        self.current_state.setReadOnly(True)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 20, 881, 361))
        self.frame.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(30, 30, 361, 91))
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
        self.cpu_usage.setGeometry(QRect(200, 30, 111, 51))
        self.cpu_usage.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpu_usage.setStyleSheet(u"font: 700 40pt \"\ub9d1\uc740 \uace0\ub515\";\n"
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
        self.cpu_progressBar.setGeometry(QRect(20, 40, 171, 41))
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
        self.cpu_name_2.setGeometry(QRect(320, 40, 21, 21))
        self.cpu_name_2.setFont(font)
        self.cpu_name_2.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")
        self.cpu_name_3 = QLabel(self.frame_2)
        self.cpu_name_3.setObjectName(u"cpu_name_3")
        self.cpu_name_3.setGeometry(QRect(60, 10, 171, 21))
        font1 = QFont()
        font1.setFamilies([u"\ub9d1\uc740 \uace0\ub515"])
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setItalic(False)
        self.cpu_name_3.setFont(font1)
        self.cpu_name_3.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(155, 155, 155)")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(760, 150, 111, 171))
        self.frame_3.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.onButton = QPushButton(self.frame_3)
        self.onButton.setObjectName(u"onButton")
        self.onButton.setGeometry(QRect(10, 10, 91, 71))
        self.onButton.setStyleSheet(u"\n"
"QPushButton {\n"
"   font: 700 20pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"font: 700 20pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:grey;\n"
"}\n"
"")
        self.offButton = QPushButton(self.frame_3)
        self.offButton.setObjectName(u"offButton")
        self.offButton.setGeometry(QRect(10, 90, 91, 71))
        self.offButton.setStyleSheet(u"font: 700 20pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(30, 130, 361, 91))
        self.frame_4.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.cpu_name_4 = QLabel(self.frame_4)
        self.cpu_name_4.setObjectName(u"cpu_name_4")
        self.cpu_name_4.setGeometry(QRect(20, 10, 51, 21))
        self.cpu_name_4.setFont(font)
        self.cpu_name_4.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")
        self.gpu1_usage = QLabel(self.frame_4)
        self.gpu1_usage.setObjectName(u"gpu1_usage")
        self.gpu1_usage.setGeometry(QRect(210, 30, 101, 51))
        self.gpu1_usage.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1_usage.setStyleSheet(u"font: 700 40pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1_usage.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_13 = QLabel(self.frame_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(170, 110, 91, 31))
        self.label_13.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_14 = QLabel(self.frame_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(30, 140, 131, 31))
        self.label_14.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.memory_usage_2 = QLabel(self.frame_4)
        self.memory_usage_2.setObjectName(u"memory_usage_2")
        self.memory_usage_2.setGeometry(QRect(170, 140, 91, 31))
        self.memory_usage_2.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.gpu1_progressBar = QProgressBar(self.frame_4)
        self.gpu1_progressBar.setObjectName(u"gpu1_progressBar")
        self.gpu1_progressBar.setGeometry(QRect(20, 40, 171, 41))
        self.gpu1_progressBar.setStyleSheet(u"QProgressBar{\n"
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
        self.gpu1_progressBar.setValue(24)
        self.gpu1_progressBar.setTextVisible(False)
        self.cpu_name_5 = QLabel(self.frame_4)
        self.cpu_name_5.setObjectName(u"cpu_name_5")
        self.cpu_name_5.setGeometry(QRect(320, 40, 21, 21))
        self.cpu_name_5.setFont(font)
        self.cpu_name_5.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")
        self.cpu_name_6 = QLabel(self.frame_4)
        self.cpu_name_6.setObjectName(u"cpu_name_6")
        self.cpu_name_6.setGeometry(QRect(70, 10, 181, 21))
        self.cpu_name_6.setFont(font1)
        self.cpu_name_6.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(155, 155, 155)")
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(400, 30, 351, 91))
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
        self.gpu0_progressBar = QProgressBar(self.frame_5)
        self.gpu0_progressBar.setObjectName(u"gpu0_progressBar")
        self.gpu0_progressBar.setGeometry(QRect(20, 40, 171, 41))
        self.gpu0_progressBar.setStyleSheet(u"QProgressBar{\n"
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
        self.gpu0_progressBar.setValue(24)
        self.gpu0_progressBar.setTextVisible(False)
        self.cpu_name_8 = QLabel(self.frame_5)
        self.cpu_name_8.setObjectName(u"cpu_name_8")
        self.cpu_name_8.setGeometry(QRect(310, 40, 21, 21))
        self.cpu_name_8.setFont(font)
        self.cpu_name_8.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")
        self.gpu0_name = QLabel(self.frame_5)
        self.gpu0_name.setObjectName(u"gpu0_name")
        self.gpu0_name.setGeometry(QRect(70, 10, 171, 21))
        self.gpu0_name.setFont(font1)
        self.gpu0_name.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(155, 155, 155)")
        self.gpu0_usage = QLabel(self.frame_5)
        self.gpu0_usage.setObjectName(u"gpu0_usage")
        self.gpu0_usage.setGeometry(QRect(200, 30, 101, 51))
        self.gpu0_usage.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0_usage.setStyleSheet(u"font: 700 40pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0_usage.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(400, 130, 351, 91))
        self.frame_6.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.cpu_name_10 = QLabel(self.frame_6)
        self.cpu_name_10.setObjectName(u"cpu_name_10")
        self.cpu_name_10.setGeometry(QRect(20, 10, 51, 21))
        self.cpu_name_10.setFont(font)
        self.cpu_name_10.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")
        self.label_19 = QLabel(self.frame_6)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(170, 110, 91, 31))
        self.label_19.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_20 = QLabel(self.frame_6)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(30, 140, 131, 31))
        self.label_20.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.memory_usage_4 = QLabel(self.frame_6)
        self.memory_usage_4.setObjectName(u"memory_usage_4")
        self.memory_usage_4.setGeometry(QRect(170, 140, 91, 31))
        self.memory_usage_4.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.gpu2_progressBar = QProgressBar(self.frame_6)
        self.gpu2_progressBar.setObjectName(u"gpu2_progressBar")
        self.gpu2_progressBar.setGeometry(QRect(20, 40, 171, 41))
        self.gpu2_progressBar.setStyleSheet(u"QProgressBar{\n"
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
        self.gpu2_progressBar.setValue(24)
        self.gpu2_progressBar.setTextVisible(False)
        self.cpu_name_11 = QLabel(self.frame_6)
        self.cpu_name_11.setObjectName(u"cpu_name_11")
        self.cpu_name_11.setGeometry(QRect(310, 40, 21, 21))
        self.cpu_name_11.setFont(font)
        self.cpu_name_11.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")
        self.cpu_name_12 = QLabel(self.frame_6)
        self.cpu_name_12.setObjectName(u"cpu_name_12")
        self.cpu_name_12.setGeometry(QRect(70, 10, 171, 21))
        self.cpu_name_12.setFont(font1)
        self.cpu_name_12.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(155, 155, 155)")
        self.gpu2_usage = QLabel(self.frame_6)
        self.gpu2_usage.setObjectName(u"gpu2_usage")
        self.gpu2_usage.setGeometry(QRect(190, 30, 111, 51))
        self.gpu2_usage.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2_usage.setStyleSheet(u"font: 700 40pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2_usage.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(400, 230, 351, 91))
        self.frame_7.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.cpu_name_13 = QLabel(self.frame_7)
        self.cpu_name_13.setObjectName(u"cpu_name_13")
        self.cpu_name_13.setGeometry(QRect(20, 10, 71, 16))
        self.cpu_name_13.setFont(font)
        self.cpu_name_13.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")
        self.label_23 = QLabel(self.frame_7)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(30, 140, 131, 31))
        self.label_23.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.memory_usage_5 = QLabel(self.frame_7)
        self.memory_usage_5.setObjectName(u"memory_usage_5")
        self.memory_usage_5.setGeometry(QRect(170, 140, 91, 31))
        self.memory_usage_5.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.memory_progressBar = QProgressBar(self.frame_7)
        self.memory_progressBar.setObjectName(u"memory_progressBar")
        self.memory_progressBar.setGeometry(QRect(20, 40, 171, 41))
        self.memory_progressBar.setStyleSheet(u"QProgressBar{\n"
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
        self.memory_progressBar.setValue(24)
        self.memory_progressBar.setTextVisible(False)
        self.cpu_name_14 = QLabel(self.frame_7)
        self.cpu_name_14.setObjectName(u"cpu_name_14")
        self.cpu_name_14.setGeometry(QRect(310, 40, 21, 21))
        self.cpu_name_14.setFont(font)
        self.cpu_name_14.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")
        self.cpu_name_15 = QLabel(self.frame_7)
        self.cpu_name_15.setObjectName(u"cpu_name_15")
        self.cpu_name_15.setGeometry(QRect(100, 10, 141, 20))
        self.cpu_name_15.setFont(font1)
        self.cpu_name_15.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(155, 155, 155)")
        self.memory_usage_per = QLabel(self.frame_7)
        self.memory_usage_per.setObjectName(u"memory_usage_per")
        self.memory_usage_per.setGeometry(QRect(190, 30, 111, 51))
        self.memory_usage_per.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memory_usage_per.setStyleSheet(u"font: 700 40pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memory_usage_per.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(30, 230, 361, 91))
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
        self.current_time.setGeometry(QRect(130, 20, 231, 61))
        font2 = QFont()
        font2.setFamilies([u"\ub9d1\uc740 \uace0\ub515"])
        font2.setPointSize(40)
        font2.setBold(True)
        font2.setItalic(False)
        self.current_time.setFont(font2)
        self.current_time.setStyleSheet(u"font: 700 40pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color:rgb(255, 255, 255)")
        self.cpu_name_16 = QLabel(self.frame_8)
        self.cpu_name_16.setObjectName(u"cpu_name_16")
        self.cpu_name_16.setGeometry(QRect(10, 0, 71, 21))
        self.cpu_name_16.setFont(font1)
        self.cpu_name_16.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(155, 155, 155)")
        self.start_time = QLabel(self.frame_8)
        self.start_time.setObjectName(u"start_time")
        self.start_time.setGeometry(QRect(10, 20, 121, 21))
        font3 = QFont()
        font3.setFamilies([u"\ub9d1\uc740 \uace0\ub515"])
        font3.setPointSize(8)
        font3.setBold(True)
        font3.setItalic(False)
        self.start_time.setFont(font3)
        self.start_time.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(200, 200, 200)")
        self.cpu_name_26 = QLabel(self.frame_8)
        self.cpu_name_26.setObjectName(u"cpu_name_26")
        self.cpu_name_26.setGeometry(QRect(10, 40, 51, 21))
        self.cpu_name_26.setFont(font1)
        self.cpu_name_26.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(155, 155, 155)")
        self.end_time = QLabel(self.frame_8)
        self.end_time.setObjectName(u"end_time")
        self.end_time.setGeometry(QRect(10, 60, 121, 21))
        self.end_time.setFont(font3)
        self.end_time.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(200, 200, 200)")
        self.frame_10 = QFrame(self.frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(760, 30, 111, 81))
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
        self.cpu_usage_9 = QLabel(self.frame_10)
        self.cpu_usage_9.setObjectName(u"cpu_usage_9")
        self.cpu_usage_9.setGeometry(QRect(10, 0, 91, 31))
        self.cpu_usage_9.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpu_usage_9.setStyleSheet(u"font: 700 13pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpu_usage_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.connect = QPushButton(self.frame_10)
        self.connect.setObjectName(u"connect")
        self.connect.setGeometry(QRect(10, 30, 91, 41))
        self.connect.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(52, 52, 52);")
        self.program_path = QLineEdit(self.frame)
        self.program_path.setObjectName(u"program_path")
        self.program_path.setGeometry(QRect(100, 330, 691, 22))
        self.program_path.setStyleSheet(u"background-color: rgb(238, 238, 238);\n"
"font: 10pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.program_path.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.cpu_name_28 = QLabel(self.frame)
        self.cpu_name_28.setObjectName(u"cpu_name_28")
        self.cpu_name_28.setGeometry(QRect(10, 330, 81, 22))
        font4 = QFont()
        font4.setFamilies([u"\ub9d1\uc740 \uace0\ub515"])
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setItalic(False)
        self.cpu_name_28.setFont(font4)
        self.cpu_name_28.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(57, 57, 57);")
        self.cpu_name_28.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.programSearchButton = QPushButton(self.frame)
        self.programSearchButton.setObjectName(u"programSearchButton")
        self.programSearchButton.setGeometry(QRect(800, 330, 51, 22))
        self.programSearchButton.setStyleSheet(u"background-color: rgb(72, 72, 72);\n"
"color: rgb(255, 255, 255);")
        self.frame_9 = QFrame(self.centralwidget)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(660, 410, 151, 61))
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
        self.frame_11 = QFrame(self.centralwidget)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(820, 410, 91, 61))
        self.frame_11.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.gpu0_usage_11 = QLabel(self.frame_11)
        self.gpu0_usage_11.setObjectName(u"gpu0_usage_11")
        self.gpu0_usage_11.setGeometry(QRect(210, 80, 91, 31))
        self.gpu0_usage_11.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_39 = QLabel(self.frame_11)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(170, 80, 81, 31))
        self.label_39.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_40 = QLabel(self.frame_11)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(170, 110, 91, 31))
        self.label_40.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_41 = QLabel(self.frame_11)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(30, 140, 131, 31))
        self.label_41.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.memory_usage_11 = QLabel(self.frame_11)
        self.memory_usage_11.setObjectName(u"memory_usage_11")
        self.memory_usage_11.setGeometry(QRect(170, 140, 91, 31))
        self.memory_usage_11.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.cpu_name_31 = QLabel(self.frame_11)
        self.cpu_name_31.setObjectName(u"cpu_name_31")
        self.cpu_name_31.setGeometry(QRect(280, 30, 21, 21))
        self.cpu_name_31.setFont(font)
        self.cpu_name_31.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")
        self.server_port = QLineEdit(self.frame_11)
        self.server_port.setObjectName(u"server_port")
        self.server_port.setGeometry(QRect(10, 31, 71, 21))
        self.server_port.setStyleSheet(u"background-color: rgb(238, 238, 238);\n"
"font: 10pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.server_port.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cpu_name_27 = QLabel(self.frame_11)
        self.cpu_name_27.setObjectName(u"cpu_name_27")
        self.cpu_name_27.setGeometry(QRect(20, 0, 51, 31))
        self.cpu_name_27.setFont(font)
        self.cpu_name_27.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")
        self.cpu_name_27.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_12 = QFrame(self.centralwidget)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(490, 410, 161, 61))
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
        self.cpu_usage.setText(QCoreApplication.translate("ClientWindow", u"0", None))
        self.label_10.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_11.setText(QCoreApplication.translate("ClientWindow", u"MEMORY:", None))
        self.memory_usage.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.cpu_name_2.setText(QCoreApplication.translate("ClientWindow", u"%", None))
        self.cpu_name_3.setText(QCoreApplication.translate("ClientWindow", u"devicename", None))
        self.onButton.setText(QCoreApplication.translate("ClientWindow", u"ON", None))
        self.offButton.setText(QCoreApplication.translate("ClientWindow", u"OFF", None))
        self.cpu_name_4.setText(QCoreApplication.translate("ClientWindow", u"GPU1", None))
        self.gpu1_usage.setText(QCoreApplication.translate("ClientWindow", u"0", None))
        self.label_13.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_14.setText(QCoreApplication.translate("ClientWindow", u"MEMORY:", None))
        self.memory_usage_2.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.cpu_name_5.setText(QCoreApplication.translate("ClientWindow", u"%", None))
        self.cpu_name_6.setText(QCoreApplication.translate("ClientWindow", u"devicename", None))
        self.cpu_name_7.setText(QCoreApplication.translate("ClientWindow", u"GPU0", None))
        self.label_16.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_17.setText(QCoreApplication.translate("ClientWindow", u"MEMORY:", None))
        self.memory_usage_3.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.cpu_name_8.setText(QCoreApplication.translate("ClientWindow", u"%", None))
        self.gpu0_name.setText(QCoreApplication.translate("ClientWindow", u"devicename", None))
        self.gpu0_usage.setText(QCoreApplication.translate("ClientWindow", u"0", None))
        self.cpu_name_10.setText(QCoreApplication.translate("ClientWindow", u"GPU2", None))
        self.label_19.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_20.setText(QCoreApplication.translate("ClientWindow", u"MEMORY:", None))
        self.memory_usage_4.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.cpu_name_11.setText(QCoreApplication.translate("ClientWindow", u"%", None))
        self.cpu_name_12.setText(QCoreApplication.translate("ClientWindow", u"devicename", None))
        self.gpu2_usage.setText(QCoreApplication.translate("ClientWindow", u"0", None))
        self.cpu_name_13.setText(QCoreApplication.translate("ClientWindow", u"MEMORY", None))
        self.label_23.setText(QCoreApplication.translate("ClientWindow", u"MEMORY:", None))
        self.memory_usage_5.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.cpu_name_14.setText(QCoreApplication.translate("ClientWindow", u"%", None))
        self.cpu_name_15.setText(QCoreApplication.translate("ClientWindow", u"devicename", None))
        self.memory_usage_per.setText(QCoreApplication.translate("ClientWindow", u"0", None))
        self.gpu0_usage_6.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_24.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_25.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_26.setText(QCoreApplication.translate("ClientWindow", u"MEMORY:", None))
        self.memory_usage_6.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.current_time.setText(QCoreApplication.translate("ClientWindow", u"00:00:00", None))
        self.cpu_name_16.setText(QCoreApplication.translate("ClientWindow", u"start time", None))
        self.start_time.setText(QCoreApplication.translate("ClientWindow", u"2024-10-11 00:00:00", None))
        self.cpu_name_26.setText(QCoreApplication.translate("ClientWindow", u"end time", None))
        self.end_time.setText(QCoreApplication.translate("ClientWindow", u"2024-10-11 00:00:00", None))
        self.gpu0_usage_9.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_33.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_34.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_35.setText(QCoreApplication.translate("ClientWindow", u"MEMORY:", None))
        self.memory_usage_9.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.cpu_name_24.setText(QCoreApplication.translate("ClientWindow", u"%", None))
        self.cpu_usage_8.setText(QCoreApplication.translate("ClientWindow", u"0", None))
        self.cpu_usage_9.setText(QCoreApplication.translate("ClientWindow", u"device1", None))
        self.connect.setText(QCoreApplication.translate("ClientWindow", u"CONNECT", None))
        self.program_path.setText(QCoreApplication.translate("ClientWindow", u"C:\\\\Program Files (x86)\\\\Kakao\\\\KakaoTalk\\\\KakaoTalk.exe", None))
        self.cpu_name_28.setText(QCoreApplication.translate("ClientWindow", u"program", None))
        self.programSearchButton.setText(QCoreApplication.translate("ClientWindow", u"search", None))
        self.gpu0_usage_8.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_30.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_31.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_32.setText(QCoreApplication.translate("ClientWindow", u"MEMORY:", None))
        self.memory_usage_8.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.cpu_name_22.setText(QCoreApplication.translate("ClientWindow", u"%", None))
        self.cpu_name_25.setText(QCoreApplication.translate("ClientWindow", u"server IP address", None))
        self.IP_address.setText(QCoreApplication.translate("ClientWindow", u"127.0.0.1", None))
        self.gpu0_usage_11.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_39.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_40.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_41.setText(QCoreApplication.translate("ClientWindow", u"MEMORY:", None))
        self.memory_usage_11.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.cpu_name_31.setText(QCoreApplication.translate("ClientWindow", u"%", None))
        self.server_port.setText(QCoreApplication.translate("ClientWindow", u"8095", None))
        self.cpu_name_27.setText(QCoreApplication.translate("ClientWindow", u"port", None))
        self.gpu0_usage_12.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_42.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_43.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.label_44.setText(QCoreApplication.translate("ClientWindow", u"MEMORY:", None))
        self.memory_usage_12.setText(QCoreApplication.translate("ClientWindow", u"0%", None))
        self.cpu_name_32.setText(QCoreApplication.translate("ClientWindow", u"%", None))
        self.client_name.setText(QCoreApplication.translate("ClientWindow", u"client1", None))
        self.cpu_name_29.setText(QCoreApplication.translate("ClientWindow", u"name", None))
    # retranslateUi


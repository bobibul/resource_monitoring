# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'serverwindowAFNrmK.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1100, 813)
        MainWindow.setMinimumSize(QSize(1100, 0))
        MainWindow.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1063, 3418))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 3400))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_70 = QFrame(self.frame_7)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setMinimumSize(QSize(240, 200))
        self.frame_70.setMaximumSize(QSize(240, 200))
        self.frame_70.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_70.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_70.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_71 = QGridLayout(self.frame_70)
        self.gridLayout_71.setObjectName(u"gridLayout_71")
        self.on_Button_1 = QPushButton(self.frame_70)
        self.on_Button_1.setObjectName(u"on_Button_1")
        self.on_Button_1.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_71.addWidget(self.on_Button_1, 1, 0, 1, 1)

        self.frame_71 = QFrame(self.frame_70)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_71.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_72 = QGridLayout(self.frame_71)
        self.gridLayout_72.setObjectName(u"gridLayout_72")
        self.gpu2usage_1 = QLabel(self.frame_71)
        self.gpu2usage_1.setObjectName(u"gpu2usage_1")
        self.gpu2usage_1.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_1.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_72.addWidget(self.gpu2usage_1, 6, 4, 1, 1)

        self.cpu_name_425 = QLabel(self.frame_71)
        self.cpu_name_425.setObjectName(u"cpu_name_425")
        font = QFont()
        font.setFamilies([u"\ub9d1\uc740 \uace0\ub515"])
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.cpu_name_425.setFont(font)
        self.cpu_name_425.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_72.addWidget(self.cpu_name_425, 3, 5, 1, 1)

        self.cpu_name_426 = QLabel(self.frame_71)
        self.cpu_name_426.setObjectName(u"cpu_name_426")
        self.cpu_name_426.setFont(font)
        self.cpu_name_426.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_72.addWidget(self.cpu_name_426, 6, 5, 1, 1)

        self.cpu_name_427 = QLabel(self.frame_71)
        self.cpu_name_427.setObjectName(u"cpu_name_427")
        font1 = QFont()
        font1.setFamilies([u"\ub9d1\uc740 \uace0\ub515"])
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        self.cpu_name_427.setFont(font1)
        self.cpu_name_427.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_72.addWidget(self.cpu_name_427, 6, 0, 1, 1)

        self.cpuusage_1 = QLabel(self.frame_71)
        self.cpuusage_1.setObjectName(u"cpuusage_1")
        self.cpuusage_1.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_1.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_72.addWidget(self.cpuusage_1, 3, 1, 1, 1)

        self.cpu_name_428 = QLabel(self.frame_71)
        self.cpu_name_428.setObjectName(u"cpu_name_428")
        self.cpu_name_428.setFont(font)
        self.cpu_name_428.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_72.addWidget(self.cpu_name_428, 3, 2, 1, 1)

        self.gpu0usage_1 = QLabel(self.frame_71)
        self.gpu0usage_1.setObjectName(u"gpu0usage_1")
        self.gpu0usage_1.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_1.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_72.addWidget(self.gpu0usage_1, 3, 4, 1, 1)

        self.cpu_name_429 = QLabel(self.frame_71)
        self.cpu_name_429.setObjectName(u"cpu_name_429")
        self.cpu_name_429.setFont(font1)
        self.cpu_name_429.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_72.addWidget(self.cpu_name_429, 3, 3, 1, 1)

        self.cpu_name_430 = QLabel(self.frame_71)
        self.cpu_name_430.setObjectName(u"cpu_name_430")
        self.cpu_name_430.setFont(font1)
        self.cpu_name_430.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_72.addWidget(self.cpu_name_430, 3, 0, 1, 1)

        self.cpu_name_431 = QLabel(self.frame_71)
        self.cpu_name_431.setObjectName(u"cpu_name_431")
        self.cpu_name_431.setFont(font)
        self.cpu_name_431.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_72.addWidget(self.cpu_name_431, 8, 2, 1, 1)

        self.cpu_name_432 = QLabel(self.frame_71)
        self.cpu_name_432.setObjectName(u"cpu_name_432")
        self.cpu_name_432.setFont(font)
        self.cpu_name_432.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_72.addWidget(self.cpu_name_432, 6, 2, 1, 1)

        self.cpu_name_433 = QLabel(self.frame_71)
        self.cpu_name_433.setObjectName(u"cpu_name_433")
        self.cpu_name_433.setFont(font1)
        self.cpu_name_433.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_72.addWidget(self.cpu_name_433, 8, 3, 1, 1)

        self.cpu_name_434 = QLabel(self.frame_71)
        self.cpu_name_434.setObjectName(u"cpu_name_434")
        self.cpu_name_434.setFont(font)
        self.cpu_name_434.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_72.addWidget(self.cpu_name_434, 8, 5, 1, 1)

        self.gpu3usage_1 = QLabel(self.frame_71)
        self.gpu3usage_1.setObjectName(u"gpu3usage_1")
        self.gpu3usage_1.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_1.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_72.addWidget(self.gpu3usage_1, 8, 1, 1, 1)

        self.cpu_name_435 = QLabel(self.frame_71)
        self.cpu_name_435.setObjectName(u"cpu_name_435")
        self.cpu_name_435.setFont(font1)
        self.cpu_name_435.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_72.addWidget(self.cpu_name_435, 8, 0, 1, 1)

        self.device1_1 = QLabel(self.frame_71)
        self.device1_1.setObjectName(u"device1_1")
        font2 = QFont()
        font2.setFamilies([u"\ub9d1\uc740 \uace0\ub515"])
        font2.setPointSize(8)
        font2.setBold(True)
        font2.setItalic(False)
        self.device1_1.setFont(font2)
        self.device1_1.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_1.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_72.addWidget(self.device1_1, 1, 0, 1, 1)

        self.clientipaddress_1 = QLabel(self.frame_71)
        self.clientipaddress_1.setObjectName(u"clientipaddress_1")
        self.clientipaddress_1.setFont(font)
        self.clientipaddress_1.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_1.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_72.addWidget(self.clientipaddress_1, 1, 1, 1, 5)

        self.gpu1usage_1 = QLabel(self.frame_71)
        self.gpu1usage_1.setObjectName(u"gpu1usage_1")
        self.gpu1usage_1.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_1.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_72.addWidget(self.gpu1usage_1, 6, 1, 1, 1)

        self.memoryusage_1 = QLabel(self.frame_71)
        self.memoryusage_1.setObjectName(u"memoryusage_1")
        self.memoryusage_1.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_1.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_72.addWidget(self.memoryusage_1, 8, 4, 1, 1)

        self.cpu_name_436 = QLabel(self.frame_71)
        self.cpu_name_436.setObjectName(u"cpu_name_436")
        self.cpu_name_436.setFont(font1)
        self.cpu_name_436.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_72.addWidget(self.cpu_name_436, 6, 3, 1, 1)


        self.gridLayout_71.addWidget(self.frame_71, 0, 0, 1, 3)

        self.elapsedtime_1 = QLabel(self.frame_70)
        self.elapsedtime_1.setObjectName(u"elapsedtime_1")
        self.elapsedtime_1.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_1.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_71.addWidget(self.elapsedtime_1, 1, 2, 1, 1)

        self.off_Button_1 = QPushButton(self.frame_70)
        self.off_Button_1.setObjectName(u"off_Button_1")
        self.off_Button_1.setEnabled(True)
        self.off_Button_1.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_71.addWidget(self.off_Button_1, 1, 1, 1, 1)


        self.horizontalLayout_9.addWidget(self.frame_70)

        self.frame_72 = QFrame(self.frame_7)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setMinimumSize(QSize(240, 200))
        self.frame_72.setMaximumSize(QSize(240, 200))
        self.frame_72.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_72.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_72.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_73 = QGridLayout(self.frame_72)
        self.gridLayout_73.setObjectName(u"gridLayout_73")
        self.on_Button_2 = QPushButton(self.frame_72)
        self.on_Button_2.setObjectName(u"on_Button_2")
        self.on_Button_2.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_73.addWidget(self.on_Button_2, 1, 0, 1, 1)

        self.frame_73 = QFrame(self.frame_72)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_73.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_74 = QGridLayout(self.frame_73)
        self.gridLayout_74.setObjectName(u"gridLayout_74")
        self.gpu2usage_2 = QLabel(self.frame_73)
        self.gpu2usage_2.setObjectName(u"gpu2usage_2")
        self.gpu2usage_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_2.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_74.addWidget(self.gpu2usage_2, 6, 4, 1, 1)

        self.cpu_name_437 = QLabel(self.frame_73)
        self.cpu_name_437.setObjectName(u"cpu_name_437")
        self.cpu_name_437.setFont(font)
        self.cpu_name_437.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_74.addWidget(self.cpu_name_437, 3, 5, 1, 1)

        self.cpu_name_438 = QLabel(self.frame_73)
        self.cpu_name_438.setObjectName(u"cpu_name_438")
        self.cpu_name_438.setFont(font)
        self.cpu_name_438.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_74.addWidget(self.cpu_name_438, 6, 5, 1, 1)

        self.cpu_name_439 = QLabel(self.frame_73)
        self.cpu_name_439.setObjectName(u"cpu_name_439")
        self.cpu_name_439.setFont(font1)
        self.cpu_name_439.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_74.addWidget(self.cpu_name_439, 6, 0, 1, 1)

        self.cpuusage_2 = QLabel(self.frame_73)
        self.cpuusage_2.setObjectName(u"cpuusage_2")
        self.cpuusage_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_2.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_74.addWidget(self.cpuusage_2, 3, 1, 1, 1)

        self.cpu_name_440 = QLabel(self.frame_73)
        self.cpu_name_440.setObjectName(u"cpu_name_440")
        self.cpu_name_440.setFont(font)
        self.cpu_name_440.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_74.addWidget(self.cpu_name_440, 3, 2, 1, 1)

        self.gpu0usage_2 = QLabel(self.frame_73)
        self.gpu0usage_2.setObjectName(u"gpu0usage_2")
        self.gpu0usage_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_2.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_74.addWidget(self.gpu0usage_2, 3, 4, 1, 1)

        self.cpu_name_441 = QLabel(self.frame_73)
        self.cpu_name_441.setObjectName(u"cpu_name_441")
        self.cpu_name_441.setFont(font1)
        self.cpu_name_441.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_74.addWidget(self.cpu_name_441, 3, 3, 1, 1)

        self.cpu_name_442 = QLabel(self.frame_73)
        self.cpu_name_442.setObjectName(u"cpu_name_442")
        self.cpu_name_442.setFont(font1)
        self.cpu_name_442.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_74.addWidget(self.cpu_name_442, 3, 0, 1, 1)

        self.cpu_name_443 = QLabel(self.frame_73)
        self.cpu_name_443.setObjectName(u"cpu_name_443")
        self.cpu_name_443.setFont(font)
        self.cpu_name_443.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_74.addWidget(self.cpu_name_443, 8, 2, 1, 1)

        self.cpu_name_444 = QLabel(self.frame_73)
        self.cpu_name_444.setObjectName(u"cpu_name_444")
        self.cpu_name_444.setFont(font)
        self.cpu_name_444.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_74.addWidget(self.cpu_name_444, 6, 2, 1, 1)

        self.cpu_name_445 = QLabel(self.frame_73)
        self.cpu_name_445.setObjectName(u"cpu_name_445")
        self.cpu_name_445.setFont(font1)
        self.cpu_name_445.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_74.addWidget(self.cpu_name_445, 8, 3, 1, 1)

        self.cpu_name_446 = QLabel(self.frame_73)
        self.cpu_name_446.setObjectName(u"cpu_name_446")
        self.cpu_name_446.setFont(font)
        self.cpu_name_446.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_74.addWidget(self.cpu_name_446, 8, 5, 1, 1)

        self.gpu3usage_2 = QLabel(self.frame_73)
        self.gpu3usage_2.setObjectName(u"gpu3usage_2")
        self.gpu3usage_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_2.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_74.addWidget(self.gpu3usage_2, 8, 1, 1, 1)

        self.cpu_name_447 = QLabel(self.frame_73)
        self.cpu_name_447.setObjectName(u"cpu_name_447")
        self.cpu_name_447.setFont(font1)
        self.cpu_name_447.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_74.addWidget(self.cpu_name_447, 8, 0, 1, 1)

        self.device1_2 = QLabel(self.frame_73)
        self.device1_2.setObjectName(u"device1_2")
        self.device1_2.setFont(font2)
        self.device1_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_2.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_74.addWidget(self.device1_2, 1, 0, 1, 1)

        self.clientipaddress_2 = QLabel(self.frame_73)
        self.clientipaddress_2.setObjectName(u"clientipaddress_2")
        self.clientipaddress_2.setFont(font)
        self.clientipaddress_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_2.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_74.addWidget(self.clientipaddress_2, 1, 1, 1, 5)

        self.gpu1usage_2 = QLabel(self.frame_73)
        self.gpu1usage_2.setObjectName(u"gpu1usage_2")
        self.gpu1usage_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_2.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_74.addWidget(self.gpu1usage_2, 6, 1, 1, 1)

        self.memoryusage_2 = QLabel(self.frame_73)
        self.memoryusage_2.setObjectName(u"memoryusage_2")
        self.memoryusage_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_2.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_74.addWidget(self.memoryusage_2, 8, 4, 1, 1)

        self.cpu_name_448 = QLabel(self.frame_73)
        self.cpu_name_448.setObjectName(u"cpu_name_448")
        self.cpu_name_448.setFont(font1)
        self.cpu_name_448.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_74.addWidget(self.cpu_name_448, 6, 3, 1, 1)


        self.gridLayout_73.addWidget(self.frame_73, 0, 0, 1, 3)

        self.elapsedtime_2 = QLabel(self.frame_72)
        self.elapsedtime_2.setObjectName(u"elapsedtime_2")
        self.elapsedtime_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_2.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_73.addWidget(self.elapsedtime_2, 1, 2, 1, 1)

        self.off_Button_2 = QPushButton(self.frame_72)
        self.off_Button_2.setObjectName(u"off_Button_2")
        self.off_Button_2.setEnabled(True)
        self.off_Button_2.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_73.addWidget(self.off_Button_2, 1, 1, 1, 1)


        self.horizontalLayout_9.addWidget(self.frame_72)

        self.frame_74 = QFrame(self.frame_7)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setMinimumSize(QSize(240, 200))
        self.frame_74.setMaximumSize(QSize(240, 200))
        self.frame_74.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_74.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_74.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_75 = QGridLayout(self.frame_74)
        self.gridLayout_75.setObjectName(u"gridLayout_75")
        self.on_Button_3 = QPushButton(self.frame_74)
        self.on_Button_3.setObjectName(u"on_Button_3")
        self.on_Button_3.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_75.addWidget(self.on_Button_3, 1, 0, 1, 1)

        self.frame_75 = QFrame(self.frame_74)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_75.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_76 = QGridLayout(self.frame_75)
        self.gridLayout_76.setObjectName(u"gridLayout_76")
        self.gpu2usage_3 = QLabel(self.frame_75)
        self.gpu2usage_3.setObjectName(u"gpu2usage_3")
        self.gpu2usage_3.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_3.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_76.addWidget(self.gpu2usage_3, 6, 4, 1, 1)

        self.cpu_name_449 = QLabel(self.frame_75)
        self.cpu_name_449.setObjectName(u"cpu_name_449")
        self.cpu_name_449.setFont(font)
        self.cpu_name_449.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_76.addWidget(self.cpu_name_449, 3, 5, 1, 1)

        self.cpu_name_450 = QLabel(self.frame_75)
        self.cpu_name_450.setObjectName(u"cpu_name_450")
        self.cpu_name_450.setFont(font)
        self.cpu_name_450.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_76.addWidget(self.cpu_name_450, 6, 5, 1, 1)

        self.cpu_name_451 = QLabel(self.frame_75)
        self.cpu_name_451.setObjectName(u"cpu_name_451")
        self.cpu_name_451.setFont(font1)
        self.cpu_name_451.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_76.addWidget(self.cpu_name_451, 6, 0, 1, 1)

        self.cpuusage_3 = QLabel(self.frame_75)
        self.cpuusage_3.setObjectName(u"cpuusage_3")
        self.cpuusage_3.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_3.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_76.addWidget(self.cpuusage_3, 3, 1, 1, 1)

        self.cpu_name_452 = QLabel(self.frame_75)
        self.cpu_name_452.setObjectName(u"cpu_name_452")
        self.cpu_name_452.setFont(font)
        self.cpu_name_452.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_76.addWidget(self.cpu_name_452, 3, 2, 1, 1)

        self.gpu0usage_3 = QLabel(self.frame_75)
        self.gpu0usage_3.setObjectName(u"gpu0usage_3")
        self.gpu0usage_3.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_3.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_76.addWidget(self.gpu0usage_3, 3, 4, 1, 1)

        self.cpu_name_453 = QLabel(self.frame_75)
        self.cpu_name_453.setObjectName(u"cpu_name_453")
        self.cpu_name_453.setFont(font1)
        self.cpu_name_453.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_76.addWidget(self.cpu_name_453, 3, 3, 1, 1)

        self.cpu_name_454 = QLabel(self.frame_75)
        self.cpu_name_454.setObjectName(u"cpu_name_454")
        self.cpu_name_454.setFont(font1)
        self.cpu_name_454.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_76.addWidget(self.cpu_name_454, 3, 0, 1, 1)

        self.cpu_name_455 = QLabel(self.frame_75)
        self.cpu_name_455.setObjectName(u"cpu_name_455")
        self.cpu_name_455.setFont(font)
        self.cpu_name_455.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_76.addWidget(self.cpu_name_455, 8, 2, 1, 1)

        self.cpu_name_456 = QLabel(self.frame_75)
        self.cpu_name_456.setObjectName(u"cpu_name_456")
        self.cpu_name_456.setFont(font)
        self.cpu_name_456.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_76.addWidget(self.cpu_name_456, 6, 2, 1, 1)

        self.cpu_name_457 = QLabel(self.frame_75)
        self.cpu_name_457.setObjectName(u"cpu_name_457")
        self.cpu_name_457.setFont(font1)
        self.cpu_name_457.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_76.addWidget(self.cpu_name_457, 8, 3, 1, 1)

        self.cpu_name_458 = QLabel(self.frame_75)
        self.cpu_name_458.setObjectName(u"cpu_name_458")
        self.cpu_name_458.setFont(font)
        self.cpu_name_458.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_76.addWidget(self.cpu_name_458, 8, 5, 1, 1)

        self.gpu3usage_3 = QLabel(self.frame_75)
        self.gpu3usage_3.setObjectName(u"gpu3usage_3")
        self.gpu3usage_3.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_3.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_76.addWidget(self.gpu3usage_3, 8, 1, 1, 1)

        self.cpu_name_459 = QLabel(self.frame_75)
        self.cpu_name_459.setObjectName(u"cpu_name_459")
        self.cpu_name_459.setFont(font1)
        self.cpu_name_459.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_76.addWidget(self.cpu_name_459, 8, 0, 1, 1)

        self.device1_3 = QLabel(self.frame_75)
        self.device1_3.setObjectName(u"device1_3")
        self.device1_3.setFont(font2)
        self.device1_3.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_3.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_76.addWidget(self.device1_3, 1, 0, 1, 1)

        self.clientipaddress_3 = QLabel(self.frame_75)
        self.clientipaddress_3.setObjectName(u"clientipaddress_3")
        self.clientipaddress_3.setFont(font)
        self.clientipaddress_3.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_3.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_76.addWidget(self.clientipaddress_3, 1, 1, 1, 5)

        self.gpu1usage_3 = QLabel(self.frame_75)
        self.gpu1usage_3.setObjectName(u"gpu1usage_3")
        self.gpu1usage_3.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_3.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_76.addWidget(self.gpu1usage_3, 6, 1, 1, 1)

        self.memoryusage_3 = QLabel(self.frame_75)
        self.memoryusage_3.setObjectName(u"memoryusage_3")
        self.memoryusage_3.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_3.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_76.addWidget(self.memoryusage_3, 8, 4, 1, 1)

        self.cpu_name_460 = QLabel(self.frame_75)
        self.cpu_name_460.setObjectName(u"cpu_name_460")
        self.cpu_name_460.setFont(font1)
        self.cpu_name_460.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_76.addWidget(self.cpu_name_460, 6, 3, 1, 1)


        self.gridLayout_75.addWidget(self.frame_75, 0, 0, 1, 3)

        self.elapsedtime_3 = QLabel(self.frame_74)
        self.elapsedtime_3.setObjectName(u"elapsedtime_3")
        self.elapsedtime_3.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_3.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_75.addWidget(self.elapsedtime_3, 1, 2, 1, 1)

        self.off_Button_3 = QPushButton(self.frame_74)
        self.off_Button_3.setObjectName(u"off_Button_3")
        self.off_Button_3.setEnabled(True)
        self.off_Button_3.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_75.addWidget(self.off_Button_3, 1, 1, 1, 1)


        self.horizontalLayout_9.addWidget(self.frame_74)

        self.frame_76 = QFrame(self.frame_7)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setMinimumSize(QSize(240, 200))
        self.frame_76.setMaximumSize(QSize(240, 200))
        self.frame_76.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_76.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_76.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_77 = QGridLayout(self.frame_76)
        self.gridLayout_77.setObjectName(u"gridLayout_77")
        self.on_Button_4 = QPushButton(self.frame_76)
        self.on_Button_4.setObjectName(u"on_Button_4")
        self.on_Button_4.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_77.addWidget(self.on_Button_4, 1, 0, 1, 1)

        self.frame_77 = QFrame(self.frame_76)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_77.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_78 = QGridLayout(self.frame_77)
        self.gridLayout_78.setObjectName(u"gridLayout_78")
        self.gpu2usage_4 = QLabel(self.frame_77)
        self.gpu2usage_4.setObjectName(u"gpu2usage_4")
        self.gpu2usage_4.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_4.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_78.addWidget(self.gpu2usage_4, 6, 4, 1, 1)

        self.cpu_name_461 = QLabel(self.frame_77)
        self.cpu_name_461.setObjectName(u"cpu_name_461")
        self.cpu_name_461.setFont(font)
        self.cpu_name_461.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_78.addWidget(self.cpu_name_461, 3, 5, 1, 1)

        self.cpu_name_462 = QLabel(self.frame_77)
        self.cpu_name_462.setObjectName(u"cpu_name_462")
        self.cpu_name_462.setFont(font)
        self.cpu_name_462.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_78.addWidget(self.cpu_name_462, 6, 5, 1, 1)

        self.cpu_name_463 = QLabel(self.frame_77)
        self.cpu_name_463.setObjectName(u"cpu_name_463")
        self.cpu_name_463.setFont(font1)
        self.cpu_name_463.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_78.addWidget(self.cpu_name_463, 6, 0, 1, 1)

        self.cpuusage_4 = QLabel(self.frame_77)
        self.cpuusage_4.setObjectName(u"cpuusage_4")
        self.cpuusage_4.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_4.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_78.addWidget(self.cpuusage_4, 3, 1, 1, 1)

        self.cpu_name_464 = QLabel(self.frame_77)
        self.cpu_name_464.setObjectName(u"cpu_name_464")
        self.cpu_name_464.setFont(font)
        self.cpu_name_464.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_78.addWidget(self.cpu_name_464, 3, 2, 1, 1)

        self.gpu0usage_4 = QLabel(self.frame_77)
        self.gpu0usage_4.setObjectName(u"gpu0usage_4")
        self.gpu0usage_4.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_4.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_78.addWidget(self.gpu0usage_4, 3, 4, 1, 1)

        self.cpu_name_465 = QLabel(self.frame_77)
        self.cpu_name_465.setObjectName(u"cpu_name_465")
        self.cpu_name_465.setFont(font1)
        self.cpu_name_465.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_78.addWidget(self.cpu_name_465, 3, 3, 1, 1)

        self.cpu_name_466 = QLabel(self.frame_77)
        self.cpu_name_466.setObjectName(u"cpu_name_466")
        self.cpu_name_466.setFont(font1)
        self.cpu_name_466.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_78.addWidget(self.cpu_name_466, 3, 0, 1, 1)

        self.cpu_name_467 = QLabel(self.frame_77)
        self.cpu_name_467.setObjectName(u"cpu_name_467")
        self.cpu_name_467.setFont(font)
        self.cpu_name_467.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_78.addWidget(self.cpu_name_467, 8, 2, 1, 1)

        self.cpu_name_468 = QLabel(self.frame_77)
        self.cpu_name_468.setObjectName(u"cpu_name_468")
        self.cpu_name_468.setFont(font)
        self.cpu_name_468.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_78.addWidget(self.cpu_name_468, 6, 2, 1, 1)

        self.cpu_name_469 = QLabel(self.frame_77)
        self.cpu_name_469.setObjectName(u"cpu_name_469")
        self.cpu_name_469.setFont(font1)
        self.cpu_name_469.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_78.addWidget(self.cpu_name_469, 8, 3, 1, 1)

        self.cpu_name_470 = QLabel(self.frame_77)
        self.cpu_name_470.setObjectName(u"cpu_name_470")
        self.cpu_name_470.setFont(font)
        self.cpu_name_470.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_78.addWidget(self.cpu_name_470, 8, 5, 1, 1)

        self.gpu3usage_4 = QLabel(self.frame_77)
        self.gpu3usage_4.setObjectName(u"gpu3usage_4")
        self.gpu3usage_4.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_4.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_78.addWidget(self.gpu3usage_4, 8, 1, 1, 1)

        self.cpu_name_471 = QLabel(self.frame_77)
        self.cpu_name_471.setObjectName(u"cpu_name_471")
        self.cpu_name_471.setFont(font1)
        self.cpu_name_471.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_78.addWidget(self.cpu_name_471, 8, 0, 1, 1)

        self.device1_4 = QLabel(self.frame_77)
        self.device1_4.setObjectName(u"device1_4")
        self.device1_4.setFont(font2)
        self.device1_4.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_4.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_78.addWidget(self.device1_4, 1, 0, 1, 1)

        self.clientipaddress_4 = QLabel(self.frame_77)
        self.clientipaddress_4.setObjectName(u"clientipaddress_4")
        self.clientipaddress_4.setFont(font)
        self.clientipaddress_4.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_4.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_78.addWidget(self.clientipaddress_4, 1, 1, 1, 5)

        self.gpu1usage_4 = QLabel(self.frame_77)
        self.gpu1usage_4.setObjectName(u"gpu1usage_4")
        self.gpu1usage_4.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_4.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_78.addWidget(self.gpu1usage_4, 6, 1, 1, 1)

        self.memoryusage_4 = QLabel(self.frame_77)
        self.memoryusage_4.setObjectName(u"memoryusage_4")
        self.memoryusage_4.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_4.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_78.addWidget(self.memoryusage_4, 8, 4, 1, 1)

        self.cpu_name_472 = QLabel(self.frame_77)
        self.cpu_name_472.setObjectName(u"cpu_name_472")
        self.cpu_name_472.setFont(font1)
        self.cpu_name_472.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_78.addWidget(self.cpu_name_472, 6, 3, 1, 1)


        self.gridLayout_77.addWidget(self.frame_77, 0, 0, 1, 3)

        self.elapsedtime_4 = QLabel(self.frame_76)
        self.elapsedtime_4.setObjectName(u"elapsedtime_4")
        self.elapsedtime_4.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_4.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_77.addWidget(self.elapsedtime_4, 1, 2, 1, 1)

        self.off_Button_4 = QPushButton(self.frame_76)
        self.off_Button_4.setObjectName(u"off_Button_4")
        self.off_Button_4.setEnabled(True)
        self.off_Button_4.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_77.addWidget(self.off_Button_4, 1, 1, 1, 1)


        self.horizontalLayout_9.addWidget(self.frame_76)


        self.verticalLayout_3.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_78 = QFrame(self.frame_8)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setMinimumSize(QSize(240, 200))
        self.frame_78.setMaximumSize(QSize(240, 200))
        self.frame_78.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_78.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_78.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_79 = QGridLayout(self.frame_78)
        self.gridLayout_79.setObjectName(u"gridLayout_79")
        self.on_Button_5 = QPushButton(self.frame_78)
        self.on_Button_5.setObjectName(u"on_Button_5")
        self.on_Button_5.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_79.addWidget(self.on_Button_5, 1, 0, 1, 1)

        self.frame_79 = QFrame(self.frame_78)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_79.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_80 = QGridLayout(self.frame_79)
        self.gridLayout_80.setObjectName(u"gridLayout_80")
        self.gpu2usage_5 = QLabel(self.frame_79)
        self.gpu2usage_5.setObjectName(u"gpu2usage_5")
        self.gpu2usage_5.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_5.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_80.addWidget(self.gpu2usage_5, 6, 4, 1, 1)

        self.cpu_name_473 = QLabel(self.frame_79)
        self.cpu_name_473.setObjectName(u"cpu_name_473")
        self.cpu_name_473.setFont(font)
        self.cpu_name_473.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_80.addWidget(self.cpu_name_473, 3, 5, 1, 1)

        self.cpu_name_474 = QLabel(self.frame_79)
        self.cpu_name_474.setObjectName(u"cpu_name_474")
        self.cpu_name_474.setFont(font)
        self.cpu_name_474.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_80.addWidget(self.cpu_name_474, 6, 5, 1, 1)

        self.cpu_name_475 = QLabel(self.frame_79)
        self.cpu_name_475.setObjectName(u"cpu_name_475")
        self.cpu_name_475.setFont(font1)
        self.cpu_name_475.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_80.addWidget(self.cpu_name_475, 6, 0, 1, 1)

        self.cpuusage_5 = QLabel(self.frame_79)
        self.cpuusage_5.setObjectName(u"cpuusage_5")
        self.cpuusage_5.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_5.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_80.addWidget(self.cpuusage_5, 3, 1, 1, 1)

        self.cpu_name_476 = QLabel(self.frame_79)
        self.cpu_name_476.setObjectName(u"cpu_name_476")
        self.cpu_name_476.setFont(font)
        self.cpu_name_476.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_80.addWidget(self.cpu_name_476, 3, 2, 1, 1)

        self.gpu0usage_5 = QLabel(self.frame_79)
        self.gpu0usage_5.setObjectName(u"gpu0usage_5")
        self.gpu0usage_5.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_5.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_80.addWidget(self.gpu0usage_5, 3, 4, 1, 1)

        self.cpu_name_477 = QLabel(self.frame_79)
        self.cpu_name_477.setObjectName(u"cpu_name_477")
        self.cpu_name_477.setFont(font1)
        self.cpu_name_477.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_80.addWidget(self.cpu_name_477, 3, 3, 1, 1)

        self.cpu_name_478 = QLabel(self.frame_79)
        self.cpu_name_478.setObjectName(u"cpu_name_478")
        self.cpu_name_478.setFont(font1)
        self.cpu_name_478.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_80.addWidget(self.cpu_name_478, 3, 0, 1, 1)

        self.cpu_name_479 = QLabel(self.frame_79)
        self.cpu_name_479.setObjectName(u"cpu_name_479")
        self.cpu_name_479.setFont(font)
        self.cpu_name_479.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_80.addWidget(self.cpu_name_479, 8, 2, 1, 1)

        self.cpu_name_480 = QLabel(self.frame_79)
        self.cpu_name_480.setObjectName(u"cpu_name_480")
        self.cpu_name_480.setFont(font)
        self.cpu_name_480.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_80.addWidget(self.cpu_name_480, 6, 2, 1, 1)

        self.cpu_name_481 = QLabel(self.frame_79)
        self.cpu_name_481.setObjectName(u"cpu_name_481")
        self.cpu_name_481.setFont(font1)
        self.cpu_name_481.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_80.addWidget(self.cpu_name_481, 8, 3, 1, 1)

        self.cpu_name_482 = QLabel(self.frame_79)
        self.cpu_name_482.setObjectName(u"cpu_name_482")
        self.cpu_name_482.setFont(font)
        self.cpu_name_482.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_80.addWidget(self.cpu_name_482, 8, 5, 1, 1)

        self.gpu3usage_5 = QLabel(self.frame_79)
        self.gpu3usage_5.setObjectName(u"gpu3usage_5")
        self.gpu3usage_5.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_5.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_80.addWidget(self.gpu3usage_5, 8, 1, 1, 1)

        self.cpu_name_483 = QLabel(self.frame_79)
        self.cpu_name_483.setObjectName(u"cpu_name_483")
        self.cpu_name_483.setFont(font1)
        self.cpu_name_483.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_80.addWidget(self.cpu_name_483, 8, 0, 1, 1)

        self.device1_5 = QLabel(self.frame_79)
        self.device1_5.setObjectName(u"device1_5")
        self.device1_5.setFont(font2)
        self.device1_5.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_5.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_80.addWidget(self.device1_5, 1, 0, 1, 1)

        self.clientipaddress_5 = QLabel(self.frame_79)
        self.clientipaddress_5.setObjectName(u"clientipaddress_5")
        self.clientipaddress_5.setFont(font)
        self.clientipaddress_5.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_5.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_80.addWidget(self.clientipaddress_5, 1, 1, 1, 5)

        self.gpu1usage_5 = QLabel(self.frame_79)
        self.gpu1usage_5.setObjectName(u"gpu1usage_5")
        self.gpu1usage_5.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_5.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_80.addWidget(self.gpu1usage_5, 6, 1, 1, 1)

        self.memoryusage_5 = QLabel(self.frame_79)
        self.memoryusage_5.setObjectName(u"memoryusage_5")
        self.memoryusage_5.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_5.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_80.addWidget(self.memoryusage_5, 8, 4, 1, 1)

        self.cpu_name_484 = QLabel(self.frame_79)
        self.cpu_name_484.setObjectName(u"cpu_name_484")
        self.cpu_name_484.setFont(font1)
        self.cpu_name_484.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_80.addWidget(self.cpu_name_484, 6, 3, 1, 1)


        self.gridLayout_79.addWidget(self.frame_79, 0, 0, 1, 3)

        self.elapsedtime_5 = QLabel(self.frame_78)
        self.elapsedtime_5.setObjectName(u"elapsedtime_5")
        self.elapsedtime_5.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_5.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_79.addWidget(self.elapsedtime_5, 1, 2, 1, 1)

        self.off_Button_5 = QPushButton(self.frame_78)
        self.off_Button_5.setObjectName(u"off_Button_5")
        self.off_Button_5.setEnabled(True)
        self.off_Button_5.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_79.addWidget(self.off_Button_5, 1, 1, 1, 1)


        self.horizontalLayout_10.addWidget(self.frame_78)

        self.frame_80 = QFrame(self.frame_8)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setMinimumSize(QSize(240, 200))
        self.frame_80.setMaximumSize(QSize(240, 200))
        self.frame_80.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_80.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_80.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_81 = QGridLayout(self.frame_80)
        self.gridLayout_81.setObjectName(u"gridLayout_81")
        self.on_Button_6 = QPushButton(self.frame_80)
        self.on_Button_6.setObjectName(u"on_Button_6")
        self.on_Button_6.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_81.addWidget(self.on_Button_6, 1, 0, 1, 1)

        self.frame_81 = QFrame(self.frame_80)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_81.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_82 = QGridLayout(self.frame_81)
        self.gridLayout_82.setObjectName(u"gridLayout_82")
        self.gpu2usage_6 = QLabel(self.frame_81)
        self.gpu2usage_6.setObjectName(u"gpu2usage_6")
        self.gpu2usage_6.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_6.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_82.addWidget(self.gpu2usage_6, 6, 4, 1, 1)

        self.cpu_name_485 = QLabel(self.frame_81)
        self.cpu_name_485.setObjectName(u"cpu_name_485")
        self.cpu_name_485.setFont(font)
        self.cpu_name_485.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_82.addWidget(self.cpu_name_485, 3, 5, 1, 1)

        self.cpu_name_486 = QLabel(self.frame_81)
        self.cpu_name_486.setObjectName(u"cpu_name_486")
        self.cpu_name_486.setFont(font)
        self.cpu_name_486.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_82.addWidget(self.cpu_name_486, 6, 5, 1, 1)

        self.cpu_name_487 = QLabel(self.frame_81)
        self.cpu_name_487.setObjectName(u"cpu_name_487")
        self.cpu_name_487.setFont(font1)
        self.cpu_name_487.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_82.addWidget(self.cpu_name_487, 6, 0, 1, 1)

        self.cpuusage_6 = QLabel(self.frame_81)
        self.cpuusage_6.setObjectName(u"cpuusage_6")
        self.cpuusage_6.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_6.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_82.addWidget(self.cpuusage_6, 3, 1, 1, 1)

        self.cpu_name_488 = QLabel(self.frame_81)
        self.cpu_name_488.setObjectName(u"cpu_name_488")
        self.cpu_name_488.setFont(font)
        self.cpu_name_488.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_82.addWidget(self.cpu_name_488, 3, 2, 1, 1)

        self.gpu0usage_6 = QLabel(self.frame_81)
        self.gpu0usage_6.setObjectName(u"gpu0usage_6")
        self.gpu0usage_6.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_6.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_82.addWidget(self.gpu0usage_6, 3, 4, 1, 1)

        self.cpu_name_489 = QLabel(self.frame_81)
        self.cpu_name_489.setObjectName(u"cpu_name_489")
        self.cpu_name_489.setFont(font1)
        self.cpu_name_489.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_82.addWidget(self.cpu_name_489, 3, 3, 1, 1)

        self.cpu_name_490 = QLabel(self.frame_81)
        self.cpu_name_490.setObjectName(u"cpu_name_490")
        self.cpu_name_490.setFont(font1)
        self.cpu_name_490.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_82.addWidget(self.cpu_name_490, 3, 0, 1, 1)

        self.cpu_name_491 = QLabel(self.frame_81)
        self.cpu_name_491.setObjectName(u"cpu_name_491")
        self.cpu_name_491.setFont(font)
        self.cpu_name_491.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_82.addWidget(self.cpu_name_491, 8, 2, 1, 1)

        self.cpu_name_492 = QLabel(self.frame_81)
        self.cpu_name_492.setObjectName(u"cpu_name_492")
        self.cpu_name_492.setFont(font)
        self.cpu_name_492.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_82.addWidget(self.cpu_name_492, 6, 2, 1, 1)

        self.cpu_name_493 = QLabel(self.frame_81)
        self.cpu_name_493.setObjectName(u"cpu_name_493")
        self.cpu_name_493.setFont(font1)
        self.cpu_name_493.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_82.addWidget(self.cpu_name_493, 8, 3, 1, 1)

        self.cpu_name_494 = QLabel(self.frame_81)
        self.cpu_name_494.setObjectName(u"cpu_name_494")
        self.cpu_name_494.setFont(font)
        self.cpu_name_494.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_82.addWidget(self.cpu_name_494, 8, 5, 1, 1)

        self.gpu3usage_6 = QLabel(self.frame_81)
        self.gpu3usage_6.setObjectName(u"gpu3usage_6")
        self.gpu3usage_6.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_6.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_82.addWidget(self.gpu3usage_6, 8, 1, 1, 1)

        self.cpu_name_495 = QLabel(self.frame_81)
        self.cpu_name_495.setObjectName(u"cpu_name_495")
        self.cpu_name_495.setFont(font1)
        self.cpu_name_495.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_82.addWidget(self.cpu_name_495, 8, 0, 1, 1)

        self.device1_6 = QLabel(self.frame_81)
        self.device1_6.setObjectName(u"device1_6")
        self.device1_6.setFont(font2)
        self.device1_6.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_6.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_82.addWidget(self.device1_6, 1, 0, 1, 1)

        self.clientipaddress_6 = QLabel(self.frame_81)
        self.clientipaddress_6.setObjectName(u"clientipaddress_6")
        self.clientipaddress_6.setFont(font)
        self.clientipaddress_6.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_6.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_82.addWidget(self.clientipaddress_6, 1, 1, 1, 5)

        self.gpu1usage_6 = QLabel(self.frame_81)
        self.gpu1usage_6.setObjectName(u"gpu1usage_6")
        self.gpu1usage_6.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_6.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_82.addWidget(self.gpu1usage_6, 6, 1, 1, 1)

        self.memoryusage_6 = QLabel(self.frame_81)
        self.memoryusage_6.setObjectName(u"memoryusage_6")
        self.memoryusage_6.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_6.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_82.addWidget(self.memoryusage_6, 8, 4, 1, 1)

        self.cpu_name_496 = QLabel(self.frame_81)
        self.cpu_name_496.setObjectName(u"cpu_name_496")
        self.cpu_name_496.setFont(font1)
        self.cpu_name_496.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_82.addWidget(self.cpu_name_496, 6, 3, 1, 1)


        self.gridLayout_81.addWidget(self.frame_81, 0, 0, 1, 3)

        self.elapsedtime_6 = QLabel(self.frame_80)
        self.elapsedtime_6.setObjectName(u"elapsedtime_6")
        self.elapsedtime_6.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_6.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_81.addWidget(self.elapsedtime_6, 1, 2, 1, 1)

        self.off_Button_6 = QPushButton(self.frame_80)
        self.off_Button_6.setObjectName(u"off_Button_6")
        self.off_Button_6.setEnabled(True)
        self.off_Button_6.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_81.addWidget(self.off_Button_6, 1, 1, 1, 1)


        self.horizontalLayout_10.addWidget(self.frame_80)

        self.frame_82 = QFrame(self.frame_8)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setMinimumSize(QSize(240, 200))
        self.frame_82.setMaximumSize(QSize(240, 200))
        self.frame_82.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_82.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_82.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_83 = QGridLayout(self.frame_82)
        self.gridLayout_83.setObjectName(u"gridLayout_83")
        self.on_Button_7 = QPushButton(self.frame_82)
        self.on_Button_7.setObjectName(u"on_Button_7")
        self.on_Button_7.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_83.addWidget(self.on_Button_7, 1, 0, 1, 1)

        self.frame_83 = QFrame(self.frame_82)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_83.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_84 = QGridLayout(self.frame_83)
        self.gridLayout_84.setObjectName(u"gridLayout_84")
        self.gpu2usage_7 = QLabel(self.frame_83)
        self.gpu2usage_7.setObjectName(u"gpu2usage_7")
        self.gpu2usage_7.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_7.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_84.addWidget(self.gpu2usage_7, 6, 4, 1, 1)

        self.cpu_name_497 = QLabel(self.frame_83)
        self.cpu_name_497.setObjectName(u"cpu_name_497")
        self.cpu_name_497.setFont(font)
        self.cpu_name_497.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_84.addWidget(self.cpu_name_497, 3, 5, 1, 1)

        self.cpu_name_498 = QLabel(self.frame_83)
        self.cpu_name_498.setObjectName(u"cpu_name_498")
        self.cpu_name_498.setFont(font)
        self.cpu_name_498.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_84.addWidget(self.cpu_name_498, 6, 5, 1, 1)

        self.cpu_name_499 = QLabel(self.frame_83)
        self.cpu_name_499.setObjectName(u"cpu_name_499")
        self.cpu_name_499.setFont(font1)
        self.cpu_name_499.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_84.addWidget(self.cpu_name_499, 6, 0, 1, 1)

        self.cpuusage_7 = QLabel(self.frame_83)
        self.cpuusage_7.setObjectName(u"cpuusage_7")
        self.cpuusage_7.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_7.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_84.addWidget(self.cpuusage_7, 3, 1, 1, 1)

        self.cpu_name_500 = QLabel(self.frame_83)
        self.cpu_name_500.setObjectName(u"cpu_name_500")
        self.cpu_name_500.setFont(font)
        self.cpu_name_500.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_84.addWidget(self.cpu_name_500, 3, 2, 1, 1)

        self.gpu0usage_7 = QLabel(self.frame_83)
        self.gpu0usage_7.setObjectName(u"gpu0usage_7")
        self.gpu0usage_7.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_7.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_84.addWidget(self.gpu0usage_7, 3, 4, 1, 1)

        self.cpu_name_501 = QLabel(self.frame_83)
        self.cpu_name_501.setObjectName(u"cpu_name_501")
        self.cpu_name_501.setFont(font1)
        self.cpu_name_501.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_84.addWidget(self.cpu_name_501, 3, 3, 1, 1)

        self.cpu_name_502 = QLabel(self.frame_83)
        self.cpu_name_502.setObjectName(u"cpu_name_502")
        self.cpu_name_502.setFont(font1)
        self.cpu_name_502.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_84.addWidget(self.cpu_name_502, 3, 0, 1, 1)

        self.cpu_name_503 = QLabel(self.frame_83)
        self.cpu_name_503.setObjectName(u"cpu_name_503")
        self.cpu_name_503.setFont(font)
        self.cpu_name_503.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_84.addWidget(self.cpu_name_503, 8, 2, 1, 1)

        self.cpu_name_504 = QLabel(self.frame_83)
        self.cpu_name_504.setObjectName(u"cpu_name_504")
        self.cpu_name_504.setFont(font)
        self.cpu_name_504.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_84.addWidget(self.cpu_name_504, 6, 2, 1, 1)

        self.cpu_name_505 = QLabel(self.frame_83)
        self.cpu_name_505.setObjectName(u"cpu_name_505")
        self.cpu_name_505.setFont(font1)
        self.cpu_name_505.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_84.addWidget(self.cpu_name_505, 8, 3, 1, 1)

        self.cpu_name_506 = QLabel(self.frame_83)
        self.cpu_name_506.setObjectName(u"cpu_name_506")
        self.cpu_name_506.setFont(font)
        self.cpu_name_506.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_84.addWidget(self.cpu_name_506, 8, 5, 1, 1)

        self.gpu3usage_7 = QLabel(self.frame_83)
        self.gpu3usage_7.setObjectName(u"gpu3usage_7")
        self.gpu3usage_7.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_7.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_84.addWidget(self.gpu3usage_7, 8, 1, 1, 1)

        self.cpu_name_507 = QLabel(self.frame_83)
        self.cpu_name_507.setObjectName(u"cpu_name_507")
        self.cpu_name_507.setFont(font1)
        self.cpu_name_507.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_84.addWidget(self.cpu_name_507, 8, 0, 1, 1)

        self.device1_7 = QLabel(self.frame_83)
        self.device1_7.setObjectName(u"device1_7")
        self.device1_7.setFont(font2)
        self.device1_7.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_7.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_84.addWidget(self.device1_7, 1, 0, 1, 1)

        self.clientipaddress_7 = QLabel(self.frame_83)
        self.clientipaddress_7.setObjectName(u"clientipaddress_7")
        self.clientipaddress_7.setFont(font)
        self.clientipaddress_7.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_7.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_84.addWidget(self.clientipaddress_7, 1, 1, 1, 5)

        self.gpu1usage_7 = QLabel(self.frame_83)
        self.gpu1usage_7.setObjectName(u"gpu1usage_7")
        self.gpu1usage_7.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_7.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_84.addWidget(self.gpu1usage_7, 6, 1, 1, 1)

        self.memoryusage_7 = QLabel(self.frame_83)
        self.memoryusage_7.setObjectName(u"memoryusage_7")
        self.memoryusage_7.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_7.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_84.addWidget(self.memoryusage_7, 8, 4, 1, 1)

        self.cpu_name_508 = QLabel(self.frame_83)
        self.cpu_name_508.setObjectName(u"cpu_name_508")
        self.cpu_name_508.setFont(font1)
        self.cpu_name_508.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_84.addWidget(self.cpu_name_508, 6, 3, 1, 1)


        self.gridLayout_83.addWidget(self.frame_83, 0, 0, 1, 3)

        self.elapsedtime_7 = QLabel(self.frame_82)
        self.elapsedtime_7.setObjectName(u"elapsedtime_7")
        self.elapsedtime_7.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_7.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_83.addWidget(self.elapsedtime_7, 1, 2, 1, 1)

        self.off_Button_7 = QPushButton(self.frame_82)
        self.off_Button_7.setObjectName(u"off_Button_7")
        self.off_Button_7.setEnabled(True)
        self.off_Button_7.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_83.addWidget(self.off_Button_7, 1, 1, 1, 1)


        self.horizontalLayout_10.addWidget(self.frame_82)

        self.frame_84 = QFrame(self.frame_8)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setMinimumSize(QSize(240, 200))
        self.frame_84.setMaximumSize(QSize(240, 200))
        self.frame_84.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_84.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_84.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_85 = QGridLayout(self.frame_84)
        self.gridLayout_85.setObjectName(u"gridLayout_85")
        self.on_Button_8 = QPushButton(self.frame_84)
        self.on_Button_8.setObjectName(u"on_Button_8")
        self.on_Button_8.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_85.addWidget(self.on_Button_8, 1, 0, 1, 1)

        self.frame_85 = QFrame(self.frame_84)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_85.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_86 = QGridLayout(self.frame_85)
        self.gridLayout_86.setObjectName(u"gridLayout_86")
        self.gpu2usage_8 = QLabel(self.frame_85)
        self.gpu2usage_8.setObjectName(u"gpu2usage_8")
        self.gpu2usage_8.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_8.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_86.addWidget(self.gpu2usage_8, 6, 4, 1, 1)

        self.cpu_name_509 = QLabel(self.frame_85)
        self.cpu_name_509.setObjectName(u"cpu_name_509")
        self.cpu_name_509.setFont(font)
        self.cpu_name_509.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_86.addWidget(self.cpu_name_509, 3, 5, 1, 1)

        self.cpu_name_510 = QLabel(self.frame_85)
        self.cpu_name_510.setObjectName(u"cpu_name_510")
        self.cpu_name_510.setFont(font)
        self.cpu_name_510.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_86.addWidget(self.cpu_name_510, 6, 5, 1, 1)

        self.cpu_name_511 = QLabel(self.frame_85)
        self.cpu_name_511.setObjectName(u"cpu_name_511")
        self.cpu_name_511.setFont(font1)
        self.cpu_name_511.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_86.addWidget(self.cpu_name_511, 6, 0, 1, 1)

        self.cpuusage_8 = QLabel(self.frame_85)
        self.cpuusage_8.setObjectName(u"cpuusage_8")
        self.cpuusage_8.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_8.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_86.addWidget(self.cpuusage_8, 3, 1, 1, 1)

        self.cpu_name_512 = QLabel(self.frame_85)
        self.cpu_name_512.setObjectName(u"cpu_name_512")
        self.cpu_name_512.setFont(font)
        self.cpu_name_512.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_86.addWidget(self.cpu_name_512, 3, 2, 1, 1)

        self.gpu0usage_8 = QLabel(self.frame_85)
        self.gpu0usage_8.setObjectName(u"gpu0usage_8")
        self.gpu0usage_8.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_8.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_86.addWidget(self.gpu0usage_8, 3, 4, 1, 1)

        self.cpu_name_513 = QLabel(self.frame_85)
        self.cpu_name_513.setObjectName(u"cpu_name_513")
        self.cpu_name_513.setFont(font1)
        self.cpu_name_513.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_86.addWidget(self.cpu_name_513, 3, 3, 1, 1)

        self.cpu_name_514 = QLabel(self.frame_85)
        self.cpu_name_514.setObjectName(u"cpu_name_514")
        self.cpu_name_514.setFont(font1)
        self.cpu_name_514.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_86.addWidget(self.cpu_name_514, 3, 0, 1, 1)

        self.cpu_name_515 = QLabel(self.frame_85)
        self.cpu_name_515.setObjectName(u"cpu_name_515")
        self.cpu_name_515.setFont(font)
        self.cpu_name_515.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_86.addWidget(self.cpu_name_515, 8, 2, 1, 1)

        self.cpu_name_516 = QLabel(self.frame_85)
        self.cpu_name_516.setObjectName(u"cpu_name_516")
        self.cpu_name_516.setFont(font)
        self.cpu_name_516.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_86.addWidget(self.cpu_name_516, 6, 2, 1, 1)

        self.cpu_name_517 = QLabel(self.frame_85)
        self.cpu_name_517.setObjectName(u"cpu_name_517")
        self.cpu_name_517.setFont(font1)
        self.cpu_name_517.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_86.addWidget(self.cpu_name_517, 8, 3, 1, 1)

        self.cpu_name_518 = QLabel(self.frame_85)
        self.cpu_name_518.setObjectName(u"cpu_name_518")
        self.cpu_name_518.setFont(font)
        self.cpu_name_518.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_86.addWidget(self.cpu_name_518, 8, 5, 1, 1)

        self.gpu3usage_8 = QLabel(self.frame_85)
        self.gpu3usage_8.setObjectName(u"gpu3usage_8")
        self.gpu3usage_8.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_8.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_86.addWidget(self.gpu3usage_8, 8, 1, 1, 1)

        self.cpu_name_519 = QLabel(self.frame_85)
        self.cpu_name_519.setObjectName(u"cpu_name_519")
        self.cpu_name_519.setFont(font1)
        self.cpu_name_519.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_86.addWidget(self.cpu_name_519, 8, 0, 1, 1)

        self.device1_8 = QLabel(self.frame_85)
        self.device1_8.setObjectName(u"device1_8")
        self.device1_8.setFont(font2)
        self.device1_8.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_8.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_86.addWidget(self.device1_8, 1, 0, 1, 1)

        self.clientipaddress_8 = QLabel(self.frame_85)
        self.clientipaddress_8.setObjectName(u"clientipaddress_8")
        self.clientipaddress_8.setFont(font)
        self.clientipaddress_8.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_8.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_86.addWidget(self.clientipaddress_8, 1, 1, 1, 5)

        self.gpu1usage_8 = QLabel(self.frame_85)
        self.gpu1usage_8.setObjectName(u"gpu1usage_8")
        self.gpu1usage_8.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_8.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_86.addWidget(self.gpu1usage_8, 6, 1, 1, 1)

        self.memoryusage_8 = QLabel(self.frame_85)
        self.memoryusage_8.setObjectName(u"memoryusage_8")
        self.memoryusage_8.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_8.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_86.addWidget(self.memoryusage_8, 8, 4, 1, 1)

        self.cpu_name_520 = QLabel(self.frame_85)
        self.cpu_name_520.setObjectName(u"cpu_name_520")
        self.cpu_name_520.setFont(font1)
        self.cpu_name_520.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_86.addWidget(self.cpu_name_520, 6, 3, 1, 1)


        self.gridLayout_85.addWidget(self.frame_85, 0, 0, 1, 3)

        self.elapsedtime_8 = QLabel(self.frame_84)
        self.elapsedtime_8.setObjectName(u"elapsedtime_8")
        self.elapsedtime_8.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_8.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_85.addWidget(self.elapsedtime_8, 1, 2, 1, 1)

        self.off_Button_8 = QPushButton(self.frame_84)
        self.off_Button_8.setObjectName(u"off_Button_8")
        self.off_Button_8.setEnabled(True)
        self.off_Button_8.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_85.addWidget(self.off_Button_8, 1, 1, 1, 1)


        self.horizontalLayout_10.addWidget(self.frame_84)


        self.verticalLayout_3.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_86 = QFrame(self.frame_9)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setMinimumSize(QSize(240, 200))
        self.frame_86.setMaximumSize(QSize(240, 200))
        self.frame_86.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_86.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_86.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_87 = QGridLayout(self.frame_86)
        self.gridLayout_87.setObjectName(u"gridLayout_87")
        self.on_Button_9 = QPushButton(self.frame_86)
        self.on_Button_9.setObjectName(u"on_Button_9")
        self.on_Button_9.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_87.addWidget(self.on_Button_9, 1, 0, 1, 1)

        self.frame_87 = QFrame(self.frame_86)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_87.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_88 = QGridLayout(self.frame_87)
        self.gridLayout_88.setObjectName(u"gridLayout_88")
        self.gpu2usage_9 = QLabel(self.frame_87)
        self.gpu2usage_9.setObjectName(u"gpu2usage_9")
        self.gpu2usage_9.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_9.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_9.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_88.addWidget(self.gpu2usage_9, 6, 4, 1, 1)

        self.cpu_name_521 = QLabel(self.frame_87)
        self.cpu_name_521.setObjectName(u"cpu_name_521")
        self.cpu_name_521.setFont(font)
        self.cpu_name_521.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_88.addWidget(self.cpu_name_521, 3, 5, 1, 1)

        self.cpu_name_522 = QLabel(self.frame_87)
        self.cpu_name_522.setObjectName(u"cpu_name_522")
        self.cpu_name_522.setFont(font)
        self.cpu_name_522.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_88.addWidget(self.cpu_name_522, 6, 5, 1, 1)

        self.cpu_name_523 = QLabel(self.frame_87)
        self.cpu_name_523.setObjectName(u"cpu_name_523")
        self.cpu_name_523.setFont(font1)
        self.cpu_name_523.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_88.addWidget(self.cpu_name_523, 6, 0, 1, 1)

        self.cpuusage_9 = QLabel(self.frame_87)
        self.cpuusage_9.setObjectName(u"cpuusage_9")
        self.cpuusage_9.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_9.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_9.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_88.addWidget(self.cpuusage_9, 3, 1, 1, 1)

        self.cpu_name_524 = QLabel(self.frame_87)
        self.cpu_name_524.setObjectName(u"cpu_name_524")
        self.cpu_name_524.setFont(font)
        self.cpu_name_524.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_88.addWidget(self.cpu_name_524, 3, 2, 1, 1)

        self.gpu0usage_9 = QLabel(self.frame_87)
        self.gpu0usage_9.setObjectName(u"gpu0usage_9")
        self.gpu0usage_9.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_9.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_9.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_88.addWidget(self.gpu0usage_9, 3, 4, 1, 1)

        self.cpu_name_525 = QLabel(self.frame_87)
        self.cpu_name_525.setObjectName(u"cpu_name_525")
        self.cpu_name_525.setFont(font1)
        self.cpu_name_525.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_88.addWidget(self.cpu_name_525, 3, 3, 1, 1)

        self.cpu_name_526 = QLabel(self.frame_87)
        self.cpu_name_526.setObjectName(u"cpu_name_526")
        self.cpu_name_526.setFont(font1)
        self.cpu_name_526.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_88.addWidget(self.cpu_name_526, 3, 0, 1, 1)

        self.cpu_name_527 = QLabel(self.frame_87)
        self.cpu_name_527.setObjectName(u"cpu_name_527")
        self.cpu_name_527.setFont(font)
        self.cpu_name_527.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_88.addWidget(self.cpu_name_527, 8, 2, 1, 1)

        self.cpu_name_528 = QLabel(self.frame_87)
        self.cpu_name_528.setObjectName(u"cpu_name_528")
        self.cpu_name_528.setFont(font)
        self.cpu_name_528.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_88.addWidget(self.cpu_name_528, 6, 2, 1, 1)

        self.cpu_name_529 = QLabel(self.frame_87)
        self.cpu_name_529.setObjectName(u"cpu_name_529")
        self.cpu_name_529.setFont(font1)
        self.cpu_name_529.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_88.addWidget(self.cpu_name_529, 8, 3, 1, 1)

        self.cpu_name_530 = QLabel(self.frame_87)
        self.cpu_name_530.setObjectName(u"cpu_name_530")
        self.cpu_name_530.setFont(font)
        self.cpu_name_530.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_88.addWidget(self.cpu_name_530, 8, 5, 1, 1)

        self.gpu3usage_9 = QLabel(self.frame_87)
        self.gpu3usage_9.setObjectName(u"gpu3usage_9")
        self.gpu3usage_9.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_9.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_9.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_88.addWidget(self.gpu3usage_9, 8, 1, 1, 1)

        self.cpu_name_531 = QLabel(self.frame_87)
        self.cpu_name_531.setObjectName(u"cpu_name_531")
        self.cpu_name_531.setFont(font1)
        self.cpu_name_531.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_88.addWidget(self.cpu_name_531, 8, 0, 1, 1)

        self.device1_9 = QLabel(self.frame_87)
        self.device1_9.setObjectName(u"device1_9")
        self.device1_9.setFont(font2)
        self.device1_9.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_9.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_88.addWidget(self.device1_9, 1, 0, 1, 1)

        self.clientipaddress_9 = QLabel(self.frame_87)
        self.clientipaddress_9.setObjectName(u"clientipaddress_9")
        self.clientipaddress_9.setFont(font)
        self.clientipaddress_9.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_9.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_88.addWidget(self.clientipaddress_9, 1, 1, 1, 5)

        self.gpu1usage_9 = QLabel(self.frame_87)
        self.gpu1usage_9.setObjectName(u"gpu1usage_9")
        self.gpu1usage_9.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_9.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_9.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_88.addWidget(self.gpu1usage_9, 6, 1, 1, 1)

        self.memoryusage_9 = QLabel(self.frame_87)
        self.memoryusage_9.setObjectName(u"memoryusage_9")
        self.memoryusage_9.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_9.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_9.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_88.addWidget(self.memoryusage_9, 8, 4, 1, 1)

        self.cpu_name_532 = QLabel(self.frame_87)
        self.cpu_name_532.setObjectName(u"cpu_name_532")
        self.cpu_name_532.setFont(font1)
        self.cpu_name_532.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_88.addWidget(self.cpu_name_532, 6, 3, 1, 1)


        self.gridLayout_87.addWidget(self.frame_87, 0, 0, 1, 3)

        self.elapsedtime_9 = QLabel(self.frame_86)
        self.elapsedtime_9.setObjectName(u"elapsedtime_9")
        self.elapsedtime_9.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_9.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_87.addWidget(self.elapsedtime_9, 1, 2, 1, 1)

        self.off_Button_9 = QPushButton(self.frame_86)
        self.off_Button_9.setObjectName(u"off_Button_9")
        self.off_Button_9.setEnabled(True)
        self.off_Button_9.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_87.addWidget(self.off_Button_9, 1, 1, 1, 1)


        self.horizontalLayout_11.addWidget(self.frame_86)

        self.frame_88 = QFrame(self.frame_9)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setMinimumSize(QSize(240, 200))
        self.frame_88.setMaximumSize(QSize(240, 200))
        self.frame_88.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_88.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_88.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_89 = QGridLayout(self.frame_88)
        self.gridLayout_89.setObjectName(u"gridLayout_89")
        self.on_Button_10 = QPushButton(self.frame_88)
        self.on_Button_10.setObjectName(u"on_Button_10")
        self.on_Button_10.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_89.addWidget(self.on_Button_10, 1, 0, 1, 1)

        self.frame_89 = QFrame(self.frame_88)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_89.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_90 = QGridLayout(self.frame_89)
        self.gridLayout_90.setObjectName(u"gridLayout_90")
        self.gpu2usage_10 = QLabel(self.frame_89)
        self.gpu2usage_10.setObjectName(u"gpu2usage_10")
        self.gpu2usage_10.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_10.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_10.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_90.addWidget(self.gpu2usage_10, 6, 4, 1, 1)

        self.cpu_name_533 = QLabel(self.frame_89)
        self.cpu_name_533.setObjectName(u"cpu_name_533")
        self.cpu_name_533.setFont(font)
        self.cpu_name_533.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_90.addWidget(self.cpu_name_533, 3, 5, 1, 1)

        self.cpu_name_534 = QLabel(self.frame_89)
        self.cpu_name_534.setObjectName(u"cpu_name_534")
        self.cpu_name_534.setFont(font)
        self.cpu_name_534.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_90.addWidget(self.cpu_name_534, 6, 5, 1, 1)

        self.cpu_name_535 = QLabel(self.frame_89)
        self.cpu_name_535.setObjectName(u"cpu_name_535")
        self.cpu_name_535.setFont(font1)
        self.cpu_name_535.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_90.addWidget(self.cpu_name_535, 6, 0, 1, 1)

        self.cpuusage_10 = QLabel(self.frame_89)
        self.cpuusage_10.setObjectName(u"cpuusage_10")
        self.cpuusage_10.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_10.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_10.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_90.addWidget(self.cpuusage_10, 3, 1, 1, 1)

        self.cpu_name_536 = QLabel(self.frame_89)
        self.cpu_name_536.setObjectName(u"cpu_name_536")
        self.cpu_name_536.setFont(font)
        self.cpu_name_536.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_90.addWidget(self.cpu_name_536, 3, 2, 1, 1)

        self.gpu0usage_10 = QLabel(self.frame_89)
        self.gpu0usage_10.setObjectName(u"gpu0usage_10")
        self.gpu0usage_10.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_10.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_10.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_90.addWidget(self.gpu0usage_10, 3, 4, 1, 1)

        self.cpu_name_537 = QLabel(self.frame_89)
        self.cpu_name_537.setObjectName(u"cpu_name_537")
        self.cpu_name_537.setFont(font1)
        self.cpu_name_537.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_90.addWidget(self.cpu_name_537, 3, 3, 1, 1)

        self.cpu_name_538 = QLabel(self.frame_89)
        self.cpu_name_538.setObjectName(u"cpu_name_538")
        self.cpu_name_538.setFont(font1)
        self.cpu_name_538.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_90.addWidget(self.cpu_name_538, 3, 0, 1, 1)

        self.cpu_name_539 = QLabel(self.frame_89)
        self.cpu_name_539.setObjectName(u"cpu_name_539")
        self.cpu_name_539.setFont(font)
        self.cpu_name_539.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_90.addWidget(self.cpu_name_539, 8, 2, 1, 1)

        self.cpu_name_540 = QLabel(self.frame_89)
        self.cpu_name_540.setObjectName(u"cpu_name_540")
        self.cpu_name_540.setFont(font)
        self.cpu_name_540.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_90.addWidget(self.cpu_name_540, 6, 2, 1, 1)

        self.cpu_name_541 = QLabel(self.frame_89)
        self.cpu_name_541.setObjectName(u"cpu_name_541")
        self.cpu_name_541.setFont(font1)
        self.cpu_name_541.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_90.addWidget(self.cpu_name_541, 8, 3, 1, 1)

        self.cpu_name_542 = QLabel(self.frame_89)
        self.cpu_name_542.setObjectName(u"cpu_name_542")
        self.cpu_name_542.setFont(font)
        self.cpu_name_542.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_90.addWidget(self.cpu_name_542, 8, 5, 1, 1)

        self.gpu3usage_10 = QLabel(self.frame_89)
        self.gpu3usage_10.setObjectName(u"gpu3usage_10")
        self.gpu3usage_10.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_10.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_10.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_90.addWidget(self.gpu3usage_10, 8, 1, 1, 1)

        self.cpu_name_543 = QLabel(self.frame_89)
        self.cpu_name_543.setObjectName(u"cpu_name_543")
        self.cpu_name_543.setFont(font1)
        self.cpu_name_543.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_90.addWidget(self.cpu_name_543, 8, 0, 1, 1)

        self.device1_10 = QLabel(self.frame_89)
        self.device1_10.setObjectName(u"device1_10")
        self.device1_10.setFont(font2)
        self.device1_10.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_10.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_90.addWidget(self.device1_10, 1, 0, 1, 1)

        self.clientipaddress_10 = QLabel(self.frame_89)
        self.clientipaddress_10.setObjectName(u"clientipaddress_10")
        self.clientipaddress_10.setFont(font)
        self.clientipaddress_10.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_10.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_90.addWidget(self.clientipaddress_10, 1, 1, 1, 5)

        self.gpu1usage_10 = QLabel(self.frame_89)
        self.gpu1usage_10.setObjectName(u"gpu1usage_10")
        self.gpu1usage_10.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_10.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_10.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_90.addWidget(self.gpu1usage_10, 6, 1, 1, 1)

        self.memoryusage_10 = QLabel(self.frame_89)
        self.memoryusage_10.setObjectName(u"memoryusage_10")
        self.memoryusage_10.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_10.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_10.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_90.addWidget(self.memoryusage_10, 8, 4, 1, 1)

        self.cpu_name_544 = QLabel(self.frame_89)
        self.cpu_name_544.setObjectName(u"cpu_name_544")
        self.cpu_name_544.setFont(font1)
        self.cpu_name_544.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_90.addWidget(self.cpu_name_544, 6, 3, 1, 1)


        self.gridLayout_89.addWidget(self.frame_89, 0, 0, 1, 3)

        self.elapsedtime_10 = QLabel(self.frame_88)
        self.elapsedtime_10.setObjectName(u"elapsedtime_10")
        self.elapsedtime_10.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_10.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_89.addWidget(self.elapsedtime_10, 1, 2, 1, 1)

        self.off_Button_10 = QPushButton(self.frame_88)
        self.off_Button_10.setObjectName(u"off_Button_10")
        self.off_Button_10.setEnabled(True)
        self.off_Button_10.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_89.addWidget(self.off_Button_10, 1, 1, 1, 1)


        self.horizontalLayout_11.addWidget(self.frame_88)

        self.frame_90 = QFrame(self.frame_9)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setMinimumSize(QSize(240, 200))
        self.frame_90.setMaximumSize(QSize(240, 200))
        self.frame_90.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_90.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_90.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_91 = QGridLayout(self.frame_90)
        self.gridLayout_91.setObjectName(u"gridLayout_91")
        self.on_Button_11 = QPushButton(self.frame_90)
        self.on_Button_11.setObjectName(u"on_Button_11")
        self.on_Button_11.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_91.addWidget(self.on_Button_11, 1, 0, 1, 1)

        self.frame_91 = QFrame(self.frame_90)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_91.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_92 = QGridLayout(self.frame_91)
        self.gridLayout_92.setObjectName(u"gridLayout_92")
        self.gpu2usage_11 = QLabel(self.frame_91)
        self.gpu2usage_11.setObjectName(u"gpu2usage_11")
        self.gpu2usage_11.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_11.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_92.addWidget(self.gpu2usage_11, 6, 4, 1, 1)

        self.cpu_name_545 = QLabel(self.frame_91)
        self.cpu_name_545.setObjectName(u"cpu_name_545")
        self.cpu_name_545.setFont(font)
        self.cpu_name_545.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_92.addWidget(self.cpu_name_545, 3, 5, 1, 1)

        self.cpu_name_546 = QLabel(self.frame_91)
        self.cpu_name_546.setObjectName(u"cpu_name_546")
        self.cpu_name_546.setFont(font)
        self.cpu_name_546.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_92.addWidget(self.cpu_name_546, 6, 5, 1, 1)

        self.cpu_name_547 = QLabel(self.frame_91)
        self.cpu_name_547.setObjectName(u"cpu_name_547")
        self.cpu_name_547.setFont(font1)
        self.cpu_name_547.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_92.addWidget(self.cpu_name_547, 6, 0, 1, 1)

        self.cpuusage_11 = QLabel(self.frame_91)
        self.cpuusage_11.setObjectName(u"cpuusage_11")
        self.cpuusage_11.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_11.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_92.addWidget(self.cpuusage_11, 3, 1, 1, 1)

        self.cpu_name_548 = QLabel(self.frame_91)
        self.cpu_name_548.setObjectName(u"cpu_name_548")
        self.cpu_name_548.setFont(font)
        self.cpu_name_548.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_92.addWidget(self.cpu_name_548, 3, 2, 1, 1)

        self.gpu0usage_11 = QLabel(self.frame_91)
        self.gpu0usage_11.setObjectName(u"gpu0usage_11")
        self.gpu0usage_11.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_11.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_92.addWidget(self.gpu0usage_11, 3, 4, 1, 1)

        self.cpu_name_549 = QLabel(self.frame_91)
        self.cpu_name_549.setObjectName(u"cpu_name_549")
        self.cpu_name_549.setFont(font1)
        self.cpu_name_549.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_92.addWidget(self.cpu_name_549, 3, 3, 1, 1)

        self.cpu_name_550 = QLabel(self.frame_91)
        self.cpu_name_550.setObjectName(u"cpu_name_550")
        self.cpu_name_550.setFont(font1)
        self.cpu_name_550.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_92.addWidget(self.cpu_name_550, 3, 0, 1, 1)

        self.cpu_name_551 = QLabel(self.frame_91)
        self.cpu_name_551.setObjectName(u"cpu_name_551")
        self.cpu_name_551.setFont(font)
        self.cpu_name_551.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_92.addWidget(self.cpu_name_551, 8, 2, 1, 1)

        self.cpu_name_552 = QLabel(self.frame_91)
        self.cpu_name_552.setObjectName(u"cpu_name_552")
        self.cpu_name_552.setFont(font)
        self.cpu_name_552.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_92.addWidget(self.cpu_name_552, 6, 2, 1, 1)

        self.cpu_name_553 = QLabel(self.frame_91)
        self.cpu_name_553.setObjectName(u"cpu_name_553")
        self.cpu_name_553.setFont(font1)
        self.cpu_name_553.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_92.addWidget(self.cpu_name_553, 8, 3, 1, 1)

        self.cpu_name_554 = QLabel(self.frame_91)
        self.cpu_name_554.setObjectName(u"cpu_name_554")
        self.cpu_name_554.setFont(font)
        self.cpu_name_554.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_92.addWidget(self.cpu_name_554, 8, 5, 1, 1)

        self.gpu3usage_11 = QLabel(self.frame_91)
        self.gpu3usage_11.setObjectName(u"gpu3usage_11")
        self.gpu3usage_11.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_11.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_92.addWidget(self.gpu3usage_11, 8, 1, 1, 1)

        self.cpu_name_555 = QLabel(self.frame_91)
        self.cpu_name_555.setObjectName(u"cpu_name_555")
        self.cpu_name_555.setFont(font1)
        self.cpu_name_555.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_92.addWidget(self.cpu_name_555, 8, 0, 1, 1)

        self.device1_11 = QLabel(self.frame_91)
        self.device1_11.setObjectName(u"device1_11")
        self.device1_11.setFont(font2)
        self.device1_11.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_11.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_92.addWidget(self.device1_11, 1, 0, 1, 1)

        self.clientipaddress_11 = QLabel(self.frame_91)
        self.clientipaddress_11.setObjectName(u"clientipaddress_11")
        self.clientipaddress_11.setFont(font)
        self.clientipaddress_11.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_11.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_92.addWidget(self.clientipaddress_11, 1, 1, 1, 5)

        self.gpu1usage_11 = QLabel(self.frame_91)
        self.gpu1usage_11.setObjectName(u"gpu1usage_11")
        self.gpu1usage_11.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_11.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_92.addWidget(self.gpu1usage_11, 6, 1, 1, 1)

        self.memoryusage_11 = QLabel(self.frame_91)
        self.memoryusage_11.setObjectName(u"memoryusage_11")
        self.memoryusage_11.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_11.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_92.addWidget(self.memoryusage_11, 8, 4, 1, 1)

        self.cpu_name_556 = QLabel(self.frame_91)
        self.cpu_name_556.setObjectName(u"cpu_name_556")
        self.cpu_name_556.setFont(font1)
        self.cpu_name_556.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_92.addWidget(self.cpu_name_556, 6, 3, 1, 1)


        self.gridLayout_91.addWidget(self.frame_91, 0, 0, 1, 3)

        self.elapsedtime_11 = QLabel(self.frame_90)
        self.elapsedtime_11.setObjectName(u"elapsedtime_11")
        self.elapsedtime_11.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_11.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_91.addWidget(self.elapsedtime_11, 1, 2, 1, 1)

        self.off_Button_11 = QPushButton(self.frame_90)
        self.off_Button_11.setObjectName(u"off_Button_11")
        self.off_Button_11.setEnabled(True)
        self.off_Button_11.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_91.addWidget(self.off_Button_11, 1, 1, 1, 1)


        self.horizontalLayout_11.addWidget(self.frame_90)

        self.frame_92 = QFrame(self.frame_9)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setMinimumSize(QSize(240, 200))
        self.frame_92.setMaximumSize(QSize(240, 200))
        self.frame_92.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_92.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_92.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_93 = QGridLayout(self.frame_92)
        self.gridLayout_93.setObjectName(u"gridLayout_93")
        self.on_Button_12 = QPushButton(self.frame_92)
        self.on_Button_12.setObjectName(u"on_Button_12")
        self.on_Button_12.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_93.addWidget(self.on_Button_12, 1, 0, 1, 1)

        self.frame_93 = QFrame(self.frame_92)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_93.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_94 = QGridLayout(self.frame_93)
        self.gridLayout_94.setObjectName(u"gridLayout_94")
        self.gpu2usage_12 = QLabel(self.frame_93)
        self.gpu2usage_12.setObjectName(u"gpu2usage_12")
        self.gpu2usage_12.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_12.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_12.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_94.addWidget(self.gpu2usage_12, 6, 4, 1, 1)

        self.cpu_name_557 = QLabel(self.frame_93)
        self.cpu_name_557.setObjectName(u"cpu_name_557")
        self.cpu_name_557.setFont(font)
        self.cpu_name_557.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_94.addWidget(self.cpu_name_557, 3, 5, 1, 1)

        self.cpu_name_558 = QLabel(self.frame_93)
        self.cpu_name_558.setObjectName(u"cpu_name_558")
        self.cpu_name_558.setFont(font)
        self.cpu_name_558.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_94.addWidget(self.cpu_name_558, 6, 5, 1, 1)

        self.cpu_name_559 = QLabel(self.frame_93)
        self.cpu_name_559.setObjectName(u"cpu_name_559")
        self.cpu_name_559.setFont(font1)
        self.cpu_name_559.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_94.addWidget(self.cpu_name_559, 6, 0, 1, 1)

        self.cpuusage_12 = QLabel(self.frame_93)
        self.cpuusage_12.setObjectName(u"cpuusage_12")
        self.cpuusage_12.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_12.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_12.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_94.addWidget(self.cpuusage_12, 3, 1, 1, 1)

        self.cpu_name_560 = QLabel(self.frame_93)
        self.cpu_name_560.setObjectName(u"cpu_name_560")
        self.cpu_name_560.setFont(font)
        self.cpu_name_560.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_94.addWidget(self.cpu_name_560, 3, 2, 1, 1)

        self.gpu0usage_12 = QLabel(self.frame_93)
        self.gpu0usage_12.setObjectName(u"gpu0usage_12")
        self.gpu0usage_12.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_12.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_12.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_94.addWidget(self.gpu0usage_12, 3, 4, 1, 1)

        self.cpu_name_561 = QLabel(self.frame_93)
        self.cpu_name_561.setObjectName(u"cpu_name_561")
        self.cpu_name_561.setFont(font1)
        self.cpu_name_561.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_94.addWidget(self.cpu_name_561, 3, 3, 1, 1)

        self.cpu_name_562 = QLabel(self.frame_93)
        self.cpu_name_562.setObjectName(u"cpu_name_562")
        self.cpu_name_562.setFont(font1)
        self.cpu_name_562.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_94.addWidget(self.cpu_name_562, 3, 0, 1, 1)

        self.cpu_name_563 = QLabel(self.frame_93)
        self.cpu_name_563.setObjectName(u"cpu_name_563")
        self.cpu_name_563.setFont(font)
        self.cpu_name_563.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_94.addWidget(self.cpu_name_563, 8, 2, 1, 1)

        self.cpu_name_564 = QLabel(self.frame_93)
        self.cpu_name_564.setObjectName(u"cpu_name_564")
        self.cpu_name_564.setFont(font)
        self.cpu_name_564.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_94.addWidget(self.cpu_name_564, 6, 2, 1, 1)

        self.cpu_name_565 = QLabel(self.frame_93)
        self.cpu_name_565.setObjectName(u"cpu_name_565")
        self.cpu_name_565.setFont(font1)
        self.cpu_name_565.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_94.addWidget(self.cpu_name_565, 8, 3, 1, 1)

        self.cpu_name_566 = QLabel(self.frame_93)
        self.cpu_name_566.setObjectName(u"cpu_name_566")
        self.cpu_name_566.setFont(font)
        self.cpu_name_566.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_94.addWidget(self.cpu_name_566, 8, 5, 1, 1)

        self.gpu3usage_12 = QLabel(self.frame_93)
        self.gpu3usage_12.setObjectName(u"gpu3usage_12")
        self.gpu3usage_12.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_12.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_12.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_94.addWidget(self.gpu3usage_12, 8, 1, 1, 1)

        self.cpu_name_567 = QLabel(self.frame_93)
        self.cpu_name_567.setObjectName(u"cpu_name_567")
        self.cpu_name_567.setFont(font1)
        self.cpu_name_567.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_94.addWidget(self.cpu_name_567, 8, 0, 1, 1)

        self.device1_12 = QLabel(self.frame_93)
        self.device1_12.setObjectName(u"device1_12")
        self.device1_12.setFont(font2)
        self.device1_12.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_12.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_94.addWidget(self.device1_12, 1, 0, 1, 1)

        self.clientipaddress_12 = QLabel(self.frame_93)
        self.clientipaddress_12.setObjectName(u"clientipaddress_12")
        self.clientipaddress_12.setFont(font)
        self.clientipaddress_12.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_12.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_94.addWidget(self.clientipaddress_12, 1, 1, 1, 5)

        self.gpu1usage_12 = QLabel(self.frame_93)
        self.gpu1usage_12.setObjectName(u"gpu1usage_12")
        self.gpu1usage_12.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_12.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_12.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_94.addWidget(self.gpu1usage_12, 6, 1, 1, 1)

        self.memoryusage_12 = QLabel(self.frame_93)
        self.memoryusage_12.setObjectName(u"memoryusage_12")
        self.memoryusage_12.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_12.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_12.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_94.addWidget(self.memoryusage_12, 8, 4, 1, 1)

        self.cpu_name_568 = QLabel(self.frame_93)
        self.cpu_name_568.setObjectName(u"cpu_name_568")
        self.cpu_name_568.setFont(font1)
        self.cpu_name_568.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_94.addWidget(self.cpu_name_568, 6, 3, 1, 1)


        self.gridLayout_93.addWidget(self.frame_93, 0, 0, 1, 3)

        self.elapsedtime_12 = QLabel(self.frame_92)
        self.elapsedtime_12.setObjectName(u"elapsedtime_12")
        self.elapsedtime_12.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_12.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_93.addWidget(self.elapsedtime_12, 1, 2, 1, 1)

        self.off_Button_12 = QPushButton(self.frame_92)
        self.off_Button_12.setObjectName(u"off_Button_12")
        self.off_Button_12.setEnabled(True)
        self.off_Button_12.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_93.addWidget(self.off_Button_12, 1, 1, 1, 1)


        self.horizontalLayout_11.addWidget(self.frame_92)


        self.verticalLayout_3.addWidget(self.frame_9)

        self.frame_15 = QFrame(self.frame_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_94 = QFrame(self.frame_15)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setMinimumSize(QSize(240, 200))
        self.frame_94.setMaximumSize(QSize(240, 200))
        self.frame_94.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_94.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_94.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_95 = QGridLayout(self.frame_94)
        self.gridLayout_95.setObjectName(u"gridLayout_95")
        self.on_Button_13 = QPushButton(self.frame_94)
        self.on_Button_13.setObjectName(u"on_Button_13")
        self.on_Button_13.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_95.addWidget(self.on_Button_13, 1, 0, 1, 1)

        self.frame_95 = QFrame(self.frame_94)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_95.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_96 = QGridLayout(self.frame_95)
        self.gridLayout_96.setObjectName(u"gridLayout_96")
        self.gpu2usage_13 = QLabel(self.frame_95)
        self.gpu2usage_13.setObjectName(u"gpu2usage_13")
        self.gpu2usage_13.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_13.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_13.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_96.addWidget(self.gpu2usage_13, 6, 4, 1, 1)

        self.cpu_name_569 = QLabel(self.frame_95)
        self.cpu_name_569.setObjectName(u"cpu_name_569")
        self.cpu_name_569.setFont(font)
        self.cpu_name_569.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_96.addWidget(self.cpu_name_569, 3, 5, 1, 1)

        self.cpu_name_570 = QLabel(self.frame_95)
        self.cpu_name_570.setObjectName(u"cpu_name_570")
        self.cpu_name_570.setFont(font)
        self.cpu_name_570.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_96.addWidget(self.cpu_name_570, 6, 5, 1, 1)

        self.cpu_name_571 = QLabel(self.frame_95)
        self.cpu_name_571.setObjectName(u"cpu_name_571")
        self.cpu_name_571.setFont(font1)
        self.cpu_name_571.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_96.addWidget(self.cpu_name_571, 6, 0, 1, 1)

        self.cpuusage_13 = QLabel(self.frame_95)
        self.cpuusage_13.setObjectName(u"cpuusage_13")
        self.cpuusage_13.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_13.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_13.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_96.addWidget(self.cpuusage_13, 3, 1, 1, 1)

        self.cpu_name_572 = QLabel(self.frame_95)
        self.cpu_name_572.setObjectName(u"cpu_name_572")
        self.cpu_name_572.setFont(font)
        self.cpu_name_572.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_96.addWidget(self.cpu_name_572, 3, 2, 1, 1)

        self.gpu0usage_13 = QLabel(self.frame_95)
        self.gpu0usage_13.setObjectName(u"gpu0usage_13")
        self.gpu0usage_13.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_13.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_13.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_96.addWidget(self.gpu0usage_13, 3, 4, 1, 1)

        self.cpu_name_573 = QLabel(self.frame_95)
        self.cpu_name_573.setObjectName(u"cpu_name_573")
        self.cpu_name_573.setFont(font1)
        self.cpu_name_573.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_96.addWidget(self.cpu_name_573, 3, 3, 1, 1)

        self.cpu_name_574 = QLabel(self.frame_95)
        self.cpu_name_574.setObjectName(u"cpu_name_574")
        self.cpu_name_574.setFont(font1)
        self.cpu_name_574.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_96.addWidget(self.cpu_name_574, 3, 0, 1, 1)

        self.cpu_name_575 = QLabel(self.frame_95)
        self.cpu_name_575.setObjectName(u"cpu_name_575")
        self.cpu_name_575.setFont(font)
        self.cpu_name_575.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_96.addWidget(self.cpu_name_575, 8, 2, 1, 1)

        self.cpu_name_576 = QLabel(self.frame_95)
        self.cpu_name_576.setObjectName(u"cpu_name_576")
        self.cpu_name_576.setFont(font)
        self.cpu_name_576.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_96.addWidget(self.cpu_name_576, 6, 2, 1, 1)

        self.cpu_name_577 = QLabel(self.frame_95)
        self.cpu_name_577.setObjectName(u"cpu_name_577")
        self.cpu_name_577.setFont(font1)
        self.cpu_name_577.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_96.addWidget(self.cpu_name_577, 8, 3, 1, 1)

        self.cpu_name_578 = QLabel(self.frame_95)
        self.cpu_name_578.setObjectName(u"cpu_name_578")
        self.cpu_name_578.setFont(font)
        self.cpu_name_578.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_96.addWidget(self.cpu_name_578, 8, 5, 1, 1)

        self.gpu3usage_13 = QLabel(self.frame_95)
        self.gpu3usage_13.setObjectName(u"gpu3usage_13")
        self.gpu3usage_13.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_13.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_13.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_96.addWidget(self.gpu3usage_13, 8, 1, 1, 1)

        self.cpu_name_579 = QLabel(self.frame_95)
        self.cpu_name_579.setObjectName(u"cpu_name_579")
        self.cpu_name_579.setFont(font1)
        self.cpu_name_579.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_96.addWidget(self.cpu_name_579, 8, 0, 1, 1)

        self.device1_13 = QLabel(self.frame_95)
        self.device1_13.setObjectName(u"device1_13")
        self.device1_13.setFont(font2)
        self.device1_13.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_13.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_96.addWidget(self.device1_13, 1, 0, 1, 1)

        self.clientipaddress_13 = QLabel(self.frame_95)
        self.clientipaddress_13.setObjectName(u"clientipaddress_13")
        self.clientipaddress_13.setFont(font)
        self.clientipaddress_13.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_13.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_96.addWidget(self.clientipaddress_13, 1, 1, 1, 5)

        self.gpu1usage_13 = QLabel(self.frame_95)
        self.gpu1usage_13.setObjectName(u"gpu1usage_13")
        self.gpu1usage_13.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_13.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_13.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_96.addWidget(self.gpu1usage_13, 6, 1, 1, 1)

        self.memoryusage_13 = QLabel(self.frame_95)
        self.memoryusage_13.setObjectName(u"memoryusage_13")
        self.memoryusage_13.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_13.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_13.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_96.addWidget(self.memoryusage_13, 8, 4, 1, 1)

        self.cpu_name_580 = QLabel(self.frame_95)
        self.cpu_name_580.setObjectName(u"cpu_name_580")
        self.cpu_name_580.setFont(font1)
        self.cpu_name_580.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_96.addWidget(self.cpu_name_580, 6, 3, 1, 1)


        self.gridLayout_95.addWidget(self.frame_95, 0, 0, 1, 3)

        self.elapsedtime_13 = QLabel(self.frame_94)
        self.elapsedtime_13.setObjectName(u"elapsedtime_13")
        self.elapsedtime_13.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_13.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_95.addWidget(self.elapsedtime_13, 1, 2, 1, 1)

        self.off_Button_13 = QPushButton(self.frame_94)
        self.off_Button_13.setObjectName(u"off_Button_13")
        self.off_Button_13.setEnabled(True)
        self.off_Button_13.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_95.addWidget(self.off_Button_13, 1, 1, 1, 1)


        self.horizontalLayout_12.addWidget(self.frame_94)

        self.frame_96 = QFrame(self.frame_15)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setMinimumSize(QSize(240, 200))
        self.frame_96.setMaximumSize(QSize(240, 200))
        self.frame_96.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_96.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_96.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_97 = QGridLayout(self.frame_96)
        self.gridLayout_97.setObjectName(u"gridLayout_97")
        self.on_Button_14 = QPushButton(self.frame_96)
        self.on_Button_14.setObjectName(u"on_Button_14")
        self.on_Button_14.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_97.addWidget(self.on_Button_14, 1, 0, 1, 1)

        self.frame_97 = QFrame(self.frame_96)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_97.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_98 = QGridLayout(self.frame_97)
        self.gridLayout_98.setObjectName(u"gridLayout_98")
        self.gpu2usage_14 = QLabel(self.frame_97)
        self.gpu2usage_14.setObjectName(u"gpu2usage_14")
        self.gpu2usage_14.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_14.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_14.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_98.addWidget(self.gpu2usage_14, 6, 4, 1, 1)

        self.cpu_name_581 = QLabel(self.frame_97)
        self.cpu_name_581.setObjectName(u"cpu_name_581")
        self.cpu_name_581.setFont(font)
        self.cpu_name_581.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_98.addWidget(self.cpu_name_581, 3, 5, 1, 1)

        self.cpu_name_582 = QLabel(self.frame_97)
        self.cpu_name_582.setObjectName(u"cpu_name_582")
        self.cpu_name_582.setFont(font)
        self.cpu_name_582.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_98.addWidget(self.cpu_name_582, 6, 5, 1, 1)

        self.cpu_name_583 = QLabel(self.frame_97)
        self.cpu_name_583.setObjectName(u"cpu_name_583")
        self.cpu_name_583.setFont(font1)
        self.cpu_name_583.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_98.addWidget(self.cpu_name_583, 6, 0, 1, 1)

        self.cpuusage_14 = QLabel(self.frame_97)
        self.cpuusage_14.setObjectName(u"cpuusage_14")
        self.cpuusage_14.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_14.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_14.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_98.addWidget(self.cpuusage_14, 3, 1, 1, 1)

        self.cpu_name_584 = QLabel(self.frame_97)
        self.cpu_name_584.setObjectName(u"cpu_name_584")
        self.cpu_name_584.setFont(font)
        self.cpu_name_584.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_98.addWidget(self.cpu_name_584, 3, 2, 1, 1)

        self.gpu0usage_14 = QLabel(self.frame_97)
        self.gpu0usage_14.setObjectName(u"gpu0usage_14")
        self.gpu0usage_14.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_14.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_14.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_98.addWidget(self.gpu0usage_14, 3, 4, 1, 1)

        self.cpu_name_585 = QLabel(self.frame_97)
        self.cpu_name_585.setObjectName(u"cpu_name_585")
        self.cpu_name_585.setFont(font1)
        self.cpu_name_585.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_98.addWidget(self.cpu_name_585, 3, 3, 1, 1)

        self.cpu_name_586 = QLabel(self.frame_97)
        self.cpu_name_586.setObjectName(u"cpu_name_586")
        self.cpu_name_586.setFont(font1)
        self.cpu_name_586.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_98.addWidget(self.cpu_name_586, 3, 0, 1, 1)

        self.cpu_name_587 = QLabel(self.frame_97)
        self.cpu_name_587.setObjectName(u"cpu_name_587")
        self.cpu_name_587.setFont(font)
        self.cpu_name_587.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_98.addWidget(self.cpu_name_587, 8, 2, 1, 1)

        self.cpu_name_588 = QLabel(self.frame_97)
        self.cpu_name_588.setObjectName(u"cpu_name_588")
        self.cpu_name_588.setFont(font)
        self.cpu_name_588.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_98.addWidget(self.cpu_name_588, 6, 2, 1, 1)

        self.cpu_name_589 = QLabel(self.frame_97)
        self.cpu_name_589.setObjectName(u"cpu_name_589")
        self.cpu_name_589.setFont(font1)
        self.cpu_name_589.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_98.addWidget(self.cpu_name_589, 8, 3, 1, 1)

        self.cpu_name_590 = QLabel(self.frame_97)
        self.cpu_name_590.setObjectName(u"cpu_name_590")
        self.cpu_name_590.setFont(font)
        self.cpu_name_590.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_98.addWidget(self.cpu_name_590, 8, 5, 1, 1)

        self.gpu3usage_14 = QLabel(self.frame_97)
        self.gpu3usage_14.setObjectName(u"gpu3usage_14")
        self.gpu3usage_14.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_14.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_14.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_98.addWidget(self.gpu3usage_14, 8, 1, 1, 1)

        self.cpu_name_591 = QLabel(self.frame_97)
        self.cpu_name_591.setObjectName(u"cpu_name_591")
        self.cpu_name_591.setFont(font1)
        self.cpu_name_591.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_98.addWidget(self.cpu_name_591, 8, 0, 1, 1)

        self.device1_14 = QLabel(self.frame_97)
        self.device1_14.setObjectName(u"device1_14")
        self.device1_14.setFont(font2)
        self.device1_14.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_14.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_98.addWidget(self.device1_14, 1, 0, 1, 1)

        self.clientipaddress_14 = QLabel(self.frame_97)
        self.clientipaddress_14.setObjectName(u"clientipaddress_14")
        self.clientipaddress_14.setFont(font)
        self.clientipaddress_14.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_14.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_98.addWidget(self.clientipaddress_14, 1, 1, 1, 5)

        self.gpu1usage_14 = QLabel(self.frame_97)
        self.gpu1usage_14.setObjectName(u"gpu1usage_14")
        self.gpu1usage_14.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_14.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_14.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_98.addWidget(self.gpu1usage_14, 6, 1, 1, 1)

        self.memoryusage_14 = QLabel(self.frame_97)
        self.memoryusage_14.setObjectName(u"memoryusage_14")
        self.memoryusage_14.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_14.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_14.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_98.addWidget(self.memoryusage_14, 8, 4, 1, 1)

        self.cpu_name_592 = QLabel(self.frame_97)
        self.cpu_name_592.setObjectName(u"cpu_name_592")
        self.cpu_name_592.setFont(font1)
        self.cpu_name_592.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_98.addWidget(self.cpu_name_592, 6, 3, 1, 1)


        self.gridLayout_97.addWidget(self.frame_97, 0, 0, 1, 3)

        self.elapsedtime_14 = QLabel(self.frame_96)
        self.elapsedtime_14.setObjectName(u"elapsedtime_14")
        self.elapsedtime_14.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_14.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_97.addWidget(self.elapsedtime_14, 1, 2, 1, 1)

        self.off_Button_14 = QPushButton(self.frame_96)
        self.off_Button_14.setObjectName(u"off_Button_14")
        self.off_Button_14.setEnabled(True)
        self.off_Button_14.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_97.addWidget(self.off_Button_14, 1, 1, 1, 1)


        self.horizontalLayout_12.addWidget(self.frame_96)

        self.frame_98 = QFrame(self.frame_15)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setMinimumSize(QSize(240, 200))
        self.frame_98.setMaximumSize(QSize(240, 200))
        self.frame_98.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_98.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_98.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_99 = QGridLayout(self.frame_98)
        self.gridLayout_99.setObjectName(u"gridLayout_99")
        self.on_Button_15 = QPushButton(self.frame_98)
        self.on_Button_15.setObjectName(u"on_Button_15")
        self.on_Button_15.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_99.addWidget(self.on_Button_15, 1, 0, 1, 1)

        self.frame_99 = QFrame(self.frame_98)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_99.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_100 = QGridLayout(self.frame_99)
        self.gridLayout_100.setObjectName(u"gridLayout_100")
        self.gpu3usage_15 = QLabel(self.frame_99)
        self.gpu3usage_15.setObjectName(u"gpu3usage_15")
        self.gpu3usage_15.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_15.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_15.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_100.addWidget(self.gpu3usage_15, 8, 1, 1, 1)

        self.memoryusage_15 = QLabel(self.frame_99)
        self.memoryusage_15.setObjectName(u"memoryusage_15")
        self.memoryusage_15.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_15.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_15.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_100.addWidget(self.memoryusage_15, 8, 4, 1, 1)

        self.cpu_name_595 = QLabel(self.frame_99)
        self.cpu_name_595.setObjectName(u"cpu_name_595")
        self.cpu_name_595.setFont(font1)
        self.cpu_name_595.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_100.addWidget(self.cpu_name_595, 6, 0, 1, 1)

        self.cpu_name_601 = QLabel(self.frame_99)
        self.cpu_name_601.setObjectName(u"cpu_name_601")
        self.cpu_name_601.setFont(font1)
        self.cpu_name_601.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_100.addWidget(self.cpu_name_601, 8, 3, 1, 1)

        self.cpu_name_604 = QLabel(self.frame_99)
        self.cpu_name_604.setObjectName(u"cpu_name_604")
        self.cpu_name_604.setFont(font1)
        self.cpu_name_604.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_100.addWidget(self.cpu_name_604, 6, 3, 1, 1)

        self.cpu_name_596 = QLabel(self.frame_99)
        self.cpu_name_596.setObjectName(u"cpu_name_596")
        self.cpu_name_596.setFont(font)
        self.cpu_name_596.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_100.addWidget(self.cpu_name_596, 3, 2, 1, 1)

        self.cpu_name_597 = QLabel(self.frame_99)
        self.cpu_name_597.setObjectName(u"cpu_name_597")
        self.cpu_name_597.setFont(font1)
        self.cpu_name_597.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_100.addWidget(self.cpu_name_597, 3, 3, 1, 1)

        self.clientipaddress_15 = QLabel(self.frame_99)
        self.clientipaddress_15.setObjectName(u"clientipaddress_15")
        self.clientipaddress_15.setFont(font)
        self.clientipaddress_15.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_15.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_100.addWidget(self.clientipaddress_15, 1, 1, 1, 5)

        self.cpu_name_603 = QLabel(self.frame_99)
        self.cpu_name_603.setObjectName(u"cpu_name_603")
        self.cpu_name_603.setFont(font1)
        self.cpu_name_603.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_100.addWidget(self.cpu_name_603, 8, 0, 1, 1)

        self.gpu1usage_15 = QLabel(self.frame_99)
        self.gpu1usage_15.setObjectName(u"gpu1usage_15")
        self.gpu1usage_15.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_15.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_15.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_100.addWidget(self.gpu1usage_15, 6, 1, 1, 1)

        self.gpu2usage_15 = QLabel(self.frame_99)
        self.gpu2usage_15.setObjectName(u"gpu2usage_15")
        self.gpu2usage_15.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_15.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_15.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_100.addWidget(self.gpu2usage_15, 6, 4, 1, 1)

        self.cpuusage_15 = QLabel(self.frame_99)
        self.cpuusage_15.setObjectName(u"cpuusage_15")
        self.cpuusage_15.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_15.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_15.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_100.addWidget(self.cpuusage_15, 3, 1, 1, 1)

        self.cpu_name_593 = QLabel(self.frame_99)
        self.cpu_name_593.setObjectName(u"cpu_name_593")
        self.cpu_name_593.setFont(font)
        self.cpu_name_593.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_100.addWidget(self.cpu_name_593, 3, 5, 1, 1)

        self.cpu_name_598 = QLabel(self.frame_99)
        self.cpu_name_598.setObjectName(u"cpu_name_598")
        self.cpu_name_598.setFont(font1)
        self.cpu_name_598.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_100.addWidget(self.cpu_name_598, 3, 0, 1, 1)

        self.cpu_name_602 = QLabel(self.frame_99)
        self.cpu_name_602.setObjectName(u"cpu_name_602")
        self.cpu_name_602.setFont(font)
        self.cpu_name_602.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_100.addWidget(self.cpu_name_602, 8, 5, 1, 1)

        self.cpu_name_599 = QLabel(self.frame_99)
        self.cpu_name_599.setObjectName(u"cpu_name_599")
        self.cpu_name_599.setFont(font)
        self.cpu_name_599.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_100.addWidget(self.cpu_name_599, 8, 2, 1, 1)

        self.cpu_name_600 = QLabel(self.frame_99)
        self.cpu_name_600.setObjectName(u"cpu_name_600")
        self.cpu_name_600.setFont(font)
        self.cpu_name_600.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_100.addWidget(self.cpu_name_600, 6, 2, 1, 1)

        self.gpu0usage_15 = QLabel(self.frame_99)
        self.gpu0usage_15.setObjectName(u"gpu0usage_15")
        self.gpu0usage_15.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_15.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_15.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_100.addWidget(self.gpu0usage_15, 3, 4, 1, 1)

        self.device1_15 = QLabel(self.frame_99)
        self.device1_15.setObjectName(u"device1_15")
        self.device1_15.setFont(font2)
        self.device1_15.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_15.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_100.addWidget(self.device1_15, 1, 0, 1, 1)

        self.cpu_name_594 = QLabel(self.frame_99)
        self.cpu_name_594.setObjectName(u"cpu_name_594")
        self.cpu_name_594.setFont(font)
        self.cpu_name_594.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_100.addWidget(self.cpu_name_594, 6, 5, 1, 1)


        self.gridLayout_99.addWidget(self.frame_99, 0, 0, 1, 3)

        self.elapsedtime_15 = QLabel(self.frame_98)
        self.elapsedtime_15.setObjectName(u"elapsedtime_15")
        self.elapsedtime_15.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_15.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_99.addWidget(self.elapsedtime_15, 1, 2, 1, 1)

        self.off_Button_15 = QPushButton(self.frame_98)
        self.off_Button_15.setObjectName(u"off_Button_15")
        self.off_Button_15.setEnabled(True)
        self.off_Button_15.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_99.addWidget(self.off_Button_15, 1, 1, 1, 1)


        self.horizontalLayout_12.addWidget(self.frame_98)

        self.frame_100 = QFrame(self.frame_15)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setMinimumSize(QSize(240, 200))
        self.frame_100.setMaximumSize(QSize(240, 200))
        self.frame_100.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_100.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_100.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_101 = QGridLayout(self.frame_100)
        self.gridLayout_101.setObjectName(u"gridLayout_101")
        self.on_Button_16 = QPushButton(self.frame_100)
        self.on_Button_16.setObjectName(u"on_Button_16")
        self.on_Button_16.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_101.addWidget(self.on_Button_16, 1, 0, 1, 1)

        self.frame_101 = QFrame(self.frame_100)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_101.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_102 = QGridLayout(self.frame_101)
        self.gridLayout_102.setObjectName(u"gridLayout_102")
        self.gpu2usage_16 = QLabel(self.frame_101)
        self.gpu2usage_16.setObjectName(u"gpu2usage_16")
        self.gpu2usage_16.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_16.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_16.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_102.addWidget(self.gpu2usage_16, 6, 4, 1, 1)

        self.cpu_name_605 = QLabel(self.frame_101)
        self.cpu_name_605.setObjectName(u"cpu_name_605")
        self.cpu_name_605.setFont(font)
        self.cpu_name_605.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_102.addWidget(self.cpu_name_605, 3, 5, 1, 1)

        self.cpu_name_606 = QLabel(self.frame_101)
        self.cpu_name_606.setObjectName(u"cpu_name_606")
        self.cpu_name_606.setFont(font)
        self.cpu_name_606.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_102.addWidget(self.cpu_name_606, 6, 5, 1, 1)

        self.cpu_name_607 = QLabel(self.frame_101)
        self.cpu_name_607.setObjectName(u"cpu_name_607")
        self.cpu_name_607.setFont(font1)
        self.cpu_name_607.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_102.addWidget(self.cpu_name_607, 6, 0, 1, 1)

        self.cpuusage_16 = QLabel(self.frame_101)
        self.cpuusage_16.setObjectName(u"cpuusage_16")
        self.cpuusage_16.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_16.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_16.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_102.addWidget(self.cpuusage_16, 3, 1, 1, 1)

        self.cpu_name_608 = QLabel(self.frame_101)
        self.cpu_name_608.setObjectName(u"cpu_name_608")
        self.cpu_name_608.setFont(font)
        self.cpu_name_608.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_102.addWidget(self.cpu_name_608, 3, 2, 1, 1)

        self.gpu0usage_16 = QLabel(self.frame_101)
        self.gpu0usage_16.setObjectName(u"gpu0usage_16")
        self.gpu0usage_16.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_16.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_16.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_102.addWidget(self.gpu0usage_16, 3, 4, 1, 1)

        self.cpu_name_609 = QLabel(self.frame_101)
        self.cpu_name_609.setObjectName(u"cpu_name_609")
        self.cpu_name_609.setFont(font1)
        self.cpu_name_609.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_102.addWidget(self.cpu_name_609, 3, 3, 1, 1)

        self.cpu_name_610 = QLabel(self.frame_101)
        self.cpu_name_610.setObjectName(u"cpu_name_610")
        self.cpu_name_610.setFont(font1)
        self.cpu_name_610.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_102.addWidget(self.cpu_name_610, 3, 0, 1, 1)

        self.cpu_name_611 = QLabel(self.frame_101)
        self.cpu_name_611.setObjectName(u"cpu_name_611")
        self.cpu_name_611.setFont(font)
        self.cpu_name_611.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_102.addWidget(self.cpu_name_611, 8, 2, 1, 1)

        self.cpu_name_612 = QLabel(self.frame_101)
        self.cpu_name_612.setObjectName(u"cpu_name_612")
        self.cpu_name_612.setFont(font)
        self.cpu_name_612.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_102.addWidget(self.cpu_name_612, 6, 2, 1, 1)

        self.cpu_name_613 = QLabel(self.frame_101)
        self.cpu_name_613.setObjectName(u"cpu_name_613")
        self.cpu_name_613.setFont(font1)
        self.cpu_name_613.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_102.addWidget(self.cpu_name_613, 8, 3, 1, 1)

        self.cpu_name_614 = QLabel(self.frame_101)
        self.cpu_name_614.setObjectName(u"cpu_name_614")
        self.cpu_name_614.setFont(font)
        self.cpu_name_614.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_102.addWidget(self.cpu_name_614, 8, 5, 1, 1)

        self.gpu3usage_16 = QLabel(self.frame_101)
        self.gpu3usage_16.setObjectName(u"gpu3usage_16")
        self.gpu3usage_16.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_16.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_16.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_102.addWidget(self.gpu3usage_16, 8, 1, 1, 1)

        self.cpu_name_615 = QLabel(self.frame_101)
        self.cpu_name_615.setObjectName(u"cpu_name_615")
        self.cpu_name_615.setFont(font1)
        self.cpu_name_615.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_102.addWidget(self.cpu_name_615, 8, 0, 1, 1)

        self.device1_16 = QLabel(self.frame_101)
        self.device1_16.setObjectName(u"device1_16")
        self.device1_16.setFont(font2)
        self.device1_16.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_16.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_102.addWidget(self.device1_16, 1, 0, 1, 1)

        self.clientipaddress_16 = QLabel(self.frame_101)
        self.clientipaddress_16.setObjectName(u"clientipaddress_16")
        self.clientipaddress_16.setFont(font)
        self.clientipaddress_16.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_16.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_102.addWidget(self.clientipaddress_16, 1, 1, 1, 5)

        self.gpu1usage_16 = QLabel(self.frame_101)
        self.gpu1usage_16.setObjectName(u"gpu1usage_16")
        self.gpu1usage_16.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_16.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_16.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_102.addWidget(self.gpu1usage_16, 6, 1, 1, 1)

        self.memoryusage_16 = QLabel(self.frame_101)
        self.memoryusage_16.setObjectName(u"memoryusage_16")
        self.memoryusage_16.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_16.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_16.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_102.addWidget(self.memoryusage_16, 8, 4, 1, 1)

        self.cpu_name_616 = QLabel(self.frame_101)
        self.cpu_name_616.setObjectName(u"cpu_name_616")
        self.cpu_name_616.setFont(font1)
        self.cpu_name_616.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_102.addWidget(self.cpu_name_616, 6, 3, 1, 1)


        self.gridLayout_101.addWidget(self.frame_101, 0, 0, 1, 3)

        self.elapsedtime_16 = QLabel(self.frame_100)
        self.elapsedtime_16.setObjectName(u"elapsedtime_16")
        self.elapsedtime_16.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_16.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_101.addWidget(self.elapsedtime_16, 1, 2, 1, 1)

        self.off_Button_16 = QPushButton(self.frame_100)
        self.off_Button_16.setObjectName(u"off_Button_16")
        self.off_Button_16.setEnabled(True)
        self.off_Button_16.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_101.addWidget(self.off_Button_16, 1, 1, 1, 1)


        self.horizontalLayout_12.addWidget(self.frame_100)


        self.verticalLayout_3.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frame_102 = QFrame(self.frame_16)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setMinimumSize(QSize(240, 200))
        self.frame_102.setMaximumSize(QSize(240, 200))
        self.frame_102.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_102.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_102.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_102.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_103 = QGridLayout(self.frame_102)
        self.gridLayout_103.setObjectName(u"gridLayout_103")
        self.on_Button_17 = QPushButton(self.frame_102)
        self.on_Button_17.setObjectName(u"on_Button_17")
        self.on_Button_17.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_103.addWidget(self.on_Button_17, 1, 0, 1, 1)

        self.frame_103 = QFrame(self.frame_102)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_103.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_104 = QGridLayout(self.frame_103)
        self.gridLayout_104.setObjectName(u"gridLayout_104")
        self.gpu2usage_17 = QLabel(self.frame_103)
        self.gpu2usage_17.setObjectName(u"gpu2usage_17")
        self.gpu2usage_17.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_17.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_17.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_104.addWidget(self.gpu2usage_17, 6, 4, 1, 1)

        self.cpu_name_617 = QLabel(self.frame_103)
        self.cpu_name_617.setObjectName(u"cpu_name_617")
        self.cpu_name_617.setFont(font)
        self.cpu_name_617.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_104.addWidget(self.cpu_name_617, 3, 5, 1, 1)

        self.cpu_name_618 = QLabel(self.frame_103)
        self.cpu_name_618.setObjectName(u"cpu_name_618")
        self.cpu_name_618.setFont(font)
        self.cpu_name_618.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_104.addWidget(self.cpu_name_618, 6, 5, 1, 1)

        self.cpu_name_619 = QLabel(self.frame_103)
        self.cpu_name_619.setObjectName(u"cpu_name_619")
        self.cpu_name_619.setFont(font1)
        self.cpu_name_619.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_104.addWidget(self.cpu_name_619, 6, 0, 1, 1)

        self.cpuusage_17 = QLabel(self.frame_103)
        self.cpuusage_17.setObjectName(u"cpuusage_17")
        self.cpuusage_17.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_17.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_17.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_104.addWidget(self.cpuusage_17, 3, 1, 1, 1)

        self.cpu_name_620 = QLabel(self.frame_103)
        self.cpu_name_620.setObjectName(u"cpu_name_620")
        self.cpu_name_620.setFont(font)
        self.cpu_name_620.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_104.addWidget(self.cpu_name_620, 3, 2, 1, 1)

        self.gpu0usage_17 = QLabel(self.frame_103)
        self.gpu0usage_17.setObjectName(u"gpu0usage_17")
        self.gpu0usage_17.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_17.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_17.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_104.addWidget(self.gpu0usage_17, 3, 4, 1, 1)

        self.cpu_name_621 = QLabel(self.frame_103)
        self.cpu_name_621.setObjectName(u"cpu_name_621")
        self.cpu_name_621.setFont(font1)
        self.cpu_name_621.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_104.addWidget(self.cpu_name_621, 3, 3, 1, 1)

        self.cpu_name_622 = QLabel(self.frame_103)
        self.cpu_name_622.setObjectName(u"cpu_name_622")
        self.cpu_name_622.setFont(font1)
        self.cpu_name_622.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_104.addWidget(self.cpu_name_622, 3, 0, 1, 1)

        self.cpu_name_623 = QLabel(self.frame_103)
        self.cpu_name_623.setObjectName(u"cpu_name_623")
        self.cpu_name_623.setFont(font)
        self.cpu_name_623.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_104.addWidget(self.cpu_name_623, 8, 2, 1, 1)

        self.cpu_name_624 = QLabel(self.frame_103)
        self.cpu_name_624.setObjectName(u"cpu_name_624")
        self.cpu_name_624.setFont(font)
        self.cpu_name_624.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_104.addWidget(self.cpu_name_624, 6, 2, 1, 1)

        self.cpu_name_625 = QLabel(self.frame_103)
        self.cpu_name_625.setObjectName(u"cpu_name_625")
        self.cpu_name_625.setFont(font1)
        self.cpu_name_625.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_104.addWidget(self.cpu_name_625, 8, 3, 1, 1)

        self.cpu_name_626 = QLabel(self.frame_103)
        self.cpu_name_626.setObjectName(u"cpu_name_626")
        self.cpu_name_626.setFont(font)
        self.cpu_name_626.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_104.addWidget(self.cpu_name_626, 8, 5, 1, 1)

        self.gpu3usage_17 = QLabel(self.frame_103)
        self.gpu3usage_17.setObjectName(u"gpu3usage_17")
        self.gpu3usage_17.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_17.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_17.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_104.addWidget(self.gpu3usage_17, 8, 1, 1, 1)

        self.cpu_name_627 = QLabel(self.frame_103)
        self.cpu_name_627.setObjectName(u"cpu_name_627")
        self.cpu_name_627.setFont(font1)
        self.cpu_name_627.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_104.addWidget(self.cpu_name_627, 8, 0, 1, 1)

        self.device1_17 = QLabel(self.frame_103)
        self.device1_17.setObjectName(u"device1_17")
        self.device1_17.setFont(font2)
        self.device1_17.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_17.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_104.addWidget(self.device1_17, 1, 0, 1, 1)

        self.clientipaddress_17 = QLabel(self.frame_103)
        self.clientipaddress_17.setObjectName(u"clientipaddress_17")
        self.clientipaddress_17.setFont(font)
        self.clientipaddress_17.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_17.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_104.addWidget(self.clientipaddress_17, 1, 1, 1, 5)

        self.gpu1usage_17 = QLabel(self.frame_103)
        self.gpu1usage_17.setObjectName(u"gpu1usage_17")
        self.gpu1usage_17.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_17.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_17.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_104.addWidget(self.gpu1usage_17, 6, 1, 1, 1)

        self.memoryusage_17 = QLabel(self.frame_103)
        self.memoryusage_17.setObjectName(u"memoryusage_17")
        self.memoryusage_17.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_17.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_17.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_104.addWidget(self.memoryusage_17, 8, 4, 1, 1)

        self.cpu_name_628 = QLabel(self.frame_103)
        self.cpu_name_628.setObjectName(u"cpu_name_628")
        self.cpu_name_628.setFont(font1)
        self.cpu_name_628.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_104.addWidget(self.cpu_name_628, 6, 3, 1, 1)


        self.gridLayout_103.addWidget(self.frame_103, 0, 0, 1, 3)

        self.elapsedtime_17 = QLabel(self.frame_102)
        self.elapsedtime_17.setObjectName(u"elapsedtime_17")
        self.elapsedtime_17.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_17.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_103.addWidget(self.elapsedtime_17, 1, 2, 1, 1)

        self.off_Button_17 = QPushButton(self.frame_102)
        self.off_Button_17.setObjectName(u"off_Button_17")
        self.off_Button_17.setEnabled(True)
        self.off_Button_17.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_103.addWidget(self.off_Button_17, 1, 1, 1, 1)


        self.horizontalLayout_13.addWidget(self.frame_102)

        self.frame_104 = QFrame(self.frame_16)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setMinimumSize(QSize(240, 200))
        self.frame_104.setMaximumSize(QSize(240, 200))
        self.frame_104.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_104.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_104.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_104.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_105 = QGridLayout(self.frame_104)
        self.gridLayout_105.setObjectName(u"gridLayout_105")
        self.on_Button_18 = QPushButton(self.frame_104)
        self.on_Button_18.setObjectName(u"on_Button_18")
        self.on_Button_18.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_105.addWidget(self.on_Button_18, 1, 0, 1, 1)

        self.frame_105 = QFrame(self.frame_104)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_105.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_105.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_106 = QGridLayout(self.frame_105)
        self.gridLayout_106.setObjectName(u"gridLayout_106")
        self.gpu2usage_18 = QLabel(self.frame_105)
        self.gpu2usage_18.setObjectName(u"gpu2usage_18")
        self.gpu2usage_18.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_18.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_18.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_106.addWidget(self.gpu2usage_18, 6, 4, 1, 1)

        self.cpu_name_629 = QLabel(self.frame_105)
        self.cpu_name_629.setObjectName(u"cpu_name_629")
        self.cpu_name_629.setFont(font)
        self.cpu_name_629.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_106.addWidget(self.cpu_name_629, 3, 5, 1, 1)

        self.cpu_name_630 = QLabel(self.frame_105)
        self.cpu_name_630.setObjectName(u"cpu_name_630")
        self.cpu_name_630.setFont(font)
        self.cpu_name_630.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_106.addWidget(self.cpu_name_630, 6, 5, 1, 1)

        self.cpu_name_631 = QLabel(self.frame_105)
        self.cpu_name_631.setObjectName(u"cpu_name_631")
        self.cpu_name_631.setFont(font1)
        self.cpu_name_631.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_106.addWidget(self.cpu_name_631, 6, 0, 1, 1)

        self.cpuusage_18 = QLabel(self.frame_105)
        self.cpuusage_18.setObjectName(u"cpuusage_18")
        self.cpuusage_18.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_18.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_18.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_106.addWidget(self.cpuusage_18, 3, 1, 1, 1)

        self.cpu_name_632 = QLabel(self.frame_105)
        self.cpu_name_632.setObjectName(u"cpu_name_632")
        self.cpu_name_632.setFont(font)
        self.cpu_name_632.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_106.addWidget(self.cpu_name_632, 3, 2, 1, 1)

        self.gpu0usage_18 = QLabel(self.frame_105)
        self.gpu0usage_18.setObjectName(u"gpu0usage_18")
        self.gpu0usage_18.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_18.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_18.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_106.addWidget(self.gpu0usage_18, 3, 4, 1, 1)

        self.cpu_name_633 = QLabel(self.frame_105)
        self.cpu_name_633.setObjectName(u"cpu_name_633")
        self.cpu_name_633.setFont(font1)
        self.cpu_name_633.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_106.addWidget(self.cpu_name_633, 3, 3, 1, 1)

        self.cpu_name_634 = QLabel(self.frame_105)
        self.cpu_name_634.setObjectName(u"cpu_name_634")
        self.cpu_name_634.setFont(font1)
        self.cpu_name_634.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_106.addWidget(self.cpu_name_634, 3, 0, 1, 1)

        self.cpu_name_635 = QLabel(self.frame_105)
        self.cpu_name_635.setObjectName(u"cpu_name_635")
        self.cpu_name_635.setFont(font)
        self.cpu_name_635.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_106.addWidget(self.cpu_name_635, 8, 2, 1, 1)

        self.cpu_name_636 = QLabel(self.frame_105)
        self.cpu_name_636.setObjectName(u"cpu_name_636")
        self.cpu_name_636.setFont(font)
        self.cpu_name_636.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_106.addWidget(self.cpu_name_636, 6, 2, 1, 1)

        self.cpu_name_637 = QLabel(self.frame_105)
        self.cpu_name_637.setObjectName(u"cpu_name_637")
        self.cpu_name_637.setFont(font1)
        self.cpu_name_637.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_106.addWidget(self.cpu_name_637, 8, 3, 1, 1)

        self.cpu_name_638 = QLabel(self.frame_105)
        self.cpu_name_638.setObjectName(u"cpu_name_638")
        self.cpu_name_638.setFont(font)
        self.cpu_name_638.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_106.addWidget(self.cpu_name_638, 8, 5, 1, 1)

        self.gpu3usage_18 = QLabel(self.frame_105)
        self.gpu3usage_18.setObjectName(u"gpu3usage_18")
        self.gpu3usage_18.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_18.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_18.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_106.addWidget(self.gpu3usage_18, 8, 1, 1, 1)

        self.cpu_name_639 = QLabel(self.frame_105)
        self.cpu_name_639.setObjectName(u"cpu_name_639")
        self.cpu_name_639.setFont(font1)
        self.cpu_name_639.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_106.addWidget(self.cpu_name_639, 8, 0, 1, 1)

        self.device1_18 = QLabel(self.frame_105)
        self.device1_18.setObjectName(u"device1_18")
        self.device1_18.setFont(font2)
        self.device1_18.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_18.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_106.addWidget(self.device1_18, 1, 0, 1, 1)

        self.clientipaddress_18 = QLabel(self.frame_105)
        self.clientipaddress_18.setObjectName(u"clientipaddress_18")
        self.clientipaddress_18.setFont(font)
        self.clientipaddress_18.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_18.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_106.addWidget(self.clientipaddress_18, 1, 1, 1, 5)

        self.gpu1usage_18 = QLabel(self.frame_105)
        self.gpu1usage_18.setObjectName(u"gpu1usage_18")
        self.gpu1usage_18.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_18.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_18.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_106.addWidget(self.gpu1usage_18, 6, 1, 1, 1)

        self.memoryusage_18 = QLabel(self.frame_105)
        self.memoryusage_18.setObjectName(u"memoryusage_18")
        self.memoryusage_18.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_18.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_18.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_106.addWidget(self.memoryusage_18, 8, 4, 1, 1)

        self.cpu_name_640 = QLabel(self.frame_105)
        self.cpu_name_640.setObjectName(u"cpu_name_640")
        self.cpu_name_640.setFont(font1)
        self.cpu_name_640.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_106.addWidget(self.cpu_name_640, 6, 3, 1, 1)


        self.gridLayout_105.addWidget(self.frame_105, 0, 0, 1, 3)

        self.elapsedtime_18 = QLabel(self.frame_104)
        self.elapsedtime_18.setObjectName(u"elapsedtime_18")
        self.elapsedtime_18.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_18.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_105.addWidget(self.elapsedtime_18, 1, 2, 1, 1)

        self.off_Button_18 = QPushButton(self.frame_104)
        self.off_Button_18.setObjectName(u"off_Button_18")
        self.off_Button_18.setEnabled(True)
        self.off_Button_18.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_105.addWidget(self.off_Button_18, 1, 1, 1, 1)


        self.horizontalLayout_13.addWidget(self.frame_104)

        self.frame_106 = QFrame(self.frame_16)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setMinimumSize(QSize(240, 200))
        self.frame_106.setMaximumSize(QSize(240, 200))
        self.frame_106.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_106.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_106.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_106.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_107 = QGridLayout(self.frame_106)
        self.gridLayout_107.setObjectName(u"gridLayout_107")
        self.on_Button_19 = QPushButton(self.frame_106)
        self.on_Button_19.setObjectName(u"on_Button_19")
        self.on_Button_19.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_107.addWidget(self.on_Button_19, 1, 0, 1, 1)

        self.frame_107 = QFrame(self.frame_106)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_107.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_107.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_108 = QGridLayout(self.frame_107)
        self.gridLayout_108.setObjectName(u"gridLayout_108")
        self.gpu2usage_19 = QLabel(self.frame_107)
        self.gpu2usage_19.setObjectName(u"gpu2usage_19")
        self.gpu2usage_19.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_19.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_19.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_108.addWidget(self.gpu2usage_19, 6, 4, 1, 1)

        self.cpu_name_641 = QLabel(self.frame_107)
        self.cpu_name_641.setObjectName(u"cpu_name_641")
        self.cpu_name_641.setFont(font)
        self.cpu_name_641.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_108.addWidget(self.cpu_name_641, 3, 5, 1, 1)

        self.cpu_name_642 = QLabel(self.frame_107)
        self.cpu_name_642.setObjectName(u"cpu_name_642")
        self.cpu_name_642.setFont(font)
        self.cpu_name_642.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_108.addWidget(self.cpu_name_642, 6, 5, 1, 1)

        self.cpu_name_643 = QLabel(self.frame_107)
        self.cpu_name_643.setObjectName(u"cpu_name_643")
        self.cpu_name_643.setFont(font1)
        self.cpu_name_643.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_108.addWidget(self.cpu_name_643, 6, 0, 1, 1)

        self.cpuusage_19 = QLabel(self.frame_107)
        self.cpuusage_19.setObjectName(u"cpuusage_19")
        self.cpuusage_19.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_19.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_19.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_108.addWidget(self.cpuusage_19, 3, 1, 1, 1)

        self.cpu_name_644 = QLabel(self.frame_107)
        self.cpu_name_644.setObjectName(u"cpu_name_644")
        self.cpu_name_644.setFont(font)
        self.cpu_name_644.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_108.addWidget(self.cpu_name_644, 3, 2, 1, 1)

        self.gpu0usage_19 = QLabel(self.frame_107)
        self.gpu0usage_19.setObjectName(u"gpu0usage_19")
        self.gpu0usage_19.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_19.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_19.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_108.addWidget(self.gpu0usage_19, 3, 4, 1, 1)

        self.cpu_name_645 = QLabel(self.frame_107)
        self.cpu_name_645.setObjectName(u"cpu_name_645")
        self.cpu_name_645.setFont(font1)
        self.cpu_name_645.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_108.addWidget(self.cpu_name_645, 3, 3, 1, 1)

        self.cpu_name_646 = QLabel(self.frame_107)
        self.cpu_name_646.setObjectName(u"cpu_name_646")
        self.cpu_name_646.setFont(font1)
        self.cpu_name_646.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_108.addWidget(self.cpu_name_646, 3, 0, 1, 1)

        self.cpu_name_647 = QLabel(self.frame_107)
        self.cpu_name_647.setObjectName(u"cpu_name_647")
        self.cpu_name_647.setFont(font)
        self.cpu_name_647.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_108.addWidget(self.cpu_name_647, 8, 2, 1, 1)

        self.cpu_name_648 = QLabel(self.frame_107)
        self.cpu_name_648.setObjectName(u"cpu_name_648")
        self.cpu_name_648.setFont(font)
        self.cpu_name_648.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_108.addWidget(self.cpu_name_648, 6, 2, 1, 1)

        self.cpu_name_649 = QLabel(self.frame_107)
        self.cpu_name_649.setObjectName(u"cpu_name_649")
        self.cpu_name_649.setFont(font1)
        self.cpu_name_649.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_108.addWidget(self.cpu_name_649, 8, 3, 1, 1)

        self.cpu_name_650 = QLabel(self.frame_107)
        self.cpu_name_650.setObjectName(u"cpu_name_650")
        self.cpu_name_650.setFont(font)
        self.cpu_name_650.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_108.addWidget(self.cpu_name_650, 8, 5, 1, 1)

        self.gpu3usage_19 = QLabel(self.frame_107)
        self.gpu3usage_19.setObjectName(u"gpu3usage_19")
        self.gpu3usage_19.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_19.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_19.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_108.addWidget(self.gpu3usage_19, 8, 1, 1, 1)

        self.cpu_name_651 = QLabel(self.frame_107)
        self.cpu_name_651.setObjectName(u"cpu_name_651")
        self.cpu_name_651.setFont(font1)
        self.cpu_name_651.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_108.addWidget(self.cpu_name_651, 8, 0, 1, 1)

        self.device1_19 = QLabel(self.frame_107)
        self.device1_19.setObjectName(u"device1_19")
        self.device1_19.setFont(font2)
        self.device1_19.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_19.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_108.addWidget(self.device1_19, 1, 0, 1, 1)

        self.clientipaddress_19 = QLabel(self.frame_107)
        self.clientipaddress_19.setObjectName(u"clientipaddress_19")
        self.clientipaddress_19.setFont(font)
        self.clientipaddress_19.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_19.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_108.addWidget(self.clientipaddress_19, 1, 1, 1, 5)

        self.gpu1usage_19 = QLabel(self.frame_107)
        self.gpu1usage_19.setObjectName(u"gpu1usage_19")
        self.gpu1usage_19.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_19.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_19.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_108.addWidget(self.gpu1usage_19, 6, 1, 1, 1)

        self.memoryusage_19 = QLabel(self.frame_107)
        self.memoryusage_19.setObjectName(u"memoryusage_19")
        self.memoryusage_19.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_19.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_19.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_108.addWidget(self.memoryusage_19, 8, 4, 1, 1)

        self.cpu_name_652 = QLabel(self.frame_107)
        self.cpu_name_652.setObjectName(u"cpu_name_652")
        self.cpu_name_652.setFont(font1)
        self.cpu_name_652.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_108.addWidget(self.cpu_name_652, 6, 3, 1, 1)


        self.gridLayout_107.addWidget(self.frame_107, 0, 0, 1, 3)

        self.elapsedtime_19 = QLabel(self.frame_106)
        self.elapsedtime_19.setObjectName(u"elapsedtime_19")
        self.elapsedtime_19.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_19.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_107.addWidget(self.elapsedtime_19, 1, 2, 1, 1)

        self.off_Button_19 = QPushButton(self.frame_106)
        self.off_Button_19.setObjectName(u"off_Button_19")
        self.off_Button_19.setEnabled(True)
        self.off_Button_19.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_107.addWidget(self.off_Button_19, 1, 1, 1, 1)


        self.horizontalLayout_13.addWidget(self.frame_106)

        self.frame_108 = QFrame(self.frame_16)
        self.frame_108.setObjectName(u"frame_108")
        self.frame_108.setMinimumSize(QSize(240, 200))
        self.frame_108.setMaximumSize(QSize(240, 200))
        self.frame_108.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_108.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_108.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_108.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_109 = QGridLayout(self.frame_108)
        self.gridLayout_109.setObjectName(u"gridLayout_109")
        self.on_Button_20 = QPushButton(self.frame_108)
        self.on_Button_20.setObjectName(u"on_Button_20")
        self.on_Button_20.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_109.addWidget(self.on_Button_20, 1, 0, 1, 1)

        self.frame_109 = QFrame(self.frame_108)
        self.frame_109.setObjectName(u"frame_109")
        self.frame_109.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_109.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_109.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_110 = QGridLayout(self.frame_109)
        self.gridLayout_110.setObjectName(u"gridLayout_110")
        self.gpu2usage_20 = QLabel(self.frame_109)
        self.gpu2usage_20.setObjectName(u"gpu2usage_20")
        self.gpu2usage_20.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_20.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_20.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_110.addWidget(self.gpu2usage_20, 6, 4, 1, 1)

        self.cpu_name_653 = QLabel(self.frame_109)
        self.cpu_name_653.setObjectName(u"cpu_name_653")
        self.cpu_name_653.setFont(font)
        self.cpu_name_653.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_110.addWidget(self.cpu_name_653, 3, 5, 1, 1)

        self.cpu_name_654 = QLabel(self.frame_109)
        self.cpu_name_654.setObjectName(u"cpu_name_654")
        self.cpu_name_654.setFont(font)
        self.cpu_name_654.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_110.addWidget(self.cpu_name_654, 6, 5, 1, 1)

        self.cpu_name_655 = QLabel(self.frame_109)
        self.cpu_name_655.setObjectName(u"cpu_name_655")
        self.cpu_name_655.setFont(font1)
        self.cpu_name_655.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_110.addWidget(self.cpu_name_655, 6, 0, 1, 1)

        self.cpuusage_20 = QLabel(self.frame_109)
        self.cpuusage_20.setObjectName(u"cpuusage_20")
        self.cpuusage_20.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_20.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_20.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_110.addWidget(self.cpuusage_20, 3, 1, 1, 1)

        self.cpu_name_656 = QLabel(self.frame_109)
        self.cpu_name_656.setObjectName(u"cpu_name_656")
        self.cpu_name_656.setFont(font)
        self.cpu_name_656.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_110.addWidget(self.cpu_name_656, 3, 2, 1, 1)

        self.gpu0usage_20 = QLabel(self.frame_109)
        self.gpu0usage_20.setObjectName(u"gpu0usage_20")
        self.gpu0usage_20.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_20.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_20.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_110.addWidget(self.gpu0usage_20, 3, 4, 1, 1)

        self.cpu_name_657 = QLabel(self.frame_109)
        self.cpu_name_657.setObjectName(u"cpu_name_657")
        self.cpu_name_657.setFont(font1)
        self.cpu_name_657.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_110.addWidget(self.cpu_name_657, 3, 3, 1, 1)

        self.cpu_name_658 = QLabel(self.frame_109)
        self.cpu_name_658.setObjectName(u"cpu_name_658")
        self.cpu_name_658.setFont(font1)
        self.cpu_name_658.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_110.addWidget(self.cpu_name_658, 3, 0, 1, 1)

        self.cpu_name_659 = QLabel(self.frame_109)
        self.cpu_name_659.setObjectName(u"cpu_name_659")
        self.cpu_name_659.setFont(font)
        self.cpu_name_659.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_110.addWidget(self.cpu_name_659, 8, 2, 1, 1)

        self.cpu_name_660 = QLabel(self.frame_109)
        self.cpu_name_660.setObjectName(u"cpu_name_660")
        self.cpu_name_660.setFont(font)
        self.cpu_name_660.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_110.addWidget(self.cpu_name_660, 6, 2, 1, 1)

        self.cpu_name_661 = QLabel(self.frame_109)
        self.cpu_name_661.setObjectName(u"cpu_name_661")
        self.cpu_name_661.setFont(font1)
        self.cpu_name_661.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_110.addWidget(self.cpu_name_661, 8, 3, 1, 1)

        self.cpu_name_662 = QLabel(self.frame_109)
        self.cpu_name_662.setObjectName(u"cpu_name_662")
        self.cpu_name_662.setFont(font)
        self.cpu_name_662.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_110.addWidget(self.cpu_name_662, 8, 5, 1, 1)

        self.gpu3usage_20 = QLabel(self.frame_109)
        self.gpu3usage_20.setObjectName(u"gpu3usage_20")
        self.gpu3usage_20.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_20.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_20.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_110.addWidget(self.gpu3usage_20, 8, 1, 1, 1)

        self.cpu_name_663 = QLabel(self.frame_109)
        self.cpu_name_663.setObjectName(u"cpu_name_663")
        self.cpu_name_663.setFont(font1)
        self.cpu_name_663.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_110.addWidget(self.cpu_name_663, 8, 0, 1, 1)

        self.device1_20 = QLabel(self.frame_109)
        self.device1_20.setObjectName(u"device1_20")
        self.device1_20.setFont(font2)
        self.device1_20.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_20.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_110.addWidget(self.device1_20, 1, 0, 1, 1)

        self.clientipaddress_20 = QLabel(self.frame_109)
        self.clientipaddress_20.setObjectName(u"clientipaddress_20")
        self.clientipaddress_20.setFont(font)
        self.clientipaddress_20.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_20.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_110.addWidget(self.clientipaddress_20, 1, 1, 1, 5)

        self.gpu1usage_20 = QLabel(self.frame_109)
        self.gpu1usage_20.setObjectName(u"gpu1usage_20")
        self.gpu1usage_20.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_20.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_20.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_110.addWidget(self.gpu1usage_20, 6, 1, 1, 1)

        self.memoryusage_20 = QLabel(self.frame_109)
        self.memoryusage_20.setObjectName(u"memoryusage_20")
        self.memoryusage_20.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_20.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_20.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_110.addWidget(self.memoryusage_20, 8, 4, 1, 1)

        self.cpu_name_664 = QLabel(self.frame_109)
        self.cpu_name_664.setObjectName(u"cpu_name_664")
        self.cpu_name_664.setFont(font1)
        self.cpu_name_664.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_110.addWidget(self.cpu_name_664, 6, 3, 1, 1)


        self.gridLayout_109.addWidget(self.frame_109, 0, 0, 1, 3)

        self.elapsedtime_20 = QLabel(self.frame_108)
        self.elapsedtime_20.setObjectName(u"elapsedtime_20")
        self.elapsedtime_20.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_20.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_109.addWidget(self.elapsedtime_20, 1, 2, 1, 1)

        self.off_Button_20 = QPushButton(self.frame_108)
        self.off_Button_20.setObjectName(u"off_Button_20")
        self.off_Button_20.setEnabled(True)
        self.off_Button_20.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_109.addWidget(self.off_Button_20, 1, 1, 1, 1)


        self.horizontalLayout_13.addWidget(self.frame_108)


        self.verticalLayout_3.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_110 = QFrame(self.frame_17)
        self.frame_110.setObjectName(u"frame_110")
        self.frame_110.setMinimumSize(QSize(240, 200))
        self.frame_110.setMaximumSize(QSize(240, 200))
        self.frame_110.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_110.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_110.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_110.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_111 = QGridLayout(self.frame_110)
        self.gridLayout_111.setObjectName(u"gridLayout_111")
        self.on_Button_21 = QPushButton(self.frame_110)
        self.on_Button_21.setObjectName(u"on_Button_21")
        self.on_Button_21.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_111.addWidget(self.on_Button_21, 1, 0, 1, 1)

        self.frame_111 = QFrame(self.frame_110)
        self.frame_111.setObjectName(u"frame_111")
        self.frame_111.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_111.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_111.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_112 = QGridLayout(self.frame_111)
        self.gridLayout_112.setObjectName(u"gridLayout_112")
        self.gpu2usage_21 = QLabel(self.frame_111)
        self.gpu2usage_21.setObjectName(u"gpu2usage_21")
        self.gpu2usage_21.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_21.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_21.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_112.addWidget(self.gpu2usage_21, 6, 4, 1, 1)

        self.cpu_name_665 = QLabel(self.frame_111)
        self.cpu_name_665.setObjectName(u"cpu_name_665")
        self.cpu_name_665.setFont(font)
        self.cpu_name_665.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_112.addWidget(self.cpu_name_665, 3, 5, 1, 1)

        self.cpu_name_666 = QLabel(self.frame_111)
        self.cpu_name_666.setObjectName(u"cpu_name_666")
        self.cpu_name_666.setFont(font)
        self.cpu_name_666.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_112.addWidget(self.cpu_name_666, 6, 5, 1, 1)

        self.cpu_name_667 = QLabel(self.frame_111)
        self.cpu_name_667.setObjectName(u"cpu_name_667")
        self.cpu_name_667.setFont(font1)
        self.cpu_name_667.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_112.addWidget(self.cpu_name_667, 6, 0, 1, 1)

        self.cpuusage_21 = QLabel(self.frame_111)
        self.cpuusage_21.setObjectName(u"cpuusage_21")
        self.cpuusage_21.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_21.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_21.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_112.addWidget(self.cpuusage_21, 3, 1, 1, 1)

        self.cpu_name_668 = QLabel(self.frame_111)
        self.cpu_name_668.setObjectName(u"cpu_name_668")
        self.cpu_name_668.setFont(font)
        self.cpu_name_668.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_112.addWidget(self.cpu_name_668, 3, 2, 1, 1)

        self.gpu0usage_21 = QLabel(self.frame_111)
        self.gpu0usage_21.setObjectName(u"gpu0usage_21")
        self.gpu0usage_21.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_21.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_21.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_112.addWidget(self.gpu0usage_21, 3, 4, 1, 1)

        self.cpu_name_669 = QLabel(self.frame_111)
        self.cpu_name_669.setObjectName(u"cpu_name_669")
        self.cpu_name_669.setFont(font1)
        self.cpu_name_669.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_112.addWidget(self.cpu_name_669, 3, 3, 1, 1)

        self.cpu_name_670 = QLabel(self.frame_111)
        self.cpu_name_670.setObjectName(u"cpu_name_670")
        self.cpu_name_670.setFont(font1)
        self.cpu_name_670.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_112.addWidget(self.cpu_name_670, 3, 0, 1, 1)

        self.cpu_name_671 = QLabel(self.frame_111)
        self.cpu_name_671.setObjectName(u"cpu_name_671")
        self.cpu_name_671.setFont(font)
        self.cpu_name_671.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_112.addWidget(self.cpu_name_671, 8, 2, 1, 1)

        self.cpu_name_672 = QLabel(self.frame_111)
        self.cpu_name_672.setObjectName(u"cpu_name_672")
        self.cpu_name_672.setFont(font)
        self.cpu_name_672.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_112.addWidget(self.cpu_name_672, 6, 2, 1, 1)

        self.cpu_name_673 = QLabel(self.frame_111)
        self.cpu_name_673.setObjectName(u"cpu_name_673")
        self.cpu_name_673.setFont(font1)
        self.cpu_name_673.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_112.addWidget(self.cpu_name_673, 8, 3, 1, 1)

        self.cpu_name_674 = QLabel(self.frame_111)
        self.cpu_name_674.setObjectName(u"cpu_name_674")
        self.cpu_name_674.setFont(font)
        self.cpu_name_674.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_112.addWidget(self.cpu_name_674, 8, 5, 1, 1)

        self.gpu3usage_21 = QLabel(self.frame_111)
        self.gpu3usage_21.setObjectName(u"gpu3usage_21")
        self.gpu3usage_21.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_21.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_21.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_112.addWidget(self.gpu3usage_21, 8, 1, 1, 1)

        self.cpu_name_675 = QLabel(self.frame_111)
        self.cpu_name_675.setObjectName(u"cpu_name_675")
        self.cpu_name_675.setFont(font1)
        self.cpu_name_675.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_112.addWidget(self.cpu_name_675, 8, 0, 1, 1)

        self.device1_21 = QLabel(self.frame_111)
        self.device1_21.setObjectName(u"device1_21")
        self.device1_21.setFont(font2)
        self.device1_21.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_21.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_112.addWidget(self.device1_21, 1, 0, 1, 1)

        self.clientipaddress_21 = QLabel(self.frame_111)
        self.clientipaddress_21.setObjectName(u"clientipaddress_21")
        self.clientipaddress_21.setFont(font)
        self.clientipaddress_21.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_21.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_112.addWidget(self.clientipaddress_21, 1, 1, 1, 5)

        self.gpu1usage_21 = QLabel(self.frame_111)
        self.gpu1usage_21.setObjectName(u"gpu1usage_21")
        self.gpu1usage_21.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_21.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_21.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_112.addWidget(self.gpu1usage_21, 6, 1, 1, 1)

        self.memoryusage_21 = QLabel(self.frame_111)
        self.memoryusage_21.setObjectName(u"memoryusage_21")
        self.memoryusage_21.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_21.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_21.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_112.addWidget(self.memoryusage_21, 8, 4, 1, 1)

        self.cpu_name_676 = QLabel(self.frame_111)
        self.cpu_name_676.setObjectName(u"cpu_name_676")
        self.cpu_name_676.setFont(font1)
        self.cpu_name_676.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_112.addWidget(self.cpu_name_676, 6, 3, 1, 1)


        self.gridLayout_111.addWidget(self.frame_111, 0, 0, 1, 3)

        self.elapsedtime_21 = QLabel(self.frame_110)
        self.elapsedtime_21.setObjectName(u"elapsedtime_21")
        self.elapsedtime_21.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_21.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_111.addWidget(self.elapsedtime_21, 1, 2, 1, 1)

        self.off_Button_21 = QPushButton(self.frame_110)
        self.off_Button_21.setObjectName(u"off_Button_21")
        self.off_Button_21.setEnabled(True)
        self.off_Button_21.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_111.addWidget(self.off_Button_21, 1, 1, 1, 1)


        self.horizontalLayout_14.addWidget(self.frame_110)

        self.frame_112 = QFrame(self.frame_17)
        self.frame_112.setObjectName(u"frame_112")
        self.frame_112.setMinimumSize(QSize(240, 200))
        self.frame_112.setMaximumSize(QSize(240, 200))
        self.frame_112.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_112.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_112.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_112.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_113 = QGridLayout(self.frame_112)
        self.gridLayout_113.setObjectName(u"gridLayout_113")
        self.on_Button_22 = QPushButton(self.frame_112)
        self.on_Button_22.setObjectName(u"on_Button_22")
        self.on_Button_22.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_113.addWidget(self.on_Button_22, 1, 0, 1, 1)

        self.frame_113 = QFrame(self.frame_112)
        self.frame_113.setObjectName(u"frame_113")
        self.frame_113.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_113.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_113.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_114 = QGridLayout(self.frame_113)
        self.gridLayout_114.setObjectName(u"gridLayout_114")
        self.gpu2usage_22 = QLabel(self.frame_113)
        self.gpu2usage_22.setObjectName(u"gpu2usage_22")
        self.gpu2usage_22.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_22.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_22.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_114.addWidget(self.gpu2usage_22, 6, 4, 1, 1)

        self.cpu_name_677 = QLabel(self.frame_113)
        self.cpu_name_677.setObjectName(u"cpu_name_677")
        self.cpu_name_677.setFont(font)
        self.cpu_name_677.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_114.addWidget(self.cpu_name_677, 3, 5, 1, 1)

        self.cpu_name_678 = QLabel(self.frame_113)
        self.cpu_name_678.setObjectName(u"cpu_name_678")
        self.cpu_name_678.setFont(font)
        self.cpu_name_678.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_114.addWidget(self.cpu_name_678, 6, 5, 1, 1)

        self.cpu_name_679 = QLabel(self.frame_113)
        self.cpu_name_679.setObjectName(u"cpu_name_679")
        self.cpu_name_679.setFont(font1)
        self.cpu_name_679.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_114.addWidget(self.cpu_name_679, 6, 0, 1, 1)

        self.cpuusage_22 = QLabel(self.frame_113)
        self.cpuusage_22.setObjectName(u"cpuusage_22")
        self.cpuusage_22.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_22.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_22.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_114.addWidget(self.cpuusage_22, 3, 1, 1, 1)

        self.cpu_name_680 = QLabel(self.frame_113)
        self.cpu_name_680.setObjectName(u"cpu_name_680")
        self.cpu_name_680.setFont(font)
        self.cpu_name_680.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_114.addWidget(self.cpu_name_680, 3, 2, 1, 1)

        self.gpu0usage_22 = QLabel(self.frame_113)
        self.gpu0usage_22.setObjectName(u"gpu0usage_22")
        self.gpu0usage_22.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_22.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_22.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_114.addWidget(self.gpu0usage_22, 3, 4, 1, 1)

        self.cpu_name_681 = QLabel(self.frame_113)
        self.cpu_name_681.setObjectName(u"cpu_name_681")
        self.cpu_name_681.setFont(font1)
        self.cpu_name_681.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_114.addWidget(self.cpu_name_681, 3, 3, 1, 1)

        self.cpu_name_682 = QLabel(self.frame_113)
        self.cpu_name_682.setObjectName(u"cpu_name_682")
        self.cpu_name_682.setFont(font1)
        self.cpu_name_682.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_114.addWidget(self.cpu_name_682, 3, 0, 1, 1)

        self.cpu_name_683 = QLabel(self.frame_113)
        self.cpu_name_683.setObjectName(u"cpu_name_683")
        self.cpu_name_683.setFont(font)
        self.cpu_name_683.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_114.addWidget(self.cpu_name_683, 8, 2, 1, 1)

        self.cpu_name_684 = QLabel(self.frame_113)
        self.cpu_name_684.setObjectName(u"cpu_name_684")
        self.cpu_name_684.setFont(font)
        self.cpu_name_684.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_114.addWidget(self.cpu_name_684, 6, 2, 1, 1)

        self.cpu_name_685 = QLabel(self.frame_113)
        self.cpu_name_685.setObjectName(u"cpu_name_685")
        self.cpu_name_685.setFont(font1)
        self.cpu_name_685.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_114.addWidget(self.cpu_name_685, 8, 3, 1, 1)

        self.cpu_name_686 = QLabel(self.frame_113)
        self.cpu_name_686.setObjectName(u"cpu_name_686")
        self.cpu_name_686.setFont(font)
        self.cpu_name_686.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_114.addWidget(self.cpu_name_686, 8, 5, 1, 1)

        self.gpu3usage_22 = QLabel(self.frame_113)
        self.gpu3usage_22.setObjectName(u"gpu3usage_22")
        self.gpu3usage_22.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_22.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_22.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_114.addWidget(self.gpu3usage_22, 8, 1, 1, 1)

        self.cpu_name_687 = QLabel(self.frame_113)
        self.cpu_name_687.setObjectName(u"cpu_name_687")
        self.cpu_name_687.setFont(font1)
        self.cpu_name_687.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_114.addWidget(self.cpu_name_687, 8, 0, 1, 1)

        self.device1_22 = QLabel(self.frame_113)
        self.device1_22.setObjectName(u"device1_22")
        self.device1_22.setFont(font2)
        self.device1_22.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_22.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_114.addWidget(self.device1_22, 1, 0, 1, 1)

        self.clientipaddress_22 = QLabel(self.frame_113)
        self.clientipaddress_22.setObjectName(u"clientipaddress_22")
        self.clientipaddress_22.setFont(font)
        self.clientipaddress_22.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_22.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_114.addWidget(self.clientipaddress_22, 1, 1, 1, 5)

        self.gpu1usage_22 = QLabel(self.frame_113)
        self.gpu1usage_22.setObjectName(u"gpu1usage_22")
        self.gpu1usage_22.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_22.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_22.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_114.addWidget(self.gpu1usage_22, 6, 1, 1, 1)

        self.memoryusage_22 = QLabel(self.frame_113)
        self.memoryusage_22.setObjectName(u"memoryusage_22")
        self.memoryusage_22.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_22.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_22.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_114.addWidget(self.memoryusage_22, 8, 4, 1, 1)

        self.cpu_name_688 = QLabel(self.frame_113)
        self.cpu_name_688.setObjectName(u"cpu_name_688")
        self.cpu_name_688.setFont(font1)
        self.cpu_name_688.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_114.addWidget(self.cpu_name_688, 6, 3, 1, 1)


        self.gridLayout_113.addWidget(self.frame_113, 0, 0, 1, 3)

        self.elapsedtime_22 = QLabel(self.frame_112)
        self.elapsedtime_22.setObjectName(u"elapsedtime_22")
        self.elapsedtime_22.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_22.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_113.addWidget(self.elapsedtime_22, 1, 2, 1, 1)

        self.off_Button_22 = QPushButton(self.frame_112)
        self.off_Button_22.setObjectName(u"off_Button_22")
        self.off_Button_22.setEnabled(True)
        self.off_Button_22.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_113.addWidget(self.off_Button_22, 1, 1, 1, 1)


        self.horizontalLayout_14.addWidget(self.frame_112)

        self.frame_114 = QFrame(self.frame_17)
        self.frame_114.setObjectName(u"frame_114")
        self.frame_114.setMinimumSize(QSize(240, 200))
        self.frame_114.setMaximumSize(QSize(240, 200))
        self.frame_114.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_114.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_114.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_114.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_115 = QGridLayout(self.frame_114)
        self.gridLayout_115.setObjectName(u"gridLayout_115")
        self.on_Button_23 = QPushButton(self.frame_114)
        self.on_Button_23.setObjectName(u"on_Button_23")
        self.on_Button_23.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_115.addWidget(self.on_Button_23, 1, 0, 1, 1)

        self.frame_115 = QFrame(self.frame_114)
        self.frame_115.setObjectName(u"frame_115")
        self.frame_115.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_115.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_115.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_116 = QGridLayout(self.frame_115)
        self.gridLayout_116.setObjectName(u"gridLayout_116")
        self.gpu2usage_23 = QLabel(self.frame_115)
        self.gpu2usage_23.setObjectName(u"gpu2usage_23")
        self.gpu2usage_23.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_23.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_23.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_116.addWidget(self.gpu2usage_23, 6, 4, 1, 1)

        self.cpu_name_689 = QLabel(self.frame_115)
        self.cpu_name_689.setObjectName(u"cpu_name_689")
        self.cpu_name_689.setFont(font)
        self.cpu_name_689.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_116.addWidget(self.cpu_name_689, 3, 5, 1, 1)

        self.cpu_name_690 = QLabel(self.frame_115)
        self.cpu_name_690.setObjectName(u"cpu_name_690")
        self.cpu_name_690.setFont(font)
        self.cpu_name_690.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_116.addWidget(self.cpu_name_690, 6, 5, 1, 1)

        self.cpu_name_691 = QLabel(self.frame_115)
        self.cpu_name_691.setObjectName(u"cpu_name_691")
        self.cpu_name_691.setFont(font1)
        self.cpu_name_691.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_116.addWidget(self.cpu_name_691, 6, 0, 1, 1)

        self.cpuusage_23 = QLabel(self.frame_115)
        self.cpuusage_23.setObjectName(u"cpuusage_23")
        self.cpuusage_23.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_23.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_23.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_116.addWidget(self.cpuusage_23, 3, 1, 1, 1)

        self.cpu_name_692 = QLabel(self.frame_115)
        self.cpu_name_692.setObjectName(u"cpu_name_692")
        self.cpu_name_692.setFont(font)
        self.cpu_name_692.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_116.addWidget(self.cpu_name_692, 3, 2, 1, 1)

        self.gpu0usage_23 = QLabel(self.frame_115)
        self.gpu0usage_23.setObjectName(u"gpu0usage_23")
        self.gpu0usage_23.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_23.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_23.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_116.addWidget(self.gpu0usage_23, 3, 4, 1, 1)

        self.cpu_name_693 = QLabel(self.frame_115)
        self.cpu_name_693.setObjectName(u"cpu_name_693")
        self.cpu_name_693.setFont(font1)
        self.cpu_name_693.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_116.addWidget(self.cpu_name_693, 3, 3, 1, 1)

        self.cpu_name_694 = QLabel(self.frame_115)
        self.cpu_name_694.setObjectName(u"cpu_name_694")
        self.cpu_name_694.setFont(font1)
        self.cpu_name_694.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_116.addWidget(self.cpu_name_694, 3, 0, 1, 1)

        self.cpu_name_695 = QLabel(self.frame_115)
        self.cpu_name_695.setObjectName(u"cpu_name_695")
        self.cpu_name_695.setFont(font)
        self.cpu_name_695.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_116.addWidget(self.cpu_name_695, 8, 2, 1, 1)

        self.cpu_name_696 = QLabel(self.frame_115)
        self.cpu_name_696.setObjectName(u"cpu_name_696")
        self.cpu_name_696.setFont(font)
        self.cpu_name_696.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_116.addWidget(self.cpu_name_696, 6, 2, 1, 1)

        self.cpu_name_697 = QLabel(self.frame_115)
        self.cpu_name_697.setObjectName(u"cpu_name_697")
        self.cpu_name_697.setFont(font1)
        self.cpu_name_697.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_116.addWidget(self.cpu_name_697, 8, 3, 1, 1)

        self.cpu_name_698 = QLabel(self.frame_115)
        self.cpu_name_698.setObjectName(u"cpu_name_698")
        self.cpu_name_698.setFont(font)
        self.cpu_name_698.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_116.addWidget(self.cpu_name_698, 8, 5, 1, 1)

        self.gpu3usage_23 = QLabel(self.frame_115)
        self.gpu3usage_23.setObjectName(u"gpu3usage_23")
        self.gpu3usage_23.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_23.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_23.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_116.addWidget(self.gpu3usage_23, 8, 1, 1, 1)

        self.cpu_name_699 = QLabel(self.frame_115)
        self.cpu_name_699.setObjectName(u"cpu_name_699")
        self.cpu_name_699.setFont(font1)
        self.cpu_name_699.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_116.addWidget(self.cpu_name_699, 8, 0, 1, 1)

        self.device1_23 = QLabel(self.frame_115)
        self.device1_23.setObjectName(u"device1_23")
        self.device1_23.setFont(font2)
        self.device1_23.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_23.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_23.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_116.addWidget(self.device1_23, 1, 0, 1, 1)

        self.clientipaddress_23 = QLabel(self.frame_115)
        self.clientipaddress_23.setObjectName(u"clientipaddress_23")
        self.clientipaddress_23.setFont(font)
        self.clientipaddress_23.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_23.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_23.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_116.addWidget(self.clientipaddress_23, 1, 1, 1, 5)

        self.gpu1usage_23 = QLabel(self.frame_115)
        self.gpu1usage_23.setObjectName(u"gpu1usage_23")
        self.gpu1usage_23.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_23.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_23.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_116.addWidget(self.gpu1usage_23, 6, 1, 1, 1)

        self.memoryusage_23 = QLabel(self.frame_115)
        self.memoryusage_23.setObjectName(u"memoryusage_23")
        self.memoryusage_23.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_23.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_23.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_116.addWidget(self.memoryusage_23, 8, 4, 1, 1)

        self.cpu_name_700 = QLabel(self.frame_115)
        self.cpu_name_700.setObjectName(u"cpu_name_700")
        self.cpu_name_700.setFont(font1)
        self.cpu_name_700.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_116.addWidget(self.cpu_name_700, 6, 3, 1, 1)


        self.gridLayout_115.addWidget(self.frame_115, 0, 0, 1, 3)

        self.elapsedtime_23 = QLabel(self.frame_114)
        self.elapsedtime_23.setObjectName(u"elapsedtime_23")
        self.elapsedtime_23.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_23.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_23.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_115.addWidget(self.elapsedtime_23, 1, 2, 1, 1)

        self.off_Button_23 = QPushButton(self.frame_114)
        self.off_Button_23.setObjectName(u"off_Button_23")
        self.off_Button_23.setEnabled(True)
        self.off_Button_23.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_115.addWidget(self.off_Button_23, 1, 1, 1, 1)


        self.horizontalLayout_14.addWidget(self.frame_114)

        self.frame_116 = QFrame(self.frame_17)
        self.frame_116.setObjectName(u"frame_116")
        self.frame_116.setMinimumSize(QSize(240, 200))
        self.frame_116.setMaximumSize(QSize(240, 200))
        self.frame_116.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_116.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_116.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_116.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_117 = QGridLayout(self.frame_116)
        self.gridLayout_117.setObjectName(u"gridLayout_117")
        self.on_Button_24 = QPushButton(self.frame_116)
        self.on_Button_24.setObjectName(u"on_Button_24")
        self.on_Button_24.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_117.addWidget(self.on_Button_24, 1, 0, 1, 1)

        self.frame_117 = QFrame(self.frame_116)
        self.frame_117.setObjectName(u"frame_117")
        self.frame_117.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_117.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_117.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_118 = QGridLayout(self.frame_117)
        self.gridLayout_118.setObjectName(u"gridLayout_118")
        self.gpu2usage_24 = QLabel(self.frame_117)
        self.gpu2usage_24.setObjectName(u"gpu2usage_24")
        self.gpu2usage_24.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_24.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_24.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_118.addWidget(self.gpu2usage_24, 6, 4, 1, 1)

        self.cpu_name_701 = QLabel(self.frame_117)
        self.cpu_name_701.setObjectName(u"cpu_name_701")
        self.cpu_name_701.setFont(font)
        self.cpu_name_701.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_118.addWidget(self.cpu_name_701, 3, 5, 1, 1)

        self.cpu_name_702 = QLabel(self.frame_117)
        self.cpu_name_702.setObjectName(u"cpu_name_702")
        self.cpu_name_702.setFont(font)
        self.cpu_name_702.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_118.addWidget(self.cpu_name_702, 6, 5, 1, 1)

        self.cpu_name_703 = QLabel(self.frame_117)
        self.cpu_name_703.setObjectName(u"cpu_name_703")
        self.cpu_name_703.setFont(font1)
        self.cpu_name_703.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_118.addWidget(self.cpu_name_703, 6, 0, 1, 1)

        self.cpuusage_24 = QLabel(self.frame_117)
        self.cpuusage_24.setObjectName(u"cpuusage_24")
        self.cpuusage_24.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_24.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_24.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_118.addWidget(self.cpuusage_24, 3, 1, 1, 1)

        self.cpu_name_704 = QLabel(self.frame_117)
        self.cpu_name_704.setObjectName(u"cpu_name_704")
        self.cpu_name_704.setFont(font)
        self.cpu_name_704.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_118.addWidget(self.cpu_name_704, 3, 2, 1, 1)

        self.gpu0usage_24 = QLabel(self.frame_117)
        self.gpu0usage_24.setObjectName(u"gpu0usage_24")
        self.gpu0usage_24.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_24.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_24.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_118.addWidget(self.gpu0usage_24, 3, 4, 1, 1)

        self.cpu_name_705 = QLabel(self.frame_117)
        self.cpu_name_705.setObjectName(u"cpu_name_705")
        self.cpu_name_705.setFont(font1)
        self.cpu_name_705.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_118.addWidget(self.cpu_name_705, 3, 3, 1, 1)

        self.cpu_name_706 = QLabel(self.frame_117)
        self.cpu_name_706.setObjectName(u"cpu_name_706")
        self.cpu_name_706.setFont(font1)
        self.cpu_name_706.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_118.addWidget(self.cpu_name_706, 3, 0, 1, 1)

        self.cpu_name_707 = QLabel(self.frame_117)
        self.cpu_name_707.setObjectName(u"cpu_name_707")
        self.cpu_name_707.setFont(font)
        self.cpu_name_707.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_118.addWidget(self.cpu_name_707, 8, 2, 1, 1)

        self.cpu_name_708 = QLabel(self.frame_117)
        self.cpu_name_708.setObjectName(u"cpu_name_708")
        self.cpu_name_708.setFont(font)
        self.cpu_name_708.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_118.addWidget(self.cpu_name_708, 6, 2, 1, 1)

        self.cpu_name_709 = QLabel(self.frame_117)
        self.cpu_name_709.setObjectName(u"cpu_name_709")
        self.cpu_name_709.setFont(font1)
        self.cpu_name_709.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_118.addWidget(self.cpu_name_709, 8, 3, 1, 1)

        self.cpu_name_710 = QLabel(self.frame_117)
        self.cpu_name_710.setObjectName(u"cpu_name_710")
        self.cpu_name_710.setFont(font)
        self.cpu_name_710.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_118.addWidget(self.cpu_name_710, 8, 5, 1, 1)

        self.gpu3usage_24 = QLabel(self.frame_117)
        self.gpu3usage_24.setObjectName(u"gpu3usage_24")
        self.gpu3usage_24.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_24.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_24.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_118.addWidget(self.gpu3usage_24, 8, 1, 1, 1)

        self.cpu_name_711 = QLabel(self.frame_117)
        self.cpu_name_711.setObjectName(u"cpu_name_711")
        self.cpu_name_711.setFont(font1)
        self.cpu_name_711.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_118.addWidget(self.cpu_name_711, 8, 0, 1, 1)

        self.device1_24 = QLabel(self.frame_117)
        self.device1_24.setObjectName(u"device1_24")
        self.device1_24.setFont(font2)
        self.device1_24.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_24.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_24.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_118.addWidget(self.device1_24, 1, 0, 1, 1)

        self.clientipaddress_24 = QLabel(self.frame_117)
        self.clientipaddress_24.setObjectName(u"clientipaddress_24")
        self.clientipaddress_24.setFont(font)
        self.clientipaddress_24.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_24.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_24.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_118.addWidget(self.clientipaddress_24, 1, 1, 1, 5)

        self.gpu1usage_24 = QLabel(self.frame_117)
        self.gpu1usage_24.setObjectName(u"gpu1usage_24")
        self.gpu1usage_24.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_24.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_24.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_118.addWidget(self.gpu1usage_24, 6, 1, 1, 1)

        self.memoryusage_24 = QLabel(self.frame_117)
        self.memoryusage_24.setObjectName(u"memoryusage_24")
        self.memoryusage_24.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_24.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_24.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_118.addWidget(self.memoryusage_24, 8, 4, 1, 1)

        self.cpu_name_712 = QLabel(self.frame_117)
        self.cpu_name_712.setObjectName(u"cpu_name_712")
        self.cpu_name_712.setFont(font1)
        self.cpu_name_712.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_118.addWidget(self.cpu_name_712, 6, 3, 1, 1)


        self.gridLayout_117.addWidget(self.frame_117, 0, 0, 1, 3)

        self.elapsedtime_24 = QLabel(self.frame_116)
        self.elapsedtime_24.setObjectName(u"elapsedtime_24")
        self.elapsedtime_24.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_24.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_24.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_117.addWidget(self.elapsedtime_24, 1, 2, 1, 1)

        self.off_Button_24 = QPushButton(self.frame_116)
        self.off_Button_24.setObjectName(u"off_Button_24")
        self.off_Button_24.setEnabled(True)
        self.off_Button_24.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_117.addWidget(self.off_Button_24, 1, 1, 1, 1)


        self.horizontalLayout_14.addWidget(self.frame_116)


        self.verticalLayout_3.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame_2)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_118 = QFrame(self.frame_18)
        self.frame_118.setObjectName(u"frame_118")
        self.frame_118.setMinimumSize(QSize(240, 200))
        self.frame_118.setMaximumSize(QSize(240, 200))
        self.frame_118.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_118.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_118.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_118.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_119 = QGridLayout(self.frame_118)
        self.gridLayout_119.setObjectName(u"gridLayout_119")
        self.on_Button_25 = QPushButton(self.frame_118)
        self.on_Button_25.setObjectName(u"on_Button_25")
        self.on_Button_25.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_119.addWidget(self.on_Button_25, 1, 0, 1, 1)

        self.frame_119 = QFrame(self.frame_118)
        self.frame_119.setObjectName(u"frame_119")
        self.frame_119.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_119.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_119.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_120 = QGridLayout(self.frame_119)
        self.gridLayout_120.setObjectName(u"gridLayout_120")
        self.gpu2usage_25 = QLabel(self.frame_119)
        self.gpu2usage_25.setObjectName(u"gpu2usage_25")
        self.gpu2usage_25.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_25.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_25.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_120.addWidget(self.gpu2usage_25, 6, 4, 1, 1)

        self.cpu_name_713 = QLabel(self.frame_119)
        self.cpu_name_713.setObjectName(u"cpu_name_713")
        self.cpu_name_713.setFont(font)
        self.cpu_name_713.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_120.addWidget(self.cpu_name_713, 3, 5, 1, 1)

        self.cpu_name_714 = QLabel(self.frame_119)
        self.cpu_name_714.setObjectName(u"cpu_name_714")
        self.cpu_name_714.setFont(font)
        self.cpu_name_714.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_120.addWidget(self.cpu_name_714, 6, 5, 1, 1)

        self.cpu_name_715 = QLabel(self.frame_119)
        self.cpu_name_715.setObjectName(u"cpu_name_715")
        self.cpu_name_715.setFont(font1)
        self.cpu_name_715.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_120.addWidget(self.cpu_name_715, 6, 0, 1, 1)

        self.cpuusage_25 = QLabel(self.frame_119)
        self.cpuusage_25.setObjectName(u"cpuusage_25")
        self.cpuusage_25.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_25.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_25.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_120.addWidget(self.cpuusage_25, 3, 1, 1, 1)

        self.cpu_name_716 = QLabel(self.frame_119)
        self.cpu_name_716.setObjectName(u"cpu_name_716")
        self.cpu_name_716.setFont(font)
        self.cpu_name_716.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_120.addWidget(self.cpu_name_716, 3, 2, 1, 1)

        self.gpu0usage_25 = QLabel(self.frame_119)
        self.gpu0usage_25.setObjectName(u"gpu0usage_25")
        self.gpu0usage_25.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_25.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_25.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_120.addWidget(self.gpu0usage_25, 3, 4, 1, 1)

        self.cpu_name_717 = QLabel(self.frame_119)
        self.cpu_name_717.setObjectName(u"cpu_name_717")
        self.cpu_name_717.setFont(font1)
        self.cpu_name_717.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_120.addWidget(self.cpu_name_717, 3, 3, 1, 1)

        self.cpu_name_718 = QLabel(self.frame_119)
        self.cpu_name_718.setObjectName(u"cpu_name_718")
        self.cpu_name_718.setFont(font1)
        self.cpu_name_718.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_120.addWidget(self.cpu_name_718, 3, 0, 1, 1)

        self.cpu_name_719 = QLabel(self.frame_119)
        self.cpu_name_719.setObjectName(u"cpu_name_719")
        self.cpu_name_719.setFont(font)
        self.cpu_name_719.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_120.addWidget(self.cpu_name_719, 8, 2, 1, 1)

        self.cpu_name_720 = QLabel(self.frame_119)
        self.cpu_name_720.setObjectName(u"cpu_name_720")
        self.cpu_name_720.setFont(font)
        self.cpu_name_720.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_120.addWidget(self.cpu_name_720, 6, 2, 1, 1)

        self.cpu_name_721 = QLabel(self.frame_119)
        self.cpu_name_721.setObjectName(u"cpu_name_721")
        self.cpu_name_721.setFont(font1)
        self.cpu_name_721.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_120.addWidget(self.cpu_name_721, 8, 3, 1, 1)

        self.cpu_name_722 = QLabel(self.frame_119)
        self.cpu_name_722.setObjectName(u"cpu_name_722")
        self.cpu_name_722.setFont(font)
        self.cpu_name_722.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_120.addWidget(self.cpu_name_722, 8, 5, 1, 1)

        self.gpu3usage_25 = QLabel(self.frame_119)
        self.gpu3usage_25.setObjectName(u"gpu3usage_25")
        self.gpu3usage_25.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_25.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_25.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_120.addWidget(self.gpu3usage_25, 8, 1, 1, 1)

        self.cpu_name_723 = QLabel(self.frame_119)
        self.cpu_name_723.setObjectName(u"cpu_name_723")
        self.cpu_name_723.setFont(font1)
        self.cpu_name_723.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_120.addWidget(self.cpu_name_723, 8, 0, 1, 1)

        self.device1_25 = QLabel(self.frame_119)
        self.device1_25.setObjectName(u"device1_25")
        self.device1_25.setFont(font2)
        self.device1_25.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_25.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_25.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_120.addWidget(self.device1_25, 1, 0, 1, 1)

        self.clientipaddress_25 = QLabel(self.frame_119)
        self.clientipaddress_25.setObjectName(u"clientipaddress_25")
        self.clientipaddress_25.setFont(font)
        self.clientipaddress_25.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_25.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_25.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_120.addWidget(self.clientipaddress_25, 1, 1, 1, 5)

        self.gpu1usage_25 = QLabel(self.frame_119)
        self.gpu1usage_25.setObjectName(u"gpu1usage_25")
        self.gpu1usage_25.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_25.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_25.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_120.addWidget(self.gpu1usage_25, 6, 1, 1, 1)

        self.memoryusage_25 = QLabel(self.frame_119)
        self.memoryusage_25.setObjectName(u"memoryusage_25")
        self.memoryusage_25.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_25.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_25.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_120.addWidget(self.memoryusage_25, 8, 4, 1, 1)

        self.cpu_name_724 = QLabel(self.frame_119)
        self.cpu_name_724.setObjectName(u"cpu_name_724")
        self.cpu_name_724.setFont(font1)
        self.cpu_name_724.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_120.addWidget(self.cpu_name_724, 6, 3, 1, 1)


        self.gridLayout_119.addWidget(self.frame_119, 0, 0, 1, 3)

        self.elapsedtime_25 = QLabel(self.frame_118)
        self.elapsedtime_25.setObjectName(u"elapsedtime_25")
        self.elapsedtime_25.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_25.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_25.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_119.addWidget(self.elapsedtime_25, 1, 2, 1, 1)

        self.off_Button_25 = QPushButton(self.frame_118)
        self.off_Button_25.setObjectName(u"off_Button_25")
        self.off_Button_25.setEnabled(True)
        self.off_Button_25.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_119.addWidget(self.off_Button_25, 1, 1, 1, 1)


        self.horizontalLayout_15.addWidget(self.frame_118)

        self.frame_120 = QFrame(self.frame_18)
        self.frame_120.setObjectName(u"frame_120")
        self.frame_120.setMinimumSize(QSize(240, 200))
        self.frame_120.setMaximumSize(QSize(240, 200))
        self.frame_120.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_120.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_120.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_120.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_121 = QGridLayout(self.frame_120)
        self.gridLayout_121.setObjectName(u"gridLayout_121")
        self.on_Button_26 = QPushButton(self.frame_120)
        self.on_Button_26.setObjectName(u"on_Button_26")
        self.on_Button_26.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_121.addWidget(self.on_Button_26, 1, 0, 1, 1)

        self.frame_121 = QFrame(self.frame_120)
        self.frame_121.setObjectName(u"frame_121")
        self.frame_121.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_121.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_121.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_122 = QGridLayout(self.frame_121)
        self.gridLayout_122.setObjectName(u"gridLayout_122")
        self.gpu2usage_26 = QLabel(self.frame_121)
        self.gpu2usage_26.setObjectName(u"gpu2usage_26")
        self.gpu2usage_26.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_26.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_26.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_122.addWidget(self.gpu2usage_26, 6, 4, 1, 1)

        self.cpu_name_725 = QLabel(self.frame_121)
        self.cpu_name_725.setObjectName(u"cpu_name_725")
        self.cpu_name_725.setFont(font)
        self.cpu_name_725.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_122.addWidget(self.cpu_name_725, 3, 5, 1, 1)

        self.cpu_name_726 = QLabel(self.frame_121)
        self.cpu_name_726.setObjectName(u"cpu_name_726")
        self.cpu_name_726.setFont(font)
        self.cpu_name_726.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_122.addWidget(self.cpu_name_726, 6, 5, 1, 1)

        self.cpu_name_727 = QLabel(self.frame_121)
        self.cpu_name_727.setObjectName(u"cpu_name_727")
        self.cpu_name_727.setFont(font1)
        self.cpu_name_727.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_122.addWidget(self.cpu_name_727, 6, 0, 1, 1)

        self.cpuusage_26 = QLabel(self.frame_121)
        self.cpuusage_26.setObjectName(u"cpuusage_26")
        self.cpuusage_26.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_26.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_26.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_122.addWidget(self.cpuusage_26, 3, 1, 1, 1)

        self.cpu_name_728 = QLabel(self.frame_121)
        self.cpu_name_728.setObjectName(u"cpu_name_728")
        self.cpu_name_728.setFont(font)
        self.cpu_name_728.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_122.addWidget(self.cpu_name_728, 3, 2, 1, 1)

        self.gpu0usage_26 = QLabel(self.frame_121)
        self.gpu0usage_26.setObjectName(u"gpu0usage_26")
        self.gpu0usage_26.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_26.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_26.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_122.addWidget(self.gpu0usage_26, 3, 4, 1, 1)

        self.cpu_name_729 = QLabel(self.frame_121)
        self.cpu_name_729.setObjectName(u"cpu_name_729")
        self.cpu_name_729.setFont(font1)
        self.cpu_name_729.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_122.addWidget(self.cpu_name_729, 3, 3, 1, 1)

        self.cpu_name_730 = QLabel(self.frame_121)
        self.cpu_name_730.setObjectName(u"cpu_name_730")
        self.cpu_name_730.setFont(font1)
        self.cpu_name_730.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_122.addWidget(self.cpu_name_730, 3, 0, 1, 1)

        self.cpu_name_731 = QLabel(self.frame_121)
        self.cpu_name_731.setObjectName(u"cpu_name_731")
        self.cpu_name_731.setFont(font)
        self.cpu_name_731.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_122.addWidget(self.cpu_name_731, 8, 2, 1, 1)

        self.cpu_name_732 = QLabel(self.frame_121)
        self.cpu_name_732.setObjectName(u"cpu_name_732")
        self.cpu_name_732.setFont(font)
        self.cpu_name_732.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_122.addWidget(self.cpu_name_732, 6, 2, 1, 1)

        self.cpu_name_733 = QLabel(self.frame_121)
        self.cpu_name_733.setObjectName(u"cpu_name_733")
        self.cpu_name_733.setFont(font1)
        self.cpu_name_733.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_122.addWidget(self.cpu_name_733, 8, 3, 1, 1)

        self.cpu_name_734 = QLabel(self.frame_121)
        self.cpu_name_734.setObjectName(u"cpu_name_734")
        self.cpu_name_734.setFont(font)
        self.cpu_name_734.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_122.addWidget(self.cpu_name_734, 8, 5, 1, 1)

        self.gpu3usage_26 = QLabel(self.frame_121)
        self.gpu3usage_26.setObjectName(u"gpu3usage_26")
        self.gpu3usage_26.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_26.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_26.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_122.addWidget(self.gpu3usage_26, 8, 1, 1, 1)

        self.cpu_name_735 = QLabel(self.frame_121)
        self.cpu_name_735.setObjectName(u"cpu_name_735")
        self.cpu_name_735.setFont(font1)
        self.cpu_name_735.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_122.addWidget(self.cpu_name_735, 8, 0, 1, 1)

        self.device1_26 = QLabel(self.frame_121)
        self.device1_26.setObjectName(u"device1_26")
        self.device1_26.setFont(font2)
        self.device1_26.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_26.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_26.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_122.addWidget(self.device1_26, 1, 0, 1, 1)

        self.clientipaddress_26 = QLabel(self.frame_121)
        self.clientipaddress_26.setObjectName(u"clientipaddress_26")
        self.clientipaddress_26.setFont(font)
        self.clientipaddress_26.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_26.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_26.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_122.addWidget(self.clientipaddress_26, 1, 1, 1, 5)

        self.gpu1usage_26 = QLabel(self.frame_121)
        self.gpu1usage_26.setObjectName(u"gpu1usage_26")
        self.gpu1usage_26.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_26.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_26.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_122.addWidget(self.gpu1usage_26, 6, 1, 1, 1)

        self.memoryusage_26 = QLabel(self.frame_121)
        self.memoryusage_26.setObjectName(u"memoryusage_26")
        self.memoryusage_26.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_26.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_26.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_122.addWidget(self.memoryusage_26, 8, 4, 1, 1)

        self.cpu_name_736 = QLabel(self.frame_121)
        self.cpu_name_736.setObjectName(u"cpu_name_736")
        self.cpu_name_736.setFont(font1)
        self.cpu_name_736.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_122.addWidget(self.cpu_name_736, 6, 3, 1, 1)


        self.gridLayout_121.addWidget(self.frame_121, 0, 0, 1, 3)

        self.elapsedtime_26 = QLabel(self.frame_120)
        self.elapsedtime_26.setObjectName(u"elapsedtime_26")
        self.elapsedtime_26.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_26.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_26.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_121.addWidget(self.elapsedtime_26, 1, 2, 1, 1)

        self.off_Button_26 = QPushButton(self.frame_120)
        self.off_Button_26.setObjectName(u"off_Button_26")
        self.off_Button_26.setEnabled(True)
        self.off_Button_26.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_121.addWidget(self.off_Button_26, 1, 1, 1, 1)


        self.horizontalLayout_15.addWidget(self.frame_120)

        self.frame_122 = QFrame(self.frame_18)
        self.frame_122.setObjectName(u"frame_122")
        self.frame_122.setMinimumSize(QSize(240, 200))
        self.frame_122.setMaximumSize(QSize(240, 200))
        self.frame_122.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_122.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_122.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_122.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_123 = QGridLayout(self.frame_122)
        self.gridLayout_123.setObjectName(u"gridLayout_123")
        self.on_Button_27 = QPushButton(self.frame_122)
        self.on_Button_27.setObjectName(u"on_Button_27")
        self.on_Button_27.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_123.addWidget(self.on_Button_27, 1, 0, 1, 1)

        self.frame_123 = QFrame(self.frame_122)
        self.frame_123.setObjectName(u"frame_123")
        self.frame_123.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_123.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_123.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_124 = QGridLayout(self.frame_123)
        self.gridLayout_124.setObjectName(u"gridLayout_124")
        self.gpu2usage_27 = QLabel(self.frame_123)
        self.gpu2usage_27.setObjectName(u"gpu2usage_27")
        self.gpu2usage_27.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_27.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_27.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_124.addWidget(self.gpu2usage_27, 6, 4, 1, 1)

        self.cpu_name_737 = QLabel(self.frame_123)
        self.cpu_name_737.setObjectName(u"cpu_name_737")
        self.cpu_name_737.setFont(font)
        self.cpu_name_737.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_124.addWidget(self.cpu_name_737, 3, 5, 1, 1)

        self.cpu_name_738 = QLabel(self.frame_123)
        self.cpu_name_738.setObjectName(u"cpu_name_738")
        self.cpu_name_738.setFont(font)
        self.cpu_name_738.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_124.addWidget(self.cpu_name_738, 6, 5, 1, 1)

        self.cpu_name_739 = QLabel(self.frame_123)
        self.cpu_name_739.setObjectName(u"cpu_name_739")
        self.cpu_name_739.setFont(font1)
        self.cpu_name_739.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_124.addWidget(self.cpu_name_739, 6, 0, 1, 1)

        self.cpuusage_27 = QLabel(self.frame_123)
        self.cpuusage_27.setObjectName(u"cpuusage_27")
        self.cpuusage_27.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_27.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_27.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_124.addWidget(self.cpuusage_27, 3, 1, 1, 1)

        self.cpu_name_740 = QLabel(self.frame_123)
        self.cpu_name_740.setObjectName(u"cpu_name_740")
        self.cpu_name_740.setFont(font)
        self.cpu_name_740.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_124.addWidget(self.cpu_name_740, 3, 2, 1, 1)

        self.gpu0usage_27 = QLabel(self.frame_123)
        self.gpu0usage_27.setObjectName(u"gpu0usage_27")
        self.gpu0usage_27.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_27.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_27.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_124.addWidget(self.gpu0usage_27, 3, 4, 1, 1)

        self.cpu_name_741 = QLabel(self.frame_123)
        self.cpu_name_741.setObjectName(u"cpu_name_741")
        self.cpu_name_741.setFont(font1)
        self.cpu_name_741.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_124.addWidget(self.cpu_name_741, 3, 3, 1, 1)

        self.cpu_name_742 = QLabel(self.frame_123)
        self.cpu_name_742.setObjectName(u"cpu_name_742")
        self.cpu_name_742.setFont(font1)
        self.cpu_name_742.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_124.addWidget(self.cpu_name_742, 3, 0, 1, 1)

        self.cpu_name_743 = QLabel(self.frame_123)
        self.cpu_name_743.setObjectName(u"cpu_name_743")
        self.cpu_name_743.setFont(font)
        self.cpu_name_743.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_124.addWidget(self.cpu_name_743, 8, 2, 1, 1)

        self.cpu_name_744 = QLabel(self.frame_123)
        self.cpu_name_744.setObjectName(u"cpu_name_744")
        self.cpu_name_744.setFont(font)
        self.cpu_name_744.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_124.addWidget(self.cpu_name_744, 6, 2, 1, 1)

        self.cpu_name_745 = QLabel(self.frame_123)
        self.cpu_name_745.setObjectName(u"cpu_name_745")
        self.cpu_name_745.setFont(font1)
        self.cpu_name_745.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_124.addWidget(self.cpu_name_745, 8, 3, 1, 1)

        self.cpu_name_746 = QLabel(self.frame_123)
        self.cpu_name_746.setObjectName(u"cpu_name_746")
        self.cpu_name_746.setFont(font)
        self.cpu_name_746.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_124.addWidget(self.cpu_name_746, 8, 5, 1, 1)

        self.gpu3usage_27 = QLabel(self.frame_123)
        self.gpu3usage_27.setObjectName(u"gpu3usage_27")
        self.gpu3usage_27.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_27.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_27.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_124.addWidget(self.gpu3usage_27, 8, 1, 1, 1)

        self.cpu_name_747 = QLabel(self.frame_123)
        self.cpu_name_747.setObjectName(u"cpu_name_747")
        self.cpu_name_747.setFont(font1)
        self.cpu_name_747.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_124.addWidget(self.cpu_name_747, 8, 0, 1, 1)

        self.device1_27 = QLabel(self.frame_123)
        self.device1_27.setObjectName(u"device1_27")
        self.device1_27.setFont(font2)
        self.device1_27.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_27.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_27.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_124.addWidget(self.device1_27, 1, 0, 1, 1)

        self.clientipaddress_27 = QLabel(self.frame_123)
        self.clientipaddress_27.setObjectName(u"clientipaddress_27")
        self.clientipaddress_27.setFont(font)
        self.clientipaddress_27.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_27.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_27.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_124.addWidget(self.clientipaddress_27, 1, 1, 1, 5)

        self.gpu1usage_27 = QLabel(self.frame_123)
        self.gpu1usage_27.setObjectName(u"gpu1usage_27")
        self.gpu1usage_27.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_27.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_27.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_124.addWidget(self.gpu1usage_27, 6, 1, 1, 1)

        self.memoryusage_27 = QLabel(self.frame_123)
        self.memoryusage_27.setObjectName(u"memoryusage_27")
        self.memoryusage_27.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_27.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_27.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_124.addWidget(self.memoryusage_27, 8, 4, 1, 1)

        self.cpu_name_748 = QLabel(self.frame_123)
        self.cpu_name_748.setObjectName(u"cpu_name_748")
        self.cpu_name_748.setFont(font1)
        self.cpu_name_748.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_124.addWidget(self.cpu_name_748, 6, 3, 1, 1)


        self.gridLayout_123.addWidget(self.frame_123, 0, 0, 1, 3)

        self.elapsedtime_27 = QLabel(self.frame_122)
        self.elapsedtime_27.setObjectName(u"elapsedtime_27")
        self.elapsedtime_27.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_27.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_27.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_123.addWidget(self.elapsedtime_27, 1, 2, 1, 1)

        self.off_Button_27 = QPushButton(self.frame_122)
        self.off_Button_27.setObjectName(u"off_Button_27")
        self.off_Button_27.setEnabled(True)
        self.off_Button_27.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_123.addWidget(self.off_Button_27, 1, 1, 1, 1)


        self.horizontalLayout_15.addWidget(self.frame_122)

        self.frame_124 = QFrame(self.frame_18)
        self.frame_124.setObjectName(u"frame_124")
        self.frame_124.setMinimumSize(QSize(240, 200))
        self.frame_124.setMaximumSize(QSize(240, 200))
        self.frame_124.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_124.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_124.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_124.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_125 = QGridLayout(self.frame_124)
        self.gridLayout_125.setObjectName(u"gridLayout_125")
        self.on_Button_28 = QPushButton(self.frame_124)
        self.on_Button_28.setObjectName(u"on_Button_28")
        self.on_Button_28.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_125.addWidget(self.on_Button_28, 1, 0, 1, 1)

        self.frame_125 = QFrame(self.frame_124)
        self.frame_125.setObjectName(u"frame_125")
        self.frame_125.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_125.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_125.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_126 = QGridLayout(self.frame_125)
        self.gridLayout_126.setObjectName(u"gridLayout_126")
        self.gpu2usage_28 = QLabel(self.frame_125)
        self.gpu2usage_28.setObjectName(u"gpu2usage_28")
        self.gpu2usage_28.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_28.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_28.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_126.addWidget(self.gpu2usage_28, 6, 4, 1, 1)

        self.cpu_name_749 = QLabel(self.frame_125)
        self.cpu_name_749.setObjectName(u"cpu_name_749")
        self.cpu_name_749.setFont(font)
        self.cpu_name_749.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_126.addWidget(self.cpu_name_749, 3, 5, 1, 1)

        self.cpu_name_750 = QLabel(self.frame_125)
        self.cpu_name_750.setObjectName(u"cpu_name_750")
        self.cpu_name_750.setFont(font)
        self.cpu_name_750.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_126.addWidget(self.cpu_name_750, 6, 5, 1, 1)

        self.cpu_name_751 = QLabel(self.frame_125)
        self.cpu_name_751.setObjectName(u"cpu_name_751")
        self.cpu_name_751.setFont(font1)
        self.cpu_name_751.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_126.addWidget(self.cpu_name_751, 6, 0, 1, 1)

        self.cpuusage_28 = QLabel(self.frame_125)
        self.cpuusage_28.setObjectName(u"cpuusage_28")
        self.cpuusage_28.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_28.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_28.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_126.addWidget(self.cpuusage_28, 3, 1, 1, 1)

        self.cpu_name_752 = QLabel(self.frame_125)
        self.cpu_name_752.setObjectName(u"cpu_name_752")
        self.cpu_name_752.setFont(font)
        self.cpu_name_752.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_126.addWidget(self.cpu_name_752, 3, 2, 1, 1)

        self.gpu0usage_28 = QLabel(self.frame_125)
        self.gpu0usage_28.setObjectName(u"gpu0usage_28")
        self.gpu0usage_28.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_28.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_28.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_126.addWidget(self.gpu0usage_28, 3, 4, 1, 1)

        self.cpu_name_753 = QLabel(self.frame_125)
        self.cpu_name_753.setObjectName(u"cpu_name_753")
        self.cpu_name_753.setFont(font1)
        self.cpu_name_753.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_126.addWidget(self.cpu_name_753, 3, 3, 1, 1)

        self.cpu_name_754 = QLabel(self.frame_125)
        self.cpu_name_754.setObjectName(u"cpu_name_754")
        self.cpu_name_754.setFont(font1)
        self.cpu_name_754.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_126.addWidget(self.cpu_name_754, 3, 0, 1, 1)

        self.cpu_name_755 = QLabel(self.frame_125)
        self.cpu_name_755.setObjectName(u"cpu_name_755")
        self.cpu_name_755.setFont(font)
        self.cpu_name_755.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_126.addWidget(self.cpu_name_755, 8, 2, 1, 1)

        self.cpu_name_756 = QLabel(self.frame_125)
        self.cpu_name_756.setObjectName(u"cpu_name_756")
        self.cpu_name_756.setFont(font)
        self.cpu_name_756.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_126.addWidget(self.cpu_name_756, 6, 2, 1, 1)

        self.cpu_name_757 = QLabel(self.frame_125)
        self.cpu_name_757.setObjectName(u"cpu_name_757")
        self.cpu_name_757.setFont(font1)
        self.cpu_name_757.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_126.addWidget(self.cpu_name_757, 8, 3, 1, 1)

        self.cpu_name_758 = QLabel(self.frame_125)
        self.cpu_name_758.setObjectName(u"cpu_name_758")
        self.cpu_name_758.setFont(font)
        self.cpu_name_758.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_126.addWidget(self.cpu_name_758, 8, 5, 1, 1)

        self.gpu3usage_28 = QLabel(self.frame_125)
        self.gpu3usage_28.setObjectName(u"gpu3usage_28")
        self.gpu3usage_28.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_28.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_28.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_126.addWidget(self.gpu3usage_28, 8, 1, 1, 1)

        self.cpu_name_759 = QLabel(self.frame_125)
        self.cpu_name_759.setObjectName(u"cpu_name_759")
        self.cpu_name_759.setFont(font1)
        self.cpu_name_759.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_126.addWidget(self.cpu_name_759, 8, 0, 1, 1)

        self.device1_28 = QLabel(self.frame_125)
        self.device1_28.setObjectName(u"device1_28")
        self.device1_28.setFont(font2)
        self.device1_28.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_28.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_28.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_126.addWidget(self.device1_28, 1, 0, 1, 1)

        self.clientipaddress_28 = QLabel(self.frame_125)
        self.clientipaddress_28.setObjectName(u"clientipaddress_28")
        self.clientipaddress_28.setFont(font)
        self.clientipaddress_28.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_28.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_28.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_126.addWidget(self.clientipaddress_28, 1, 1, 1, 5)

        self.gpu1usage_28 = QLabel(self.frame_125)
        self.gpu1usage_28.setObjectName(u"gpu1usage_28")
        self.gpu1usage_28.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_28.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_28.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_126.addWidget(self.gpu1usage_28, 6, 1, 1, 1)

        self.memoryusage_28 = QLabel(self.frame_125)
        self.memoryusage_28.setObjectName(u"memoryusage_28")
        self.memoryusage_28.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_28.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_28.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_126.addWidget(self.memoryusage_28, 8, 4, 1, 1)

        self.cpu_name_760 = QLabel(self.frame_125)
        self.cpu_name_760.setObjectName(u"cpu_name_760")
        self.cpu_name_760.setFont(font1)
        self.cpu_name_760.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_126.addWidget(self.cpu_name_760, 6, 3, 1, 1)


        self.gridLayout_125.addWidget(self.frame_125, 0, 0, 1, 3)

        self.elapsedtime_28 = QLabel(self.frame_124)
        self.elapsedtime_28.setObjectName(u"elapsedtime_28")
        self.elapsedtime_28.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_28.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_28.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_125.addWidget(self.elapsedtime_28, 1, 2, 1, 1)

        self.off_Button_28 = QPushButton(self.frame_124)
        self.off_Button_28.setObjectName(u"off_Button_28")
        self.off_Button_28.setEnabled(True)
        self.off_Button_28.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_125.addWidget(self.off_Button_28, 1, 1, 1, 1)


        self.horizontalLayout_15.addWidget(self.frame_124)


        self.verticalLayout_3.addWidget(self.frame_18)

        self.frame_23 = QFrame(self.frame_2)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_126 = QFrame(self.frame_23)
        self.frame_126.setObjectName(u"frame_126")
        self.frame_126.setMinimumSize(QSize(240, 200))
        self.frame_126.setMaximumSize(QSize(240, 200))
        self.frame_126.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_126.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_126.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_126.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_127 = QGridLayout(self.frame_126)
        self.gridLayout_127.setObjectName(u"gridLayout_127")
        self.on_Button_29 = QPushButton(self.frame_126)
        self.on_Button_29.setObjectName(u"on_Button_29")
        self.on_Button_29.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_127.addWidget(self.on_Button_29, 1, 0, 1, 1)

        self.frame_127 = QFrame(self.frame_126)
        self.frame_127.setObjectName(u"frame_127")
        self.frame_127.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_127.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_127.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_128 = QGridLayout(self.frame_127)
        self.gridLayout_128.setObjectName(u"gridLayout_128")
        self.gpu2usage_29 = QLabel(self.frame_127)
        self.gpu2usage_29.setObjectName(u"gpu2usage_29")
        self.gpu2usage_29.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_29.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_29.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_128.addWidget(self.gpu2usage_29, 6, 4, 1, 1)

        self.cpu_name_761 = QLabel(self.frame_127)
        self.cpu_name_761.setObjectName(u"cpu_name_761")
        self.cpu_name_761.setFont(font)
        self.cpu_name_761.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_128.addWidget(self.cpu_name_761, 3, 5, 1, 1)

        self.cpu_name_762 = QLabel(self.frame_127)
        self.cpu_name_762.setObjectName(u"cpu_name_762")
        self.cpu_name_762.setFont(font)
        self.cpu_name_762.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_128.addWidget(self.cpu_name_762, 6, 5, 1, 1)

        self.cpu_name_763 = QLabel(self.frame_127)
        self.cpu_name_763.setObjectName(u"cpu_name_763")
        self.cpu_name_763.setFont(font1)
        self.cpu_name_763.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_128.addWidget(self.cpu_name_763, 6, 0, 1, 1)

        self.cpuusage_29 = QLabel(self.frame_127)
        self.cpuusage_29.setObjectName(u"cpuusage_29")
        self.cpuusage_29.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_29.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_29.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_128.addWidget(self.cpuusage_29, 3, 1, 1, 1)

        self.cpu_name_764 = QLabel(self.frame_127)
        self.cpu_name_764.setObjectName(u"cpu_name_764")
        self.cpu_name_764.setFont(font)
        self.cpu_name_764.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_128.addWidget(self.cpu_name_764, 3, 2, 1, 1)

        self.gpu0usage_29 = QLabel(self.frame_127)
        self.gpu0usage_29.setObjectName(u"gpu0usage_29")
        self.gpu0usage_29.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_29.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_29.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_128.addWidget(self.gpu0usage_29, 3, 4, 1, 1)

        self.cpu_name_765 = QLabel(self.frame_127)
        self.cpu_name_765.setObjectName(u"cpu_name_765")
        self.cpu_name_765.setFont(font1)
        self.cpu_name_765.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_128.addWidget(self.cpu_name_765, 3, 3, 1, 1)

        self.cpu_name_766 = QLabel(self.frame_127)
        self.cpu_name_766.setObjectName(u"cpu_name_766")
        self.cpu_name_766.setFont(font1)
        self.cpu_name_766.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_128.addWidget(self.cpu_name_766, 3, 0, 1, 1)

        self.cpu_name_767 = QLabel(self.frame_127)
        self.cpu_name_767.setObjectName(u"cpu_name_767")
        self.cpu_name_767.setFont(font)
        self.cpu_name_767.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_128.addWidget(self.cpu_name_767, 8, 2, 1, 1)

        self.cpu_name_768 = QLabel(self.frame_127)
        self.cpu_name_768.setObjectName(u"cpu_name_768")
        self.cpu_name_768.setFont(font)
        self.cpu_name_768.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_128.addWidget(self.cpu_name_768, 6, 2, 1, 1)

        self.cpu_name_769 = QLabel(self.frame_127)
        self.cpu_name_769.setObjectName(u"cpu_name_769")
        self.cpu_name_769.setFont(font1)
        self.cpu_name_769.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_128.addWidget(self.cpu_name_769, 8, 3, 1, 1)

        self.cpu_name_770 = QLabel(self.frame_127)
        self.cpu_name_770.setObjectName(u"cpu_name_770")
        self.cpu_name_770.setFont(font)
        self.cpu_name_770.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_128.addWidget(self.cpu_name_770, 8, 5, 1, 1)

        self.gpu3usage_29 = QLabel(self.frame_127)
        self.gpu3usage_29.setObjectName(u"gpu3usage_29")
        self.gpu3usage_29.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_29.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_29.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_128.addWidget(self.gpu3usage_29, 8, 1, 1, 1)

        self.cpu_name_771 = QLabel(self.frame_127)
        self.cpu_name_771.setObjectName(u"cpu_name_771")
        self.cpu_name_771.setFont(font1)
        self.cpu_name_771.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_128.addWidget(self.cpu_name_771, 8, 0, 1, 1)

        self.device1_29 = QLabel(self.frame_127)
        self.device1_29.setObjectName(u"device1_29")
        self.device1_29.setFont(font2)
        self.device1_29.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_29.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_29.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_128.addWidget(self.device1_29, 1, 0, 1, 1)

        self.clientipaddress_29 = QLabel(self.frame_127)
        self.clientipaddress_29.setObjectName(u"clientipaddress_29")
        self.clientipaddress_29.setFont(font)
        self.clientipaddress_29.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_29.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_29.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_128.addWidget(self.clientipaddress_29, 1, 1, 1, 5)

        self.gpu1usage_29 = QLabel(self.frame_127)
        self.gpu1usage_29.setObjectName(u"gpu1usage_29")
        self.gpu1usage_29.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_29.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_29.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_128.addWidget(self.gpu1usage_29, 6, 1, 1, 1)

        self.memoryusage_29 = QLabel(self.frame_127)
        self.memoryusage_29.setObjectName(u"memoryusage_29")
        self.memoryusage_29.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_29.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_29.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_128.addWidget(self.memoryusage_29, 8, 4, 1, 1)

        self.cpu_name_772 = QLabel(self.frame_127)
        self.cpu_name_772.setObjectName(u"cpu_name_772")
        self.cpu_name_772.setFont(font1)
        self.cpu_name_772.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_128.addWidget(self.cpu_name_772, 6, 3, 1, 1)


        self.gridLayout_127.addWidget(self.frame_127, 0, 0, 1, 3)

        self.elapsedtime_29 = QLabel(self.frame_126)
        self.elapsedtime_29.setObjectName(u"elapsedtime_29")
        self.elapsedtime_29.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_29.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_29.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_127.addWidget(self.elapsedtime_29, 1, 2, 1, 1)

        self.off_Button_29 = QPushButton(self.frame_126)
        self.off_Button_29.setObjectName(u"off_Button_29")
        self.off_Button_29.setEnabled(True)
        self.off_Button_29.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_127.addWidget(self.off_Button_29, 1, 1, 1, 1)


        self.horizontalLayout_16.addWidget(self.frame_126)

        self.frame_128 = QFrame(self.frame_23)
        self.frame_128.setObjectName(u"frame_128")
        self.frame_128.setMinimumSize(QSize(240, 200))
        self.frame_128.setMaximumSize(QSize(240, 200))
        self.frame_128.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_128.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_128.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_128.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_129 = QGridLayout(self.frame_128)
        self.gridLayout_129.setObjectName(u"gridLayout_129")
        self.on_Button_30 = QPushButton(self.frame_128)
        self.on_Button_30.setObjectName(u"on_Button_30")
        self.on_Button_30.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_129.addWidget(self.on_Button_30, 1, 0, 1, 1)

        self.frame_129 = QFrame(self.frame_128)
        self.frame_129.setObjectName(u"frame_129")
        self.frame_129.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_129.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_129.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_130 = QGridLayout(self.frame_129)
        self.gridLayout_130.setObjectName(u"gridLayout_130")
        self.gpu2usage_30 = QLabel(self.frame_129)
        self.gpu2usage_30.setObjectName(u"gpu2usage_30")
        self.gpu2usage_30.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_30.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_30.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_130.addWidget(self.gpu2usage_30, 6, 4, 1, 1)

        self.cpu_name_773 = QLabel(self.frame_129)
        self.cpu_name_773.setObjectName(u"cpu_name_773")
        self.cpu_name_773.setFont(font)
        self.cpu_name_773.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_130.addWidget(self.cpu_name_773, 3, 5, 1, 1)

        self.cpu_name_774 = QLabel(self.frame_129)
        self.cpu_name_774.setObjectName(u"cpu_name_774")
        self.cpu_name_774.setFont(font)
        self.cpu_name_774.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_130.addWidget(self.cpu_name_774, 6, 5, 1, 1)

        self.cpu_name_775 = QLabel(self.frame_129)
        self.cpu_name_775.setObjectName(u"cpu_name_775")
        self.cpu_name_775.setFont(font1)
        self.cpu_name_775.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_130.addWidget(self.cpu_name_775, 6, 0, 1, 1)

        self.cpuusage_30 = QLabel(self.frame_129)
        self.cpuusage_30.setObjectName(u"cpuusage_30")
        self.cpuusage_30.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_30.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_30.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_130.addWidget(self.cpuusage_30, 3, 1, 1, 1)

        self.cpu_name_776 = QLabel(self.frame_129)
        self.cpu_name_776.setObjectName(u"cpu_name_776")
        self.cpu_name_776.setFont(font)
        self.cpu_name_776.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_130.addWidget(self.cpu_name_776, 3, 2, 1, 1)

        self.gpu0usage_30 = QLabel(self.frame_129)
        self.gpu0usage_30.setObjectName(u"gpu0usage_30")
        self.gpu0usage_30.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_30.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_30.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_130.addWidget(self.gpu0usage_30, 3, 4, 1, 1)

        self.cpu_name_777 = QLabel(self.frame_129)
        self.cpu_name_777.setObjectName(u"cpu_name_777")
        self.cpu_name_777.setFont(font1)
        self.cpu_name_777.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_130.addWidget(self.cpu_name_777, 3, 3, 1, 1)

        self.cpu_name_778 = QLabel(self.frame_129)
        self.cpu_name_778.setObjectName(u"cpu_name_778")
        self.cpu_name_778.setFont(font1)
        self.cpu_name_778.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_130.addWidget(self.cpu_name_778, 3, 0, 1, 1)

        self.cpu_name_779 = QLabel(self.frame_129)
        self.cpu_name_779.setObjectName(u"cpu_name_779")
        self.cpu_name_779.setFont(font)
        self.cpu_name_779.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_130.addWidget(self.cpu_name_779, 8, 2, 1, 1)

        self.cpu_name_780 = QLabel(self.frame_129)
        self.cpu_name_780.setObjectName(u"cpu_name_780")
        self.cpu_name_780.setFont(font)
        self.cpu_name_780.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_130.addWidget(self.cpu_name_780, 6, 2, 1, 1)

        self.cpu_name_781 = QLabel(self.frame_129)
        self.cpu_name_781.setObjectName(u"cpu_name_781")
        self.cpu_name_781.setFont(font1)
        self.cpu_name_781.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_130.addWidget(self.cpu_name_781, 8, 3, 1, 1)

        self.cpu_name_782 = QLabel(self.frame_129)
        self.cpu_name_782.setObjectName(u"cpu_name_782")
        self.cpu_name_782.setFont(font)
        self.cpu_name_782.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_130.addWidget(self.cpu_name_782, 8, 5, 1, 1)

        self.gpu3usage_30 = QLabel(self.frame_129)
        self.gpu3usage_30.setObjectName(u"gpu3usage_30")
        self.gpu3usage_30.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_30.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_30.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_130.addWidget(self.gpu3usage_30, 8, 1, 1, 1)

        self.cpu_name_783 = QLabel(self.frame_129)
        self.cpu_name_783.setObjectName(u"cpu_name_783")
        self.cpu_name_783.setFont(font1)
        self.cpu_name_783.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_130.addWidget(self.cpu_name_783, 8, 0, 1, 1)

        self.device1_30 = QLabel(self.frame_129)
        self.device1_30.setObjectName(u"device1_30")
        self.device1_30.setFont(font2)
        self.device1_30.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_30.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_30.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_130.addWidget(self.device1_30, 1, 0, 1, 1)

        self.clientipaddress_30 = QLabel(self.frame_129)
        self.clientipaddress_30.setObjectName(u"clientipaddress_30")
        self.clientipaddress_30.setFont(font)
        self.clientipaddress_30.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_30.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_30.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_130.addWidget(self.clientipaddress_30, 1, 1, 1, 5)

        self.gpu1usage_30 = QLabel(self.frame_129)
        self.gpu1usage_30.setObjectName(u"gpu1usage_30")
        self.gpu1usage_30.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_30.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_30.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_130.addWidget(self.gpu1usage_30, 6, 1, 1, 1)

        self.memoryusage_30 = QLabel(self.frame_129)
        self.memoryusage_30.setObjectName(u"memoryusage_30")
        self.memoryusage_30.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_30.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_30.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_130.addWidget(self.memoryusage_30, 8, 4, 1, 1)

        self.cpu_name_784 = QLabel(self.frame_129)
        self.cpu_name_784.setObjectName(u"cpu_name_784")
        self.cpu_name_784.setFont(font1)
        self.cpu_name_784.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_130.addWidget(self.cpu_name_784, 6, 3, 1, 1)


        self.gridLayout_129.addWidget(self.frame_129, 0, 0, 1, 3)

        self.elapsedtime_30 = QLabel(self.frame_128)
        self.elapsedtime_30.setObjectName(u"elapsedtime_30")
        self.elapsedtime_30.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_30.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_30.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_129.addWidget(self.elapsedtime_30, 1, 2, 1, 1)

        self.off_Button_30 = QPushButton(self.frame_128)
        self.off_Button_30.setObjectName(u"off_Button_30")
        self.off_Button_30.setEnabled(True)
        self.off_Button_30.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_129.addWidget(self.off_Button_30, 1, 1, 1, 1)


        self.horizontalLayout_16.addWidget(self.frame_128)

        self.frame_130 = QFrame(self.frame_23)
        self.frame_130.setObjectName(u"frame_130")
        self.frame_130.setMinimumSize(QSize(240, 200))
        self.frame_130.setMaximumSize(QSize(240, 200))
        self.frame_130.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_130.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_130.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_130.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_131 = QGridLayout(self.frame_130)
        self.gridLayout_131.setObjectName(u"gridLayout_131")
        self.on_Button_31 = QPushButton(self.frame_130)
        self.on_Button_31.setObjectName(u"on_Button_31")
        self.on_Button_31.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_131.addWidget(self.on_Button_31, 1, 0, 1, 1)

        self.frame_131 = QFrame(self.frame_130)
        self.frame_131.setObjectName(u"frame_131")
        self.frame_131.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_131.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_131.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_132 = QGridLayout(self.frame_131)
        self.gridLayout_132.setObjectName(u"gridLayout_132")
        self.gpu2usage_31 = QLabel(self.frame_131)
        self.gpu2usage_31.setObjectName(u"gpu2usage_31")
        self.gpu2usage_31.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_31.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_31.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_132.addWidget(self.gpu2usage_31, 6, 4, 1, 1)

        self.cpu_name_785 = QLabel(self.frame_131)
        self.cpu_name_785.setObjectName(u"cpu_name_785")
        self.cpu_name_785.setFont(font)
        self.cpu_name_785.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_132.addWidget(self.cpu_name_785, 3, 5, 1, 1)

        self.cpu_name_786 = QLabel(self.frame_131)
        self.cpu_name_786.setObjectName(u"cpu_name_786")
        self.cpu_name_786.setFont(font)
        self.cpu_name_786.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_132.addWidget(self.cpu_name_786, 6, 5, 1, 1)

        self.cpu_name_787 = QLabel(self.frame_131)
        self.cpu_name_787.setObjectName(u"cpu_name_787")
        self.cpu_name_787.setFont(font1)
        self.cpu_name_787.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_132.addWidget(self.cpu_name_787, 6, 0, 1, 1)

        self.cpuusage_31 = QLabel(self.frame_131)
        self.cpuusage_31.setObjectName(u"cpuusage_31")
        self.cpuusage_31.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_31.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_31.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_132.addWidget(self.cpuusage_31, 3, 1, 1, 1)

        self.cpu_name_788 = QLabel(self.frame_131)
        self.cpu_name_788.setObjectName(u"cpu_name_788")
        self.cpu_name_788.setFont(font)
        self.cpu_name_788.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_132.addWidget(self.cpu_name_788, 3, 2, 1, 1)

        self.gpu0usage_31 = QLabel(self.frame_131)
        self.gpu0usage_31.setObjectName(u"gpu0usage_31")
        self.gpu0usage_31.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_31.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_31.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_132.addWidget(self.gpu0usage_31, 3, 4, 1, 1)

        self.cpu_name_789 = QLabel(self.frame_131)
        self.cpu_name_789.setObjectName(u"cpu_name_789")
        self.cpu_name_789.setFont(font1)
        self.cpu_name_789.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_132.addWidget(self.cpu_name_789, 3, 3, 1, 1)

        self.cpu_name_790 = QLabel(self.frame_131)
        self.cpu_name_790.setObjectName(u"cpu_name_790")
        self.cpu_name_790.setFont(font1)
        self.cpu_name_790.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_132.addWidget(self.cpu_name_790, 3, 0, 1, 1)

        self.cpu_name_791 = QLabel(self.frame_131)
        self.cpu_name_791.setObjectName(u"cpu_name_791")
        self.cpu_name_791.setFont(font)
        self.cpu_name_791.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_132.addWidget(self.cpu_name_791, 8, 2, 1, 1)

        self.cpu_name_792 = QLabel(self.frame_131)
        self.cpu_name_792.setObjectName(u"cpu_name_792")
        self.cpu_name_792.setFont(font)
        self.cpu_name_792.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_132.addWidget(self.cpu_name_792, 6, 2, 1, 1)

        self.cpu_name_793 = QLabel(self.frame_131)
        self.cpu_name_793.setObjectName(u"cpu_name_793")
        self.cpu_name_793.setFont(font1)
        self.cpu_name_793.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_132.addWidget(self.cpu_name_793, 8, 3, 1, 1)

        self.cpu_name_794 = QLabel(self.frame_131)
        self.cpu_name_794.setObjectName(u"cpu_name_794")
        self.cpu_name_794.setFont(font)
        self.cpu_name_794.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_132.addWidget(self.cpu_name_794, 8, 5, 1, 1)

        self.gpu3usage_31 = QLabel(self.frame_131)
        self.gpu3usage_31.setObjectName(u"gpu3usage_31")
        self.gpu3usage_31.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_31.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_31.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_132.addWidget(self.gpu3usage_31, 8, 1, 1, 1)

        self.cpu_name_795 = QLabel(self.frame_131)
        self.cpu_name_795.setObjectName(u"cpu_name_795")
        self.cpu_name_795.setFont(font1)
        self.cpu_name_795.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_132.addWidget(self.cpu_name_795, 8, 0, 1, 1)

        self.device1_31 = QLabel(self.frame_131)
        self.device1_31.setObjectName(u"device1_31")
        self.device1_31.setFont(font2)
        self.device1_31.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_31.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_31.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_132.addWidget(self.device1_31, 1, 0, 1, 1)

        self.clientipaddress_31 = QLabel(self.frame_131)
        self.clientipaddress_31.setObjectName(u"clientipaddress_31")
        self.clientipaddress_31.setFont(font)
        self.clientipaddress_31.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_31.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_31.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_132.addWidget(self.clientipaddress_31, 1, 1, 1, 5)

        self.gpu1usage_31 = QLabel(self.frame_131)
        self.gpu1usage_31.setObjectName(u"gpu1usage_31")
        self.gpu1usage_31.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_31.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_31.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_132.addWidget(self.gpu1usage_31, 6, 1, 1, 1)

        self.memoryusage_31 = QLabel(self.frame_131)
        self.memoryusage_31.setObjectName(u"memoryusage_31")
        self.memoryusage_31.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_31.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_31.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_132.addWidget(self.memoryusage_31, 8, 4, 1, 1)

        self.cpu_name_796 = QLabel(self.frame_131)
        self.cpu_name_796.setObjectName(u"cpu_name_796")
        self.cpu_name_796.setFont(font1)
        self.cpu_name_796.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_132.addWidget(self.cpu_name_796, 6, 3, 1, 1)


        self.gridLayout_131.addWidget(self.frame_131, 0, 0, 1, 3)

        self.elapsedtime_31 = QLabel(self.frame_130)
        self.elapsedtime_31.setObjectName(u"elapsedtime_31")
        self.elapsedtime_31.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_31.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_31.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_131.addWidget(self.elapsedtime_31, 1, 2, 1, 1)

        self.off_Button_31 = QPushButton(self.frame_130)
        self.off_Button_31.setObjectName(u"off_Button_31")
        self.off_Button_31.setEnabled(True)
        self.off_Button_31.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_131.addWidget(self.off_Button_31, 1, 1, 1, 1)


        self.horizontalLayout_16.addWidget(self.frame_130)

        self.frame_132 = QFrame(self.frame_23)
        self.frame_132.setObjectName(u"frame_132")
        self.frame_132.setMinimumSize(QSize(240, 200))
        self.frame_132.setMaximumSize(QSize(240, 200))
        self.frame_132.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_132.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_132.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_132.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_133 = QGridLayout(self.frame_132)
        self.gridLayout_133.setObjectName(u"gridLayout_133")
        self.on_Button_32 = QPushButton(self.frame_132)
        self.on_Button_32.setObjectName(u"on_Button_32")
        self.on_Button_32.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_133.addWidget(self.on_Button_32, 1, 0, 1, 1)

        self.frame_133 = QFrame(self.frame_132)
        self.frame_133.setObjectName(u"frame_133")
        self.frame_133.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_133.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_133.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_134 = QGridLayout(self.frame_133)
        self.gridLayout_134.setObjectName(u"gridLayout_134")
        self.gpu2usage_32 = QLabel(self.frame_133)
        self.gpu2usage_32.setObjectName(u"gpu2usage_32")
        self.gpu2usage_32.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_32.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_32.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_134.addWidget(self.gpu2usage_32, 6, 4, 1, 1)

        self.cpu_name_797 = QLabel(self.frame_133)
        self.cpu_name_797.setObjectName(u"cpu_name_797")
        self.cpu_name_797.setFont(font)
        self.cpu_name_797.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_134.addWidget(self.cpu_name_797, 3, 5, 1, 1)

        self.cpu_name_798 = QLabel(self.frame_133)
        self.cpu_name_798.setObjectName(u"cpu_name_798")
        self.cpu_name_798.setFont(font)
        self.cpu_name_798.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_134.addWidget(self.cpu_name_798, 6, 5, 1, 1)

        self.cpu_name_799 = QLabel(self.frame_133)
        self.cpu_name_799.setObjectName(u"cpu_name_799")
        self.cpu_name_799.setFont(font1)
        self.cpu_name_799.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_134.addWidget(self.cpu_name_799, 6, 0, 1, 1)

        self.cpuusage_32 = QLabel(self.frame_133)
        self.cpuusage_32.setObjectName(u"cpuusage_32")
        self.cpuusage_32.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_32.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_32.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_134.addWidget(self.cpuusage_32, 3, 1, 1, 1)

        self.cpu_name_800 = QLabel(self.frame_133)
        self.cpu_name_800.setObjectName(u"cpu_name_800")
        self.cpu_name_800.setFont(font)
        self.cpu_name_800.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_134.addWidget(self.cpu_name_800, 3, 2, 1, 1)

        self.gpu0usage_32 = QLabel(self.frame_133)
        self.gpu0usage_32.setObjectName(u"gpu0usage_32")
        self.gpu0usage_32.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_32.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_32.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_134.addWidget(self.gpu0usage_32, 3, 4, 1, 1)

        self.cpu_name_801 = QLabel(self.frame_133)
        self.cpu_name_801.setObjectName(u"cpu_name_801")
        self.cpu_name_801.setFont(font1)
        self.cpu_name_801.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_134.addWidget(self.cpu_name_801, 3, 3, 1, 1)

        self.cpu_name_802 = QLabel(self.frame_133)
        self.cpu_name_802.setObjectName(u"cpu_name_802")
        self.cpu_name_802.setFont(font1)
        self.cpu_name_802.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_134.addWidget(self.cpu_name_802, 3, 0, 1, 1)

        self.cpu_name_803 = QLabel(self.frame_133)
        self.cpu_name_803.setObjectName(u"cpu_name_803")
        self.cpu_name_803.setFont(font)
        self.cpu_name_803.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_134.addWidget(self.cpu_name_803, 8, 2, 1, 1)

        self.cpu_name_804 = QLabel(self.frame_133)
        self.cpu_name_804.setObjectName(u"cpu_name_804")
        self.cpu_name_804.setFont(font)
        self.cpu_name_804.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_134.addWidget(self.cpu_name_804, 6, 2, 1, 1)

        self.cpu_name_805 = QLabel(self.frame_133)
        self.cpu_name_805.setObjectName(u"cpu_name_805")
        self.cpu_name_805.setFont(font1)
        self.cpu_name_805.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_134.addWidget(self.cpu_name_805, 8, 3, 1, 1)

        self.cpu_name_806 = QLabel(self.frame_133)
        self.cpu_name_806.setObjectName(u"cpu_name_806")
        self.cpu_name_806.setFont(font)
        self.cpu_name_806.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_134.addWidget(self.cpu_name_806, 8, 5, 1, 1)

        self.gpu3usage_32 = QLabel(self.frame_133)
        self.gpu3usage_32.setObjectName(u"gpu3usage_32")
        self.gpu3usage_32.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_32.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_32.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_134.addWidget(self.gpu3usage_32, 8, 1, 1, 1)

        self.cpu_name_807 = QLabel(self.frame_133)
        self.cpu_name_807.setObjectName(u"cpu_name_807")
        self.cpu_name_807.setFont(font1)
        self.cpu_name_807.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_134.addWidget(self.cpu_name_807, 8, 0, 1, 1)

        self.device1_32 = QLabel(self.frame_133)
        self.device1_32.setObjectName(u"device1_32")
        self.device1_32.setFont(font2)
        self.device1_32.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_32.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_32.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_134.addWidget(self.device1_32, 1, 0, 1, 1)

        self.clientipaddress_32 = QLabel(self.frame_133)
        self.clientipaddress_32.setObjectName(u"clientipaddress_32")
        self.clientipaddress_32.setFont(font)
        self.clientipaddress_32.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_32.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_32.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_134.addWidget(self.clientipaddress_32, 1, 1, 1, 5)

        self.gpu1usage_32 = QLabel(self.frame_133)
        self.gpu1usage_32.setObjectName(u"gpu1usage_32")
        self.gpu1usage_32.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_32.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_32.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_134.addWidget(self.gpu1usage_32, 6, 1, 1, 1)

        self.memoryusage_32 = QLabel(self.frame_133)
        self.memoryusage_32.setObjectName(u"memoryusage_32")
        self.memoryusage_32.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_32.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_32.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_134.addWidget(self.memoryusage_32, 8, 4, 1, 1)

        self.cpu_name_808 = QLabel(self.frame_133)
        self.cpu_name_808.setObjectName(u"cpu_name_808")
        self.cpu_name_808.setFont(font1)
        self.cpu_name_808.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_134.addWidget(self.cpu_name_808, 6, 3, 1, 1)


        self.gridLayout_133.addWidget(self.frame_133, 0, 0, 1, 3)

        self.elapsedtime_32 = QLabel(self.frame_132)
        self.elapsedtime_32.setObjectName(u"elapsedtime_32")
        self.elapsedtime_32.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_32.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_32.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_133.addWidget(self.elapsedtime_32, 1, 2, 1, 1)

        self.off_Button_32 = QPushButton(self.frame_132)
        self.off_Button_32.setObjectName(u"off_Button_32")
        self.off_Button_32.setEnabled(True)
        self.off_Button_32.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_133.addWidget(self.off_Button_32, 1, 1, 1, 1)


        self.horizontalLayout_16.addWidget(self.frame_132)


        self.verticalLayout_3.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.frame_2)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.frame_134 = QFrame(self.frame_24)
        self.frame_134.setObjectName(u"frame_134")
        self.frame_134.setMinimumSize(QSize(240, 200))
        self.frame_134.setMaximumSize(QSize(240, 200))
        self.frame_134.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_134.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_134.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_134.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_135 = QGridLayout(self.frame_134)
        self.gridLayout_135.setObjectName(u"gridLayout_135")
        self.on_Button_33 = QPushButton(self.frame_134)
        self.on_Button_33.setObjectName(u"on_Button_33")
        self.on_Button_33.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_135.addWidget(self.on_Button_33, 1, 0, 1, 1)

        self.frame_135 = QFrame(self.frame_134)
        self.frame_135.setObjectName(u"frame_135")
        self.frame_135.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_135.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_135.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_136 = QGridLayout(self.frame_135)
        self.gridLayout_136.setObjectName(u"gridLayout_136")
        self.gpu2usage_33 = QLabel(self.frame_135)
        self.gpu2usage_33.setObjectName(u"gpu2usage_33")
        self.gpu2usage_33.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_33.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_33.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_136.addWidget(self.gpu2usage_33, 6, 4, 1, 1)

        self.cpu_name_809 = QLabel(self.frame_135)
        self.cpu_name_809.setObjectName(u"cpu_name_809")
        self.cpu_name_809.setFont(font)
        self.cpu_name_809.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_136.addWidget(self.cpu_name_809, 3, 5, 1, 1)

        self.cpu_name_810 = QLabel(self.frame_135)
        self.cpu_name_810.setObjectName(u"cpu_name_810")
        self.cpu_name_810.setFont(font)
        self.cpu_name_810.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_136.addWidget(self.cpu_name_810, 6, 5, 1, 1)

        self.cpu_name_811 = QLabel(self.frame_135)
        self.cpu_name_811.setObjectName(u"cpu_name_811")
        self.cpu_name_811.setFont(font1)
        self.cpu_name_811.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_136.addWidget(self.cpu_name_811, 6, 0, 1, 1)

        self.cpuusage_33 = QLabel(self.frame_135)
        self.cpuusage_33.setObjectName(u"cpuusage_33")
        self.cpuusage_33.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_33.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_33.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_136.addWidget(self.cpuusage_33, 3, 1, 1, 1)

        self.cpu_name_812 = QLabel(self.frame_135)
        self.cpu_name_812.setObjectName(u"cpu_name_812")
        self.cpu_name_812.setFont(font)
        self.cpu_name_812.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_136.addWidget(self.cpu_name_812, 3, 2, 1, 1)

        self.gpu0usage_33 = QLabel(self.frame_135)
        self.gpu0usage_33.setObjectName(u"gpu0usage_33")
        self.gpu0usage_33.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_33.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_33.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_136.addWidget(self.gpu0usage_33, 3, 4, 1, 1)

        self.cpu_name_813 = QLabel(self.frame_135)
        self.cpu_name_813.setObjectName(u"cpu_name_813")
        self.cpu_name_813.setFont(font1)
        self.cpu_name_813.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_136.addWidget(self.cpu_name_813, 3, 3, 1, 1)

        self.cpu_name_814 = QLabel(self.frame_135)
        self.cpu_name_814.setObjectName(u"cpu_name_814")
        self.cpu_name_814.setFont(font1)
        self.cpu_name_814.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_136.addWidget(self.cpu_name_814, 3, 0, 1, 1)

        self.cpu_name_815 = QLabel(self.frame_135)
        self.cpu_name_815.setObjectName(u"cpu_name_815")
        self.cpu_name_815.setFont(font)
        self.cpu_name_815.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_136.addWidget(self.cpu_name_815, 8, 2, 1, 1)

        self.cpu_name_816 = QLabel(self.frame_135)
        self.cpu_name_816.setObjectName(u"cpu_name_816")
        self.cpu_name_816.setFont(font)
        self.cpu_name_816.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_136.addWidget(self.cpu_name_816, 6, 2, 1, 1)

        self.cpu_name_817 = QLabel(self.frame_135)
        self.cpu_name_817.setObjectName(u"cpu_name_817")
        self.cpu_name_817.setFont(font1)
        self.cpu_name_817.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_136.addWidget(self.cpu_name_817, 8, 3, 1, 1)

        self.cpu_name_818 = QLabel(self.frame_135)
        self.cpu_name_818.setObjectName(u"cpu_name_818")
        self.cpu_name_818.setFont(font)
        self.cpu_name_818.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_136.addWidget(self.cpu_name_818, 8, 5, 1, 1)

        self.gpu3usage_33 = QLabel(self.frame_135)
        self.gpu3usage_33.setObjectName(u"gpu3usage_33")
        self.gpu3usage_33.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_33.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_33.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_136.addWidget(self.gpu3usage_33, 8, 1, 1, 1)

        self.cpu_name_819 = QLabel(self.frame_135)
        self.cpu_name_819.setObjectName(u"cpu_name_819")
        self.cpu_name_819.setFont(font1)
        self.cpu_name_819.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_136.addWidget(self.cpu_name_819, 8, 0, 1, 1)

        self.device1_33 = QLabel(self.frame_135)
        self.device1_33.setObjectName(u"device1_33")
        self.device1_33.setFont(font2)
        self.device1_33.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_33.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_33.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_136.addWidget(self.device1_33, 1, 0, 1, 1)

        self.clientipaddress_33 = QLabel(self.frame_135)
        self.clientipaddress_33.setObjectName(u"clientipaddress_33")
        self.clientipaddress_33.setFont(font)
        self.clientipaddress_33.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_33.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_33.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_136.addWidget(self.clientipaddress_33, 1, 1, 1, 5)

        self.gpu1usage_33 = QLabel(self.frame_135)
        self.gpu1usage_33.setObjectName(u"gpu1usage_33")
        self.gpu1usage_33.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_33.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_33.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_136.addWidget(self.gpu1usage_33, 6, 1, 1, 1)

        self.memoryusage_33 = QLabel(self.frame_135)
        self.memoryusage_33.setObjectName(u"memoryusage_33")
        self.memoryusage_33.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_33.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_33.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_136.addWidget(self.memoryusage_33, 8, 4, 1, 1)

        self.cpu_name_820 = QLabel(self.frame_135)
        self.cpu_name_820.setObjectName(u"cpu_name_820")
        self.cpu_name_820.setFont(font1)
        self.cpu_name_820.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_136.addWidget(self.cpu_name_820, 6, 3, 1, 1)


        self.gridLayout_135.addWidget(self.frame_135, 0, 0, 1, 3)

        self.elapsedtime_33 = QLabel(self.frame_134)
        self.elapsedtime_33.setObjectName(u"elapsedtime_33")
        self.elapsedtime_33.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_33.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_33.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_135.addWidget(self.elapsedtime_33, 1, 2, 1, 1)

        self.off_Button_33 = QPushButton(self.frame_134)
        self.off_Button_33.setObjectName(u"off_Button_33")
        self.off_Button_33.setEnabled(True)
        self.off_Button_33.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_135.addWidget(self.off_Button_33, 1, 1, 1, 1)


        self.horizontalLayout_17.addWidget(self.frame_134)

        self.frame_136 = QFrame(self.frame_24)
        self.frame_136.setObjectName(u"frame_136")
        self.frame_136.setMinimumSize(QSize(240, 200))
        self.frame_136.setMaximumSize(QSize(240, 200))
        self.frame_136.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_136.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_136.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_136.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_137 = QGridLayout(self.frame_136)
        self.gridLayout_137.setObjectName(u"gridLayout_137")
        self.on_Button_34 = QPushButton(self.frame_136)
        self.on_Button_34.setObjectName(u"on_Button_34")
        self.on_Button_34.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_137.addWidget(self.on_Button_34, 1, 0, 1, 1)

        self.frame_137 = QFrame(self.frame_136)
        self.frame_137.setObjectName(u"frame_137")
        self.frame_137.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_137.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_137.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_138 = QGridLayout(self.frame_137)
        self.gridLayout_138.setObjectName(u"gridLayout_138")
        self.gpu2usage_34 = QLabel(self.frame_137)
        self.gpu2usage_34.setObjectName(u"gpu2usage_34")
        self.gpu2usage_34.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_34.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_34.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_138.addWidget(self.gpu2usage_34, 6, 4, 1, 1)

        self.cpu_name_821 = QLabel(self.frame_137)
        self.cpu_name_821.setObjectName(u"cpu_name_821")
        self.cpu_name_821.setFont(font)
        self.cpu_name_821.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_138.addWidget(self.cpu_name_821, 3, 5, 1, 1)

        self.cpu_name_822 = QLabel(self.frame_137)
        self.cpu_name_822.setObjectName(u"cpu_name_822")
        self.cpu_name_822.setFont(font)
        self.cpu_name_822.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_138.addWidget(self.cpu_name_822, 6, 5, 1, 1)

        self.cpu_name_823 = QLabel(self.frame_137)
        self.cpu_name_823.setObjectName(u"cpu_name_823")
        self.cpu_name_823.setFont(font1)
        self.cpu_name_823.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_138.addWidget(self.cpu_name_823, 6, 0, 1, 1)

        self.cpuusage_34 = QLabel(self.frame_137)
        self.cpuusage_34.setObjectName(u"cpuusage_34")
        self.cpuusage_34.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_34.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_34.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_138.addWidget(self.cpuusage_34, 3, 1, 1, 1)

        self.cpu_name_824 = QLabel(self.frame_137)
        self.cpu_name_824.setObjectName(u"cpu_name_824")
        self.cpu_name_824.setFont(font)
        self.cpu_name_824.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_138.addWidget(self.cpu_name_824, 3, 2, 1, 1)

        self.gpu0usage_34 = QLabel(self.frame_137)
        self.gpu0usage_34.setObjectName(u"gpu0usage_34")
        self.gpu0usage_34.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_34.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_34.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_138.addWidget(self.gpu0usage_34, 3, 4, 1, 1)

        self.cpu_name_825 = QLabel(self.frame_137)
        self.cpu_name_825.setObjectName(u"cpu_name_825")
        self.cpu_name_825.setFont(font1)
        self.cpu_name_825.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_138.addWidget(self.cpu_name_825, 3, 3, 1, 1)

        self.cpu_name_826 = QLabel(self.frame_137)
        self.cpu_name_826.setObjectName(u"cpu_name_826")
        self.cpu_name_826.setFont(font1)
        self.cpu_name_826.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_138.addWidget(self.cpu_name_826, 3, 0, 1, 1)

        self.cpu_name_827 = QLabel(self.frame_137)
        self.cpu_name_827.setObjectName(u"cpu_name_827")
        self.cpu_name_827.setFont(font)
        self.cpu_name_827.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_138.addWidget(self.cpu_name_827, 8, 2, 1, 1)

        self.cpu_name_828 = QLabel(self.frame_137)
        self.cpu_name_828.setObjectName(u"cpu_name_828")
        self.cpu_name_828.setFont(font)
        self.cpu_name_828.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_138.addWidget(self.cpu_name_828, 6, 2, 1, 1)

        self.cpu_name_829 = QLabel(self.frame_137)
        self.cpu_name_829.setObjectName(u"cpu_name_829")
        self.cpu_name_829.setFont(font1)
        self.cpu_name_829.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_138.addWidget(self.cpu_name_829, 8, 3, 1, 1)

        self.cpu_name_830 = QLabel(self.frame_137)
        self.cpu_name_830.setObjectName(u"cpu_name_830")
        self.cpu_name_830.setFont(font)
        self.cpu_name_830.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_138.addWidget(self.cpu_name_830, 8, 5, 1, 1)

        self.gpu3usage_34 = QLabel(self.frame_137)
        self.gpu3usage_34.setObjectName(u"gpu3usage_34")
        self.gpu3usage_34.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_34.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_34.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_138.addWidget(self.gpu3usage_34, 8, 1, 1, 1)

        self.cpu_name_831 = QLabel(self.frame_137)
        self.cpu_name_831.setObjectName(u"cpu_name_831")
        self.cpu_name_831.setFont(font1)
        self.cpu_name_831.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_138.addWidget(self.cpu_name_831, 8, 0, 1, 1)

        self.device1_34 = QLabel(self.frame_137)
        self.device1_34.setObjectName(u"device1_34")
        self.device1_34.setFont(font2)
        self.device1_34.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_34.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_34.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_138.addWidget(self.device1_34, 1, 0, 1, 1)

        self.clientipaddress_34 = QLabel(self.frame_137)
        self.clientipaddress_34.setObjectName(u"clientipaddress_34")
        self.clientipaddress_34.setFont(font)
        self.clientipaddress_34.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_34.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_34.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_138.addWidget(self.clientipaddress_34, 1, 1, 1, 5)

        self.gpu1usage_34 = QLabel(self.frame_137)
        self.gpu1usage_34.setObjectName(u"gpu1usage_34")
        self.gpu1usage_34.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_34.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_34.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_138.addWidget(self.gpu1usage_34, 6, 1, 1, 1)

        self.memoryusage_34 = QLabel(self.frame_137)
        self.memoryusage_34.setObjectName(u"memoryusage_34")
        self.memoryusage_34.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_34.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_34.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_138.addWidget(self.memoryusage_34, 8, 4, 1, 1)

        self.cpu_name_832 = QLabel(self.frame_137)
        self.cpu_name_832.setObjectName(u"cpu_name_832")
        self.cpu_name_832.setFont(font1)
        self.cpu_name_832.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_138.addWidget(self.cpu_name_832, 6, 3, 1, 1)


        self.gridLayout_137.addWidget(self.frame_137, 0, 0, 1, 3)

        self.elapsedtime_34 = QLabel(self.frame_136)
        self.elapsedtime_34.setObjectName(u"elapsedtime_34")
        self.elapsedtime_34.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_34.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_34.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_137.addWidget(self.elapsedtime_34, 1, 2, 1, 1)

        self.off_Button_34 = QPushButton(self.frame_136)
        self.off_Button_34.setObjectName(u"off_Button_34")
        self.off_Button_34.setEnabled(True)
        self.off_Button_34.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_137.addWidget(self.off_Button_34, 1, 1, 1, 1)


        self.horizontalLayout_17.addWidget(self.frame_136)

        self.frame_138 = QFrame(self.frame_24)
        self.frame_138.setObjectName(u"frame_138")
        self.frame_138.setMinimumSize(QSize(240, 200))
        self.frame_138.setMaximumSize(QSize(240, 200))
        self.frame_138.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_138.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_138.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_138.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_139 = QGridLayout(self.frame_138)
        self.gridLayout_139.setObjectName(u"gridLayout_139")
        self.on_Button_35 = QPushButton(self.frame_138)
        self.on_Button_35.setObjectName(u"on_Button_35")
        self.on_Button_35.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_139.addWidget(self.on_Button_35, 1, 0, 1, 1)

        self.frame_139 = QFrame(self.frame_138)
        self.frame_139.setObjectName(u"frame_139")
        self.frame_139.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_139.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_139.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_140 = QGridLayout(self.frame_139)
        self.gridLayout_140.setObjectName(u"gridLayout_140")
        self.gpu2usage_35 = QLabel(self.frame_139)
        self.gpu2usage_35.setObjectName(u"gpu2usage_35")
        self.gpu2usage_35.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_35.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_35.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_140.addWidget(self.gpu2usage_35, 6, 4, 1, 1)

        self.cpu_name_833 = QLabel(self.frame_139)
        self.cpu_name_833.setObjectName(u"cpu_name_833")
        self.cpu_name_833.setFont(font)
        self.cpu_name_833.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_140.addWidget(self.cpu_name_833, 3, 5, 1, 1)

        self.cpu_name_834 = QLabel(self.frame_139)
        self.cpu_name_834.setObjectName(u"cpu_name_834")
        self.cpu_name_834.setFont(font)
        self.cpu_name_834.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_140.addWidget(self.cpu_name_834, 6, 5, 1, 1)

        self.cpu_name_835 = QLabel(self.frame_139)
        self.cpu_name_835.setObjectName(u"cpu_name_835")
        self.cpu_name_835.setFont(font1)
        self.cpu_name_835.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_140.addWidget(self.cpu_name_835, 6, 0, 1, 1)

        self.cpuusage_35 = QLabel(self.frame_139)
        self.cpuusage_35.setObjectName(u"cpuusage_35")
        self.cpuusage_35.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_35.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_35.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_140.addWidget(self.cpuusage_35, 3, 1, 1, 1)

        self.cpu_name_836 = QLabel(self.frame_139)
        self.cpu_name_836.setObjectName(u"cpu_name_836")
        self.cpu_name_836.setFont(font)
        self.cpu_name_836.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_140.addWidget(self.cpu_name_836, 3, 2, 1, 1)

        self.gpu0usage_35 = QLabel(self.frame_139)
        self.gpu0usage_35.setObjectName(u"gpu0usage_35")
        self.gpu0usage_35.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_35.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_35.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_140.addWidget(self.gpu0usage_35, 3, 4, 1, 1)

        self.cpu_name_837 = QLabel(self.frame_139)
        self.cpu_name_837.setObjectName(u"cpu_name_837")
        self.cpu_name_837.setFont(font1)
        self.cpu_name_837.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_140.addWidget(self.cpu_name_837, 3, 3, 1, 1)

        self.cpu_name_838 = QLabel(self.frame_139)
        self.cpu_name_838.setObjectName(u"cpu_name_838")
        self.cpu_name_838.setFont(font1)
        self.cpu_name_838.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_140.addWidget(self.cpu_name_838, 3, 0, 1, 1)

        self.cpu_name_839 = QLabel(self.frame_139)
        self.cpu_name_839.setObjectName(u"cpu_name_839")
        self.cpu_name_839.setFont(font)
        self.cpu_name_839.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_140.addWidget(self.cpu_name_839, 8, 2, 1, 1)

        self.cpu_name_840 = QLabel(self.frame_139)
        self.cpu_name_840.setObjectName(u"cpu_name_840")
        self.cpu_name_840.setFont(font)
        self.cpu_name_840.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_140.addWidget(self.cpu_name_840, 6, 2, 1, 1)

        self.cpu_name_841 = QLabel(self.frame_139)
        self.cpu_name_841.setObjectName(u"cpu_name_841")
        self.cpu_name_841.setFont(font1)
        self.cpu_name_841.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_140.addWidget(self.cpu_name_841, 8, 3, 1, 1)

        self.cpu_name_842 = QLabel(self.frame_139)
        self.cpu_name_842.setObjectName(u"cpu_name_842")
        self.cpu_name_842.setFont(font)
        self.cpu_name_842.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_140.addWidget(self.cpu_name_842, 8, 5, 1, 1)

        self.gpu3usage_35 = QLabel(self.frame_139)
        self.gpu3usage_35.setObjectName(u"gpu3usage_35")
        self.gpu3usage_35.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_35.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_35.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_140.addWidget(self.gpu3usage_35, 8, 1, 1, 1)

        self.cpu_name_843 = QLabel(self.frame_139)
        self.cpu_name_843.setObjectName(u"cpu_name_843")
        self.cpu_name_843.setFont(font1)
        self.cpu_name_843.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_140.addWidget(self.cpu_name_843, 8, 0, 1, 1)

        self.device1_35 = QLabel(self.frame_139)
        self.device1_35.setObjectName(u"device1_35")
        self.device1_35.setFont(font2)
        self.device1_35.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_35.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_35.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_140.addWidget(self.device1_35, 1, 0, 1, 1)

        self.clientipaddress_35 = QLabel(self.frame_139)
        self.clientipaddress_35.setObjectName(u"clientipaddress_35")
        self.clientipaddress_35.setFont(font)
        self.clientipaddress_35.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_35.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_35.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_140.addWidget(self.clientipaddress_35, 1, 1, 1, 5)

        self.gpu1usage_35 = QLabel(self.frame_139)
        self.gpu1usage_35.setObjectName(u"gpu1usage_35")
        self.gpu1usage_35.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_35.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_35.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_140.addWidget(self.gpu1usage_35, 6, 1, 1, 1)

        self.memoryusage_35 = QLabel(self.frame_139)
        self.memoryusage_35.setObjectName(u"memoryusage_35")
        self.memoryusage_35.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_35.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_35.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_140.addWidget(self.memoryusage_35, 8, 4, 1, 1)

        self.cpu_name_844 = QLabel(self.frame_139)
        self.cpu_name_844.setObjectName(u"cpu_name_844")
        self.cpu_name_844.setFont(font1)
        self.cpu_name_844.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_140.addWidget(self.cpu_name_844, 6, 3, 1, 1)


        self.gridLayout_139.addWidget(self.frame_139, 0, 0, 1, 3)

        self.elapsedtime_35 = QLabel(self.frame_138)
        self.elapsedtime_35.setObjectName(u"elapsedtime_35")
        self.elapsedtime_35.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_35.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_35.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_139.addWidget(self.elapsedtime_35, 1, 2, 1, 1)

        self.off_Button_35 = QPushButton(self.frame_138)
        self.off_Button_35.setObjectName(u"off_Button_35")
        self.off_Button_35.setEnabled(True)
        self.off_Button_35.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_139.addWidget(self.off_Button_35, 1, 1, 1, 1)


        self.horizontalLayout_17.addWidget(self.frame_138)

        self.frame_140 = QFrame(self.frame_24)
        self.frame_140.setObjectName(u"frame_140")
        self.frame_140.setMinimumSize(QSize(240, 200))
        self.frame_140.setMaximumSize(QSize(240, 200))
        self.frame_140.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_140.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_140.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_140.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_141 = QGridLayout(self.frame_140)
        self.gridLayout_141.setObjectName(u"gridLayout_141")
        self.on_Button_36 = QPushButton(self.frame_140)
        self.on_Button_36.setObjectName(u"on_Button_36")
        self.on_Button_36.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_141.addWidget(self.on_Button_36, 1, 0, 1, 1)

        self.frame_141 = QFrame(self.frame_140)
        self.frame_141.setObjectName(u"frame_141")
        self.frame_141.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_141.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_141.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_142 = QGridLayout(self.frame_141)
        self.gridLayout_142.setObjectName(u"gridLayout_142")
        self.gpu2usage_36 = QLabel(self.frame_141)
        self.gpu2usage_36.setObjectName(u"gpu2usage_36")
        self.gpu2usage_36.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_36.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_36.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_142.addWidget(self.gpu2usage_36, 6, 4, 1, 1)

        self.cpu_name_845 = QLabel(self.frame_141)
        self.cpu_name_845.setObjectName(u"cpu_name_845")
        self.cpu_name_845.setFont(font)
        self.cpu_name_845.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_142.addWidget(self.cpu_name_845, 3, 5, 1, 1)

        self.cpu_name_846 = QLabel(self.frame_141)
        self.cpu_name_846.setObjectName(u"cpu_name_846")
        self.cpu_name_846.setFont(font)
        self.cpu_name_846.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_142.addWidget(self.cpu_name_846, 6, 5, 1, 1)

        self.cpu_name_847 = QLabel(self.frame_141)
        self.cpu_name_847.setObjectName(u"cpu_name_847")
        self.cpu_name_847.setFont(font1)
        self.cpu_name_847.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_142.addWidget(self.cpu_name_847, 6, 0, 1, 1)

        self.cpuusage_36 = QLabel(self.frame_141)
        self.cpuusage_36.setObjectName(u"cpuusage_36")
        self.cpuusage_36.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_36.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_36.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_142.addWidget(self.cpuusage_36, 3, 1, 1, 1)

        self.cpu_name_848 = QLabel(self.frame_141)
        self.cpu_name_848.setObjectName(u"cpu_name_848")
        self.cpu_name_848.setFont(font)
        self.cpu_name_848.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_142.addWidget(self.cpu_name_848, 3, 2, 1, 1)

        self.gpu0usage_36 = QLabel(self.frame_141)
        self.gpu0usage_36.setObjectName(u"gpu0usage_36")
        self.gpu0usage_36.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_36.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_36.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_142.addWidget(self.gpu0usage_36, 3, 4, 1, 1)

        self.cpu_name_849 = QLabel(self.frame_141)
        self.cpu_name_849.setObjectName(u"cpu_name_849")
        self.cpu_name_849.setFont(font1)
        self.cpu_name_849.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_142.addWidget(self.cpu_name_849, 3, 3, 1, 1)

        self.cpu_name_850 = QLabel(self.frame_141)
        self.cpu_name_850.setObjectName(u"cpu_name_850")
        self.cpu_name_850.setFont(font1)
        self.cpu_name_850.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_142.addWidget(self.cpu_name_850, 3, 0, 1, 1)

        self.cpu_name_851 = QLabel(self.frame_141)
        self.cpu_name_851.setObjectName(u"cpu_name_851")
        self.cpu_name_851.setFont(font)
        self.cpu_name_851.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_142.addWidget(self.cpu_name_851, 8, 2, 1, 1)

        self.cpu_name_852 = QLabel(self.frame_141)
        self.cpu_name_852.setObjectName(u"cpu_name_852")
        self.cpu_name_852.setFont(font)
        self.cpu_name_852.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_142.addWidget(self.cpu_name_852, 6, 2, 1, 1)

        self.cpu_name_853 = QLabel(self.frame_141)
        self.cpu_name_853.setObjectName(u"cpu_name_853")
        self.cpu_name_853.setFont(font1)
        self.cpu_name_853.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_142.addWidget(self.cpu_name_853, 8, 3, 1, 1)

        self.cpu_name_854 = QLabel(self.frame_141)
        self.cpu_name_854.setObjectName(u"cpu_name_854")
        self.cpu_name_854.setFont(font)
        self.cpu_name_854.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_142.addWidget(self.cpu_name_854, 8, 5, 1, 1)

        self.gpu3usage_36 = QLabel(self.frame_141)
        self.gpu3usage_36.setObjectName(u"gpu3usage_36")
        self.gpu3usage_36.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_36.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_36.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_142.addWidget(self.gpu3usage_36, 8, 1, 1, 1)

        self.cpu_name_855 = QLabel(self.frame_141)
        self.cpu_name_855.setObjectName(u"cpu_name_855")
        self.cpu_name_855.setFont(font1)
        self.cpu_name_855.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_142.addWidget(self.cpu_name_855, 8, 0, 1, 1)

        self.device1_36 = QLabel(self.frame_141)
        self.device1_36.setObjectName(u"device1_36")
        self.device1_36.setFont(font2)
        self.device1_36.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_36.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_36.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_142.addWidget(self.device1_36, 1, 0, 1, 1)

        self.clientipaddress_36 = QLabel(self.frame_141)
        self.clientipaddress_36.setObjectName(u"clientipaddress_36")
        self.clientipaddress_36.setFont(font)
        self.clientipaddress_36.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_36.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_36.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_142.addWidget(self.clientipaddress_36, 1, 1, 1, 5)

        self.gpu1usage_36 = QLabel(self.frame_141)
        self.gpu1usage_36.setObjectName(u"gpu1usage_36")
        self.gpu1usage_36.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_36.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_36.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_142.addWidget(self.gpu1usage_36, 6, 1, 1, 1)

        self.memoryusage_36 = QLabel(self.frame_141)
        self.memoryusage_36.setObjectName(u"memoryusage_36")
        self.memoryusage_36.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_36.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_36.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_142.addWidget(self.memoryusage_36, 8, 4, 1, 1)

        self.cpu_name_856 = QLabel(self.frame_141)
        self.cpu_name_856.setObjectName(u"cpu_name_856")
        self.cpu_name_856.setFont(font1)
        self.cpu_name_856.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_142.addWidget(self.cpu_name_856, 6, 3, 1, 1)


        self.gridLayout_141.addWidget(self.frame_141, 0, 0, 1, 3)

        self.elapsedtime_36 = QLabel(self.frame_140)
        self.elapsedtime_36.setObjectName(u"elapsedtime_36")
        self.elapsedtime_36.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_36.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_36.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_141.addWidget(self.elapsedtime_36, 1, 2, 1, 1)

        self.off_Button_36 = QPushButton(self.frame_140)
        self.off_Button_36.setObjectName(u"off_Button_36")
        self.off_Button_36.setEnabled(True)
        self.off_Button_36.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_141.addWidget(self.off_Button_36, 1, 1, 1, 1)


        self.horizontalLayout_17.addWidget(self.frame_140)


        self.verticalLayout_3.addWidget(self.frame_24)

        self.frame_25 = QFrame(self.frame_2)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.frame_150 = QFrame(self.frame_25)
        self.frame_150.setObjectName(u"frame_150")
        self.frame_150.setMinimumSize(QSize(240, 200))
        self.frame_150.setMaximumSize(QSize(240, 200))
        self.frame_150.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_150.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_150.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_150.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_151 = QGridLayout(self.frame_150)
        self.gridLayout_151.setObjectName(u"gridLayout_151")
        self.on_Button_41 = QPushButton(self.frame_150)
        self.on_Button_41.setObjectName(u"on_Button_41")
        self.on_Button_41.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_151.addWidget(self.on_Button_41, 1, 0, 1, 1)

        self.frame_151 = QFrame(self.frame_150)
        self.frame_151.setObjectName(u"frame_151")
        self.frame_151.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_151.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_151.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_152 = QGridLayout(self.frame_151)
        self.gridLayout_152.setObjectName(u"gridLayout_152")
        self.gpu2usage_41 = QLabel(self.frame_151)
        self.gpu2usage_41.setObjectName(u"gpu2usage_41")
        self.gpu2usage_41.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_41.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_41.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_152.addWidget(self.gpu2usage_41, 6, 4, 1, 1)

        self.cpu_name_905 = QLabel(self.frame_151)
        self.cpu_name_905.setObjectName(u"cpu_name_905")
        self.cpu_name_905.setFont(font)
        self.cpu_name_905.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_152.addWidget(self.cpu_name_905, 3, 5, 1, 1)

        self.cpu_name_906 = QLabel(self.frame_151)
        self.cpu_name_906.setObjectName(u"cpu_name_906")
        self.cpu_name_906.setFont(font)
        self.cpu_name_906.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_152.addWidget(self.cpu_name_906, 6, 5, 1, 1)

        self.cpu_name_907 = QLabel(self.frame_151)
        self.cpu_name_907.setObjectName(u"cpu_name_907")
        self.cpu_name_907.setFont(font1)
        self.cpu_name_907.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_152.addWidget(self.cpu_name_907, 6, 0, 1, 1)

        self.cpuusage_41 = QLabel(self.frame_151)
        self.cpuusage_41.setObjectName(u"cpuusage_41")
        self.cpuusage_41.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_41.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_41.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_152.addWidget(self.cpuusage_41, 3, 1, 1, 1)

        self.cpu_name_908 = QLabel(self.frame_151)
        self.cpu_name_908.setObjectName(u"cpu_name_908")
        self.cpu_name_908.setFont(font)
        self.cpu_name_908.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_152.addWidget(self.cpu_name_908, 3, 2, 1, 1)

        self.gpu0usage_41 = QLabel(self.frame_151)
        self.gpu0usage_41.setObjectName(u"gpu0usage_41")
        self.gpu0usage_41.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_41.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_41.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_152.addWidget(self.gpu0usage_41, 3, 4, 1, 1)

        self.cpu_name_909 = QLabel(self.frame_151)
        self.cpu_name_909.setObjectName(u"cpu_name_909")
        self.cpu_name_909.setFont(font1)
        self.cpu_name_909.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_152.addWidget(self.cpu_name_909, 3, 3, 1, 1)

        self.cpu_name_910 = QLabel(self.frame_151)
        self.cpu_name_910.setObjectName(u"cpu_name_910")
        self.cpu_name_910.setFont(font1)
        self.cpu_name_910.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_152.addWidget(self.cpu_name_910, 3, 0, 1, 1)

        self.cpu_name_911 = QLabel(self.frame_151)
        self.cpu_name_911.setObjectName(u"cpu_name_911")
        self.cpu_name_911.setFont(font)
        self.cpu_name_911.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_152.addWidget(self.cpu_name_911, 8, 2, 1, 1)

        self.cpu_name_912 = QLabel(self.frame_151)
        self.cpu_name_912.setObjectName(u"cpu_name_912")
        self.cpu_name_912.setFont(font)
        self.cpu_name_912.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_152.addWidget(self.cpu_name_912, 6, 2, 1, 1)

        self.cpu_name_913 = QLabel(self.frame_151)
        self.cpu_name_913.setObjectName(u"cpu_name_913")
        self.cpu_name_913.setFont(font1)
        self.cpu_name_913.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_152.addWidget(self.cpu_name_913, 8, 3, 1, 1)

        self.cpu_name_914 = QLabel(self.frame_151)
        self.cpu_name_914.setObjectName(u"cpu_name_914")
        self.cpu_name_914.setFont(font)
        self.cpu_name_914.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_152.addWidget(self.cpu_name_914, 8, 5, 1, 1)

        self.gpu3usage_41 = QLabel(self.frame_151)
        self.gpu3usage_41.setObjectName(u"gpu3usage_41")
        self.gpu3usage_41.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_41.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_41.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_152.addWidget(self.gpu3usage_41, 8, 1, 1, 1)

        self.cpu_name_915 = QLabel(self.frame_151)
        self.cpu_name_915.setObjectName(u"cpu_name_915")
        self.cpu_name_915.setFont(font1)
        self.cpu_name_915.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_152.addWidget(self.cpu_name_915, 8, 0, 1, 1)

        self.device1_41 = QLabel(self.frame_151)
        self.device1_41.setObjectName(u"device1_41")
        self.device1_41.setFont(font2)
        self.device1_41.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_41.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_41.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_152.addWidget(self.device1_41, 1, 0, 1, 1)

        self.clientipaddress_41 = QLabel(self.frame_151)
        self.clientipaddress_41.setObjectName(u"clientipaddress_41")
        self.clientipaddress_41.setFont(font)
        self.clientipaddress_41.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_41.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_41.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_152.addWidget(self.clientipaddress_41, 1, 1, 1, 5)

        self.gpu1usage_41 = QLabel(self.frame_151)
        self.gpu1usage_41.setObjectName(u"gpu1usage_41")
        self.gpu1usage_41.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_41.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_41.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_152.addWidget(self.gpu1usage_41, 6, 1, 1, 1)

        self.memoryusage_41 = QLabel(self.frame_151)
        self.memoryusage_41.setObjectName(u"memoryusage_41")
        self.memoryusage_41.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_41.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_41.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_152.addWidget(self.memoryusage_41, 8, 4, 1, 1)

        self.cpu_name_916 = QLabel(self.frame_151)
        self.cpu_name_916.setObjectName(u"cpu_name_916")
        self.cpu_name_916.setFont(font1)
        self.cpu_name_916.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_152.addWidget(self.cpu_name_916, 6, 3, 1, 1)


        self.gridLayout_151.addWidget(self.frame_151, 0, 0, 1, 3)

        self.elapsedtime_41 = QLabel(self.frame_150)
        self.elapsedtime_41.setObjectName(u"elapsedtime_41")
        self.elapsedtime_41.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_41.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_41.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_151.addWidget(self.elapsedtime_41, 1, 2, 1, 1)

        self.off_Button_41 = QPushButton(self.frame_150)
        self.off_Button_41.setObjectName(u"off_Button_41")
        self.off_Button_41.setEnabled(True)
        self.off_Button_41.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_151.addWidget(self.off_Button_41, 1, 1, 1, 1)


        self.horizontalLayout_19.addWidget(self.frame_150)

        self.frame_152 = QFrame(self.frame_25)
        self.frame_152.setObjectName(u"frame_152")
        self.frame_152.setMinimumSize(QSize(240, 200))
        self.frame_152.setMaximumSize(QSize(240, 200))
        self.frame_152.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_152.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_152.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_152.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_153 = QGridLayout(self.frame_152)
        self.gridLayout_153.setObjectName(u"gridLayout_153")
        self.on_Button_42 = QPushButton(self.frame_152)
        self.on_Button_42.setObjectName(u"on_Button_42")
        self.on_Button_42.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_153.addWidget(self.on_Button_42, 1, 0, 1, 1)

        self.frame_153 = QFrame(self.frame_152)
        self.frame_153.setObjectName(u"frame_153")
        self.frame_153.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_153.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_153.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_154 = QGridLayout(self.frame_153)
        self.gridLayout_154.setObjectName(u"gridLayout_154")
        self.gpu2usage_42 = QLabel(self.frame_153)
        self.gpu2usage_42.setObjectName(u"gpu2usage_42")
        self.gpu2usage_42.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_42.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_42.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_154.addWidget(self.gpu2usage_42, 6, 4, 1, 1)

        self.cpu_name_917 = QLabel(self.frame_153)
        self.cpu_name_917.setObjectName(u"cpu_name_917")
        self.cpu_name_917.setFont(font)
        self.cpu_name_917.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_154.addWidget(self.cpu_name_917, 3, 5, 1, 1)

        self.cpu_name_918 = QLabel(self.frame_153)
        self.cpu_name_918.setObjectName(u"cpu_name_918")
        self.cpu_name_918.setFont(font)
        self.cpu_name_918.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_154.addWidget(self.cpu_name_918, 6, 5, 1, 1)

        self.cpu_name_919 = QLabel(self.frame_153)
        self.cpu_name_919.setObjectName(u"cpu_name_919")
        self.cpu_name_919.setFont(font1)
        self.cpu_name_919.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_154.addWidget(self.cpu_name_919, 6, 0, 1, 1)

        self.cpuusage_42 = QLabel(self.frame_153)
        self.cpuusage_42.setObjectName(u"cpuusage_42")
        self.cpuusage_42.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_42.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_42.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_154.addWidget(self.cpuusage_42, 3, 1, 1, 1)

        self.cpu_name_920 = QLabel(self.frame_153)
        self.cpu_name_920.setObjectName(u"cpu_name_920")
        self.cpu_name_920.setFont(font)
        self.cpu_name_920.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_154.addWidget(self.cpu_name_920, 3, 2, 1, 1)

        self.gpu0usage_42 = QLabel(self.frame_153)
        self.gpu0usage_42.setObjectName(u"gpu0usage_42")
        self.gpu0usage_42.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_42.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_42.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_154.addWidget(self.gpu0usage_42, 3, 4, 1, 1)

        self.cpu_name_921 = QLabel(self.frame_153)
        self.cpu_name_921.setObjectName(u"cpu_name_921")
        self.cpu_name_921.setFont(font1)
        self.cpu_name_921.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_154.addWidget(self.cpu_name_921, 3, 3, 1, 1)

        self.cpu_name_922 = QLabel(self.frame_153)
        self.cpu_name_922.setObjectName(u"cpu_name_922")
        self.cpu_name_922.setFont(font1)
        self.cpu_name_922.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_154.addWidget(self.cpu_name_922, 3, 0, 1, 1)

        self.cpu_name_923 = QLabel(self.frame_153)
        self.cpu_name_923.setObjectName(u"cpu_name_923")
        self.cpu_name_923.setFont(font)
        self.cpu_name_923.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_154.addWidget(self.cpu_name_923, 8, 2, 1, 1)

        self.cpu_name_924 = QLabel(self.frame_153)
        self.cpu_name_924.setObjectName(u"cpu_name_924")
        self.cpu_name_924.setFont(font)
        self.cpu_name_924.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_154.addWidget(self.cpu_name_924, 6, 2, 1, 1)

        self.cpu_name_925 = QLabel(self.frame_153)
        self.cpu_name_925.setObjectName(u"cpu_name_925")
        self.cpu_name_925.setFont(font1)
        self.cpu_name_925.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_154.addWidget(self.cpu_name_925, 8, 3, 1, 1)

        self.cpu_name_926 = QLabel(self.frame_153)
        self.cpu_name_926.setObjectName(u"cpu_name_926")
        self.cpu_name_926.setFont(font)
        self.cpu_name_926.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_154.addWidget(self.cpu_name_926, 8, 5, 1, 1)

        self.gpu3usage_42 = QLabel(self.frame_153)
        self.gpu3usage_42.setObjectName(u"gpu3usage_42")
        self.gpu3usage_42.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_42.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_42.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_154.addWidget(self.gpu3usage_42, 8, 1, 1, 1)

        self.cpu_name_927 = QLabel(self.frame_153)
        self.cpu_name_927.setObjectName(u"cpu_name_927")
        self.cpu_name_927.setFont(font1)
        self.cpu_name_927.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_154.addWidget(self.cpu_name_927, 8, 0, 1, 1)

        self.device1_42 = QLabel(self.frame_153)
        self.device1_42.setObjectName(u"device1_42")
        self.device1_42.setFont(font2)
        self.device1_42.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_42.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_42.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_154.addWidget(self.device1_42, 1, 0, 1, 1)

        self.clientipaddress_42 = QLabel(self.frame_153)
        self.clientipaddress_42.setObjectName(u"clientipaddress_42")
        self.clientipaddress_42.setFont(font)
        self.clientipaddress_42.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_42.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_42.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_154.addWidget(self.clientipaddress_42, 1, 1, 1, 5)

        self.gpu1usage_42 = QLabel(self.frame_153)
        self.gpu1usage_42.setObjectName(u"gpu1usage_42")
        self.gpu1usage_42.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_42.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_42.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_154.addWidget(self.gpu1usage_42, 6, 1, 1, 1)

        self.memoryusage_42 = QLabel(self.frame_153)
        self.memoryusage_42.setObjectName(u"memoryusage_42")
        self.memoryusage_42.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_42.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_42.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_154.addWidget(self.memoryusage_42, 8, 4, 1, 1)

        self.cpu_name_928 = QLabel(self.frame_153)
        self.cpu_name_928.setObjectName(u"cpu_name_928")
        self.cpu_name_928.setFont(font1)
        self.cpu_name_928.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_154.addWidget(self.cpu_name_928, 6, 3, 1, 1)


        self.gridLayout_153.addWidget(self.frame_153, 0, 0, 1, 3)

        self.elapsedtime_42 = QLabel(self.frame_152)
        self.elapsedtime_42.setObjectName(u"elapsedtime_42")
        self.elapsedtime_42.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_42.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_42.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_153.addWidget(self.elapsedtime_42, 1, 2, 1, 1)

        self.off_Button_42 = QPushButton(self.frame_152)
        self.off_Button_42.setObjectName(u"off_Button_42")
        self.off_Button_42.setEnabled(True)
        self.off_Button_42.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_153.addWidget(self.off_Button_42, 1, 1, 1, 1)


        self.horizontalLayout_19.addWidget(self.frame_152)

        self.frame_154 = QFrame(self.frame_25)
        self.frame_154.setObjectName(u"frame_154")
        self.frame_154.setMinimumSize(QSize(240, 200))
        self.frame_154.setMaximumSize(QSize(240, 200))
        self.frame_154.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_154.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_154.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_154.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_155 = QGridLayout(self.frame_154)
        self.gridLayout_155.setObjectName(u"gridLayout_155")
        self.on_Button_43 = QPushButton(self.frame_154)
        self.on_Button_43.setObjectName(u"on_Button_43")
        self.on_Button_43.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_155.addWidget(self.on_Button_43, 1, 0, 1, 1)

        self.frame_155 = QFrame(self.frame_154)
        self.frame_155.setObjectName(u"frame_155")
        self.frame_155.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_155.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_155.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_156 = QGridLayout(self.frame_155)
        self.gridLayout_156.setObjectName(u"gridLayout_156")
        self.gpu2usage_43 = QLabel(self.frame_155)
        self.gpu2usage_43.setObjectName(u"gpu2usage_43")
        self.gpu2usage_43.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_43.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_43.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_156.addWidget(self.gpu2usage_43, 6, 4, 1, 1)

        self.cpu_name_929 = QLabel(self.frame_155)
        self.cpu_name_929.setObjectName(u"cpu_name_929")
        self.cpu_name_929.setFont(font)
        self.cpu_name_929.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_156.addWidget(self.cpu_name_929, 3, 5, 1, 1)

        self.cpu_name_930 = QLabel(self.frame_155)
        self.cpu_name_930.setObjectName(u"cpu_name_930")
        self.cpu_name_930.setFont(font)
        self.cpu_name_930.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_156.addWidget(self.cpu_name_930, 6, 5, 1, 1)

        self.cpu_name_931 = QLabel(self.frame_155)
        self.cpu_name_931.setObjectName(u"cpu_name_931")
        self.cpu_name_931.setFont(font1)
        self.cpu_name_931.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_156.addWidget(self.cpu_name_931, 6, 0, 1, 1)

        self.cpuusage_43 = QLabel(self.frame_155)
        self.cpuusage_43.setObjectName(u"cpuusage_43")
        self.cpuusage_43.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_43.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_43.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_156.addWidget(self.cpuusage_43, 3, 1, 1, 1)

        self.cpu_name_932 = QLabel(self.frame_155)
        self.cpu_name_932.setObjectName(u"cpu_name_932")
        self.cpu_name_932.setFont(font)
        self.cpu_name_932.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_156.addWidget(self.cpu_name_932, 3, 2, 1, 1)

        self.gpu0usage_43 = QLabel(self.frame_155)
        self.gpu0usage_43.setObjectName(u"gpu0usage_43")
        self.gpu0usage_43.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_43.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_43.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_156.addWidget(self.gpu0usage_43, 3, 4, 1, 1)

        self.cpu_name_933 = QLabel(self.frame_155)
        self.cpu_name_933.setObjectName(u"cpu_name_933")
        self.cpu_name_933.setFont(font1)
        self.cpu_name_933.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_156.addWidget(self.cpu_name_933, 3, 3, 1, 1)

        self.cpu_name_934 = QLabel(self.frame_155)
        self.cpu_name_934.setObjectName(u"cpu_name_934")
        self.cpu_name_934.setFont(font1)
        self.cpu_name_934.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_156.addWidget(self.cpu_name_934, 3, 0, 1, 1)

        self.cpu_name_935 = QLabel(self.frame_155)
        self.cpu_name_935.setObjectName(u"cpu_name_935")
        self.cpu_name_935.setFont(font)
        self.cpu_name_935.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_156.addWidget(self.cpu_name_935, 8, 2, 1, 1)

        self.cpu_name_936 = QLabel(self.frame_155)
        self.cpu_name_936.setObjectName(u"cpu_name_936")
        self.cpu_name_936.setFont(font)
        self.cpu_name_936.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_156.addWidget(self.cpu_name_936, 6, 2, 1, 1)

        self.cpu_name_937 = QLabel(self.frame_155)
        self.cpu_name_937.setObjectName(u"cpu_name_937")
        self.cpu_name_937.setFont(font1)
        self.cpu_name_937.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_156.addWidget(self.cpu_name_937, 8, 3, 1, 1)

        self.cpu_name_938 = QLabel(self.frame_155)
        self.cpu_name_938.setObjectName(u"cpu_name_938")
        self.cpu_name_938.setFont(font)
        self.cpu_name_938.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_156.addWidget(self.cpu_name_938, 8, 5, 1, 1)

        self.gpu3usage_43 = QLabel(self.frame_155)
        self.gpu3usage_43.setObjectName(u"gpu3usage_43")
        self.gpu3usage_43.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_43.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_43.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_156.addWidget(self.gpu3usage_43, 8, 1, 1, 1)

        self.cpu_name_939 = QLabel(self.frame_155)
        self.cpu_name_939.setObjectName(u"cpu_name_939")
        self.cpu_name_939.setFont(font1)
        self.cpu_name_939.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_156.addWidget(self.cpu_name_939, 8, 0, 1, 1)

        self.device1_43 = QLabel(self.frame_155)
        self.device1_43.setObjectName(u"device1_43")
        self.device1_43.setFont(font2)
        self.device1_43.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_43.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_43.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_156.addWidget(self.device1_43, 1, 0, 1, 1)

        self.clientipaddress_43 = QLabel(self.frame_155)
        self.clientipaddress_43.setObjectName(u"clientipaddress_43")
        self.clientipaddress_43.setFont(font)
        self.clientipaddress_43.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_43.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_43.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_156.addWidget(self.clientipaddress_43, 1, 1, 1, 5)

        self.gpu1usage_43 = QLabel(self.frame_155)
        self.gpu1usage_43.setObjectName(u"gpu1usage_43")
        self.gpu1usage_43.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_43.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_43.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_156.addWidget(self.gpu1usage_43, 6, 1, 1, 1)

        self.memoryusage_43 = QLabel(self.frame_155)
        self.memoryusage_43.setObjectName(u"memoryusage_43")
        self.memoryusage_43.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_43.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_43.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_156.addWidget(self.memoryusage_43, 8, 4, 1, 1)

        self.cpu_name_940 = QLabel(self.frame_155)
        self.cpu_name_940.setObjectName(u"cpu_name_940")
        self.cpu_name_940.setFont(font1)
        self.cpu_name_940.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_156.addWidget(self.cpu_name_940, 6, 3, 1, 1)


        self.gridLayout_155.addWidget(self.frame_155, 0, 0, 1, 3)

        self.elapsedtime_43 = QLabel(self.frame_154)
        self.elapsedtime_43.setObjectName(u"elapsedtime_43")
        self.elapsedtime_43.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_43.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_43.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_155.addWidget(self.elapsedtime_43, 1, 2, 1, 1)

        self.off_Button_43 = QPushButton(self.frame_154)
        self.off_Button_43.setObjectName(u"off_Button_43")
        self.off_Button_43.setEnabled(True)
        self.off_Button_43.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_155.addWidget(self.off_Button_43, 1, 1, 1, 1)


        self.horizontalLayout_19.addWidget(self.frame_154)

        self.frame_156 = QFrame(self.frame_25)
        self.frame_156.setObjectName(u"frame_156")
        self.frame_156.setMinimumSize(QSize(240, 200))
        self.frame_156.setMaximumSize(QSize(240, 200))
        self.frame_156.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_156.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_156.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_156.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_157 = QGridLayout(self.frame_156)
        self.gridLayout_157.setObjectName(u"gridLayout_157")
        self.on_Button_44 = QPushButton(self.frame_156)
        self.on_Button_44.setObjectName(u"on_Button_44")
        self.on_Button_44.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_157.addWidget(self.on_Button_44, 1, 0, 1, 1)

        self.frame_157 = QFrame(self.frame_156)
        self.frame_157.setObjectName(u"frame_157")
        self.frame_157.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_157.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_157.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_158 = QGridLayout(self.frame_157)
        self.gridLayout_158.setObjectName(u"gridLayout_158")
        self.gpu2usage_44 = QLabel(self.frame_157)
        self.gpu2usage_44.setObjectName(u"gpu2usage_44")
        self.gpu2usage_44.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_44.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_44.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_158.addWidget(self.gpu2usage_44, 6, 4, 1, 1)

        self.cpu_name_941 = QLabel(self.frame_157)
        self.cpu_name_941.setObjectName(u"cpu_name_941")
        self.cpu_name_941.setFont(font)
        self.cpu_name_941.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_158.addWidget(self.cpu_name_941, 3, 5, 1, 1)

        self.cpu_name_942 = QLabel(self.frame_157)
        self.cpu_name_942.setObjectName(u"cpu_name_942")
        self.cpu_name_942.setFont(font)
        self.cpu_name_942.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_158.addWidget(self.cpu_name_942, 6, 5, 1, 1)

        self.cpu_name_943 = QLabel(self.frame_157)
        self.cpu_name_943.setObjectName(u"cpu_name_943")
        self.cpu_name_943.setFont(font1)
        self.cpu_name_943.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_158.addWidget(self.cpu_name_943, 6, 0, 1, 1)

        self.cpuusage_44 = QLabel(self.frame_157)
        self.cpuusage_44.setObjectName(u"cpuusage_44")
        self.cpuusage_44.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_44.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_44.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_158.addWidget(self.cpuusage_44, 3, 1, 1, 1)

        self.cpu_name_944 = QLabel(self.frame_157)
        self.cpu_name_944.setObjectName(u"cpu_name_944")
        self.cpu_name_944.setFont(font)
        self.cpu_name_944.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_158.addWidget(self.cpu_name_944, 3, 2, 1, 1)

        self.gpu0usage_44 = QLabel(self.frame_157)
        self.gpu0usage_44.setObjectName(u"gpu0usage_44")
        self.gpu0usage_44.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_44.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_44.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_158.addWidget(self.gpu0usage_44, 3, 4, 1, 1)

        self.cpu_name_945 = QLabel(self.frame_157)
        self.cpu_name_945.setObjectName(u"cpu_name_945")
        self.cpu_name_945.setFont(font1)
        self.cpu_name_945.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_158.addWidget(self.cpu_name_945, 3, 3, 1, 1)

        self.cpu_name_946 = QLabel(self.frame_157)
        self.cpu_name_946.setObjectName(u"cpu_name_946")
        self.cpu_name_946.setFont(font1)
        self.cpu_name_946.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_158.addWidget(self.cpu_name_946, 3, 0, 1, 1)

        self.cpu_name_947 = QLabel(self.frame_157)
        self.cpu_name_947.setObjectName(u"cpu_name_947")
        self.cpu_name_947.setFont(font)
        self.cpu_name_947.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_158.addWidget(self.cpu_name_947, 8, 2, 1, 1)

        self.cpu_name_948 = QLabel(self.frame_157)
        self.cpu_name_948.setObjectName(u"cpu_name_948")
        self.cpu_name_948.setFont(font)
        self.cpu_name_948.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_158.addWidget(self.cpu_name_948, 6, 2, 1, 1)

        self.cpu_name_949 = QLabel(self.frame_157)
        self.cpu_name_949.setObjectName(u"cpu_name_949")
        self.cpu_name_949.setFont(font1)
        self.cpu_name_949.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_158.addWidget(self.cpu_name_949, 8, 3, 1, 1)

        self.cpu_name_950 = QLabel(self.frame_157)
        self.cpu_name_950.setObjectName(u"cpu_name_950")
        self.cpu_name_950.setFont(font)
        self.cpu_name_950.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_158.addWidget(self.cpu_name_950, 8, 5, 1, 1)

        self.gpu3usage_44 = QLabel(self.frame_157)
        self.gpu3usage_44.setObjectName(u"gpu3usage_44")
        self.gpu3usage_44.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_44.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_44.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_158.addWidget(self.gpu3usage_44, 8, 1, 1, 1)

        self.cpu_name_951 = QLabel(self.frame_157)
        self.cpu_name_951.setObjectName(u"cpu_name_951")
        self.cpu_name_951.setFont(font1)
        self.cpu_name_951.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_158.addWidget(self.cpu_name_951, 8, 0, 1, 1)

        self.device1_44 = QLabel(self.frame_157)
        self.device1_44.setObjectName(u"device1_44")
        self.device1_44.setFont(font2)
        self.device1_44.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_44.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_44.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_158.addWidget(self.device1_44, 1, 0, 1, 1)

        self.clientipaddress_44 = QLabel(self.frame_157)
        self.clientipaddress_44.setObjectName(u"clientipaddress_44")
        self.clientipaddress_44.setFont(font)
        self.clientipaddress_44.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_44.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_44.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_158.addWidget(self.clientipaddress_44, 1, 1, 1, 5)

        self.gpu1usage_44 = QLabel(self.frame_157)
        self.gpu1usage_44.setObjectName(u"gpu1usage_44")
        self.gpu1usage_44.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_44.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_44.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_158.addWidget(self.gpu1usage_44, 6, 1, 1, 1)

        self.memoryusage_44 = QLabel(self.frame_157)
        self.memoryusage_44.setObjectName(u"memoryusage_44")
        self.memoryusage_44.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_44.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_44.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_158.addWidget(self.memoryusage_44, 8, 4, 1, 1)

        self.cpu_name_952 = QLabel(self.frame_157)
        self.cpu_name_952.setObjectName(u"cpu_name_952")
        self.cpu_name_952.setFont(font1)
        self.cpu_name_952.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_158.addWidget(self.cpu_name_952, 6, 3, 1, 1)


        self.gridLayout_157.addWidget(self.frame_157, 0, 0, 1, 3)

        self.elapsedtime_44 = QLabel(self.frame_156)
        self.elapsedtime_44.setObjectName(u"elapsedtime_44")
        self.elapsedtime_44.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_44.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_44.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_157.addWidget(self.elapsedtime_44, 1, 2, 1, 1)

        self.off_Button_44 = QPushButton(self.frame_156)
        self.off_Button_44.setObjectName(u"off_Button_44")
        self.off_Button_44.setEnabled(True)
        self.off_Button_44.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_157.addWidget(self.off_Button_44, 1, 1, 1, 1)


        self.horizontalLayout_19.addWidget(self.frame_156)


        self.verticalLayout_3.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.frame_2)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.frame_158 = QFrame(self.frame_26)
        self.frame_158.setObjectName(u"frame_158")
        self.frame_158.setMinimumSize(QSize(240, 200))
        self.frame_158.setMaximumSize(QSize(240, 200))
        self.frame_158.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_158.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_158.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_158.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_159 = QGridLayout(self.frame_158)
        self.gridLayout_159.setObjectName(u"gridLayout_159")
        self.on_Button_45 = QPushButton(self.frame_158)
        self.on_Button_45.setObjectName(u"on_Button_45")
        self.on_Button_45.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_159.addWidget(self.on_Button_45, 1, 0, 1, 1)

        self.frame_159 = QFrame(self.frame_158)
        self.frame_159.setObjectName(u"frame_159")
        self.frame_159.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_159.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_159.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_160 = QGridLayout(self.frame_159)
        self.gridLayout_160.setObjectName(u"gridLayout_160")
        self.gpu2usage_45 = QLabel(self.frame_159)
        self.gpu2usage_45.setObjectName(u"gpu2usage_45")
        self.gpu2usage_45.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_45.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_45.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_160.addWidget(self.gpu2usage_45, 6, 4, 1, 1)

        self.cpu_name_953 = QLabel(self.frame_159)
        self.cpu_name_953.setObjectName(u"cpu_name_953")
        self.cpu_name_953.setFont(font)
        self.cpu_name_953.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_160.addWidget(self.cpu_name_953, 3, 5, 1, 1)

        self.cpu_name_954 = QLabel(self.frame_159)
        self.cpu_name_954.setObjectName(u"cpu_name_954")
        self.cpu_name_954.setFont(font)
        self.cpu_name_954.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_160.addWidget(self.cpu_name_954, 6, 5, 1, 1)

        self.cpu_name_955 = QLabel(self.frame_159)
        self.cpu_name_955.setObjectName(u"cpu_name_955")
        self.cpu_name_955.setFont(font1)
        self.cpu_name_955.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_160.addWidget(self.cpu_name_955, 6, 0, 1, 1)

        self.cpuusage_45 = QLabel(self.frame_159)
        self.cpuusage_45.setObjectName(u"cpuusage_45")
        self.cpuusage_45.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_45.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_45.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_160.addWidget(self.cpuusage_45, 3, 1, 1, 1)

        self.cpu_name_956 = QLabel(self.frame_159)
        self.cpu_name_956.setObjectName(u"cpu_name_956")
        self.cpu_name_956.setFont(font)
        self.cpu_name_956.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_160.addWidget(self.cpu_name_956, 3, 2, 1, 1)

        self.gpu0usage_45 = QLabel(self.frame_159)
        self.gpu0usage_45.setObjectName(u"gpu0usage_45")
        self.gpu0usage_45.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_45.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_45.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_160.addWidget(self.gpu0usage_45, 3, 4, 1, 1)

        self.cpu_name_957 = QLabel(self.frame_159)
        self.cpu_name_957.setObjectName(u"cpu_name_957")
        self.cpu_name_957.setFont(font1)
        self.cpu_name_957.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_160.addWidget(self.cpu_name_957, 3, 3, 1, 1)

        self.cpu_name_958 = QLabel(self.frame_159)
        self.cpu_name_958.setObjectName(u"cpu_name_958")
        self.cpu_name_958.setFont(font1)
        self.cpu_name_958.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_160.addWidget(self.cpu_name_958, 3, 0, 1, 1)

        self.cpu_name_959 = QLabel(self.frame_159)
        self.cpu_name_959.setObjectName(u"cpu_name_959")
        self.cpu_name_959.setFont(font)
        self.cpu_name_959.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_160.addWidget(self.cpu_name_959, 8, 2, 1, 1)

        self.cpu_name_960 = QLabel(self.frame_159)
        self.cpu_name_960.setObjectName(u"cpu_name_960")
        self.cpu_name_960.setFont(font)
        self.cpu_name_960.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_160.addWidget(self.cpu_name_960, 6, 2, 1, 1)

        self.cpu_name_961 = QLabel(self.frame_159)
        self.cpu_name_961.setObjectName(u"cpu_name_961")
        self.cpu_name_961.setFont(font1)
        self.cpu_name_961.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_160.addWidget(self.cpu_name_961, 8, 3, 1, 1)

        self.cpu_name_962 = QLabel(self.frame_159)
        self.cpu_name_962.setObjectName(u"cpu_name_962")
        self.cpu_name_962.setFont(font)
        self.cpu_name_962.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_160.addWidget(self.cpu_name_962, 8, 5, 1, 1)

        self.gpu3usage_45 = QLabel(self.frame_159)
        self.gpu3usage_45.setObjectName(u"gpu3usage_45")
        self.gpu3usage_45.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_45.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_45.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_160.addWidget(self.gpu3usage_45, 8, 1, 1, 1)

        self.cpu_name_963 = QLabel(self.frame_159)
        self.cpu_name_963.setObjectName(u"cpu_name_963")
        self.cpu_name_963.setFont(font1)
        self.cpu_name_963.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_160.addWidget(self.cpu_name_963, 8, 0, 1, 1)

        self.device1_45 = QLabel(self.frame_159)
        self.device1_45.setObjectName(u"device1_45")
        self.device1_45.setFont(font2)
        self.device1_45.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_45.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_45.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_160.addWidget(self.device1_45, 1, 0, 1, 1)

        self.clientipaddress_45 = QLabel(self.frame_159)
        self.clientipaddress_45.setObjectName(u"clientipaddress_45")
        self.clientipaddress_45.setFont(font)
        self.clientipaddress_45.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_45.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_45.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_160.addWidget(self.clientipaddress_45, 1, 1, 1, 5)

        self.gpu1usage_45 = QLabel(self.frame_159)
        self.gpu1usage_45.setObjectName(u"gpu1usage_45")
        self.gpu1usage_45.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_45.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_45.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_160.addWidget(self.gpu1usage_45, 6, 1, 1, 1)

        self.memoryusage_45 = QLabel(self.frame_159)
        self.memoryusage_45.setObjectName(u"memoryusage_45")
        self.memoryusage_45.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_45.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_45.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_160.addWidget(self.memoryusage_45, 8, 4, 1, 1)

        self.cpu_name_964 = QLabel(self.frame_159)
        self.cpu_name_964.setObjectName(u"cpu_name_964")
        self.cpu_name_964.setFont(font1)
        self.cpu_name_964.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_160.addWidget(self.cpu_name_964, 6, 3, 1, 1)


        self.gridLayout_159.addWidget(self.frame_159, 0, 0, 1, 3)

        self.elapsedtime_45 = QLabel(self.frame_158)
        self.elapsedtime_45.setObjectName(u"elapsedtime_45")
        self.elapsedtime_45.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_45.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_45.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_159.addWidget(self.elapsedtime_45, 1, 2, 1, 1)

        self.off_Button_45 = QPushButton(self.frame_158)
        self.off_Button_45.setObjectName(u"off_Button_45")
        self.off_Button_45.setEnabled(True)
        self.off_Button_45.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_159.addWidget(self.off_Button_45, 1, 1, 1, 1)


        self.horizontalLayout_20.addWidget(self.frame_158)

        self.frame_160 = QFrame(self.frame_26)
        self.frame_160.setObjectName(u"frame_160")
        self.frame_160.setMinimumSize(QSize(240, 200))
        self.frame_160.setMaximumSize(QSize(240, 200))
        self.frame_160.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_160.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_160.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_160.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_161 = QGridLayout(self.frame_160)
        self.gridLayout_161.setObjectName(u"gridLayout_161")
        self.on_Button_46 = QPushButton(self.frame_160)
        self.on_Button_46.setObjectName(u"on_Button_46")
        self.on_Button_46.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_161.addWidget(self.on_Button_46, 1, 0, 1, 1)

        self.frame_161 = QFrame(self.frame_160)
        self.frame_161.setObjectName(u"frame_161")
        self.frame_161.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_161.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_161.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_162 = QGridLayout(self.frame_161)
        self.gridLayout_162.setObjectName(u"gridLayout_162")
        self.gpu2usage_46 = QLabel(self.frame_161)
        self.gpu2usage_46.setObjectName(u"gpu2usage_46")
        self.gpu2usage_46.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_46.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_46.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_162.addWidget(self.gpu2usage_46, 6, 4, 1, 1)

        self.cpu_name_965 = QLabel(self.frame_161)
        self.cpu_name_965.setObjectName(u"cpu_name_965")
        self.cpu_name_965.setFont(font)
        self.cpu_name_965.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_162.addWidget(self.cpu_name_965, 3, 5, 1, 1)

        self.cpu_name_966 = QLabel(self.frame_161)
        self.cpu_name_966.setObjectName(u"cpu_name_966")
        self.cpu_name_966.setFont(font)
        self.cpu_name_966.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_162.addWidget(self.cpu_name_966, 6, 5, 1, 1)

        self.cpu_name_967 = QLabel(self.frame_161)
        self.cpu_name_967.setObjectName(u"cpu_name_967")
        self.cpu_name_967.setFont(font1)
        self.cpu_name_967.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_162.addWidget(self.cpu_name_967, 6, 0, 1, 1)

        self.cpuusage_46 = QLabel(self.frame_161)
        self.cpuusage_46.setObjectName(u"cpuusage_46")
        self.cpuusage_46.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_46.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_46.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_162.addWidget(self.cpuusage_46, 3, 1, 1, 1)

        self.cpu_name_968 = QLabel(self.frame_161)
        self.cpu_name_968.setObjectName(u"cpu_name_968")
        self.cpu_name_968.setFont(font)
        self.cpu_name_968.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_162.addWidget(self.cpu_name_968, 3, 2, 1, 1)

        self.gpu0usage_46 = QLabel(self.frame_161)
        self.gpu0usage_46.setObjectName(u"gpu0usage_46")
        self.gpu0usage_46.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_46.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_46.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_162.addWidget(self.gpu0usage_46, 3, 4, 1, 1)

        self.cpu_name_969 = QLabel(self.frame_161)
        self.cpu_name_969.setObjectName(u"cpu_name_969")
        self.cpu_name_969.setFont(font1)
        self.cpu_name_969.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_162.addWidget(self.cpu_name_969, 3, 3, 1, 1)

        self.cpu_name_970 = QLabel(self.frame_161)
        self.cpu_name_970.setObjectName(u"cpu_name_970")
        self.cpu_name_970.setFont(font1)
        self.cpu_name_970.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_162.addWidget(self.cpu_name_970, 3, 0, 1, 1)

        self.cpu_name_971 = QLabel(self.frame_161)
        self.cpu_name_971.setObjectName(u"cpu_name_971")
        self.cpu_name_971.setFont(font)
        self.cpu_name_971.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_162.addWidget(self.cpu_name_971, 8, 2, 1, 1)

        self.cpu_name_972 = QLabel(self.frame_161)
        self.cpu_name_972.setObjectName(u"cpu_name_972")
        self.cpu_name_972.setFont(font)
        self.cpu_name_972.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_162.addWidget(self.cpu_name_972, 6, 2, 1, 1)

        self.cpu_name_973 = QLabel(self.frame_161)
        self.cpu_name_973.setObjectName(u"cpu_name_973")
        self.cpu_name_973.setFont(font1)
        self.cpu_name_973.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_162.addWidget(self.cpu_name_973, 8, 3, 1, 1)

        self.cpu_name_974 = QLabel(self.frame_161)
        self.cpu_name_974.setObjectName(u"cpu_name_974")
        self.cpu_name_974.setFont(font)
        self.cpu_name_974.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_162.addWidget(self.cpu_name_974, 8, 5, 1, 1)

        self.gpu3usage_46 = QLabel(self.frame_161)
        self.gpu3usage_46.setObjectName(u"gpu3usage_46")
        self.gpu3usage_46.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_46.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_46.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_162.addWidget(self.gpu3usage_46, 8, 1, 1, 1)

        self.cpu_name_975 = QLabel(self.frame_161)
        self.cpu_name_975.setObjectName(u"cpu_name_975")
        self.cpu_name_975.setFont(font1)
        self.cpu_name_975.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_162.addWidget(self.cpu_name_975, 8, 0, 1, 1)

        self.device1_46 = QLabel(self.frame_161)
        self.device1_46.setObjectName(u"device1_46")
        self.device1_46.setFont(font2)
        self.device1_46.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_46.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_46.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_162.addWidget(self.device1_46, 1, 0, 1, 1)

        self.clientipaddress_46 = QLabel(self.frame_161)
        self.clientipaddress_46.setObjectName(u"clientipaddress_46")
        self.clientipaddress_46.setFont(font)
        self.clientipaddress_46.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_46.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_46.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_162.addWidget(self.clientipaddress_46, 1, 1, 1, 5)

        self.gpu1usage_46 = QLabel(self.frame_161)
        self.gpu1usage_46.setObjectName(u"gpu1usage_46")
        self.gpu1usage_46.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_46.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_46.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_162.addWidget(self.gpu1usage_46, 6, 1, 1, 1)

        self.memoryusage_46 = QLabel(self.frame_161)
        self.memoryusage_46.setObjectName(u"memoryusage_46")
        self.memoryusage_46.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_46.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_46.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_162.addWidget(self.memoryusage_46, 8, 4, 1, 1)

        self.cpu_name_976 = QLabel(self.frame_161)
        self.cpu_name_976.setObjectName(u"cpu_name_976")
        self.cpu_name_976.setFont(font1)
        self.cpu_name_976.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_162.addWidget(self.cpu_name_976, 6, 3, 1, 1)


        self.gridLayout_161.addWidget(self.frame_161, 0, 0, 1, 3)

        self.elapsedtime_46 = QLabel(self.frame_160)
        self.elapsedtime_46.setObjectName(u"elapsedtime_46")
        self.elapsedtime_46.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_46.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_46.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_161.addWidget(self.elapsedtime_46, 1, 2, 1, 1)

        self.off_Button_46 = QPushButton(self.frame_160)
        self.off_Button_46.setObjectName(u"off_Button_46")
        self.off_Button_46.setEnabled(True)
        self.off_Button_46.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_161.addWidget(self.off_Button_46, 1, 1, 1, 1)


        self.horizontalLayout_20.addWidget(self.frame_160)

        self.frame_162 = QFrame(self.frame_26)
        self.frame_162.setObjectName(u"frame_162")
        self.frame_162.setMinimumSize(QSize(240, 200))
        self.frame_162.setMaximumSize(QSize(240, 200))
        self.frame_162.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_162.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_162.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_162.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_163 = QGridLayout(self.frame_162)
        self.gridLayout_163.setObjectName(u"gridLayout_163")
        self.on_Button_47 = QPushButton(self.frame_162)
        self.on_Button_47.setObjectName(u"on_Button_47")
        self.on_Button_47.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_163.addWidget(self.on_Button_47, 1, 0, 1, 1)

        self.frame_163 = QFrame(self.frame_162)
        self.frame_163.setObjectName(u"frame_163")
        self.frame_163.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_163.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_163.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_164 = QGridLayout(self.frame_163)
        self.gridLayout_164.setObjectName(u"gridLayout_164")
        self.gpu2usage_47 = QLabel(self.frame_163)
        self.gpu2usage_47.setObjectName(u"gpu2usage_47")
        self.gpu2usage_47.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_47.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_47.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_164.addWidget(self.gpu2usage_47, 6, 4, 1, 1)

        self.cpu_name_977 = QLabel(self.frame_163)
        self.cpu_name_977.setObjectName(u"cpu_name_977")
        self.cpu_name_977.setFont(font)
        self.cpu_name_977.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_164.addWidget(self.cpu_name_977, 3, 5, 1, 1)

        self.cpu_name_978 = QLabel(self.frame_163)
        self.cpu_name_978.setObjectName(u"cpu_name_978")
        self.cpu_name_978.setFont(font)
        self.cpu_name_978.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_164.addWidget(self.cpu_name_978, 6, 5, 1, 1)

        self.cpu_name_979 = QLabel(self.frame_163)
        self.cpu_name_979.setObjectName(u"cpu_name_979")
        self.cpu_name_979.setFont(font1)
        self.cpu_name_979.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_164.addWidget(self.cpu_name_979, 6, 0, 1, 1)

        self.cpuusage_47 = QLabel(self.frame_163)
        self.cpuusage_47.setObjectName(u"cpuusage_47")
        self.cpuusage_47.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_47.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_47.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_164.addWidget(self.cpuusage_47, 3, 1, 1, 1)

        self.cpu_name_980 = QLabel(self.frame_163)
        self.cpu_name_980.setObjectName(u"cpu_name_980")
        self.cpu_name_980.setFont(font)
        self.cpu_name_980.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_164.addWidget(self.cpu_name_980, 3, 2, 1, 1)

        self.gpu0usage_47 = QLabel(self.frame_163)
        self.gpu0usage_47.setObjectName(u"gpu0usage_47")
        self.gpu0usage_47.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_47.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_47.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_164.addWidget(self.gpu0usage_47, 3, 4, 1, 1)

        self.cpu_name_981 = QLabel(self.frame_163)
        self.cpu_name_981.setObjectName(u"cpu_name_981")
        self.cpu_name_981.setFont(font1)
        self.cpu_name_981.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_164.addWidget(self.cpu_name_981, 3, 3, 1, 1)

        self.cpu_name_982 = QLabel(self.frame_163)
        self.cpu_name_982.setObjectName(u"cpu_name_982")
        self.cpu_name_982.setFont(font1)
        self.cpu_name_982.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_164.addWidget(self.cpu_name_982, 3, 0, 1, 1)

        self.cpu_name_983 = QLabel(self.frame_163)
        self.cpu_name_983.setObjectName(u"cpu_name_983")
        self.cpu_name_983.setFont(font)
        self.cpu_name_983.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_164.addWidget(self.cpu_name_983, 8, 2, 1, 1)

        self.cpu_name_984 = QLabel(self.frame_163)
        self.cpu_name_984.setObjectName(u"cpu_name_984")
        self.cpu_name_984.setFont(font)
        self.cpu_name_984.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_164.addWidget(self.cpu_name_984, 6, 2, 1, 1)

        self.cpu_name_985 = QLabel(self.frame_163)
        self.cpu_name_985.setObjectName(u"cpu_name_985")
        self.cpu_name_985.setFont(font1)
        self.cpu_name_985.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_164.addWidget(self.cpu_name_985, 8, 3, 1, 1)

        self.cpu_name_986 = QLabel(self.frame_163)
        self.cpu_name_986.setObjectName(u"cpu_name_986")
        self.cpu_name_986.setFont(font)
        self.cpu_name_986.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_164.addWidget(self.cpu_name_986, 8, 5, 1, 1)

        self.gpu3usage_47 = QLabel(self.frame_163)
        self.gpu3usage_47.setObjectName(u"gpu3usage_47")
        self.gpu3usage_47.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_47.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_47.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_164.addWidget(self.gpu3usage_47, 8, 1, 1, 1)

        self.cpu_name_987 = QLabel(self.frame_163)
        self.cpu_name_987.setObjectName(u"cpu_name_987")
        self.cpu_name_987.setFont(font1)
        self.cpu_name_987.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_164.addWidget(self.cpu_name_987, 8, 0, 1, 1)

        self.device1_47 = QLabel(self.frame_163)
        self.device1_47.setObjectName(u"device1_47")
        self.device1_47.setFont(font2)
        self.device1_47.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_47.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_47.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_164.addWidget(self.device1_47, 1, 0, 1, 1)

        self.clientipaddress_47 = QLabel(self.frame_163)
        self.clientipaddress_47.setObjectName(u"clientipaddress_47")
        self.clientipaddress_47.setFont(font)
        self.clientipaddress_47.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_47.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_47.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_164.addWidget(self.clientipaddress_47, 1, 1, 1, 5)

        self.gpu1usage_47 = QLabel(self.frame_163)
        self.gpu1usage_47.setObjectName(u"gpu1usage_47")
        self.gpu1usage_47.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_47.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_47.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_164.addWidget(self.gpu1usage_47, 6, 1, 1, 1)

        self.memoryusage_47 = QLabel(self.frame_163)
        self.memoryusage_47.setObjectName(u"memoryusage_47")
        self.memoryusage_47.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_47.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_47.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_164.addWidget(self.memoryusage_47, 8, 4, 1, 1)

        self.cpu_name_988 = QLabel(self.frame_163)
        self.cpu_name_988.setObjectName(u"cpu_name_988")
        self.cpu_name_988.setFont(font1)
        self.cpu_name_988.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_164.addWidget(self.cpu_name_988, 6, 3, 1, 1)


        self.gridLayout_163.addWidget(self.frame_163, 0, 0, 1, 3)

        self.elapsedtime_47 = QLabel(self.frame_162)
        self.elapsedtime_47.setObjectName(u"elapsedtime_47")
        self.elapsedtime_47.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_47.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_47.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_163.addWidget(self.elapsedtime_47, 1, 2, 1, 1)

        self.off_Button_47 = QPushButton(self.frame_162)
        self.off_Button_47.setObjectName(u"off_Button_47")
        self.off_Button_47.setEnabled(True)
        self.off_Button_47.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_163.addWidget(self.off_Button_47, 1, 1, 1, 1)


        self.horizontalLayout_20.addWidget(self.frame_162)

        self.frame_164 = QFrame(self.frame_26)
        self.frame_164.setObjectName(u"frame_164")
        self.frame_164.setMinimumSize(QSize(240, 200))
        self.frame_164.setMaximumSize(QSize(240, 200))
        self.frame_164.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_164.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_164.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_164.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_165 = QGridLayout(self.frame_164)
        self.gridLayout_165.setObjectName(u"gridLayout_165")
        self.on_Button_48 = QPushButton(self.frame_164)
        self.on_Button_48.setObjectName(u"on_Button_48")
        self.on_Button_48.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_165.addWidget(self.on_Button_48, 1, 0, 1, 1)

        self.frame_165 = QFrame(self.frame_164)
        self.frame_165.setObjectName(u"frame_165")
        self.frame_165.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_165.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_165.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_166 = QGridLayout(self.frame_165)
        self.gridLayout_166.setObjectName(u"gridLayout_166")
        self.gpu2usage_48 = QLabel(self.frame_165)
        self.gpu2usage_48.setObjectName(u"gpu2usage_48")
        self.gpu2usage_48.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_48.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_48.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_166.addWidget(self.gpu2usage_48, 6, 4, 1, 1)

        self.cpu_name_989 = QLabel(self.frame_165)
        self.cpu_name_989.setObjectName(u"cpu_name_989")
        self.cpu_name_989.setFont(font)
        self.cpu_name_989.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_166.addWidget(self.cpu_name_989, 3, 5, 1, 1)

        self.cpu_name_990 = QLabel(self.frame_165)
        self.cpu_name_990.setObjectName(u"cpu_name_990")
        self.cpu_name_990.setFont(font)
        self.cpu_name_990.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_166.addWidget(self.cpu_name_990, 6, 5, 1, 1)

        self.cpu_name_991 = QLabel(self.frame_165)
        self.cpu_name_991.setObjectName(u"cpu_name_991")
        self.cpu_name_991.setFont(font1)
        self.cpu_name_991.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_166.addWidget(self.cpu_name_991, 6, 0, 1, 1)

        self.cpuusage_48 = QLabel(self.frame_165)
        self.cpuusage_48.setObjectName(u"cpuusage_48")
        self.cpuusage_48.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_48.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_48.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_166.addWidget(self.cpuusage_48, 3, 1, 1, 1)

        self.cpu_name_992 = QLabel(self.frame_165)
        self.cpu_name_992.setObjectName(u"cpu_name_992")
        self.cpu_name_992.setFont(font)
        self.cpu_name_992.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_166.addWidget(self.cpu_name_992, 3, 2, 1, 1)

        self.gpu0usage_48 = QLabel(self.frame_165)
        self.gpu0usage_48.setObjectName(u"gpu0usage_48")
        self.gpu0usage_48.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_48.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_48.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_166.addWidget(self.gpu0usage_48, 3, 4, 1, 1)

        self.cpu_name_993 = QLabel(self.frame_165)
        self.cpu_name_993.setObjectName(u"cpu_name_993")
        self.cpu_name_993.setFont(font1)
        self.cpu_name_993.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_166.addWidget(self.cpu_name_993, 3, 3, 1, 1)

        self.cpu_name_994 = QLabel(self.frame_165)
        self.cpu_name_994.setObjectName(u"cpu_name_994")
        self.cpu_name_994.setFont(font1)
        self.cpu_name_994.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_166.addWidget(self.cpu_name_994, 3, 0, 1, 1)

        self.cpu_name_995 = QLabel(self.frame_165)
        self.cpu_name_995.setObjectName(u"cpu_name_995")
        self.cpu_name_995.setFont(font)
        self.cpu_name_995.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_166.addWidget(self.cpu_name_995, 8, 2, 1, 1)

        self.cpu_name_996 = QLabel(self.frame_165)
        self.cpu_name_996.setObjectName(u"cpu_name_996")
        self.cpu_name_996.setFont(font)
        self.cpu_name_996.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_166.addWidget(self.cpu_name_996, 6, 2, 1, 1)

        self.cpu_name_997 = QLabel(self.frame_165)
        self.cpu_name_997.setObjectName(u"cpu_name_997")
        self.cpu_name_997.setFont(font1)
        self.cpu_name_997.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_166.addWidget(self.cpu_name_997, 8, 3, 1, 1)

        self.cpu_name_998 = QLabel(self.frame_165)
        self.cpu_name_998.setObjectName(u"cpu_name_998")
        self.cpu_name_998.setFont(font)
        self.cpu_name_998.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_166.addWidget(self.cpu_name_998, 8, 5, 1, 1)

        self.gpu3usage_48 = QLabel(self.frame_165)
        self.gpu3usage_48.setObjectName(u"gpu3usage_48")
        self.gpu3usage_48.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_48.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_48.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_166.addWidget(self.gpu3usage_48, 8, 1, 1, 1)

        self.cpu_name_999 = QLabel(self.frame_165)
        self.cpu_name_999.setObjectName(u"cpu_name_999")
        self.cpu_name_999.setFont(font1)
        self.cpu_name_999.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_166.addWidget(self.cpu_name_999, 8, 0, 1, 1)

        self.device1_48 = QLabel(self.frame_165)
        self.device1_48.setObjectName(u"device1_48")
        self.device1_48.setFont(font2)
        self.device1_48.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_48.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_48.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_166.addWidget(self.device1_48, 1, 0, 1, 1)

        self.clientipaddress_48 = QLabel(self.frame_165)
        self.clientipaddress_48.setObjectName(u"clientipaddress_48")
        self.clientipaddress_48.setFont(font)
        self.clientipaddress_48.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_48.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_48.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_166.addWidget(self.clientipaddress_48, 1, 1, 1, 5)

        self.gpu1usage_48 = QLabel(self.frame_165)
        self.gpu1usage_48.setObjectName(u"gpu1usage_48")
        self.gpu1usage_48.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_48.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_48.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_166.addWidget(self.gpu1usage_48, 6, 1, 1, 1)

        self.memoryusage_48 = QLabel(self.frame_165)
        self.memoryusage_48.setObjectName(u"memoryusage_48")
        self.memoryusage_48.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_48.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_48.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_166.addWidget(self.memoryusage_48, 8, 4, 1, 1)

        self.cpu_name_1000 = QLabel(self.frame_165)
        self.cpu_name_1000.setObjectName(u"cpu_name_1000")
        self.cpu_name_1000.setFont(font1)
        self.cpu_name_1000.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_166.addWidget(self.cpu_name_1000, 6, 3, 1, 1)


        self.gridLayout_165.addWidget(self.frame_165, 0, 0, 1, 3)

        self.elapsedtime_48 = QLabel(self.frame_164)
        self.elapsedtime_48.setObjectName(u"elapsedtime_48")
        self.elapsedtime_48.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_48.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_48.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_165.addWidget(self.elapsedtime_48, 1, 2, 1, 1)

        self.off_Button_48 = QPushButton(self.frame_164)
        self.off_Button_48.setObjectName(u"off_Button_48")
        self.off_Button_48.setEnabled(True)
        self.off_Button_48.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_165.addWidget(self.off_Button_48, 1, 1, 1, 1)


        self.horizontalLayout_20.addWidget(self.frame_164)


        self.verticalLayout_3.addWidget(self.frame_26)

        self.frame_27 = QFrame(self.frame_2)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.frame_166 = QFrame(self.frame_27)
        self.frame_166.setObjectName(u"frame_166")
        self.frame_166.setMinimumSize(QSize(240, 200))
        self.frame_166.setMaximumSize(QSize(240, 200))
        self.frame_166.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_166.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_166.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_166.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_167 = QGridLayout(self.frame_166)
        self.gridLayout_167.setObjectName(u"gridLayout_167")
        self.on_Button_49 = QPushButton(self.frame_166)
        self.on_Button_49.setObjectName(u"on_Button_49")
        self.on_Button_49.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_167.addWidget(self.on_Button_49, 1, 0, 1, 1)

        self.frame_167 = QFrame(self.frame_166)
        self.frame_167.setObjectName(u"frame_167")
        self.frame_167.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_167.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_167.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_168 = QGridLayout(self.frame_167)
        self.gridLayout_168.setObjectName(u"gridLayout_168")
        self.gpu2usage_49 = QLabel(self.frame_167)
        self.gpu2usage_49.setObjectName(u"gpu2usage_49")
        self.gpu2usage_49.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_49.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_49.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_168.addWidget(self.gpu2usage_49, 6, 4, 1, 1)

        self.cpu_name_1001 = QLabel(self.frame_167)
        self.cpu_name_1001.setObjectName(u"cpu_name_1001")
        self.cpu_name_1001.setFont(font)
        self.cpu_name_1001.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_168.addWidget(self.cpu_name_1001, 3, 5, 1, 1)

        self.cpu_name_1002 = QLabel(self.frame_167)
        self.cpu_name_1002.setObjectName(u"cpu_name_1002")
        self.cpu_name_1002.setFont(font)
        self.cpu_name_1002.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_168.addWidget(self.cpu_name_1002, 6, 5, 1, 1)

        self.cpu_name_1003 = QLabel(self.frame_167)
        self.cpu_name_1003.setObjectName(u"cpu_name_1003")
        self.cpu_name_1003.setFont(font1)
        self.cpu_name_1003.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_168.addWidget(self.cpu_name_1003, 6, 0, 1, 1)

        self.cpuusage_49 = QLabel(self.frame_167)
        self.cpuusage_49.setObjectName(u"cpuusage_49")
        self.cpuusage_49.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_49.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_49.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_168.addWidget(self.cpuusage_49, 3, 1, 1, 1)

        self.cpu_name_1004 = QLabel(self.frame_167)
        self.cpu_name_1004.setObjectName(u"cpu_name_1004")
        self.cpu_name_1004.setFont(font)
        self.cpu_name_1004.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_168.addWidget(self.cpu_name_1004, 3, 2, 1, 1)

        self.gpu0usage_49 = QLabel(self.frame_167)
        self.gpu0usage_49.setObjectName(u"gpu0usage_49")
        self.gpu0usage_49.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_49.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_49.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_168.addWidget(self.gpu0usage_49, 3, 4, 1, 1)

        self.cpu_name_1005 = QLabel(self.frame_167)
        self.cpu_name_1005.setObjectName(u"cpu_name_1005")
        self.cpu_name_1005.setFont(font1)
        self.cpu_name_1005.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_168.addWidget(self.cpu_name_1005, 3, 3, 1, 1)

        self.cpu_name_1006 = QLabel(self.frame_167)
        self.cpu_name_1006.setObjectName(u"cpu_name_1006")
        self.cpu_name_1006.setFont(font1)
        self.cpu_name_1006.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_168.addWidget(self.cpu_name_1006, 3, 0, 1, 1)

        self.cpu_name_1007 = QLabel(self.frame_167)
        self.cpu_name_1007.setObjectName(u"cpu_name_1007")
        self.cpu_name_1007.setFont(font)
        self.cpu_name_1007.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_168.addWidget(self.cpu_name_1007, 8, 2, 1, 1)

        self.cpu_name_1008 = QLabel(self.frame_167)
        self.cpu_name_1008.setObjectName(u"cpu_name_1008")
        self.cpu_name_1008.setFont(font)
        self.cpu_name_1008.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_168.addWidget(self.cpu_name_1008, 6, 2, 1, 1)

        self.cpu_name_1009 = QLabel(self.frame_167)
        self.cpu_name_1009.setObjectName(u"cpu_name_1009")
        self.cpu_name_1009.setFont(font1)
        self.cpu_name_1009.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_168.addWidget(self.cpu_name_1009, 8, 3, 1, 1)

        self.cpu_name_1010 = QLabel(self.frame_167)
        self.cpu_name_1010.setObjectName(u"cpu_name_1010")
        self.cpu_name_1010.setFont(font)
        self.cpu_name_1010.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_168.addWidget(self.cpu_name_1010, 8, 5, 1, 1)

        self.gpu3usage_49 = QLabel(self.frame_167)
        self.gpu3usage_49.setObjectName(u"gpu3usage_49")
        self.gpu3usage_49.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_49.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_49.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_168.addWidget(self.gpu3usage_49, 8, 1, 1, 1)

        self.cpu_name_1011 = QLabel(self.frame_167)
        self.cpu_name_1011.setObjectName(u"cpu_name_1011")
        self.cpu_name_1011.setFont(font1)
        self.cpu_name_1011.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_168.addWidget(self.cpu_name_1011, 8, 0, 1, 1)

        self.device1_49 = QLabel(self.frame_167)
        self.device1_49.setObjectName(u"device1_49")
        self.device1_49.setFont(font2)
        self.device1_49.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_49.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_49.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_168.addWidget(self.device1_49, 1, 0, 1, 1)

        self.clientipaddress_49 = QLabel(self.frame_167)
        self.clientipaddress_49.setObjectName(u"clientipaddress_49")
        self.clientipaddress_49.setFont(font)
        self.clientipaddress_49.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_49.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_49.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_168.addWidget(self.clientipaddress_49, 1, 1, 1, 5)

        self.gpu1usage_49 = QLabel(self.frame_167)
        self.gpu1usage_49.setObjectName(u"gpu1usage_49")
        self.gpu1usage_49.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_49.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_49.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_168.addWidget(self.gpu1usage_49, 6, 1, 1, 1)

        self.memoryusage_49 = QLabel(self.frame_167)
        self.memoryusage_49.setObjectName(u"memoryusage_49")
        self.memoryusage_49.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_49.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_49.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_168.addWidget(self.memoryusage_49, 8, 4, 1, 1)

        self.cpu_name_1012 = QLabel(self.frame_167)
        self.cpu_name_1012.setObjectName(u"cpu_name_1012")
        self.cpu_name_1012.setFont(font1)
        self.cpu_name_1012.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_168.addWidget(self.cpu_name_1012, 6, 3, 1, 1)


        self.gridLayout_167.addWidget(self.frame_167, 0, 0, 1, 3)

        self.elapsedtime_49 = QLabel(self.frame_166)
        self.elapsedtime_49.setObjectName(u"elapsedtime_49")
        self.elapsedtime_49.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_49.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_49.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_167.addWidget(self.elapsedtime_49, 1, 2, 1, 1)

        self.off_Button_49 = QPushButton(self.frame_166)
        self.off_Button_49.setObjectName(u"off_Button_49")
        self.off_Button_49.setEnabled(True)
        self.off_Button_49.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_167.addWidget(self.off_Button_49, 1, 1, 1, 1)


        self.horizontalLayout_21.addWidget(self.frame_166)

        self.frame_168 = QFrame(self.frame_27)
        self.frame_168.setObjectName(u"frame_168")
        self.frame_168.setMinimumSize(QSize(240, 200))
        self.frame_168.setMaximumSize(QSize(240, 200))
        self.frame_168.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_168.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_168.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_168.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_169 = QGridLayout(self.frame_168)
        self.gridLayout_169.setObjectName(u"gridLayout_169")
        self.on_Button_50 = QPushButton(self.frame_168)
        self.on_Button_50.setObjectName(u"on_Button_50")
        self.on_Button_50.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_169.addWidget(self.on_Button_50, 1, 0, 1, 1)

        self.frame_169 = QFrame(self.frame_168)
        self.frame_169.setObjectName(u"frame_169")
        self.frame_169.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_169.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_169.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_170 = QGridLayout(self.frame_169)
        self.gridLayout_170.setObjectName(u"gridLayout_170")
        self.gpu2usage_50 = QLabel(self.frame_169)
        self.gpu2usage_50.setObjectName(u"gpu2usage_50")
        self.gpu2usage_50.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_50.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_50.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_170.addWidget(self.gpu2usage_50, 6, 4, 1, 1)

        self.cpu_name_1013 = QLabel(self.frame_169)
        self.cpu_name_1013.setObjectName(u"cpu_name_1013")
        self.cpu_name_1013.setFont(font)
        self.cpu_name_1013.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_170.addWidget(self.cpu_name_1013, 3, 5, 1, 1)

        self.cpu_name_1014 = QLabel(self.frame_169)
        self.cpu_name_1014.setObjectName(u"cpu_name_1014")
        self.cpu_name_1014.setFont(font)
        self.cpu_name_1014.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_170.addWidget(self.cpu_name_1014, 6, 5, 1, 1)

        self.cpu_name_1015 = QLabel(self.frame_169)
        self.cpu_name_1015.setObjectName(u"cpu_name_1015")
        self.cpu_name_1015.setFont(font1)
        self.cpu_name_1015.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_170.addWidget(self.cpu_name_1015, 6, 0, 1, 1)

        self.cpuusage_50 = QLabel(self.frame_169)
        self.cpuusage_50.setObjectName(u"cpuusage_50")
        self.cpuusage_50.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_50.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_50.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_170.addWidget(self.cpuusage_50, 3, 1, 1, 1)

        self.cpu_name_1016 = QLabel(self.frame_169)
        self.cpu_name_1016.setObjectName(u"cpu_name_1016")
        self.cpu_name_1016.setFont(font)
        self.cpu_name_1016.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_170.addWidget(self.cpu_name_1016, 3, 2, 1, 1)

        self.gpu0usage_50 = QLabel(self.frame_169)
        self.gpu0usage_50.setObjectName(u"gpu0usage_50")
        self.gpu0usage_50.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_50.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_50.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_170.addWidget(self.gpu0usage_50, 3, 4, 1, 1)

        self.cpu_name_1017 = QLabel(self.frame_169)
        self.cpu_name_1017.setObjectName(u"cpu_name_1017")
        self.cpu_name_1017.setFont(font1)
        self.cpu_name_1017.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_170.addWidget(self.cpu_name_1017, 3, 3, 1, 1)

        self.cpu_name_1018 = QLabel(self.frame_169)
        self.cpu_name_1018.setObjectName(u"cpu_name_1018")
        self.cpu_name_1018.setFont(font1)
        self.cpu_name_1018.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_170.addWidget(self.cpu_name_1018, 3, 0, 1, 1)

        self.cpu_name_1019 = QLabel(self.frame_169)
        self.cpu_name_1019.setObjectName(u"cpu_name_1019")
        self.cpu_name_1019.setFont(font)
        self.cpu_name_1019.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_170.addWidget(self.cpu_name_1019, 8, 2, 1, 1)

        self.cpu_name_1020 = QLabel(self.frame_169)
        self.cpu_name_1020.setObjectName(u"cpu_name_1020")
        self.cpu_name_1020.setFont(font)
        self.cpu_name_1020.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_170.addWidget(self.cpu_name_1020, 6, 2, 1, 1)

        self.cpu_name_1021 = QLabel(self.frame_169)
        self.cpu_name_1021.setObjectName(u"cpu_name_1021")
        self.cpu_name_1021.setFont(font1)
        self.cpu_name_1021.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_170.addWidget(self.cpu_name_1021, 8, 3, 1, 1)

        self.cpu_name_1022 = QLabel(self.frame_169)
        self.cpu_name_1022.setObjectName(u"cpu_name_1022")
        self.cpu_name_1022.setFont(font)
        self.cpu_name_1022.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_170.addWidget(self.cpu_name_1022, 8, 5, 1, 1)

        self.gpu3usage_50 = QLabel(self.frame_169)
        self.gpu3usage_50.setObjectName(u"gpu3usage_50")
        self.gpu3usage_50.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_50.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_50.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_170.addWidget(self.gpu3usage_50, 8, 1, 1, 1)

        self.cpu_name_1023 = QLabel(self.frame_169)
        self.cpu_name_1023.setObjectName(u"cpu_name_1023")
        self.cpu_name_1023.setFont(font1)
        self.cpu_name_1023.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_170.addWidget(self.cpu_name_1023, 8, 0, 1, 1)

        self.device1_50 = QLabel(self.frame_169)
        self.device1_50.setObjectName(u"device1_50")
        self.device1_50.setFont(font2)
        self.device1_50.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_50.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_50.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_170.addWidget(self.device1_50, 1, 0, 1, 1)

        self.clientipaddress_50 = QLabel(self.frame_169)
        self.clientipaddress_50.setObjectName(u"clientipaddress_50")
        self.clientipaddress_50.setFont(font)
        self.clientipaddress_50.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_50.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_50.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_170.addWidget(self.clientipaddress_50, 1, 1, 1, 5)

        self.gpu1usage_50 = QLabel(self.frame_169)
        self.gpu1usage_50.setObjectName(u"gpu1usage_50")
        self.gpu1usage_50.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_50.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_50.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_170.addWidget(self.gpu1usage_50, 6, 1, 1, 1)

        self.memoryusage_50 = QLabel(self.frame_169)
        self.memoryusage_50.setObjectName(u"memoryusage_50")
        self.memoryusage_50.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_50.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_50.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_170.addWidget(self.memoryusage_50, 8, 4, 1, 1)

        self.cpu_name_1024 = QLabel(self.frame_169)
        self.cpu_name_1024.setObjectName(u"cpu_name_1024")
        self.cpu_name_1024.setFont(font1)
        self.cpu_name_1024.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_170.addWidget(self.cpu_name_1024, 6, 3, 1, 1)


        self.gridLayout_169.addWidget(self.frame_169, 0, 0, 1, 3)

        self.elapsedtime_50 = QLabel(self.frame_168)
        self.elapsedtime_50.setObjectName(u"elapsedtime_50")
        self.elapsedtime_50.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_50.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_50.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_169.addWidget(self.elapsedtime_50, 1, 2, 1, 1)

        self.off_Button_50 = QPushButton(self.frame_168)
        self.off_Button_50.setObjectName(u"off_Button_50")
        self.off_Button_50.setEnabled(True)
        self.off_Button_50.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_169.addWidget(self.off_Button_50, 1, 1, 1, 1)


        self.horizontalLayout_21.addWidget(self.frame_168)

        self.frame_170 = QFrame(self.frame_27)
        self.frame_170.setObjectName(u"frame_170")
        self.frame_170.setMinimumSize(QSize(240, 200))
        self.frame_170.setMaximumSize(QSize(240, 200))
        self.frame_170.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_170.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_170.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_170.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_171 = QGridLayout(self.frame_170)
        self.gridLayout_171.setObjectName(u"gridLayout_171")
        self.on_Button_51 = QPushButton(self.frame_170)
        self.on_Button_51.setObjectName(u"on_Button_51")
        self.on_Button_51.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_171.addWidget(self.on_Button_51, 1, 0, 1, 1)

        self.frame_171 = QFrame(self.frame_170)
        self.frame_171.setObjectName(u"frame_171")
        self.frame_171.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_171.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_171.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_172 = QGridLayout(self.frame_171)
        self.gridLayout_172.setObjectName(u"gridLayout_172")
        self.gpu2usage_51 = QLabel(self.frame_171)
        self.gpu2usage_51.setObjectName(u"gpu2usage_51")
        self.gpu2usage_51.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_51.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_51.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_172.addWidget(self.gpu2usage_51, 6, 4, 1, 1)

        self.cpu_name_1025 = QLabel(self.frame_171)
        self.cpu_name_1025.setObjectName(u"cpu_name_1025")
        self.cpu_name_1025.setFont(font)
        self.cpu_name_1025.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_172.addWidget(self.cpu_name_1025, 3, 5, 1, 1)

        self.cpu_name_1026 = QLabel(self.frame_171)
        self.cpu_name_1026.setObjectName(u"cpu_name_1026")
        self.cpu_name_1026.setFont(font)
        self.cpu_name_1026.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_172.addWidget(self.cpu_name_1026, 6, 5, 1, 1)

        self.cpu_name_1027 = QLabel(self.frame_171)
        self.cpu_name_1027.setObjectName(u"cpu_name_1027")
        self.cpu_name_1027.setFont(font1)
        self.cpu_name_1027.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_172.addWidget(self.cpu_name_1027, 6, 0, 1, 1)

        self.cpuusage_51 = QLabel(self.frame_171)
        self.cpuusage_51.setObjectName(u"cpuusage_51")
        self.cpuusage_51.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_51.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_51.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_172.addWidget(self.cpuusage_51, 3, 1, 1, 1)

        self.cpu_name_1028 = QLabel(self.frame_171)
        self.cpu_name_1028.setObjectName(u"cpu_name_1028")
        self.cpu_name_1028.setFont(font)
        self.cpu_name_1028.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_172.addWidget(self.cpu_name_1028, 3, 2, 1, 1)

        self.gpu0usage_51 = QLabel(self.frame_171)
        self.gpu0usage_51.setObjectName(u"gpu0usage_51")
        self.gpu0usage_51.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_51.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_51.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_172.addWidget(self.gpu0usage_51, 3, 4, 1, 1)

        self.cpu_name_1029 = QLabel(self.frame_171)
        self.cpu_name_1029.setObjectName(u"cpu_name_1029")
        self.cpu_name_1029.setFont(font1)
        self.cpu_name_1029.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_172.addWidget(self.cpu_name_1029, 3, 3, 1, 1)

        self.cpu_name_1030 = QLabel(self.frame_171)
        self.cpu_name_1030.setObjectName(u"cpu_name_1030")
        self.cpu_name_1030.setFont(font1)
        self.cpu_name_1030.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_172.addWidget(self.cpu_name_1030, 3, 0, 1, 1)

        self.cpu_name_1031 = QLabel(self.frame_171)
        self.cpu_name_1031.setObjectName(u"cpu_name_1031")
        self.cpu_name_1031.setFont(font)
        self.cpu_name_1031.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_172.addWidget(self.cpu_name_1031, 8, 2, 1, 1)

        self.cpu_name_1032 = QLabel(self.frame_171)
        self.cpu_name_1032.setObjectName(u"cpu_name_1032")
        self.cpu_name_1032.setFont(font)
        self.cpu_name_1032.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_172.addWidget(self.cpu_name_1032, 6, 2, 1, 1)

        self.cpu_name_1033 = QLabel(self.frame_171)
        self.cpu_name_1033.setObjectName(u"cpu_name_1033")
        self.cpu_name_1033.setFont(font1)
        self.cpu_name_1033.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_172.addWidget(self.cpu_name_1033, 8, 3, 1, 1)

        self.cpu_name_1034 = QLabel(self.frame_171)
        self.cpu_name_1034.setObjectName(u"cpu_name_1034")
        self.cpu_name_1034.setFont(font)
        self.cpu_name_1034.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_172.addWidget(self.cpu_name_1034, 8, 5, 1, 1)

        self.gpu3usage_51 = QLabel(self.frame_171)
        self.gpu3usage_51.setObjectName(u"gpu3usage_51")
        self.gpu3usage_51.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_51.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_51.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_172.addWidget(self.gpu3usage_51, 8, 1, 1, 1)

        self.cpu_name_1035 = QLabel(self.frame_171)
        self.cpu_name_1035.setObjectName(u"cpu_name_1035")
        self.cpu_name_1035.setFont(font1)
        self.cpu_name_1035.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_172.addWidget(self.cpu_name_1035, 8, 0, 1, 1)

        self.device1_51 = QLabel(self.frame_171)
        self.device1_51.setObjectName(u"device1_51")
        self.device1_51.setFont(font2)
        self.device1_51.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_51.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_51.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_172.addWidget(self.device1_51, 1, 0, 1, 1)

        self.clientipaddress_51 = QLabel(self.frame_171)
        self.clientipaddress_51.setObjectName(u"clientipaddress_51")
        self.clientipaddress_51.setFont(font)
        self.clientipaddress_51.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_51.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_51.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_172.addWidget(self.clientipaddress_51, 1, 1, 1, 5)

        self.gpu1usage_51 = QLabel(self.frame_171)
        self.gpu1usage_51.setObjectName(u"gpu1usage_51")
        self.gpu1usage_51.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_51.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_51.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_172.addWidget(self.gpu1usage_51, 6, 1, 1, 1)

        self.memoryusage_51 = QLabel(self.frame_171)
        self.memoryusage_51.setObjectName(u"memoryusage_51")
        self.memoryusage_51.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_51.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_51.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_172.addWidget(self.memoryusage_51, 8, 4, 1, 1)

        self.cpu_name_1036 = QLabel(self.frame_171)
        self.cpu_name_1036.setObjectName(u"cpu_name_1036")
        self.cpu_name_1036.setFont(font1)
        self.cpu_name_1036.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_172.addWidget(self.cpu_name_1036, 6, 3, 1, 1)


        self.gridLayout_171.addWidget(self.frame_171, 0, 0, 1, 3)

        self.elapsedtime_51 = QLabel(self.frame_170)
        self.elapsedtime_51.setObjectName(u"elapsedtime_51")
        self.elapsedtime_51.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_51.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_51.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_171.addWidget(self.elapsedtime_51, 1, 2, 1, 1)

        self.off_Button_51 = QPushButton(self.frame_170)
        self.off_Button_51.setObjectName(u"off_Button_51")
        self.off_Button_51.setEnabled(True)
        self.off_Button_51.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_171.addWidget(self.off_Button_51, 1, 1, 1, 1)


        self.horizontalLayout_21.addWidget(self.frame_170)

        self.frame_172 = QFrame(self.frame_27)
        self.frame_172.setObjectName(u"frame_172")
        self.frame_172.setMinimumSize(QSize(240, 200))
        self.frame_172.setMaximumSize(QSize(240, 200))
        self.frame_172.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_172.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_172.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_172.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_173 = QGridLayout(self.frame_172)
        self.gridLayout_173.setObjectName(u"gridLayout_173")
        self.on_Button_52 = QPushButton(self.frame_172)
        self.on_Button_52.setObjectName(u"on_Button_52")
        self.on_Button_52.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_173.addWidget(self.on_Button_52, 1, 0, 1, 1)

        self.frame_173 = QFrame(self.frame_172)
        self.frame_173.setObjectName(u"frame_173")
        self.frame_173.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_173.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_173.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_174 = QGridLayout(self.frame_173)
        self.gridLayout_174.setObjectName(u"gridLayout_174")
        self.gpu2usage_52 = QLabel(self.frame_173)
        self.gpu2usage_52.setObjectName(u"gpu2usage_52")
        self.gpu2usage_52.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_52.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_52.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_174.addWidget(self.gpu2usage_52, 6, 4, 1, 1)

        self.cpu_name_1037 = QLabel(self.frame_173)
        self.cpu_name_1037.setObjectName(u"cpu_name_1037")
        self.cpu_name_1037.setFont(font)
        self.cpu_name_1037.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_174.addWidget(self.cpu_name_1037, 3, 5, 1, 1)

        self.cpu_name_1038 = QLabel(self.frame_173)
        self.cpu_name_1038.setObjectName(u"cpu_name_1038")
        self.cpu_name_1038.setFont(font)
        self.cpu_name_1038.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_174.addWidget(self.cpu_name_1038, 6, 5, 1, 1)

        self.cpu_name_1039 = QLabel(self.frame_173)
        self.cpu_name_1039.setObjectName(u"cpu_name_1039")
        self.cpu_name_1039.setFont(font1)
        self.cpu_name_1039.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_174.addWidget(self.cpu_name_1039, 6, 0, 1, 1)

        self.cpuusage_52 = QLabel(self.frame_173)
        self.cpuusage_52.setObjectName(u"cpuusage_52")
        self.cpuusage_52.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_52.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_52.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_174.addWidget(self.cpuusage_52, 3, 1, 1, 1)

        self.cpu_name_1040 = QLabel(self.frame_173)
        self.cpu_name_1040.setObjectName(u"cpu_name_1040")
        self.cpu_name_1040.setFont(font)
        self.cpu_name_1040.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_174.addWidget(self.cpu_name_1040, 3, 2, 1, 1)

        self.gpu0usage_52 = QLabel(self.frame_173)
        self.gpu0usage_52.setObjectName(u"gpu0usage_52")
        self.gpu0usage_52.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_52.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_52.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_174.addWidget(self.gpu0usage_52, 3, 4, 1, 1)

        self.cpu_name_1041 = QLabel(self.frame_173)
        self.cpu_name_1041.setObjectName(u"cpu_name_1041")
        self.cpu_name_1041.setFont(font1)
        self.cpu_name_1041.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_174.addWidget(self.cpu_name_1041, 3, 3, 1, 1)

        self.cpu_name_1042 = QLabel(self.frame_173)
        self.cpu_name_1042.setObjectName(u"cpu_name_1042")
        self.cpu_name_1042.setFont(font1)
        self.cpu_name_1042.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_174.addWidget(self.cpu_name_1042, 3, 0, 1, 1)

        self.cpu_name_1043 = QLabel(self.frame_173)
        self.cpu_name_1043.setObjectName(u"cpu_name_1043")
        self.cpu_name_1043.setFont(font)
        self.cpu_name_1043.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_174.addWidget(self.cpu_name_1043, 8, 2, 1, 1)

        self.cpu_name_1044 = QLabel(self.frame_173)
        self.cpu_name_1044.setObjectName(u"cpu_name_1044")
        self.cpu_name_1044.setFont(font)
        self.cpu_name_1044.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_174.addWidget(self.cpu_name_1044, 6, 2, 1, 1)

        self.cpu_name_1045 = QLabel(self.frame_173)
        self.cpu_name_1045.setObjectName(u"cpu_name_1045")
        self.cpu_name_1045.setFont(font1)
        self.cpu_name_1045.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_174.addWidget(self.cpu_name_1045, 8, 3, 1, 1)

        self.cpu_name_1046 = QLabel(self.frame_173)
        self.cpu_name_1046.setObjectName(u"cpu_name_1046")
        self.cpu_name_1046.setFont(font)
        self.cpu_name_1046.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_174.addWidget(self.cpu_name_1046, 8, 5, 1, 1)

        self.gpu3usage_52 = QLabel(self.frame_173)
        self.gpu3usage_52.setObjectName(u"gpu3usage_52")
        self.gpu3usage_52.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_52.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_52.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_174.addWidget(self.gpu3usage_52, 8, 1, 1, 1)

        self.cpu_name_1047 = QLabel(self.frame_173)
        self.cpu_name_1047.setObjectName(u"cpu_name_1047")
        self.cpu_name_1047.setFont(font1)
        self.cpu_name_1047.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_174.addWidget(self.cpu_name_1047, 8, 0, 1, 1)

        self.device1_52 = QLabel(self.frame_173)
        self.device1_52.setObjectName(u"device1_52")
        self.device1_52.setFont(font2)
        self.device1_52.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_52.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_52.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_174.addWidget(self.device1_52, 1, 0, 1, 1)

        self.clientipaddress_52 = QLabel(self.frame_173)
        self.clientipaddress_52.setObjectName(u"clientipaddress_52")
        self.clientipaddress_52.setFont(font)
        self.clientipaddress_52.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_52.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_52.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_174.addWidget(self.clientipaddress_52, 1, 1, 1, 5)

        self.gpu1usage_52 = QLabel(self.frame_173)
        self.gpu1usage_52.setObjectName(u"gpu1usage_52")
        self.gpu1usage_52.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_52.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_52.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_174.addWidget(self.gpu1usage_52, 6, 1, 1, 1)

        self.memoryusage_52 = QLabel(self.frame_173)
        self.memoryusage_52.setObjectName(u"memoryusage_52")
        self.memoryusage_52.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_52.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_52.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_174.addWidget(self.memoryusage_52, 8, 4, 1, 1)

        self.cpu_name_1048 = QLabel(self.frame_173)
        self.cpu_name_1048.setObjectName(u"cpu_name_1048")
        self.cpu_name_1048.setFont(font1)
        self.cpu_name_1048.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_174.addWidget(self.cpu_name_1048, 6, 3, 1, 1)


        self.gridLayout_173.addWidget(self.frame_173, 0, 0, 1, 3)

        self.elapsedtime_52 = QLabel(self.frame_172)
        self.elapsedtime_52.setObjectName(u"elapsedtime_52")
        self.elapsedtime_52.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_52.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_52.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_173.addWidget(self.elapsedtime_52, 1, 2, 1, 1)

        self.off_Button_52 = QPushButton(self.frame_172)
        self.off_Button_52.setObjectName(u"off_Button_52")
        self.off_Button_52.setEnabled(True)
        self.off_Button_52.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_173.addWidget(self.off_Button_52, 1, 1, 1, 1)


        self.horizontalLayout_21.addWidget(self.frame_172)


        self.verticalLayout_3.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.frame_2)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.frame_174 = QFrame(self.frame_28)
        self.frame_174.setObjectName(u"frame_174")
        self.frame_174.setMinimumSize(QSize(240, 200))
        self.frame_174.setMaximumSize(QSize(240, 200))
        self.frame_174.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_174.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_174.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_174.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_175 = QGridLayout(self.frame_174)
        self.gridLayout_175.setObjectName(u"gridLayout_175")
        self.on_Button_53 = QPushButton(self.frame_174)
        self.on_Button_53.setObjectName(u"on_Button_53")
        self.on_Button_53.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_175.addWidget(self.on_Button_53, 1, 0, 1, 1)

        self.frame_175 = QFrame(self.frame_174)
        self.frame_175.setObjectName(u"frame_175")
        self.frame_175.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_175.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_175.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_176 = QGridLayout(self.frame_175)
        self.gridLayout_176.setObjectName(u"gridLayout_176")
        self.gpu3usage_53 = QLabel(self.frame_175)
        self.gpu3usage_53.setObjectName(u"gpu3usage_53")
        self.gpu3usage_53.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_53.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_53.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_176.addWidget(self.gpu3usage_53, 8, 1, 1, 1)

        self.cpu_name_1049 = QLabel(self.frame_175)
        self.cpu_name_1049.setObjectName(u"cpu_name_1049")
        self.cpu_name_1049.setFont(font)
        self.cpu_name_1049.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_176.addWidget(self.cpu_name_1049, 8, 2, 1, 1)

        self.cpu_name_1050 = QLabel(self.frame_175)
        self.cpu_name_1050.setObjectName(u"cpu_name_1050")
        self.cpu_name_1050.setFont(font1)
        self.cpu_name_1050.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_176.addWidget(self.cpu_name_1050, 8, 3, 1, 1)

        self.cpu_name_1051 = QLabel(self.frame_175)
        self.cpu_name_1051.setObjectName(u"cpu_name_1051")
        self.cpu_name_1051.setFont(font1)
        self.cpu_name_1051.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_176.addWidget(self.cpu_name_1051, 3, 3, 1, 1)

        self.cpu_name_1052 = QLabel(self.frame_175)
        self.cpu_name_1052.setObjectName(u"cpu_name_1052")
        self.cpu_name_1052.setFont(font1)
        self.cpu_name_1052.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_176.addWidget(self.cpu_name_1052, 3, 0, 1, 1)

        self.cpu_name_1053 = QLabel(self.frame_175)
        self.cpu_name_1053.setObjectName(u"cpu_name_1053")
        self.cpu_name_1053.setFont(font1)
        self.cpu_name_1053.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_176.addWidget(self.cpu_name_1053, 8, 0, 1, 1)

        self.cpu_name_1054 = QLabel(self.frame_175)
        self.cpu_name_1054.setObjectName(u"cpu_name_1054")
        self.cpu_name_1054.setFont(font1)
        self.cpu_name_1054.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_176.addWidget(self.cpu_name_1054, 6, 0, 1, 1)

        self.cpu_name_1055 = QLabel(self.frame_175)
        self.cpu_name_1055.setObjectName(u"cpu_name_1055")
        self.cpu_name_1055.setFont(font)
        self.cpu_name_1055.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_176.addWidget(self.cpu_name_1055, 8, 5, 1, 1)

        self.gpu1usage_53 = QLabel(self.frame_175)
        self.gpu1usage_53.setObjectName(u"gpu1usage_53")
        self.gpu1usage_53.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_53.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_53.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_176.addWidget(self.gpu1usage_53, 6, 1, 1, 1)

        self.gpu0usage_53 = QLabel(self.frame_175)
        self.gpu0usage_53.setObjectName(u"gpu0usage_53")
        self.gpu0usage_53.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_53.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_53.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_176.addWidget(self.gpu0usage_53, 3, 4, 1, 1)

        self.cpu_name_1056 = QLabel(self.frame_175)
        self.cpu_name_1056.setObjectName(u"cpu_name_1056")
        self.cpu_name_1056.setFont(font)
        self.cpu_name_1056.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_176.addWidget(self.cpu_name_1056, 3, 5, 1, 1)

        self.cpu_name_1057 = QLabel(self.frame_175)
        self.cpu_name_1057.setObjectName(u"cpu_name_1057")
        self.cpu_name_1057.setFont(font)
        self.cpu_name_1057.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_176.addWidget(self.cpu_name_1057, 6, 2, 1, 1)

        self.gpu2usage_53 = QLabel(self.frame_175)
        self.gpu2usage_53.setObjectName(u"gpu2usage_53")
        self.gpu2usage_53.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_53.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_53.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_176.addWidget(self.gpu2usage_53, 6, 4, 1, 1)

        self.cpu_name_1058 = QLabel(self.frame_175)
        self.cpu_name_1058.setObjectName(u"cpu_name_1058")
        self.cpu_name_1058.setFont(font1)
        self.cpu_name_1058.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_176.addWidget(self.cpu_name_1058, 6, 3, 1, 1)

        self.cpuusage_53 = QLabel(self.frame_175)
        self.cpuusage_53.setObjectName(u"cpuusage_53")
        self.cpuusage_53.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_53.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_53.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_176.addWidget(self.cpuusage_53, 3, 1, 1, 1)

        self.clientipaddress_53 = QLabel(self.frame_175)
        self.clientipaddress_53.setObjectName(u"clientipaddress_53")
        self.clientipaddress_53.setFont(font)
        self.clientipaddress_53.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_53.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_53.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_176.addWidget(self.clientipaddress_53, 1, 1, 1, 5)

        self.memoryusage_53 = QLabel(self.frame_175)
        self.memoryusage_53.setObjectName(u"memoryusage_53")
        self.memoryusage_53.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_53.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_53.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_176.addWidget(self.memoryusage_53, 8, 4, 1, 1)

        self.cpu_name_1059 = QLabel(self.frame_175)
        self.cpu_name_1059.setObjectName(u"cpu_name_1059")
        self.cpu_name_1059.setFont(font)
        self.cpu_name_1059.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_176.addWidget(self.cpu_name_1059, 6, 5, 1, 1)

        self.cpu_name_1060 = QLabel(self.frame_175)
        self.cpu_name_1060.setObjectName(u"cpu_name_1060")
        self.cpu_name_1060.setFont(font)
        self.cpu_name_1060.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_176.addWidget(self.cpu_name_1060, 3, 2, 1, 1)

        self.device1_53 = QLabel(self.frame_175)
        self.device1_53.setObjectName(u"device1_53")
        self.device1_53.setFont(font2)
        self.device1_53.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_53.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_53.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_176.addWidget(self.device1_53, 1, 0, 1, 1)


        self.gridLayout_175.addWidget(self.frame_175, 0, 0, 1, 3)

        self.elapsedtime_53 = QLabel(self.frame_174)
        self.elapsedtime_53.setObjectName(u"elapsedtime_53")
        self.elapsedtime_53.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_53.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_53.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_175.addWidget(self.elapsedtime_53, 1, 2, 1, 1)

        self.off_Button_53 = QPushButton(self.frame_174)
        self.off_Button_53.setObjectName(u"off_Button_53")
        self.off_Button_53.setEnabled(True)
        self.off_Button_53.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_175.addWidget(self.off_Button_53, 1, 1, 1, 1)


        self.horizontalLayout_22.addWidget(self.frame_174)

        self.frame_176 = QFrame(self.frame_28)
        self.frame_176.setObjectName(u"frame_176")
        self.frame_176.setMinimumSize(QSize(240, 200))
        self.frame_176.setMaximumSize(QSize(240, 200))
        self.frame_176.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_176.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_176.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_176.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_177 = QGridLayout(self.frame_176)
        self.gridLayout_177.setObjectName(u"gridLayout_177")
        self.on_Button_54 = QPushButton(self.frame_176)
        self.on_Button_54.setObjectName(u"on_Button_54")
        self.on_Button_54.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_177.addWidget(self.on_Button_54, 1, 0, 1, 1)

        self.frame_177 = QFrame(self.frame_176)
        self.frame_177.setObjectName(u"frame_177")
        self.frame_177.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_177.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_177.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_178 = QGridLayout(self.frame_177)
        self.gridLayout_178.setObjectName(u"gridLayout_178")
        self.gpu2usage_54 = QLabel(self.frame_177)
        self.gpu2usage_54.setObjectName(u"gpu2usage_54")
        self.gpu2usage_54.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_54.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_54.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_178.addWidget(self.gpu2usage_54, 6, 4, 1, 1)

        self.cpu_name_1061 = QLabel(self.frame_177)
        self.cpu_name_1061.setObjectName(u"cpu_name_1061")
        self.cpu_name_1061.setFont(font)
        self.cpu_name_1061.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_178.addWidget(self.cpu_name_1061, 3, 5, 1, 1)

        self.cpu_name_1062 = QLabel(self.frame_177)
        self.cpu_name_1062.setObjectName(u"cpu_name_1062")
        self.cpu_name_1062.setFont(font)
        self.cpu_name_1062.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_178.addWidget(self.cpu_name_1062, 6, 5, 1, 1)

        self.cpu_name_1063 = QLabel(self.frame_177)
        self.cpu_name_1063.setObjectName(u"cpu_name_1063")
        self.cpu_name_1063.setFont(font1)
        self.cpu_name_1063.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_178.addWidget(self.cpu_name_1063, 6, 0, 1, 1)

        self.cpuusage_54 = QLabel(self.frame_177)
        self.cpuusage_54.setObjectName(u"cpuusage_54")
        self.cpuusage_54.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_54.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_54.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_178.addWidget(self.cpuusage_54, 3, 1, 1, 1)

        self.cpu_name_1064 = QLabel(self.frame_177)
        self.cpu_name_1064.setObjectName(u"cpu_name_1064")
        self.cpu_name_1064.setFont(font)
        self.cpu_name_1064.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_178.addWidget(self.cpu_name_1064, 3, 2, 1, 1)

        self.gpu0usage_54 = QLabel(self.frame_177)
        self.gpu0usage_54.setObjectName(u"gpu0usage_54")
        self.gpu0usage_54.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_54.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_54.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_178.addWidget(self.gpu0usage_54, 3, 4, 1, 1)

        self.cpu_name_1065 = QLabel(self.frame_177)
        self.cpu_name_1065.setObjectName(u"cpu_name_1065")
        self.cpu_name_1065.setFont(font1)
        self.cpu_name_1065.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_178.addWidget(self.cpu_name_1065, 3, 3, 1, 1)

        self.cpu_name_1066 = QLabel(self.frame_177)
        self.cpu_name_1066.setObjectName(u"cpu_name_1066")
        self.cpu_name_1066.setFont(font1)
        self.cpu_name_1066.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_178.addWidget(self.cpu_name_1066, 3, 0, 1, 1)

        self.cpu_name_1067 = QLabel(self.frame_177)
        self.cpu_name_1067.setObjectName(u"cpu_name_1067")
        self.cpu_name_1067.setFont(font)
        self.cpu_name_1067.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_178.addWidget(self.cpu_name_1067, 8, 2, 1, 1)

        self.cpu_name_1068 = QLabel(self.frame_177)
        self.cpu_name_1068.setObjectName(u"cpu_name_1068")
        self.cpu_name_1068.setFont(font)
        self.cpu_name_1068.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_178.addWidget(self.cpu_name_1068, 6, 2, 1, 1)

        self.cpu_name_1069 = QLabel(self.frame_177)
        self.cpu_name_1069.setObjectName(u"cpu_name_1069")
        self.cpu_name_1069.setFont(font1)
        self.cpu_name_1069.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_178.addWidget(self.cpu_name_1069, 8, 3, 1, 1)

        self.cpu_name_1070 = QLabel(self.frame_177)
        self.cpu_name_1070.setObjectName(u"cpu_name_1070")
        self.cpu_name_1070.setFont(font)
        self.cpu_name_1070.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_178.addWidget(self.cpu_name_1070, 8, 5, 1, 1)

        self.gpu3usage_54 = QLabel(self.frame_177)
        self.gpu3usage_54.setObjectName(u"gpu3usage_54")
        self.gpu3usage_54.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_54.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_54.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_178.addWidget(self.gpu3usage_54, 8, 1, 1, 1)

        self.cpu_name_1071 = QLabel(self.frame_177)
        self.cpu_name_1071.setObjectName(u"cpu_name_1071")
        self.cpu_name_1071.setFont(font1)
        self.cpu_name_1071.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_178.addWidget(self.cpu_name_1071, 8, 0, 1, 1)

        self.device1_54 = QLabel(self.frame_177)
        self.device1_54.setObjectName(u"device1_54")
        self.device1_54.setFont(font2)
        self.device1_54.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_54.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_54.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_178.addWidget(self.device1_54, 1, 0, 1, 1)

        self.clientipaddress_54 = QLabel(self.frame_177)
        self.clientipaddress_54.setObjectName(u"clientipaddress_54")
        self.clientipaddress_54.setFont(font)
        self.clientipaddress_54.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_54.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_54.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_178.addWidget(self.clientipaddress_54, 1, 1, 1, 5)

        self.gpu1usage_54 = QLabel(self.frame_177)
        self.gpu1usage_54.setObjectName(u"gpu1usage_54")
        self.gpu1usage_54.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_54.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_54.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_178.addWidget(self.gpu1usage_54, 6, 1, 1, 1)

        self.memoryusage_54 = QLabel(self.frame_177)
        self.memoryusage_54.setObjectName(u"memoryusage_54")
        self.memoryusage_54.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_54.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_54.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_178.addWidget(self.memoryusage_54, 8, 4, 1, 1)

        self.cpu_name_1072 = QLabel(self.frame_177)
        self.cpu_name_1072.setObjectName(u"cpu_name_1072")
        self.cpu_name_1072.setFont(font1)
        self.cpu_name_1072.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_178.addWidget(self.cpu_name_1072, 6, 3, 1, 1)


        self.gridLayout_177.addWidget(self.frame_177, 0, 0, 1, 3)

        self.elapsedtime_54 = QLabel(self.frame_176)
        self.elapsedtime_54.setObjectName(u"elapsedtime_54")
        self.elapsedtime_54.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_54.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_54.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_177.addWidget(self.elapsedtime_54, 1, 2, 1, 1)

        self.off_Button_54 = QPushButton(self.frame_176)
        self.off_Button_54.setObjectName(u"off_Button_54")
        self.off_Button_54.setEnabled(True)
        self.off_Button_54.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_177.addWidget(self.off_Button_54, 1, 1, 1, 1)


        self.horizontalLayout_22.addWidget(self.frame_176)

        self.frame_178 = QFrame(self.frame_28)
        self.frame_178.setObjectName(u"frame_178")
        self.frame_178.setMinimumSize(QSize(240, 200))
        self.frame_178.setMaximumSize(QSize(240, 200))
        self.frame_178.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_178.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_178.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_178.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_179 = QGridLayout(self.frame_178)
        self.gridLayout_179.setObjectName(u"gridLayout_179")
        self.on_Button_55 = QPushButton(self.frame_178)
        self.on_Button_55.setObjectName(u"on_Button_55")
        self.on_Button_55.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_179.addWidget(self.on_Button_55, 1, 0, 1, 1)

        self.frame_179 = QFrame(self.frame_178)
        self.frame_179.setObjectName(u"frame_179")
        self.frame_179.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_179.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_179.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_180 = QGridLayout(self.frame_179)
        self.gridLayout_180.setObjectName(u"gridLayout_180")
        self.gpu2usage_55 = QLabel(self.frame_179)
        self.gpu2usage_55.setObjectName(u"gpu2usage_55")
        self.gpu2usage_55.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_55.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_55.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_180.addWidget(self.gpu2usage_55, 6, 4, 1, 1)

        self.cpu_name_1073 = QLabel(self.frame_179)
        self.cpu_name_1073.setObjectName(u"cpu_name_1073")
        self.cpu_name_1073.setFont(font)
        self.cpu_name_1073.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_180.addWidget(self.cpu_name_1073, 3, 5, 1, 1)

        self.cpu_name_1074 = QLabel(self.frame_179)
        self.cpu_name_1074.setObjectName(u"cpu_name_1074")
        self.cpu_name_1074.setFont(font)
        self.cpu_name_1074.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_180.addWidget(self.cpu_name_1074, 6, 5, 1, 1)

        self.cpu_name_1075 = QLabel(self.frame_179)
        self.cpu_name_1075.setObjectName(u"cpu_name_1075")
        self.cpu_name_1075.setFont(font1)
        self.cpu_name_1075.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_180.addWidget(self.cpu_name_1075, 6, 0, 1, 1)

        self.cpuusage_55 = QLabel(self.frame_179)
        self.cpuusage_55.setObjectName(u"cpuusage_55")
        self.cpuusage_55.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_55.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_55.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_180.addWidget(self.cpuusage_55, 3, 1, 1, 1)

        self.cpu_name_1076 = QLabel(self.frame_179)
        self.cpu_name_1076.setObjectName(u"cpu_name_1076")
        self.cpu_name_1076.setFont(font)
        self.cpu_name_1076.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_180.addWidget(self.cpu_name_1076, 3, 2, 1, 1)

        self.gpu0usage_55 = QLabel(self.frame_179)
        self.gpu0usage_55.setObjectName(u"gpu0usage_55")
        self.gpu0usage_55.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_55.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_55.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_180.addWidget(self.gpu0usage_55, 3, 4, 1, 1)

        self.cpu_name_1077 = QLabel(self.frame_179)
        self.cpu_name_1077.setObjectName(u"cpu_name_1077")
        self.cpu_name_1077.setFont(font1)
        self.cpu_name_1077.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_180.addWidget(self.cpu_name_1077, 3, 3, 1, 1)

        self.cpu_name_1078 = QLabel(self.frame_179)
        self.cpu_name_1078.setObjectName(u"cpu_name_1078")
        self.cpu_name_1078.setFont(font1)
        self.cpu_name_1078.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_180.addWidget(self.cpu_name_1078, 3, 0, 1, 1)

        self.cpu_name_1079 = QLabel(self.frame_179)
        self.cpu_name_1079.setObjectName(u"cpu_name_1079")
        self.cpu_name_1079.setFont(font)
        self.cpu_name_1079.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_180.addWidget(self.cpu_name_1079, 8, 2, 1, 1)

        self.cpu_name_1080 = QLabel(self.frame_179)
        self.cpu_name_1080.setObjectName(u"cpu_name_1080")
        self.cpu_name_1080.setFont(font)
        self.cpu_name_1080.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_180.addWidget(self.cpu_name_1080, 6, 2, 1, 1)

        self.cpu_name_1081 = QLabel(self.frame_179)
        self.cpu_name_1081.setObjectName(u"cpu_name_1081")
        self.cpu_name_1081.setFont(font1)
        self.cpu_name_1081.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_180.addWidget(self.cpu_name_1081, 8, 3, 1, 1)

        self.cpu_name_1082 = QLabel(self.frame_179)
        self.cpu_name_1082.setObjectName(u"cpu_name_1082")
        self.cpu_name_1082.setFont(font)
        self.cpu_name_1082.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_180.addWidget(self.cpu_name_1082, 8, 5, 1, 1)

        self.gpu3usage_55 = QLabel(self.frame_179)
        self.gpu3usage_55.setObjectName(u"gpu3usage_55")
        self.gpu3usage_55.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_55.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_55.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_180.addWidget(self.gpu3usage_55, 8, 1, 1, 1)

        self.cpu_name_1083 = QLabel(self.frame_179)
        self.cpu_name_1083.setObjectName(u"cpu_name_1083")
        self.cpu_name_1083.setFont(font1)
        self.cpu_name_1083.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_180.addWidget(self.cpu_name_1083, 8, 0, 1, 1)

        self.device1_55 = QLabel(self.frame_179)
        self.device1_55.setObjectName(u"device1_55")
        self.device1_55.setFont(font2)
        self.device1_55.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_55.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_55.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_180.addWidget(self.device1_55, 1, 0, 1, 1)

        self.clientipaddress_55 = QLabel(self.frame_179)
        self.clientipaddress_55.setObjectName(u"clientipaddress_55")
        self.clientipaddress_55.setFont(font)
        self.clientipaddress_55.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_55.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_55.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_180.addWidget(self.clientipaddress_55, 1, 1, 1, 5)

        self.gpu1usage_55 = QLabel(self.frame_179)
        self.gpu1usage_55.setObjectName(u"gpu1usage_55")
        self.gpu1usage_55.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_55.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_55.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_180.addWidget(self.gpu1usage_55, 6, 1, 1, 1)

        self.memoryusage_55 = QLabel(self.frame_179)
        self.memoryusage_55.setObjectName(u"memoryusage_55")
        self.memoryusage_55.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_55.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_55.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_180.addWidget(self.memoryusage_55, 8, 4, 1, 1)

        self.cpu_name_1084 = QLabel(self.frame_179)
        self.cpu_name_1084.setObjectName(u"cpu_name_1084")
        self.cpu_name_1084.setFont(font1)
        self.cpu_name_1084.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_180.addWidget(self.cpu_name_1084, 6, 3, 1, 1)


        self.gridLayout_179.addWidget(self.frame_179, 0, 0, 1, 3)

        self.elapsedtime_55 = QLabel(self.frame_178)
        self.elapsedtime_55.setObjectName(u"elapsedtime_55")
        self.elapsedtime_55.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_55.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_55.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_179.addWidget(self.elapsedtime_55, 1, 2, 1, 1)

        self.off_Button_55 = QPushButton(self.frame_178)
        self.off_Button_55.setObjectName(u"off_Button_55")
        self.off_Button_55.setEnabled(True)
        self.off_Button_55.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_179.addWidget(self.off_Button_55, 1, 1, 1, 1)


        self.horizontalLayout_22.addWidget(self.frame_178)

        self.frame_180 = QFrame(self.frame_28)
        self.frame_180.setObjectName(u"frame_180")
        self.frame_180.setMinimumSize(QSize(240, 200))
        self.frame_180.setMaximumSize(QSize(240, 200))
        self.frame_180.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_180.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_180.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_180.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_181 = QGridLayout(self.frame_180)
        self.gridLayout_181.setObjectName(u"gridLayout_181")
        self.on_Button_56 = QPushButton(self.frame_180)
        self.on_Button_56.setObjectName(u"on_Button_56")
        self.on_Button_56.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_181.addWidget(self.on_Button_56, 1, 0, 1, 1)

        self.frame_181 = QFrame(self.frame_180)
        self.frame_181.setObjectName(u"frame_181")
        self.frame_181.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_181.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_181.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_182 = QGridLayout(self.frame_181)
        self.gridLayout_182.setObjectName(u"gridLayout_182")
        self.gpu2usage_56 = QLabel(self.frame_181)
        self.gpu2usage_56.setObjectName(u"gpu2usage_56")
        self.gpu2usage_56.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_56.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_56.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_182.addWidget(self.gpu2usage_56, 6, 4, 1, 1)

        self.cpu_name_1085 = QLabel(self.frame_181)
        self.cpu_name_1085.setObjectName(u"cpu_name_1085")
        self.cpu_name_1085.setFont(font)
        self.cpu_name_1085.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_182.addWidget(self.cpu_name_1085, 3, 5, 1, 1)

        self.cpu_name_1086 = QLabel(self.frame_181)
        self.cpu_name_1086.setObjectName(u"cpu_name_1086")
        self.cpu_name_1086.setFont(font)
        self.cpu_name_1086.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_182.addWidget(self.cpu_name_1086, 6, 5, 1, 1)

        self.cpu_name_1087 = QLabel(self.frame_181)
        self.cpu_name_1087.setObjectName(u"cpu_name_1087")
        self.cpu_name_1087.setFont(font1)
        self.cpu_name_1087.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_182.addWidget(self.cpu_name_1087, 6, 0, 1, 1)

        self.cpuusage_56 = QLabel(self.frame_181)
        self.cpuusage_56.setObjectName(u"cpuusage_56")
        self.cpuusage_56.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_56.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_56.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_182.addWidget(self.cpuusage_56, 3, 1, 1, 1)

        self.cpu_name_1088 = QLabel(self.frame_181)
        self.cpu_name_1088.setObjectName(u"cpu_name_1088")
        self.cpu_name_1088.setFont(font)
        self.cpu_name_1088.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_182.addWidget(self.cpu_name_1088, 3, 2, 1, 1)

        self.gpu0usage_56 = QLabel(self.frame_181)
        self.gpu0usage_56.setObjectName(u"gpu0usage_56")
        self.gpu0usage_56.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_56.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_56.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_182.addWidget(self.gpu0usage_56, 3, 4, 1, 1)

        self.cpu_name_1089 = QLabel(self.frame_181)
        self.cpu_name_1089.setObjectName(u"cpu_name_1089")
        self.cpu_name_1089.setFont(font1)
        self.cpu_name_1089.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_182.addWidget(self.cpu_name_1089, 3, 3, 1, 1)

        self.cpu_name_1090 = QLabel(self.frame_181)
        self.cpu_name_1090.setObjectName(u"cpu_name_1090")
        self.cpu_name_1090.setFont(font1)
        self.cpu_name_1090.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_182.addWidget(self.cpu_name_1090, 3, 0, 1, 1)

        self.cpu_name_1091 = QLabel(self.frame_181)
        self.cpu_name_1091.setObjectName(u"cpu_name_1091")
        self.cpu_name_1091.setFont(font)
        self.cpu_name_1091.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_182.addWidget(self.cpu_name_1091, 8, 2, 1, 1)

        self.cpu_name_1092 = QLabel(self.frame_181)
        self.cpu_name_1092.setObjectName(u"cpu_name_1092")
        self.cpu_name_1092.setFont(font)
        self.cpu_name_1092.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_182.addWidget(self.cpu_name_1092, 6, 2, 1, 1)

        self.cpu_name_1093 = QLabel(self.frame_181)
        self.cpu_name_1093.setObjectName(u"cpu_name_1093")
        self.cpu_name_1093.setFont(font1)
        self.cpu_name_1093.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_182.addWidget(self.cpu_name_1093, 8, 3, 1, 1)

        self.cpu_name_1094 = QLabel(self.frame_181)
        self.cpu_name_1094.setObjectName(u"cpu_name_1094")
        self.cpu_name_1094.setFont(font)
        self.cpu_name_1094.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_182.addWidget(self.cpu_name_1094, 8, 5, 1, 1)

        self.gpu3usage_56 = QLabel(self.frame_181)
        self.gpu3usage_56.setObjectName(u"gpu3usage_56")
        self.gpu3usage_56.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_56.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_56.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_182.addWidget(self.gpu3usage_56, 8, 1, 1, 1)

        self.cpu_name_1095 = QLabel(self.frame_181)
        self.cpu_name_1095.setObjectName(u"cpu_name_1095")
        self.cpu_name_1095.setFont(font1)
        self.cpu_name_1095.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_182.addWidget(self.cpu_name_1095, 8, 0, 1, 1)

        self.device1_56 = QLabel(self.frame_181)
        self.device1_56.setObjectName(u"device1_56")
        self.device1_56.setFont(font2)
        self.device1_56.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_56.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_56.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_182.addWidget(self.device1_56, 1, 0, 1, 1)

        self.clientipaddress_56 = QLabel(self.frame_181)
        self.clientipaddress_56.setObjectName(u"clientipaddress_56")
        self.clientipaddress_56.setFont(font)
        self.clientipaddress_56.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_56.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_56.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_182.addWidget(self.clientipaddress_56, 1, 1, 1, 5)

        self.gpu1usage_56 = QLabel(self.frame_181)
        self.gpu1usage_56.setObjectName(u"gpu1usage_56")
        self.gpu1usage_56.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_56.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_56.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_182.addWidget(self.gpu1usage_56, 6, 1, 1, 1)

        self.memoryusage_56 = QLabel(self.frame_181)
        self.memoryusage_56.setObjectName(u"memoryusage_56")
        self.memoryusage_56.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_56.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_56.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_182.addWidget(self.memoryusage_56, 8, 4, 1, 1)

        self.cpu_name_1096 = QLabel(self.frame_181)
        self.cpu_name_1096.setObjectName(u"cpu_name_1096")
        self.cpu_name_1096.setFont(font1)
        self.cpu_name_1096.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_182.addWidget(self.cpu_name_1096, 6, 3, 1, 1)


        self.gridLayout_181.addWidget(self.frame_181, 0, 0, 1, 3)

        self.elapsedtime_56 = QLabel(self.frame_180)
        self.elapsedtime_56.setObjectName(u"elapsedtime_56")
        self.elapsedtime_56.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_56.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_56.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_181.addWidget(self.elapsedtime_56, 1, 2, 1, 1)

        self.off_Button_56 = QPushButton(self.frame_180)
        self.off_Button_56.setObjectName(u"off_Button_56")
        self.off_Button_56.setEnabled(True)
        self.off_Button_56.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_181.addWidget(self.off_Button_56, 1, 1, 1, 1)


        self.horizontalLayout_22.addWidget(self.frame_180)


        self.verticalLayout_3.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.frame_2)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.frame_182 = QFrame(self.frame_29)
        self.frame_182.setObjectName(u"frame_182")
        self.frame_182.setMinimumSize(QSize(240, 200))
        self.frame_182.setMaximumSize(QSize(240, 200))
        self.frame_182.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_182.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_182.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_182.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_183 = QGridLayout(self.frame_182)
        self.gridLayout_183.setObjectName(u"gridLayout_183")
        self.on_Button_57 = QPushButton(self.frame_182)
        self.on_Button_57.setObjectName(u"on_Button_57")
        self.on_Button_57.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_183.addWidget(self.on_Button_57, 1, 0, 1, 1)

        self.frame_183 = QFrame(self.frame_182)
        self.frame_183.setObjectName(u"frame_183")
        self.frame_183.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_183.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_183.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_184 = QGridLayout(self.frame_183)
        self.gridLayout_184.setObjectName(u"gridLayout_184")
        self.gpu2usage_57 = QLabel(self.frame_183)
        self.gpu2usage_57.setObjectName(u"gpu2usage_57")
        self.gpu2usage_57.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_57.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_57.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_184.addWidget(self.gpu2usage_57, 6, 4, 1, 1)

        self.cpu_name_1097 = QLabel(self.frame_183)
        self.cpu_name_1097.setObjectName(u"cpu_name_1097")
        self.cpu_name_1097.setFont(font)
        self.cpu_name_1097.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_184.addWidget(self.cpu_name_1097, 3, 5, 1, 1)

        self.cpu_name_1098 = QLabel(self.frame_183)
        self.cpu_name_1098.setObjectName(u"cpu_name_1098")
        self.cpu_name_1098.setFont(font)
        self.cpu_name_1098.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_184.addWidget(self.cpu_name_1098, 6, 5, 1, 1)

        self.cpu_name_1099 = QLabel(self.frame_183)
        self.cpu_name_1099.setObjectName(u"cpu_name_1099")
        self.cpu_name_1099.setFont(font1)
        self.cpu_name_1099.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_184.addWidget(self.cpu_name_1099, 6, 0, 1, 1)

        self.cpuusage_57 = QLabel(self.frame_183)
        self.cpuusage_57.setObjectName(u"cpuusage_57")
        self.cpuusage_57.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_57.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_57.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_184.addWidget(self.cpuusage_57, 3, 1, 1, 1)

        self.cpu_name_1100 = QLabel(self.frame_183)
        self.cpu_name_1100.setObjectName(u"cpu_name_1100")
        self.cpu_name_1100.setFont(font)
        self.cpu_name_1100.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_184.addWidget(self.cpu_name_1100, 3, 2, 1, 1)

        self.gpu0usage_57 = QLabel(self.frame_183)
        self.gpu0usage_57.setObjectName(u"gpu0usage_57")
        self.gpu0usage_57.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_57.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_57.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_184.addWidget(self.gpu0usage_57, 3, 4, 1, 1)

        self.cpu_name_1101 = QLabel(self.frame_183)
        self.cpu_name_1101.setObjectName(u"cpu_name_1101")
        self.cpu_name_1101.setFont(font1)
        self.cpu_name_1101.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_184.addWidget(self.cpu_name_1101, 3, 3, 1, 1)

        self.cpu_name_1102 = QLabel(self.frame_183)
        self.cpu_name_1102.setObjectName(u"cpu_name_1102")
        self.cpu_name_1102.setFont(font1)
        self.cpu_name_1102.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_184.addWidget(self.cpu_name_1102, 3, 0, 1, 1)

        self.cpu_name_1103 = QLabel(self.frame_183)
        self.cpu_name_1103.setObjectName(u"cpu_name_1103")
        self.cpu_name_1103.setFont(font)
        self.cpu_name_1103.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_184.addWidget(self.cpu_name_1103, 8, 2, 1, 1)

        self.cpu_name_1104 = QLabel(self.frame_183)
        self.cpu_name_1104.setObjectName(u"cpu_name_1104")
        self.cpu_name_1104.setFont(font)
        self.cpu_name_1104.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_184.addWidget(self.cpu_name_1104, 6, 2, 1, 1)

        self.cpu_name_1105 = QLabel(self.frame_183)
        self.cpu_name_1105.setObjectName(u"cpu_name_1105")
        self.cpu_name_1105.setFont(font1)
        self.cpu_name_1105.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_184.addWidget(self.cpu_name_1105, 8, 3, 1, 1)

        self.cpu_name_1106 = QLabel(self.frame_183)
        self.cpu_name_1106.setObjectName(u"cpu_name_1106")
        self.cpu_name_1106.setFont(font)
        self.cpu_name_1106.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_184.addWidget(self.cpu_name_1106, 8, 5, 1, 1)

        self.gpu3usage_57 = QLabel(self.frame_183)
        self.gpu3usage_57.setObjectName(u"gpu3usage_57")
        self.gpu3usage_57.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_57.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_57.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_184.addWidget(self.gpu3usage_57, 8, 1, 1, 1)

        self.cpu_name_1107 = QLabel(self.frame_183)
        self.cpu_name_1107.setObjectName(u"cpu_name_1107")
        self.cpu_name_1107.setFont(font1)
        self.cpu_name_1107.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_184.addWidget(self.cpu_name_1107, 8, 0, 1, 1)

        self.device1_57 = QLabel(self.frame_183)
        self.device1_57.setObjectName(u"device1_57")
        self.device1_57.setFont(font2)
        self.device1_57.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_57.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_57.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_184.addWidget(self.device1_57, 1, 0, 1, 1)

        self.clientipaddress_57 = QLabel(self.frame_183)
        self.clientipaddress_57.setObjectName(u"clientipaddress_57")
        self.clientipaddress_57.setFont(font)
        self.clientipaddress_57.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_57.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_57.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_184.addWidget(self.clientipaddress_57, 1, 1, 1, 5)

        self.gpu1usage_57 = QLabel(self.frame_183)
        self.gpu1usage_57.setObjectName(u"gpu1usage_57")
        self.gpu1usage_57.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_57.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_57.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_184.addWidget(self.gpu1usage_57, 6, 1, 1, 1)

        self.memoryusage_57 = QLabel(self.frame_183)
        self.memoryusage_57.setObjectName(u"memoryusage_57")
        self.memoryusage_57.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_57.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_57.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_184.addWidget(self.memoryusage_57, 8, 4, 1, 1)

        self.cpu_name_1108 = QLabel(self.frame_183)
        self.cpu_name_1108.setObjectName(u"cpu_name_1108")
        self.cpu_name_1108.setFont(font1)
        self.cpu_name_1108.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_184.addWidget(self.cpu_name_1108, 6, 3, 1, 1)


        self.gridLayout_183.addWidget(self.frame_183, 0, 0, 1, 3)

        self.elapsedtime_57 = QLabel(self.frame_182)
        self.elapsedtime_57.setObjectName(u"elapsedtime_57")
        self.elapsedtime_57.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_57.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_57.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_183.addWidget(self.elapsedtime_57, 1, 2, 1, 1)

        self.off_Button_57 = QPushButton(self.frame_182)
        self.off_Button_57.setObjectName(u"off_Button_57")
        self.off_Button_57.setEnabled(True)
        self.off_Button_57.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_183.addWidget(self.off_Button_57, 1, 1, 1, 1)


        self.horizontalLayout_23.addWidget(self.frame_182)

        self.frame_184 = QFrame(self.frame_29)
        self.frame_184.setObjectName(u"frame_184")
        self.frame_184.setMinimumSize(QSize(240, 200))
        self.frame_184.setMaximumSize(QSize(240, 200))
        self.frame_184.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_184.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_184.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_184.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_185 = QGridLayout(self.frame_184)
        self.gridLayout_185.setObjectName(u"gridLayout_185")
        self.on_Button_58 = QPushButton(self.frame_184)
        self.on_Button_58.setObjectName(u"on_Button_58")
        self.on_Button_58.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_185.addWidget(self.on_Button_58, 1, 0, 1, 1)

        self.frame_185 = QFrame(self.frame_184)
        self.frame_185.setObjectName(u"frame_185")
        self.frame_185.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_185.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_185.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_186 = QGridLayout(self.frame_185)
        self.gridLayout_186.setObjectName(u"gridLayout_186")
        self.gpu2usage_58 = QLabel(self.frame_185)
        self.gpu2usage_58.setObjectName(u"gpu2usage_58")
        self.gpu2usage_58.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_58.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_58.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_186.addWidget(self.gpu2usage_58, 6, 4, 1, 1)

        self.cpu_name_1109 = QLabel(self.frame_185)
        self.cpu_name_1109.setObjectName(u"cpu_name_1109")
        self.cpu_name_1109.setFont(font)
        self.cpu_name_1109.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_186.addWidget(self.cpu_name_1109, 3, 5, 1, 1)

        self.cpu_name_1110 = QLabel(self.frame_185)
        self.cpu_name_1110.setObjectName(u"cpu_name_1110")
        self.cpu_name_1110.setFont(font)
        self.cpu_name_1110.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_186.addWidget(self.cpu_name_1110, 6, 5, 1, 1)

        self.cpu_name_1111 = QLabel(self.frame_185)
        self.cpu_name_1111.setObjectName(u"cpu_name_1111")
        self.cpu_name_1111.setFont(font1)
        self.cpu_name_1111.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_186.addWidget(self.cpu_name_1111, 6, 0, 1, 1)

        self.cpuusage_58 = QLabel(self.frame_185)
        self.cpuusage_58.setObjectName(u"cpuusage_58")
        self.cpuusage_58.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_58.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_58.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_186.addWidget(self.cpuusage_58, 3, 1, 1, 1)

        self.cpu_name_1112 = QLabel(self.frame_185)
        self.cpu_name_1112.setObjectName(u"cpu_name_1112")
        self.cpu_name_1112.setFont(font)
        self.cpu_name_1112.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_186.addWidget(self.cpu_name_1112, 3, 2, 1, 1)

        self.gpu0usage_58 = QLabel(self.frame_185)
        self.gpu0usage_58.setObjectName(u"gpu0usage_58")
        self.gpu0usage_58.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_58.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_58.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_186.addWidget(self.gpu0usage_58, 3, 4, 1, 1)

        self.cpu_name_1113 = QLabel(self.frame_185)
        self.cpu_name_1113.setObjectName(u"cpu_name_1113")
        self.cpu_name_1113.setFont(font1)
        self.cpu_name_1113.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_186.addWidget(self.cpu_name_1113, 3, 3, 1, 1)

        self.cpu_name_1114 = QLabel(self.frame_185)
        self.cpu_name_1114.setObjectName(u"cpu_name_1114")
        self.cpu_name_1114.setFont(font1)
        self.cpu_name_1114.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_186.addWidget(self.cpu_name_1114, 3, 0, 1, 1)

        self.cpu_name_1115 = QLabel(self.frame_185)
        self.cpu_name_1115.setObjectName(u"cpu_name_1115")
        self.cpu_name_1115.setFont(font)
        self.cpu_name_1115.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_186.addWidget(self.cpu_name_1115, 8, 2, 1, 1)

        self.cpu_name_1116 = QLabel(self.frame_185)
        self.cpu_name_1116.setObjectName(u"cpu_name_1116")
        self.cpu_name_1116.setFont(font)
        self.cpu_name_1116.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_186.addWidget(self.cpu_name_1116, 6, 2, 1, 1)

        self.cpu_name_1117 = QLabel(self.frame_185)
        self.cpu_name_1117.setObjectName(u"cpu_name_1117")
        self.cpu_name_1117.setFont(font1)
        self.cpu_name_1117.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_186.addWidget(self.cpu_name_1117, 8, 3, 1, 1)

        self.cpu_name_1118 = QLabel(self.frame_185)
        self.cpu_name_1118.setObjectName(u"cpu_name_1118")
        self.cpu_name_1118.setFont(font)
        self.cpu_name_1118.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_186.addWidget(self.cpu_name_1118, 8, 5, 1, 1)

        self.gpu3usage_58 = QLabel(self.frame_185)
        self.gpu3usage_58.setObjectName(u"gpu3usage_58")
        self.gpu3usage_58.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_58.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_58.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_186.addWidget(self.gpu3usage_58, 8, 1, 1, 1)

        self.cpu_name_1119 = QLabel(self.frame_185)
        self.cpu_name_1119.setObjectName(u"cpu_name_1119")
        self.cpu_name_1119.setFont(font1)
        self.cpu_name_1119.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_186.addWidget(self.cpu_name_1119, 8, 0, 1, 1)

        self.device1_58 = QLabel(self.frame_185)
        self.device1_58.setObjectName(u"device1_58")
        self.device1_58.setFont(font2)
        self.device1_58.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_58.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_58.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_186.addWidget(self.device1_58, 1, 0, 1, 1)

        self.clientipaddress_58 = QLabel(self.frame_185)
        self.clientipaddress_58.setObjectName(u"clientipaddress_58")
        self.clientipaddress_58.setFont(font)
        self.clientipaddress_58.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_58.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_58.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_186.addWidget(self.clientipaddress_58, 1, 1, 1, 5)

        self.gpu1usage_58 = QLabel(self.frame_185)
        self.gpu1usage_58.setObjectName(u"gpu1usage_58")
        self.gpu1usage_58.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_58.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_58.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_186.addWidget(self.gpu1usage_58, 6, 1, 1, 1)

        self.memoryusage_58 = QLabel(self.frame_185)
        self.memoryusage_58.setObjectName(u"memoryusage_58")
        self.memoryusage_58.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_58.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_58.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_186.addWidget(self.memoryusage_58, 8, 4, 1, 1)

        self.cpu_name_1120 = QLabel(self.frame_185)
        self.cpu_name_1120.setObjectName(u"cpu_name_1120")
        self.cpu_name_1120.setFont(font1)
        self.cpu_name_1120.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_186.addWidget(self.cpu_name_1120, 6, 3, 1, 1)


        self.gridLayout_185.addWidget(self.frame_185, 0, 0, 1, 3)

        self.elapsedtime_58 = QLabel(self.frame_184)
        self.elapsedtime_58.setObjectName(u"elapsedtime_58")
        self.elapsedtime_58.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_58.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_58.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_185.addWidget(self.elapsedtime_58, 1, 2, 1, 1)

        self.off_Button_58 = QPushButton(self.frame_184)
        self.off_Button_58.setObjectName(u"off_Button_58")
        self.off_Button_58.setEnabled(True)
        self.off_Button_58.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_185.addWidget(self.off_Button_58, 1, 1, 1, 1)


        self.horizontalLayout_23.addWidget(self.frame_184)

        self.frame_186 = QFrame(self.frame_29)
        self.frame_186.setObjectName(u"frame_186")
        self.frame_186.setMinimumSize(QSize(240, 200))
        self.frame_186.setMaximumSize(QSize(240, 200))
        self.frame_186.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_186.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_186.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_186.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_187 = QGridLayout(self.frame_186)
        self.gridLayout_187.setObjectName(u"gridLayout_187")
        self.on_Button_59 = QPushButton(self.frame_186)
        self.on_Button_59.setObjectName(u"on_Button_59")
        self.on_Button_59.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_187.addWidget(self.on_Button_59, 1, 0, 1, 1)

        self.frame_187 = QFrame(self.frame_186)
        self.frame_187.setObjectName(u"frame_187")
        self.frame_187.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_187.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_187.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_188 = QGridLayout(self.frame_187)
        self.gridLayout_188.setObjectName(u"gridLayout_188")
        self.gpu2usage_59 = QLabel(self.frame_187)
        self.gpu2usage_59.setObjectName(u"gpu2usage_59")
        self.gpu2usage_59.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_59.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_59.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_188.addWidget(self.gpu2usage_59, 6, 4, 1, 1)

        self.cpu_name_1121 = QLabel(self.frame_187)
        self.cpu_name_1121.setObjectName(u"cpu_name_1121")
        self.cpu_name_1121.setFont(font)
        self.cpu_name_1121.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_188.addWidget(self.cpu_name_1121, 3, 5, 1, 1)

        self.cpu_name_1122 = QLabel(self.frame_187)
        self.cpu_name_1122.setObjectName(u"cpu_name_1122")
        self.cpu_name_1122.setFont(font)
        self.cpu_name_1122.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_188.addWidget(self.cpu_name_1122, 6, 5, 1, 1)

        self.cpu_name_1123 = QLabel(self.frame_187)
        self.cpu_name_1123.setObjectName(u"cpu_name_1123")
        self.cpu_name_1123.setFont(font1)
        self.cpu_name_1123.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_188.addWidget(self.cpu_name_1123, 6, 0, 1, 1)

        self.cpuusage_59 = QLabel(self.frame_187)
        self.cpuusage_59.setObjectName(u"cpuusage_59")
        self.cpuusage_59.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_59.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_59.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_188.addWidget(self.cpuusage_59, 3, 1, 1, 1)

        self.cpu_name_1124 = QLabel(self.frame_187)
        self.cpu_name_1124.setObjectName(u"cpu_name_1124")
        self.cpu_name_1124.setFont(font)
        self.cpu_name_1124.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_188.addWidget(self.cpu_name_1124, 3, 2, 1, 1)

        self.gpu0usage_59 = QLabel(self.frame_187)
        self.gpu0usage_59.setObjectName(u"gpu0usage_59")
        self.gpu0usage_59.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_59.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_59.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_188.addWidget(self.gpu0usage_59, 3, 4, 1, 1)

        self.cpu_name_1125 = QLabel(self.frame_187)
        self.cpu_name_1125.setObjectName(u"cpu_name_1125")
        self.cpu_name_1125.setFont(font1)
        self.cpu_name_1125.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_188.addWidget(self.cpu_name_1125, 3, 3, 1, 1)

        self.cpu_name_1126 = QLabel(self.frame_187)
        self.cpu_name_1126.setObjectName(u"cpu_name_1126")
        self.cpu_name_1126.setFont(font1)
        self.cpu_name_1126.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_188.addWidget(self.cpu_name_1126, 3, 0, 1, 1)

        self.cpu_name_1127 = QLabel(self.frame_187)
        self.cpu_name_1127.setObjectName(u"cpu_name_1127")
        self.cpu_name_1127.setFont(font)
        self.cpu_name_1127.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_188.addWidget(self.cpu_name_1127, 8, 2, 1, 1)

        self.cpu_name_1128 = QLabel(self.frame_187)
        self.cpu_name_1128.setObjectName(u"cpu_name_1128")
        self.cpu_name_1128.setFont(font)
        self.cpu_name_1128.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_188.addWidget(self.cpu_name_1128, 6, 2, 1, 1)

        self.cpu_name_1129 = QLabel(self.frame_187)
        self.cpu_name_1129.setObjectName(u"cpu_name_1129")
        self.cpu_name_1129.setFont(font1)
        self.cpu_name_1129.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_188.addWidget(self.cpu_name_1129, 8, 3, 1, 1)

        self.cpu_name_1130 = QLabel(self.frame_187)
        self.cpu_name_1130.setObjectName(u"cpu_name_1130")
        self.cpu_name_1130.setFont(font)
        self.cpu_name_1130.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_188.addWidget(self.cpu_name_1130, 8, 5, 1, 1)

        self.gpu3usage_59 = QLabel(self.frame_187)
        self.gpu3usage_59.setObjectName(u"gpu3usage_59")
        self.gpu3usage_59.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_59.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_59.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_188.addWidget(self.gpu3usage_59, 8, 1, 1, 1)

        self.cpu_name_1131 = QLabel(self.frame_187)
        self.cpu_name_1131.setObjectName(u"cpu_name_1131")
        self.cpu_name_1131.setFont(font1)
        self.cpu_name_1131.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_188.addWidget(self.cpu_name_1131, 8, 0, 1, 1)

        self.device1_59 = QLabel(self.frame_187)
        self.device1_59.setObjectName(u"device1_59")
        self.device1_59.setFont(font2)
        self.device1_59.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_59.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_59.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_188.addWidget(self.device1_59, 1, 0, 1, 1)

        self.clientipaddress_59 = QLabel(self.frame_187)
        self.clientipaddress_59.setObjectName(u"clientipaddress_59")
        self.clientipaddress_59.setFont(font)
        self.clientipaddress_59.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_59.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_59.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_188.addWidget(self.clientipaddress_59, 1, 1, 1, 5)

        self.gpu1usage_59 = QLabel(self.frame_187)
        self.gpu1usage_59.setObjectName(u"gpu1usage_59")
        self.gpu1usage_59.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_59.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_59.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_188.addWidget(self.gpu1usage_59, 6, 1, 1, 1)

        self.memoryusage_59 = QLabel(self.frame_187)
        self.memoryusage_59.setObjectName(u"memoryusage_59")
        self.memoryusage_59.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_59.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_59.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_188.addWidget(self.memoryusage_59, 8, 4, 1, 1)

        self.cpu_name_1132 = QLabel(self.frame_187)
        self.cpu_name_1132.setObjectName(u"cpu_name_1132")
        self.cpu_name_1132.setFont(font1)
        self.cpu_name_1132.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_188.addWidget(self.cpu_name_1132, 6, 3, 1, 1)


        self.gridLayout_187.addWidget(self.frame_187, 0, 0, 1, 3)

        self.elapsedtime_59 = QLabel(self.frame_186)
        self.elapsedtime_59.setObjectName(u"elapsedtime_59")
        self.elapsedtime_59.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_59.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_59.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_187.addWidget(self.elapsedtime_59, 1, 2, 1, 1)

        self.off_Button_59 = QPushButton(self.frame_186)
        self.off_Button_59.setObjectName(u"off_Button_59")
        self.off_Button_59.setEnabled(True)
        self.off_Button_59.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_187.addWidget(self.off_Button_59, 1, 1, 1, 1)


        self.horizontalLayout_23.addWidget(self.frame_186)

        self.frame_188 = QFrame(self.frame_29)
        self.frame_188.setObjectName(u"frame_188")
        self.frame_188.setMinimumSize(QSize(240, 200))
        self.frame_188.setMaximumSize(QSize(240, 200))
        self.frame_188.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_188.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_188.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_188.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_189 = QGridLayout(self.frame_188)
        self.gridLayout_189.setObjectName(u"gridLayout_189")
        self.on_Button_60 = QPushButton(self.frame_188)
        self.on_Button_60.setObjectName(u"on_Button_60")
        self.on_Button_60.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_189.addWidget(self.on_Button_60, 1, 0, 1, 1)

        self.frame_189 = QFrame(self.frame_188)
        self.frame_189.setObjectName(u"frame_189")
        self.frame_189.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_189.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_189.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_190 = QGridLayout(self.frame_189)
        self.gridLayout_190.setObjectName(u"gridLayout_190")
        self.gpu2usage_60 = QLabel(self.frame_189)
        self.gpu2usage_60.setObjectName(u"gpu2usage_60")
        self.gpu2usage_60.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_60.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_60.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_190.addWidget(self.gpu2usage_60, 6, 4, 1, 1)

        self.cpu_name_1133 = QLabel(self.frame_189)
        self.cpu_name_1133.setObjectName(u"cpu_name_1133")
        self.cpu_name_1133.setFont(font)
        self.cpu_name_1133.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_190.addWidget(self.cpu_name_1133, 3, 5, 1, 1)

        self.cpu_name_1134 = QLabel(self.frame_189)
        self.cpu_name_1134.setObjectName(u"cpu_name_1134")
        self.cpu_name_1134.setFont(font)
        self.cpu_name_1134.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_190.addWidget(self.cpu_name_1134, 6, 5, 1, 1)

        self.cpu_name_1135 = QLabel(self.frame_189)
        self.cpu_name_1135.setObjectName(u"cpu_name_1135")
        self.cpu_name_1135.setFont(font1)
        self.cpu_name_1135.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_190.addWidget(self.cpu_name_1135, 6, 0, 1, 1)

        self.cpuusage_60 = QLabel(self.frame_189)
        self.cpuusage_60.setObjectName(u"cpuusage_60")
        self.cpuusage_60.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_60.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_60.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_190.addWidget(self.cpuusage_60, 3, 1, 1, 1)

        self.cpu_name_1136 = QLabel(self.frame_189)
        self.cpu_name_1136.setObjectName(u"cpu_name_1136")
        self.cpu_name_1136.setFont(font)
        self.cpu_name_1136.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_190.addWidget(self.cpu_name_1136, 3, 2, 1, 1)

        self.gpu0usage_60 = QLabel(self.frame_189)
        self.gpu0usage_60.setObjectName(u"gpu0usage_60")
        self.gpu0usage_60.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_60.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_60.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_190.addWidget(self.gpu0usage_60, 3, 4, 1, 1)

        self.cpu_name_1137 = QLabel(self.frame_189)
        self.cpu_name_1137.setObjectName(u"cpu_name_1137")
        self.cpu_name_1137.setFont(font1)
        self.cpu_name_1137.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_190.addWidget(self.cpu_name_1137, 3, 3, 1, 1)

        self.cpu_name_1138 = QLabel(self.frame_189)
        self.cpu_name_1138.setObjectName(u"cpu_name_1138")
        self.cpu_name_1138.setFont(font1)
        self.cpu_name_1138.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_190.addWidget(self.cpu_name_1138, 3, 0, 1, 1)

        self.cpu_name_1139 = QLabel(self.frame_189)
        self.cpu_name_1139.setObjectName(u"cpu_name_1139")
        self.cpu_name_1139.setFont(font)
        self.cpu_name_1139.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_190.addWidget(self.cpu_name_1139, 8, 2, 1, 1)

        self.cpu_name_1140 = QLabel(self.frame_189)
        self.cpu_name_1140.setObjectName(u"cpu_name_1140")
        self.cpu_name_1140.setFont(font)
        self.cpu_name_1140.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_190.addWidget(self.cpu_name_1140, 6, 2, 1, 1)

        self.cpu_name_1141 = QLabel(self.frame_189)
        self.cpu_name_1141.setObjectName(u"cpu_name_1141")
        self.cpu_name_1141.setFont(font1)
        self.cpu_name_1141.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_190.addWidget(self.cpu_name_1141, 8, 3, 1, 1)

        self.cpu_name_1142 = QLabel(self.frame_189)
        self.cpu_name_1142.setObjectName(u"cpu_name_1142")
        self.cpu_name_1142.setFont(font)
        self.cpu_name_1142.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_190.addWidget(self.cpu_name_1142, 8, 5, 1, 1)

        self.gpu3usage_60 = QLabel(self.frame_189)
        self.gpu3usage_60.setObjectName(u"gpu3usage_60")
        self.gpu3usage_60.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_60.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_60.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_190.addWidget(self.gpu3usage_60, 8, 1, 1, 1)

        self.cpu_name_1143 = QLabel(self.frame_189)
        self.cpu_name_1143.setObjectName(u"cpu_name_1143")
        self.cpu_name_1143.setFont(font1)
        self.cpu_name_1143.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_190.addWidget(self.cpu_name_1143, 8, 0, 1, 1)

        self.device1_60 = QLabel(self.frame_189)
        self.device1_60.setObjectName(u"device1_60")
        self.device1_60.setFont(font2)
        self.device1_60.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_60.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_60.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_190.addWidget(self.device1_60, 1, 0, 1, 1)

        self.clientipaddress_60 = QLabel(self.frame_189)
        self.clientipaddress_60.setObjectName(u"clientipaddress_60")
        self.clientipaddress_60.setFont(font)
        self.clientipaddress_60.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_60.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_60.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_190.addWidget(self.clientipaddress_60, 1, 1, 1, 5)

        self.gpu1usage_60 = QLabel(self.frame_189)
        self.gpu1usage_60.setObjectName(u"gpu1usage_60")
        self.gpu1usage_60.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_60.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_60.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_190.addWidget(self.gpu1usage_60, 6, 1, 1, 1)

        self.memoryusage_60 = QLabel(self.frame_189)
        self.memoryusage_60.setObjectName(u"memoryusage_60")
        self.memoryusage_60.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_60.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_60.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_190.addWidget(self.memoryusage_60, 8, 4, 1, 1)

        self.cpu_name_1144 = QLabel(self.frame_189)
        self.cpu_name_1144.setObjectName(u"cpu_name_1144")
        self.cpu_name_1144.setFont(font1)
        self.cpu_name_1144.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_190.addWidget(self.cpu_name_1144, 6, 3, 1, 1)


        self.gridLayout_189.addWidget(self.frame_189, 0, 0, 1, 3)

        self.elapsedtime_60 = QLabel(self.frame_188)
        self.elapsedtime_60.setObjectName(u"elapsedtime_60")
        self.elapsedtime_60.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_60.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_60.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_189.addWidget(self.elapsedtime_60, 1, 2, 1, 1)

        self.off_Button_60 = QPushButton(self.frame_188)
        self.off_Button_60.setObjectName(u"off_Button_60")
        self.off_Button_60.setEnabled(True)
        self.off_Button_60.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_189.addWidget(self.off_Button_60, 1, 1, 1, 1)


        self.horizontalLayout_23.addWidget(self.frame_188)


        self.verticalLayout_3.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.frame_2)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.frame_190 = QFrame(self.frame_30)
        self.frame_190.setObjectName(u"frame_190")
        self.frame_190.setMinimumSize(QSize(240, 200))
        self.frame_190.setMaximumSize(QSize(240, 200))
        self.frame_190.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_190.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_190.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_190.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_191 = QGridLayout(self.frame_190)
        self.gridLayout_191.setObjectName(u"gridLayout_191")
        self.on_Button_61 = QPushButton(self.frame_190)
        self.on_Button_61.setObjectName(u"on_Button_61")
        self.on_Button_61.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_191.addWidget(self.on_Button_61, 1, 0, 1, 1)

        self.frame_191 = QFrame(self.frame_190)
        self.frame_191.setObjectName(u"frame_191")
        self.frame_191.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_191.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_191.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_192 = QGridLayout(self.frame_191)
        self.gridLayout_192.setObjectName(u"gridLayout_192")
        self.gpu2usage_61 = QLabel(self.frame_191)
        self.gpu2usage_61.setObjectName(u"gpu2usage_61")
        self.gpu2usage_61.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_61.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_61.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_192.addWidget(self.gpu2usage_61, 6, 4, 1, 1)

        self.cpu_name_1145 = QLabel(self.frame_191)
        self.cpu_name_1145.setObjectName(u"cpu_name_1145")
        self.cpu_name_1145.setFont(font)
        self.cpu_name_1145.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_192.addWidget(self.cpu_name_1145, 3, 5, 1, 1)

        self.cpu_name_1146 = QLabel(self.frame_191)
        self.cpu_name_1146.setObjectName(u"cpu_name_1146")
        self.cpu_name_1146.setFont(font)
        self.cpu_name_1146.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_192.addWidget(self.cpu_name_1146, 6, 5, 1, 1)

        self.cpu_name_1147 = QLabel(self.frame_191)
        self.cpu_name_1147.setObjectName(u"cpu_name_1147")
        self.cpu_name_1147.setFont(font1)
        self.cpu_name_1147.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_192.addWidget(self.cpu_name_1147, 6, 0, 1, 1)

        self.cpuusage_61 = QLabel(self.frame_191)
        self.cpuusage_61.setObjectName(u"cpuusage_61")
        self.cpuusage_61.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_61.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_61.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_192.addWidget(self.cpuusage_61, 3, 1, 1, 1)

        self.cpu_name_1148 = QLabel(self.frame_191)
        self.cpu_name_1148.setObjectName(u"cpu_name_1148")
        self.cpu_name_1148.setFont(font)
        self.cpu_name_1148.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_192.addWidget(self.cpu_name_1148, 3, 2, 1, 1)

        self.gpu0usage_61 = QLabel(self.frame_191)
        self.gpu0usage_61.setObjectName(u"gpu0usage_61")
        self.gpu0usage_61.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_61.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_61.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_192.addWidget(self.gpu0usage_61, 3, 4, 1, 1)

        self.cpu_name_1149 = QLabel(self.frame_191)
        self.cpu_name_1149.setObjectName(u"cpu_name_1149")
        self.cpu_name_1149.setFont(font1)
        self.cpu_name_1149.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_192.addWidget(self.cpu_name_1149, 3, 3, 1, 1)

        self.cpu_name_1150 = QLabel(self.frame_191)
        self.cpu_name_1150.setObjectName(u"cpu_name_1150")
        self.cpu_name_1150.setFont(font1)
        self.cpu_name_1150.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_192.addWidget(self.cpu_name_1150, 3, 0, 1, 1)

        self.cpu_name_1151 = QLabel(self.frame_191)
        self.cpu_name_1151.setObjectName(u"cpu_name_1151")
        self.cpu_name_1151.setFont(font)
        self.cpu_name_1151.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_192.addWidget(self.cpu_name_1151, 8, 2, 1, 1)

        self.cpu_name_1152 = QLabel(self.frame_191)
        self.cpu_name_1152.setObjectName(u"cpu_name_1152")
        self.cpu_name_1152.setFont(font)
        self.cpu_name_1152.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_192.addWidget(self.cpu_name_1152, 6, 2, 1, 1)

        self.cpu_name_1153 = QLabel(self.frame_191)
        self.cpu_name_1153.setObjectName(u"cpu_name_1153")
        self.cpu_name_1153.setFont(font1)
        self.cpu_name_1153.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_192.addWidget(self.cpu_name_1153, 8, 3, 1, 1)

        self.cpu_name_1154 = QLabel(self.frame_191)
        self.cpu_name_1154.setObjectName(u"cpu_name_1154")
        self.cpu_name_1154.setFont(font)
        self.cpu_name_1154.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_192.addWidget(self.cpu_name_1154, 8, 5, 1, 1)

        self.gpu3usage_61 = QLabel(self.frame_191)
        self.gpu3usage_61.setObjectName(u"gpu3usage_61")
        self.gpu3usage_61.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_61.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_61.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_192.addWidget(self.gpu3usage_61, 8, 1, 1, 1)

        self.cpu_name_1155 = QLabel(self.frame_191)
        self.cpu_name_1155.setObjectName(u"cpu_name_1155")
        self.cpu_name_1155.setFont(font1)
        self.cpu_name_1155.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_192.addWidget(self.cpu_name_1155, 8, 0, 1, 1)

        self.device1_61 = QLabel(self.frame_191)
        self.device1_61.setObjectName(u"device1_61")
        self.device1_61.setFont(font2)
        self.device1_61.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_61.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_61.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_192.addWidget(self.device1_61, 1, 0, 1, 1)

        self.clientipaddress_61 = QLabel(self.frame_191)
        self.clientipaddress_61.setObjectName(u"clientipaddress_61")
        self.clientipaddress_61.setFont(font)
        self.clientipaddress_61.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_61.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_61.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_192.addWidget(self.clientipaddress_61, 1, 1, 1, 5)

        self.gpu1usage_61 = QLabel(self.frame_191)
        self.gpu1usage_61.setObjectName(u"gpu1usage_61")
        self.gpu1usage_61.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_61.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_61.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_192.addWidget(self.gpu1usage_61, 6, 1, 1, 1)

        self.memoryusage_61 = QLabel(self.frame_191)
        self.memoryusage_61.setObjectName(u"memoryusage_61")
        self.memoryusage_61.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_61.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_61.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_192.addWidget(self.memoryusage_61, 8, 4, 1, 1)

        self.cpu_name_1156 = QLabel(self.frame_191)
        self.cpu_name_1156.setObjectName(u"cpu_name_1156")
        self.cpu_name_1156.setFont(font1)
        self.cpu_name_1156.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_192.addWidget(self.cpu_name_1156, 6, 3, 1, 1)


        self.gridLayout_191.addWidget(self.frame_191, 0, 0, 1, 3)

        self.elapsedtime_61 = QLabel(self.frame_190)
        self.elapsedtime_61.setObjectName(u"elapsedtime_61")
        self.elapsedtime_61.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_61.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_61.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_191.addWidget(self.elapsedtime_61, 1, 2, 1, 1)

        self.off_Button_61 = QPushButton(self.frame_190)
        self.off_Button_61.setObjectName(u"off_Button_61")
        self.off_Button_61.setEnabled(True)
        self.off_Button_61.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_191.addWidget(self.off_Button_61, 1, 1, 1, 1)


        self.horizontalLayout_24.addWidget(self.frame_190)

        self.frame_192 = QFrame(self.frame_30)
        self.frame_192.setObjectName(u"frame_192")
        self.frame_192.setMinimumSize(QSize(240, 200))
        self.frame_192.setMaximumSize(QSize(240, 200))
        self.frame_192.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_192.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_192.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_192.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_193 = QGridLayout(self.frame_192)
        self.gridLayout_193.setObjectName(u"gridLayout_193")
        self.on_Button_62 = QPushButton(self.frame_192)
        self.on_Button_62.setObjectName(u"on_Button_62")
        self.on_Button_62.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_193.addWidget(self.on_Button_62, 1, 0, 1, 1)

        self.frame_193 = QFrame(self.frame_192)
        self.frame_193.setObjectName(u"frame_193")
        self.frame_193.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_193.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_193.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_194 = QGridLayout(self.frame_193)
        self.gridLayout_194.setObjectName(u"gridLayout_194")
        self.gpu2usage_62 = QLabel(self.frame_193)
        self.gpu2usage_62.setObjectName(u"gpu2usage_62")
        self.gpu2usage_62.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_62.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_62.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_194.addWidget(self.gpu2usage_62, 6, 4, 1, 1)

        self.cpu_name_1157 = QLabel(self.frame_193)
        self.cpu_name_1157.setObjectName(u"cpu_name_1157")
        self.cpu_name_1157.setFont(font)
        self.cpu_name_1157.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_194.addWidget(self.cpu_name_1157, 3, 5, 1, 1)

        self.cpu_name_1158 = QLabel(self.frame_193)
        self.cpu_name_1158.setObjectName(u"cpu_name_1158")
        self.cpu_name_1158.setFont(font)
        self.cpu_name_1158.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_194.addWidget(self.cpu_name_1158, 6, 5, 1, 1)

        self.cpu_name_1159 = QLabel(self.frame_193)
        self.cpu_name_1159.setObjectName(u"cpu_name_1159")
        self.cpu_name_1159.setFont(font1)
        self.cpu_name_1159.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_194.addWidget(self.cpu_name_1159, 6, 0, 1, 1)

        self.cpuusage_62 = QLabel(self.frame_193)
        self.cpuusage_62.setObjectName(u"cpuusage_62")
        self.cpuusage_62.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_62.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_62.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_194.addWidget(self.cpuusage_62, 3, 1, 1, 1)

        self.cpu_name_1160 = QLabel(self.frame_193)
        self.cpu_name_1160.setObjectName(u"cpu_name_1160")
        self.cpu_name_1160.setFont(font)
        self.cpu_name_1160.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_194.addWidget(self.cpu_name_1160, 3, 2, 1, 1)

        self.gpu0usage_62 = QLabel(self.frame_193)
        self.gpu0usage_62.setObjectName(u"gpu0usage_62")
        self.gpu0usage_62.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_62.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_62.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_194.addWidget(self.gpu0usage_62, 3, 4, 1, 1)

        self.cpu_name_1161 = QLabel(self.frame_193)
        self.cpu_name_1161.setObjectName(u"cpu_name_1161")
        self.cpu_name_1161.setFont(font1)
        self.cpu_name_1161.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_194.addWidget(self.cpu_name_1161, 3, 3, 1, 1)

        self.cpu_name_1162 = QLabel(self.frame_193)
        self.cpu_name_1162.setObjectName(u"cpu_name_1162")
        self.cpu_name_1162.setFont(font1)
        self.cpu_name_1162.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_194.addWidget(self.cpu_name_1162, 3, 0, 1, 1)

        self.cpu_name_1163 = QLabel(self.frame_193)
        self.cpu_name_1163.setObjectName(u"cpu_name_1163")
        self.cpu_name_1163.setFont(font)
        self.cpu_name_1163.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_194.addWidget(self.cpu_name_1163, 8, 2, 1, 1)

        self.cpu_name_1164 = QLabel(self.frame_193)
        self.cpu_name_1164.setObjectName(u"cpu_name_1164")
        self.cpu_name_1164.setFont(font)
        self.cpu_name_1164.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_194.addWidget(self.cpu_name_1164, 6, 2, 1, 1)

        self.cpu_name_1165 = QLabel(self.frame_193)
        self.cpu_name_1165.setObjectName(u"cpu_name_1165")
        self.cpu_name_1165.setFont(font1)
        self.cpu_name_1165.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_194.addWidget(self.cpu_name_1165, 8, 3, 1, 1)

        self.cpu_name_1166 = QLabel(self.frame_193)
        self.cpu_name_1166.setObjectName(u"cpu_name_1166")
        self.cpu_name_1166.setFont(font)
        self.cpu_name_1166.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_194.addWidget(self.cpu_name_1166, 8, 5, 1, 1)

        self.gpu3usage_62 = QLabel(self.frame_193)
        self.gpu3usage_62.setObjectName(u"gpu3usage_62")
        self.gpu3usage_62.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_62.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_62.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_194.addWidget(self.gpu3usage_62, 8, 1, 1, 1)

        self.cpu_name_1167 = QLabel(self.frame_193)
        self.cpu_name_1167.setObjectName(u"cpu_name_1167")
        self.cpu_name_1167.setFont(font1)
        self.cpu_name_1167.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_194.addWidget(self.cpu_name_1167, 8, 0, 1, 1)

        self.device1_62 = QLabel(self.frame_193)
        self.device1_62.setObjectName(u"device1_62")
        self.device1_62.setFont(font2)
        self.device1_62.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_62.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_62.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_194.addWidget(self.device1_62, 1, 0, 1, 1)

        self.clientipaddress_62 = QLabel(self.frame_193)
        self.clientipaddress_62.setObjectName(u"clientipaddress_62")
        self.clientipaddress_62.setFont(font)
        self.clientipaddress_62.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_62.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_62.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_194.addWidget(self.clientipaddress_62, 1, 1, 1, 5)

        self.gpu1usage_62 = QLabel(self.frame_193)
        self.gpu1usage_62.setObjectName(u"gpu1usage_62")
        self.gpu1usage_62.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_62.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_62.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_194.addWidget(self.gpu1usage_62, 6, 1, 1, 1)

        self.memoryusage_62 = QLabel(self.frame_193)
        self.memoryusage_62.setObjectName(u"memoryusage_62")
        self.memoryusage_62.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_62.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_62.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_194.addWidget(self.memoryusage_62, 8, 4, 1, 1)

        self.cpu_name_1168 = QLabel(self.frame_193)
        self.cpu_name_1168.setObjectName(u"cpu_name_1168")
        self.cpu_name_1168.setFont(font1)
        self.cpu_name_1168.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_194.addWidget(self.cpu_name_1168, 6, 3, 1, 1)


        self.gridLayout_193.addWidget(self.frame_193, 0, 0, 1, 3)

        self.elapsedtime_62 = QLabel(self.frame_192)
        self.elapsedtime_62.setObjectName(u"elapsedtime_62")
        self.elapsedtime_62.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_62.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_62.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_193.addWidget(self.elapsedtime_62, 1, 2, 1, 1)

        self.off_Button_62 = QPushButton(self.frame_192)
        self.off_Button_62.setObjectName(u"off_Button_62")
        self.off_Button_62.setEnabled(True)
        self.off_Button_62.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_193.addWidget(self.off_Button_62, 1, 1, 1, 1)


        self.horizontalLayout_24.addWidget(self.frame_192)

        self.frame_194 = QFrame(self.frame_30)
        self.frame_194.setObjectName(u"frame_194")
        self.frame_194.setMinimumSize(QSize(240, 200))
        self.frame_194.setMaximumSize(QSize(240, 200))
        self.frame_194.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_194.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_194.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_194.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_195 = QGridLayout(self.frame_194)
        self.gridLayout_195.setObjectName(u"gridLayout_195")
        self.on_Button_63 = QPushButton(self.frame_194)
        self.on_Button_63.setObjectName(u"on_Button_63")
        self.on_Button_63.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_195.addWidget(self.on_Button_63, 1, 0, 1, 1)

        self.frame_195 = QFrame(self.frame_194)
        self.frame_195.setObjectName(u"frame_195")
        self.frame_195.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_195.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_195.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_196 = QGridLayout(self.frame_195)
        self.gridLayout_196.setObjectName(u"gridLayout_196")
        self.gpu2usage_63 = QLabel(self.frame_195)
        self.gpu2usage_63.setObjectName(u"gpu2usage_63")
        self.gpu2usage_63.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_63.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_63.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_196.addWidget(self.gpu2usage_63, 6, 4, 1, 1)

        self.cpu_name_1169 = QLabel(self.frame_195)
        self.cpu_name_1169.setObjectName(u"cpu_name_1169")
        self.cpu_name_1169.setFont(font)
        self.cpu_name_1169.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_196.addWidget(self.cpu_name_1169, 3, 5, 1, 1)

        self.cpu_name_1170 = QLabel(self.frame_195)
        self.cpu_name_1170.setObjectName(u"cpu_name_1170")
        self.cpu_name_1170.setFont(font)
        self.cpu_name_1170.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_196.addWidget(self.cpu_name_1170, 6, 5, 1, 1)

        self.cpu_name_1171 = QLabel(self.frame_195)
        self.cpu_name_1171.setObjectName(u"cpu_name_1171")
        self.cpu_name_1171.setFont(font1)
        self.cpu_name_1171.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_196.addWidget(self.cpu_name_1171, 6, 0, 1, 1)

        self.cpuusage_63 = QLabel(self.frame_195)
        self.cpuusage_63.setObjectName(u"cpuusage_63")
        self.cpuusage_63.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_63.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_63.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_196.addWidget(self.cpuusage_63, 3, 1, 1, 1)

        self.cpu_name_1172 = QLabel(self.frame_195)
        self.cpu_name_1172.setObjectName(u"cpu_name_1172")
        self.cpu_name_1172.setFont(font)
        self.cpu_name_1172.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_196.addWidget(self.cpu_name_1172, 3, 2, 1, 1)

        self.gpu0usage_63 = QLabel(self.frame_195)
        self.gpu0usage_63.setObjectName(u"gpu0usage_63")
        self.gpu0usage_63.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_63.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_63.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_196.addWidget(self.gpu0usage_63, 3, 4, 1, 1)

        self.cpu_name_1173 = QLabel(self.frame_195)
        self.cpu_name_1173.setObjectName(u"cpu_name_1173")
        self.cpu_name_1173.setFont(font1)
        self.cpu_name_1173.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_196.addWidget(self.cpu_name_1173, 3, 3, 1, 1)

        self.cpu_name_1174 = QLabel(self.frame_195)
        self.cpu_name_1174.setObjectName(u"cpu_name_1174")
        self.cpu_name_1174.setFont(font1)
        self.cpu_name_1174.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_196.addWidget(self.cpu_name_1174, 3, 0, 1, 1)

        self.cpu_name_1175 = QLabel(self.frame_195)
        self.cpu_name_1175.setObjectName(u"cpu_name_1175")
        self.cpu_name_1175.setFont(font)
        self.cpu_name_1175.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_196.addWidget(self.cpu_name_1175, 8, 2, 1, 1)

        self.cpu_name_1176 = QLabel(self.frame_195)
        self.cpu_name_1176.setObjectName(u"cpu_name_1176")
        self.cpu_name_1176.setFont(font)
        self.cpu_name_1176.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_196.addWidget(self.cpu_name_1176, 6, 2, 1, 1)

        self.cpu_name_1177 = QLabel(self.frame_195)
        self.cpu_name_1177.setObjectName(u"cpu_name_1177")
        self.cpu_name_1177.setFont(font1)
        self.cpu_name_1177.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_196.addWidget(self.cpu_name_1177, 8, 3, 1, 1)

        self.cpu_name_1178 = QLabel(self.frame_195)
        self.cpu_name_1178.setObjectName(u"cpu_name_1178")
        self.cpu_name_1178.setFont(font)
        self.cpu_name_1178.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_196.addWidget(self.cpu_name_1178, 8, 5, 1, 1)

        self.gpu3usage_63 = QLabel(self.frame_195)
        self.gpu3usage_63.setObjectName(u"gpu3usage_63")
        self.gpu3usage_63.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_63.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_63.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_196.addWidget(self.gpu3usage_63, 8, 1, 1, 1)

        self.cpu_name_1179 = QLabel(self.frame_195)
        self.cpu_name_1179.setObjectName(u"cpu_name_1179")
        self.cpu_name_1179.setFont(font1)
        self.cpu_name_1179.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_196.addWidget(self.cpu_name_1179, 8, 0, 1, 1)

        self.device1_63 = QLabel(self.frame_195)
        self.device1_63.setObjectName(u"device1_63")
        self.device1_63.setFont(font2)
        self.device1_63.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_63.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_63.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_196.addWidget(self.device1_63, 1, 0, 1, 1)

        self.clientipaddress_63 = QLabel(self.frame_195)
        self.clientipaddress_63.setObjectName(u"clientipaddress_63")
        self.clientipaddress_63.setFont(font)
        self.clientipaddress_63.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_63.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_63.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_196.addWidget(self.clientipaddress_63, 1, 1, 1, 5)

        self.gpu1usage_63 = QLabel(self.frame_195)
        self.gpu1usage_63.setObjectName(u"gpu1usage_63")
        self.gpu1usage_63.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_63.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_63.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_196.addWidget(self.gpu1usage_63, 6, 1, 1, 1)

        self.memoryusage_63 = QLabel(self.frame_195)
        self.memoryusage_63.setObjectName(u"memoryusage_63")
        self.memoryusage_63.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_63.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_63.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_196.addWidget(self.memoryusage_63, 8, 4, 1, 1)

        self.cpu_name_1180 = QLabel(self.frame_195)
        self.cpu_name_1180.setObjectName(u"cpu_name_1180")
        self.cpu_name_1180.setFont(font1)
        self.cpu_name_1180.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_196.addWidget(self.cpu_name_1180, 6, 3, 1, 1)


        self.gridLayout_195.addWidget(self.frame_195, 0, 0, 1, 3)

        self.elapsedtime_63 = QLabel(self.frame_194)
        self.elapsedtime_63.setObjectName(u"elapsedtime_63")
        self.elapsedtime_63.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_63.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_63.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_195.addWidget(self.elapsedtime_63, 1, 2, 1, 1)

        self.off_Button_63 = QPushButton(self.frame_194)
        self.off_Button_63.setObjectName(u"off_Button_63")
        self.off_Button_63.setEnabled(True)
        self.off_Button_63.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_195.addWidget(self.off_Button_63, 1, 1, 1, 1)


        self.horizontalLayout_24.addWidget(self.frame_194)

        self.frame_196 = QFrame(self.frame_30)
        self.frame_196.setObjectName(u"frame_196")
        self.frame_196.setMinimumSize(QSize(240, 200))
        self.frame_196.setMaximumSize(QSize(240, 200))
        self.frame_196.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_196.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_196.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_196.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_197 = QGridLayout(self.frame_196)
        self.gridLayout_197.setObjectName(u"gridLayout_197")
        self.on_Button_64 = QPushButton(self.frame_196)
        self.on_Button_64.setObjectName(u"on_Button_64")
        self.on_Button_64.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_197.addWidget(self.on_Button_64, 1, 0, 1, 1)

        self.frame_197 = QFrame(self.frame_196)
        self.frame_197.setObjectName(u"frame_197")
        self.frame_197.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_197.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_197.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_198 = QGridLayout(self.frame_197)
        self.gridLayout_198.setObjectName(u"gridLayout_198")
        self.gpu2usage_64 = QLabel(self.frame_197)
        self.gpu2usage_64.setObjectName(u"gpu2usage_64")
        self.gpu2usage_64.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_64.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_64.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_198.addWidget(self.gpu2usage_64, 6, 4, 1, 1)

        self.cpu_name_1181 = QLabel(self.frame_197)
        self.cpu_name_1181.setObjectName(u"cpu_name_1181")
        self.cpu_name_1181.setFont(font)
        self.cpu_name_1181.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_198.addWidget(self.cpu_name_1181, 3, 5, 1, 1)

        self.cpu_name_1182 = QLabel(self.frame_197)
        self.cpu_name_1182.setObjectName(u"cpu_name_1182")
        self.cpu_name_1182.setFont(font)
        self.cpu_name_1182.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_198.addWidget(self.cpu_name_1182, 6, 5, 1, 1)

        self.cpu_name_1183 = QLabel(self.frame_197)
        self.cpu_name_1183.setObjectName(u"cpu_name_1183")
        self.cpu_name_1183.setFont(font1)
        self.cpu_name_1183.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_198.addWidget(self.cpu_name_1183, 6, 0, 1, 1)

        self.cpuusage_64 = QLabel(self.frame_197)
        self.cpuusage_64.setObjectName(u"cpuusage_64")
        self.cpuusage_64.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_64.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_64.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_198.addWidget(self.cpuusage_64, 3, 1, 1, 1)

        self.cpu_name_1184 = QLabel(self.frame_197)
        self.cpu_name_1184.setObjectName(u"cpu_name_1184")
        self.cpu_name_1184.setFont(font)
        self.cpu_name_1184.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_198.addWidget(self.cpu_name_1184, 3, 2, 1, 1)

        self.gpu0usage_64 = QLabel(self.frame_197)
        self.gpu0usage_64.setObjectName(u"gpu0usage_64")
        self.gpu0usage_64.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_64.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_64.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_198.addWidget(self.gpu0usage_64, 3, 4, 1, 1)

        self.cpu_name_1185 = QLabel(self.frame_197)
        self.cpu_name_1185.setObjectName(u"cpu_name_1185")
        self.cpu_name_1185.setFont(font1)
        self.cpu_name_1185.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_198.addWidget(self.cpu_name_1185, 3, 3, 1, 1)

        self.cpu_name_1186 = QLabel(self.frame_197)
        self.cpu_name_1186.setObjectName(u"cpu_name_1186")
        self.cpu_name_1186.setFont(font1)
        self.cpu_name_1186.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_198.addWidget(self.cpu_name_1186, 3, 0, 1, 1)

        self.cpu_name_1187 = QLabel(self.frame_197)
        self.cpu_name_1187.setObjectName(u"cpu_name_1187")
        self.cpu_name_1187.setFont(font)
        self.cpu_name_1187.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_198.addWidget(self.cpu_name_1187, 8, 2, 1, 1)

        self.cpu_name_1188 = QLabel(self.frame_197)
        self.cpu_name_1188.setObjectName(u"cpu_name_1188")
        self.cpu_name_1188.setFont(font)
        self.cpu_name_1188.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_198.addWidget(self.cpu_name_1188, 6, 2, 1, 1)

        self.cpu_name_1189 = QLabel(self.frame_197)
        self.cpu_name_1189.setObjectName(u"cpu_name_1189")
        self.cpu_name_1189.setFont(font1)
        self.cpu_name_1189.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_198.addWidget(self.cpu_name_1189, 8, 3, 1, 1)

        self.cpu_name_1190 = QLabel(self.frame_197)
        self.cpu_name_1190.setObjectName(u"cpu_name_1190")
        self.cpu_name_1190.setFont(font)
        self.cpu_name_1190.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_198.addWidget(self.cpu_name_1190, 8, 5, 1, 1)

        self.gpu3usage_64 = QLabel(self.frame_197)
        self.gpu3usage_64.setObjectName(u"gpu3usage_64")
        self.gpu3usage_64.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_64.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_64.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_198.addWidget(self.gpu3usage_64, 8, 1, 1, 1)

        self.cpu_name_1191 = QLabel(self.frame_197)
        self.cpu_name_1191.setObjectName(u"cpu_name_1191")
        self.cpu_name_1191.setFont(font1)
        self.cpu_name_1191.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_198.addWidget(self.cpu_name_1191, 8, 0, 1, 1)

        self.device1_64 = QLabel(self.frame_197)
        self.device1_64.setObjectName(u"device1_64")
        self.device1_64.setFont(font2)
        self.device1_64.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_64.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_64.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_198.addWidget(self.device1_64, 1, 0, 1, 1)

        self.clientipaddress_64 = QLabel(self.frame_197)
        self.clientipaddress_64.setObjectName(u"clientipaddress_64")
        self.clientipaddress_64.setFont(font)
        self.clientipaddress_64.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_64.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_64.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_198.addWidget(self.clientipaddress_64, 1, 1, 1, 5)

        self.gpu1usage_64 = QLabel(self.frame_197)
        self.gpu1usage_64.setObjectName(u"gpu1usage_64")
        self.gpu1usage_64.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_64.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_64.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_198.addWidget(self.gpu1usage_64, 6, 1, 1, 1)

        self.memoryusage_64 = QLabel(self.frame_197)
        self.memoryusage_64.setObjectName(u"memoryusage_64")
        self.memoryusage_64.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_64.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_64.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_198.addWidget(self.memoryusage_64, 8, 4, 1, 1)

        self.cpu_name_1192 = QLabel(self.frame_197)
        self.cpu_name_1192.setObjectName(u"cpu_name_1192")
        self.cpu_name_1192.setFont(font1)
        self.cpu_name_1192.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_198.addWidget(self.cpu_name_1192, 6, 3, 1, 1)


        self.gridLayout_197.addWidget(self.frame_197, 0, 0, 1, 3)

        self.elapsedtime_64 = QLabel(self.frame_196)
        self.elapsedtime_64.setObjectName(u"elapsedtime_64")
        self.elapsedtime_64.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_64.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_64.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_197.addWidget(self.elapsedtime_64, 1, 2, 1, 1)

        self.off_Button_64 = QPushButton(self.frame_196)
        self.off_Button_64.setObjectName(u"off_Button_64")
        self.off_Button_64.setEnabled(True)
        self.off_Button_64.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_197.addWidget(self.off_Button_64, 1, 1, 1, 1)


        self.horizontalLayout_24.addWidget(self.frame_196)


        self.verticalLayout_3.addWidget(self.frame_30)

        self.frame_31 = QFrame(self.frame_2)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.frame_198 = QFrame(self.frame_31)
        self.frame_198.setObjectName(u"frame_198")
        self.frame_198.setMinimumSize(QSize(240, 200))
        self.frame_198.setMaximumSize(QSize(240, 200))
        self.frame_198.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_198.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_198.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_198.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_199 = QGridLayout(self.frame_198)
        self.gridLayout_199.setObjectName(u"gridLayout_199")
        self.on_Button_65 = QPushButton(self.frame_198)
        self.on_Button_65.setObjectName(u"on_Button_65")
        self.on_Button_65.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_199.addWidget(self.on_Button_65, 1, 0, 1, 1)

        self.frame_199 = QFrame(self.frame_198)
        self.frame_199.setObjectName(u"frame_199")
        self.frame_199.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_199.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_199.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_200 = QGridLayout(self.frame_199)
        self.gridLayout_200.setObjectName(u"gridLayout_200")
        self.gpu2usage_65 = QLabel(self.frame_199)
        self.gpu2usage_65.setObjectName(u"gpu2usage_65")
        self.gpu2usage_65.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_65.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_65.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_200.addWidget(self.gpu2usage_65, 6, 4, 1, 1)

        self.cpu_name_1193 = QLabel(self.frame_199)
        self.cpu_name_1193.setObjectName(u"cpu_name_1193")
        self.cpu_name_1193.setFont(font)
        self.cpu_name_1193.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_200.addWidget(self.cpu_name_1193, 3, 5, 1, 1)

        self.cpu_name_1194 = QLabel(self.frame_199)
        self.cpu_name_1194.setObjectName(u"cpu_name_1194")
        self.cpu_name_1194.setFont(font)
        self.cpu_name_1194.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_200.addWidget(self.cpu_name_1194, 6, 5, 1, 1)

        self.cpu_name_1195 = QLabel(self.frame_199)
        self.cpu_name_1195.setObjectName(u"cpu_name_1195")
        self.cpu_name_1195.setFont(font1)
        self.cpu_name_1195.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_200.addWidget(self.cpu_name_1195, 6, 0, 1, 1)

        self.cpuusage_65 = QLabel(self.frame_199)
        self.cpuusage_65.setObjectName(u"cpuusage_65")
        self.cpuusage_65.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_65.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_65.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_200.addWidget(self.cpuusage_65, 3, 1, 1, 1)

        self.cpu_name_1196 = QLabel(self.frame_199)
        self.cpu_name_1196.setObjectName(u"cpu_name_1196")
        self.cpu_name_1196.setFont(font)
        self.cpu_name_1196.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_200.addWidget(self.cpu_name_1196, 3, 2, 1, 1)

        self.gpu0usage_65 = QLabel(self.frame_199)
        self.gpu0usage_65.setObjectName(u"gpu0usage_65")
        self.gpu0usage_65.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_65.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_65.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_200.addWidget(self.gpu0usage_65, 3, 4, 1, 1)

        self.cpu_name_1197 = QLabel(self.frame_199)
        self.cpu_name_1197.setObjectName(u"cpu_name_1197")
        self.cpu_name_1197.setFont(font1)
        self.cpu_name_1197.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_200.addWidget(self.cpu_name_1197, 3, 3, 1, 1)

        self.cpu_name_1198 = QLabel(self.frame_199)
        self.cpu_name_1198.setObjectName(u"cpu_name_1198")
        self.cpu_name_1198.setFont(font1)
        self.cpu_name_1198.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_200.addWidget(self.cpu_name_1198, 3, 0, 1, 1)

        self.cpu_name_1199 = QLabel(self.frame_199)
        self.cpu_name_1199.setObjectName(u"cpu_name_1199")
        self.cpu_name_1199.setFont(font)
        self.cpu_name_1199.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_200.addWidget(self.cpu_name_1199, 8, 2, 1, 1)

        self.cpu_name_1200 = QLabel(self.frame_199)
        self.cpu_name_1200.setObjectName(u"cpu_name_1200")
        self.cpu_name_1200.setFont(font)
        self.cpu_name_1200.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_200.addWidget(self.cpu_name_1200, 6, 2, 1, 1)

        self.cpu_name_1201 = QLabel(self.frame_199)
        self.cpu_name_1201.setObjectName(u"cpu_name_1201")
        self.cpu_name_1201.setFont(font1)
        self.cpu_name_1201.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_200.addWidget(self.cpu_name_1201, 8, 3, 1, 1)

        self.cpu_name_1202 = QLabel(self.frame_199)
        self.cpu_name_1202.setObjectName(u"cpu_name_1202")
        self.cpu_name_1202.setFont(font)
        self.cpu_name_1202.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_200.addWidget(self.cpu_name_1202, 8, 5, 1, 1)

        self.gpu3usage_65 = QLabel(self.frame_199)
        self.gpu3usage_65.setObjectName(u"gpu3usage_65")
        self.gpu3usage_65.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_65.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_65.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_200.addWidget(self.gpu3usage_65, 8, 1, 1, 1)

        self.cpu_name_1203 = QLabel(self.frame_199)
        self.cpu_name_1203.setObjectName(u"cpu_name_1203")
        self.cpu_name_1203.setFont(font1)
        self.cpu_name_1203.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_200.addWidget(self.cpu_name_1203, 8, 0, 1, 1)

        self.device1_65 = QLabel(self.frame_199)
        self.device1_65.setObjectName(u"device1_65")
        self.device1_65.setFont(font2)
        self.device1_65.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_65.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_65.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_200.addWidget(self.device1_65, 1, 0, 1, 1)

        self.clientipaddress_65 = QLabel(self.frame_199)
        self.clientipaddress_65.setObjectName(u"clientipaddress_65")
        self.clientipaddress_65.setFont(font)
        self.clientipaddress_65.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_65.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_65.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_200.addWidget(self.clientipaddress_65, 1, 1, 1, 5)

        self.gpu1usage_65 = QLabel(self.frame_199)
        self.gpu1usage_65.setObjectName(u"gpu1usage_65")
        self.gpu1usage_65.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_65.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_65.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_200.addWidget(self.gpu1usage_65, 6, 1, 1, 1)

        self.memoryusage_65 = QLabel(self.frame_199)
        self.memoryusage_65.setObjectName(u"memoryusage_65")
        self.memoryusage_65.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_65.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_65.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_200.addWidget(self.memoryusage_65, 8, 4, 1, 1)

        self.cpu_name_1204 = QLabel(self.frame_199)
        self.cpu_name_1204.setObjectName(u"cpu_name_1204")
        self.cpu_name_1204.setFont(font1)
        self.cpu_name_1204.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_200.addWidget(self.cpu_name_1204, 6, 3, 1, 1)


        self.gridLayout_199.addWidget(self.frame_199, 0, 0, 1, 3)

        self.elapsedtime_65 = QLabel(self.frame_198)
        self.elapsedtime_65.setObjectName(u"elapsedtime_65")
        self.elapsedtime_65.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_65.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_65.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_199.addWidget(self.elapsedtime_65, 1, 2, 1, 1)

        self.off_Button_65 = QPushButton(self.frame_198)
        self.off_Button_65.setObjectName(u"off_Button_65")
        self.off_Button_65.setEnabled(True)
        self.off_Button_65.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_199.addWidget(self.off_Button_65, 1, 1, 1, 1)


        self.horizontalLayout_25.addWidget(self.frame_198)

        self.frame_200 = QFrame(self.frame_31)
        self.frame_200.setObjectName(u"frame_200")
        self.frame_200.setMinimumSize(QSize(240, 200))
        self.frame_200.setMaximumSize(QSize(240, 200))
        self.frame_200.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_200.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_200.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_200.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_201 = QGridLayout(self.frame_200)
        self.gridLayout_201.setObjectName(u"gridLayout_201")
        self.on_Button_66 = QPushButton(self.frame_200)
        self.on_Button_66.setObjectName(u"on_Button_66")
        self.on_Button_66.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_201.addWidget(self.on_Button_66, 1, 0, 1, 1)

        self.frame_201 = QFrame(self.frame_200)
        self.frame_201.setObjectName(u"frame_201")
        self.frame_201.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_201.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_201.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_202 = QGridLayout(self.frame_201)
        self.gridLayout_202.setObjectName(u"gridLayout_202")
        self.gpu2usage_66 = QLabel(self.frame_201)
        self.gpu2usage_66.setObjectName(u"gpu2usage_66")
        self.gpu2usage_66.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_66.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_66.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_202.addWidget(self.gpu2usage_66, 6, 4, 1, 1)

        self.cpu_name_1205 = QLabel(self.frame_201)
        self.cpu_name_1205.setObjectName(u"cpu_name_1205")
        self.cpu_name_1205.setFont(font)
        self.cpu_name_1205.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_202.addWidget(self.cpu_name_1205, 3, 5, 1, 1)

        self.cpu_name_1206 = QLabel(self.frame_201)
        self.cpu_name_1206.setObjectName(u"cpu_name_1206")
        self.cpu_name_1206.setFont(font)
        self.cpu_name_1206.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_202.addWidget(self.cpu_name_1206, 6, 5, 1, 1)

        self.cpu_name_1207 = QLabel(self.frame_201)
        self.cpu_name_1207.setObjectName(u"cpu_name_1207")
        self.cpu_name_1207.setFont(font1)
        self.cpu_name_1207.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_202.addWidget(self.cpu_name_1207, 6, 0, 1, 1)

        self.cpuusage_66 = QLabel(self.frame_201)
        self.cpuusage_66.setObjectName(u"cpuusage_66")
        self.cpuusage_66.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_66.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_66.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_202.addWidget(self.cpuusage_66, 3, 1, 1, 1)

        self.cpu_name_1208 = QLabel(self.frame_201)
        self.cpu_name_1208.setObjectName(u"cpu_name_1208")
        self.cpu_name_1208.setFont(font)
        self.cpu_name_1208.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_202.addWidget(self.cpu_name_1208, 3, 2, 1, 1)

        self.gpu0usage_66 = QLabel(self.frame_201)
        self.gpu0usage_66.setObjectName(u"gpu0usage_66")
        self.gpu0usage_66.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_66.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_66.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_202.addWidget(self.gpu0usage_66, 3, 4, 1, 1)

        self.cpu_name_1209 = QLabel(self.frame_201)
        self.cpu_name_1209.setObjectName(u"cpu_name_1209")
        self.cpu_name_1209.setFont(font1)
        self.cpu_name_1209.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_202.addWidget(self.cpu_name_1209, 3, 3, 1, 1)

        self.cpu_name_1210 = QLabel(self.frame_201)
        self.cpu_name_1210.setObjectName(u"cpu_name_1210")
        self.cpu_name_1210.setFont(font1)
        self.cpu_name_1210.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_202.addWidget(self.cpu_name_1210, 3, 0, 1, 1)

        self.cpu_name_1211 = QLabel(self.frame_201)
        self.cpu_name_1211.setObjectName(u"cpu_name_1211")
        self.cpu_name_1211.setFont(font)
        self.cpu_name_1211.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_202.addWidget(self.cpu_name_1211, 8, 2, 1, 1)

        self.cpu_name_1212 = QLabel(self.frame_201)
        self.cpu_name_1212.setObjectName(u"cpu_name_1212")
        self.cpu_name_1212.setFont(font)
        self.cpu_name_1212.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_202.addWidget(self.cpu_name_1212, 6, 2, 1, 1)

        self.cpu_name_1213 = QLabel(self.frame_201)
        self.cpu_name_1213.setObjectName(u"cpu_name_1213")
        self.cpu_name_1213.setFont(font1)
        self.cpu_name_1213.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_202.addWidget(self.cpu_name_1213, 8, 3, 1, 1)

        self.cpu_name_1214 = QLabel(self.frame_201)
        self.cpu_name_1214.setObjectName(u"cpu_name_1214")
        self.cpu_name_1214.setFont(font)
        self.cpu_name_1214.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_202.addWidget(self.cpu_name_1214, 8, 5, 1, 1)

        self.gpu3usage_66 = QLabel(self.frame_201)
        self.gpu3usage_66.setObjectName(u"gpu3usage_66")
        self.gpu3usage_66.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_66.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_66.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_202.addWidget(self.gpu3usage_66, 8, 1, 1, 1)

        self.cpu_name_1215 = QLabel(self.frame_201)
        self.cpu_name_1215.setObjectName(u"cpu_name_1215")
        self.cpu_name_1215.setFont(font1)
        self.cpu_name_1215.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_202.addWidget(self.cpu_name_1215, 8, 0, 1, 1)

        self.device1_66 = QLabel(self.frame_201)
        self.device1_66.setObjectName(u"device1_66")
        self.device1_66.setFont(font2)
        self.device1_66.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_66.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_66.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_202.addWidget(self.device1_66, 1, 0, 1, 1)

        self.clientipaddress_66 = QLabel(self.frame_201)
        self.clientipaddress_66.setObjectName(u"clientipaddress_66")
        self.clientipaddress_66.setFont(font)
        self.clientipaddress_66.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_66.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_66.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_202.addWidget(self.clientipaddress_66, 1, 1, 1, 5)

        self.gpu1usage_66 = QLabel(self.frame_201)
        self.gpu1usage_66.setObjectName(u"gpu1usage_66")
        self.gpu1usage_66.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_66.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_66.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_202.addWidget(self.gpu1usage_66, 6, 1, 1, 1)

        self.memoryusage_66 = QLabel(self.frame_201)
        self.memoryusage_66.setObjectName(u"memoryusage_66")
        self.memoryusage_66.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_66.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_66.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_202.addWidget(self.memoryusage_66, 8, 4, 1, 1)

        self.cpu_name_1216 = QLabel(self.frame_201)
        self.cpu_name_1216.setObjectName(u"cpu_name_1216")
        self.cpu_name_1216.setFont(font1)
        self.cpu_name_1216.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_202.addWidget(self.cpu_name_1216, 6, 3, 1, 1)


        self.gridLayout_201.addWidget(self.frame_201, 0, 0, 1, 3)

        self.elapsedtime_66 = QLabel(self.frame_200)
        self.elapsedtime_66.setObjectName(u"elapsedtime_66")
        self.elapsedtime_66.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_66.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_66.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_201.addWidget(self.elapsedtime_66, 1, 2, 1, 1)

        self.off_Button_66 = QPushButton(self.frame_200)
        self.off_Button_66.setObjectName(u"off_Button_66")
        self.off_Button_66.setEnabled(True)
        self.off_Button_66.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_201.addWidget(self.off_Button_66, 1, 1, 1, 1)


        self.horizontalLayout_25.addWidget(self.frame_200)

        self.frame_202 = QFrame(self.frame_31)
        self.frame_202.setObjectName(u"frame_202")
        self.frame_202.setMinimumSize(QSize(240, 200))
        self.frame_202.setMaximumSize(QSize(240, 200))
        self.frame_202.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_202.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_202.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_202.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_203 = QGridLayout(self.frame_202)
        self.gridLayout_203.setObjectName(u"gridLayout_203")
        self.on_Button_67 = QPushButton(self.frame_202)
        self.on_Button_67.setObjectName(u"on_Button_67")
        self.on_Button_67.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_203.addWidget(self.on_Button_67, 1, 0, 1, 1)

        self.frame_203 = QFrame(self.frame_202)
        self.frame_203.setObjectName(u"frame_203")
        self.frame_203.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_203.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_203.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_204 = QGridLayout(self.frame_203)
        self.gridLayout_204.setObjectName(u"gridLayout_204")
        self.gpu2usage_67 = QLabel(self.frame_203)
        self.gpu2usage_67.setObjectName(u"gpu2usage_67")
        self.gpu2usage_67.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_67.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_67.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_204.addWidget(self.gpu2usage_67, 6, 4, 1, 1)

        self.cpu_name_1217 = QLabel(self.frame_203)
        self.cpu_name_1217.setObjectName(u"cpu_name_1217")
        self.cpu_name_1217.setFont(font)
        self.cpu_name_1217.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_204.addWidget(self.cpu_name_1217, 3, 5, 1, 1)

        self.cpu_name_1218 = QLabel(self.frame_203)
        self.cpu_name_1218.setObjectName(u"cpu_name_1218")
        self.cpu_name_1218.setFont(font)
        self.cpu_name_1218.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_204.addWidget(self.cpu_name_1218, 6, 5, 1, 1)

        self.cpu_name_1219 = QLabel(self.frame_203)
        self.cpu_name_1219.setObjectName(u"cpu_name_1219")
        self.cpu_name_1219.setFont(font1)
        self.cpu_name_1219.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_204.addWidget(self.cpu_name_1219, 6, 0, 1, 1)

        self.cpuusage_67 = QLabel(self.frame_203)
        self.cpuusage_67.setObjectName(u"cpuusage_67")
        self.cpuusage_67.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_67.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_67.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_204.addWidget(self.cpuusage_67, 3, 1, 1, 1)

        self.cpu_name_1220 = QLabel(self.frame_203)
        self.cpu_name_1220.setObjectName(u"cpu_name_1220")
        self.cpu_name_1220.setFont(font)
        self.cpu_name_1220.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_204.addWidget(self.cpu_name_1220, 3, 2, 1, 1)

        self.gpu0usage_67 = QLabel(self.frame_203)
        self.gpu0usage_67.setObjectName(u"gpu0usage_67")
        self.gpu0usage_67.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_67.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_67.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_204.addWidget(self.gpu0usage_67, 3, 4, 1, 1)

        self.cpu_name_1221 = QLabel(self.frame_203)
        self.cpu_name_1221.setObjectName(u"cpu_name_1221")
        self.cpu_name_1221.setFont(font1)
        self.cpu_name_1221.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_204.addWidget(self.cpu_name_1221, 3, 3, 1, 1)

        self.cpu_name_1222 = QLabel(self.frame_203)
        self.cpu_name_1222.setObjectName(u"cpu_name_1222")
        self.cpu_name_1222.setFont(font1)
        self.cpu_name_1222.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_204.addWidget(self.cpu_name_1222, 3, 0, 1, 1)

        self.cpu_name_1223 = QLabel(self.frame_203)
        self.cpu_name_1223.setObjectName(u"cpu_name_1223")
        self.cpu_name_1223.setFont(font)
        self.cpu_name_1223.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_204.addWidget(self.cpu_name_1223, 8, 2, 1, 1)

        self.cpu_name_1224 = QLabel(self.frame_203)
        self.cpu_name_1224.setObjectName(u"cpu_name_1224")
        self.cpu_name_1224.setFont(font)
        self.cpu_name_1224.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_204.addWidget(self.cpu_name_1224, 6, 2, 1, 1)

        self.cpu_name_1225 = QLabel(self.frame_203)
        self.cpu_name_1225.setObjectName(u"cpu_name_1225")
        self.cpu_name_1225.setFont(font1)
        self.cpu_name_1225.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_204.addWidget(self.cpu_name_1225, 8, 3, 1, 1)

        self.cpu_name_1226 = QLabel(self.frame_203)
        self.cpu_name_1226.setObjectName(u"cpu_name_1226")
        self.cpu_name_1226.setFont(font)
        self.cpu_name_1226.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_204.addWidget(self.cpu_name_1226, 8, 5, 1, 1)

        self.gpu3usage_67 = QLabel(self.frame_203)
        self.gpu3usage_67.setObjectName(u"gpu3usage_67")
        self.gpu3usage_67.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_67.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_67.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_204.addWidget(self.gpu3usage_67, 8, 1, 1, 1)

        self.cpu_name_1227 = QLabel(self.frame_203)
        self.cpu_name_1227.setObjectName(u"cpu_name_1227")
        self.cpu_name_1227.setFont(font1)
        self.cpu_name_1227.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_204.addWidget(self.cpu_name_1227, 8, 0, 1, 1)

        self.device1_67 = QLabel(self.frame_203)
        self.device1_67.setObjectName(u"device1_67")
        self.device1_67.setFont(font2)
        self.device1_67.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_67.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_67.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_204.addWidget(self.device1_67, 1, 0, 1, 1)

        self.clientipaddress_67 = QLabel(self.frame_203)
        self.clientipaddress_67.setObjectName(u"clientipaddress_67")
        self.clientipaddress_67.setFont(font)
        self.clientipaddress_67.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_67.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_67.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_204.addWidget(self.clientipaddress_67, 1, 1, 1, 5)

        self.gpu1usage_67 = QLabel(self.frame_203)
        self.gpu1usage_67.setObjectName(u"gpu1usage_67")
        self.gpu1usage_67.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_67.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_67.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_204.addWidget(self.gpu1usage_67, 6, 1, 1, 1)

        self.memoryusage_67 = QLabel(self.frame_203)
        self.memoryusage_67.setObjectName(u"memoryusage_67")
        self.memoryusage_67.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_67.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_67.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_204.addWidget(self.memoryusage_67, 8, 4, 1, 1)

        self.cpu_name_1228 = QLabel(self.frame_203)
        self.cpu_name_1228.setObjectName(u"cpu_name_1228")
        self.cpu_name_1228.setFont(font1)
        self.cpu_name_1228.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_204.addWidget(self.cpu_name_1228, 6, 3, 1, 1)


        self.gridLayout_203.addWidget(self.frame_203, 0, 0, 1, 3)

        self.elapsedtime_67 = QLabel(self.frame_202)
        self.elapsedtime_67.setObjectName(u"elapsedtime_67")
        self.elapsedtime_67.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_67.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_67.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_203.addWidget(self.elapsedtime_67, 1, 2, 1, 1)

        self.off_Button_67 = QPushButton(self.frame_202)
        self.off_Button_67.setObjectName(u"off_Button_67")
        self.off_Button_67.setEnabled(True)
        self.off_Button_67.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_203.addWidget(self.off_Button_67, 1, 1, 1, 1)


        self.horizontalLayout_25.addWidget(self.frame_202)

        self.frame_204 = QFrame(self.frame_31)
        self.frame_204.setObjectName(u"frame_204")
        self.frame_204.setMinimumSize(QSize(240, 200))
        self.frame_204.setMaximumSize(QSize(240, 200))
        self.frame_204.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_204.setStyleSheet(u"background-color:rgb(166, 166, 166);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.frame_204.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_204.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_205 = QGridLayout(self.frame_204)
        self.gridLayout_205.setObjectName(u"gridLayout_205")
        self.on_Button_68 = QPushButton(self.frame_204)
        self.on_Button_68.setObjectName(u"on_Button_68")
        self.on_Button_68.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(255, 0, 0)")

        self.gridLayout_205.addWidget(self.on_Button_68, 1, 0, 1, 1)

        self.frame_205 = QFrame(self.frame_204)
        self.frame_205.setObjectName(u"frame_205")
        self.frame_205.setStyleSheet(u"background-color:rgb(100, 100, 100);\n"
"border-style:solid;\n"
"border-radius: 10px;")
        self.frame_205.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_205.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_206 = QGridLayout(self.frame_205)
        self.gridLayout_206.setObjectName(u"gridLayout_206")
        self.gpu2usage_68 = QLabel(self.frame_205)
        self.gpu2usage_68.setObjectName(u"gpu2usage_68")
        self.gpu2usage_68.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu2usage_68.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu2usage_68.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_206.addWidget(self.gpu2usage_68, 6, 4, 1, 1)

        self.cpu_name_1229 = QLabel(self.frame_205)
        self.cpu_name_1229.setObjectName(u"cpu_name_1229")
        self.cpu_name_1229.setFont(font)
        self.cpu_name_1229.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_206.addWidget(self.cpu_name_1229, 3, 5, 1, 1)

        self.cpu_name_1230 = QLabel(self.frame_205)
        self.cpu_name_1230.setObjectName(u"cpu_name_1230")
        self.cpu_name_1230.setFont(font)
        self.cpu_name_1230.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_206.addWidget(self.cpu_name_1230, 6, 5, 1, 1)

        self.cpu_name_1231 = QLabel(self.frame_205)
        self.cpu_name_1231.setObjectName(u"cpu_name_1231")
        self.cpu_name_1231.setFont(font1)
        self.cpu_name_1231.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_206.addWidget(self.cpu_name_1231, 6, 0, 1, 1)

        self.cpuusage_68 = QLabel(self.frame_205)
        self.cpuusage_68.setObjectName(u"cpuusage_68")
        self.cpuusage_68.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cpuusage_68.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.cpuusage_68.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_206.addWidget(self.cpuusage_68, 3, 1, 1, 1)

        self.cpu_name_1232 = QLabel(self.frame_205)
        self.cpu_name_1232.setObjectName(u"cpu_name_1232")
        self.cpu_name_1232.setFont(font)
        self.cpu_name_1232.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_206.addWidget(self.cpu_name_1232, 3, 2, 1, 1)

        self.gpu0usage_68 = QLabel(self.frame_205)
        self.gpu0usage_68.setObjectName(u"gpu0usage_68")
        self.gpu0usage_68.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu0usage_68.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu0usage_68.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_206.addWidget(self.gpu0usage_68, 3, 4, 1, 1)

        self.cpu_name_1233 = QLabel(self.frame_205)
        self.cpu_name_1233.setObjectName(u"cpu_name_1233")
        self.cpu_name_1233.setFont(font1)
        self.cpu_name_1233.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_206.addWidget(self.cpu_name_1233, 3, 3, 1, 1)

        self.cpu_name_1234 = QLabel(self.frame_205)
        self.cpu_name_1234.setObjectName(u"cpu_name_1234")
        self.cpu_name_1234.setFont(font1)
        self.cpu_name_1234.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_206.addWidget(self.cpu_name_1234, 3, 0, 1, 1)

        self.cpu_name_1235 = QLabel(self.frame_205)
        self.cpu_name_1235.setObjectName(u"cpu_name_1235")
        self.cpu_name_1235.setFont(font)
        self.cpu_name_1235.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_206.addWidget(self.cpu_name_1235, 8, 2, 1, 1)

        self.cpu_name_1236 = QLabel(self.frame_205)
        self.cpu_name_1236.setObjectName(u"cpu_name_1236")
        self.cpu_name_1236.setFont(font)
        self.cpu_name_1236.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_206.addWidget(self.cpu_name_1236, 6, 2, 1, 1)

        self.cpu_name_1237 = QLabel(self.frame_205)
        self.cpu_name_1237.setObjectName(u"cpu_name_1237")
        self.cpu_name_1237.setFont(font1)
        self.cpu_name_1237.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_206.addWidget(self.cpu_name_1237, 8, 3, 1, 1)

        self.cpu_name_1238 = QLabel(self.frame_205)
        self.cpu_name_1238.setObjectName(u"cpu_name_1238")
        self.cpu_name_1238.setFont(font)
        self.cpu_name_1238.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(186, 186, 186);")

        self.gridLayout_206.addWidget(self.cpu_name_1238, 8, 5, 1, 1)

        self.gpu3usage_68 = QLabel(self.frame_205)
        self.gpu3usage_68.setObjectName(u"gpu3usage_68")
        self.gpu3usage_68.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu3usage_68.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu3usage_68.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_206.addWidget(self.gpu3usage_68, 8, 1, 1, 1)

        self.cpu_name_1239 = QLabel(self.frame_205)
        self.cpu_name_1239.setObjectName(u"cpu_name_1239")
        self.cpu_name_1239.setFont(font1)
        self.cpu_name_1239.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_206.addWidget(self.cpu_name_1239, 8, 0, 1, 1)

        self.device1_68 = QLabel(self.frame_205)
        self.device1_68.setObjectName(u"device1_68")
        self.device1_68.setFont(font2)
        self.device1_68.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.device1_68.setStyleSheet(u"font: 700 8pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.device1_68.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_206.addWidget(self.device1_68, 1, 0, 1, 1)

        self.clientipaddress_68 = QLabel(self.frame_205)
        self.clientipaddress_68.setObjectName(u"clientipaddress_68")
        self.clientipaddress_68.setFont(font)
        self.clientipaddress_68.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.clientipaddress_68.setStyleSheet(u"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.clientipaddress_68.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_206.addWidget(self.clientipaddress_68, 1, 1, 1, 5)

        self.gpu1usage_68 = QLabel(self.frame_205)
        self.gpu1usage_68.setObjectName(u"gpu1usage_68")
        self.gpu1usage_68.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gpu1usage_68.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.gpu1usage_68.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_206.addWidget(self.gpu1usage_68, 6, 1, 1, 1)

        self.memoryusage_68 = QLabel(self.frame_205)
        self.memoryusage_68.setObjectName(u"memoryusage_68")
        self.memoryusage_68.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.memoryusage_68.setStyleSheet(u"font: 700 15pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.memoryusage_68.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_206.addWidget(self.memoryusage_68, 8, 4, 1, 1)

        self.cpu_name_1240 = QLabel(self.frame_205)
        self.cpu_name_1240.setObjectName(u"cpu_name_1240")
        self.cpu_name_1240.setFont(font1)
        self.cpu_name_1240.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_206.addWidget(self.cpu_name_1240, 6, 3, 1, 1)


        self.gridLayout_205.addWidget(self.frame_205, 0, 0, 1, 3)

        self.elapsedtime_68 = QLabel(self.frame_204)
        self.elapsedtime_68.setObjectName(u"elapsedtime_68")
        self.elapsedtime_68.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.elapsedtime_68.setStyleSheet(u"font: 700 10pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-style:solid;\n"
"border-radius: 5px;")
        self.elapsedtime_68.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_205.addWidget(self.elapsedtime_68, 1, 2, 1, 1)

        self.off_Button_68 = QPushButton(self.frame_204)
        self.off_Button_68.setObjectName(u"off_Button_68")
        self.off_Button_68.setEnabled(True)
        self.off_Button_68.setStyleSheet(u"font: 700 7pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color:rgb(238, 238, 238);\n"
"color:rgb(0, 0, 255)")

        self.gridLayout_205.addWidget(self.off_Button_68, 1, 1, 1, 1)


        self.horizontalLayout_25.addWidget(self.frame_204)


        self.verticalLayout_3.addWidget(self.frame_31)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.on_Button_1.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_425.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_426.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_427.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_428.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_429.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_430.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_431.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_432.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_433.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_434.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_435.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_1.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_1.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_436.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_1.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_1.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_2.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_437.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_438.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_439.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_440.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_441.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_442.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_443.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_444.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_445.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_446.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_447.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_2.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_2.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_448.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_2.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_2.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_3.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_449.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_450.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_451.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_452.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_453.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_454.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_455.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_456.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_457.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_458.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_459.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_3.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_3.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_460.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_3.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_3.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_4.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_461.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_462.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_463.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_464.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_465.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_466.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_467.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_468.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_469.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_470.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_471.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_4.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_4.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_472.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_4.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_4.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_5.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_473.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_474.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_475.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_476.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_477.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_478.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_479.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_480.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_481.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_482.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_483.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_5.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_5.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_484.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_5.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_5.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_6.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_485.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_486.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_487.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_488.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_489.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_490.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_491.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_492.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_493.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_494.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_495.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_6.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_6.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_496.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_6.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_6.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_7.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_7.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_497.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_498.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_499.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_7.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_500.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_7.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_501.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_502.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_503.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_504.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_505.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_506.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_7.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_507.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_7.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_7.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_7.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_7.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_508.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_7.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_7.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_8.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_8.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_509.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_510.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_511.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_8.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_512.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_8.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_513.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_514.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_515.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_516.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_517.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_518.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_8.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_519.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_8.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_8.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_8.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_8.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_520.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_8.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_8.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_9.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_9.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_521.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_522.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_523.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_9.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_524.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_9.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_525.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_526.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_527.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_528.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_529.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_530.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_9.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_531.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_9.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_9.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_9.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_9.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_532.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_9.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_9.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_10.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_10.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_533.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_534.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_535.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_10.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_536.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_10.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_537.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_538.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_539.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_540.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_541.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_542.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_10.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_543.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_10.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_10.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_10.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_10.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_544.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_10.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_10.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_11.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_11.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_545.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_546.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_547.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_11.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_548.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_11.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_549.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_550.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_551.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_552.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_553.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_554.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_11.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_555.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_11.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_11.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_11.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_11.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_556.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_11.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_11.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_12.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_12.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_557.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_558.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_559.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_12.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_560.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_12.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_561.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_562.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_563.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_564.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_565.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_566.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_12.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_567.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_12.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_12.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_12.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_12.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_568.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_12.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_12.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_13.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_13.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_569.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_570.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_571.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_13.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_572.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_13.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_573.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_574.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_575.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_576.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_577.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_578.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_13.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_579.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_13.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_13.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_13.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_13.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_580.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_13.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_13.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_14.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_14.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_581.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_582.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_583.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_14.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_584.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_14.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_585.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_586.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_587.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_588.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_589.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_590.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_14.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_591.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_14.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_14.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_14.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_14.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_592.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_14.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_14.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_15.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu3usage_15.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_15.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_595.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpu_name_601.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_604.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.cpu_name_596.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_597.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.clientipaddress_15.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.cpu_name_603.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.gpu1usage_15.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.gpu2usage_15.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpuusage_15.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_593.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_598.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_602.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_599.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_600.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_15.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.device1_15.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.cpu_name_594.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.elapsedtime_15.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_15.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_16.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_16.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_605.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_606.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_607.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_16.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_608.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_16.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_609.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_610.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_611.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_612.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_613.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_614.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_16.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_615.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_16.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_16.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_16.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_16.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_616.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_16.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_16.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_17.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_17.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_617.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_618.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_619.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_17.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_620.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_17.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_621.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_622.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_623.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_624.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_625.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_626.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_17.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_627.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_17.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_17.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_17.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_17.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_628.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_17.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_17.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_18.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_18.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_629.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_630.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_631.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_18.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_632.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_18.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_633.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_634.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_635.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_636.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_637.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_638.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_18.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_639.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_18.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_18.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_18.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_18.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_640.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_18.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_18.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_19.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_19.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_641.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_642.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_643.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_19.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_644.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_19.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_645.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_646.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_647.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_648.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_649.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_650.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_19.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_651.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_19.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_19.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_19.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_19.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_652.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_19.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_19.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_20.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_20.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_653.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_654.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_655.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_20.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_656.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_20.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_657.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_658.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_659.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_660.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_661.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_662.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_20.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_663.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_20.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_20.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_20.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_20.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_664.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_20.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_20.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_21.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_21.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_665.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_666.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_667.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_21.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_668.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_21.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_669.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_670.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_671.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_672.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_673.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_674.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_21.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_675.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_21.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_21.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_21.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_21.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_676.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_21.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_21.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_22.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_22.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_677.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_678.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_679.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_22.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_680.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_22.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_681.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_682.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_683.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_684.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_685.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_686.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_22.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_687.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_22.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_22.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_22.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_22.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_688.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_22.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_22.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_23.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_23.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_689.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_690.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_691.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_23.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_692.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_23.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_693.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_694.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_695.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_696.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_697.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_698.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_23.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_699.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_23.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_23.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_23.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_23.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_700.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_23.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_23.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_24.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_24.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_701.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_702.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_703.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_24.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_704.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_24.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_705.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_706.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_707.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_708.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_709.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_710.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_24.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_711.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_24.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_24.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_24.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_24.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_712.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_24.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_24.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_25.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_25.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_713.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_714.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_715.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_25.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_716.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_25.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_717.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_718.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_719.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_720.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_721.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_722.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_25.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_723.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_25.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_25.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_25.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_25.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_724.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_25.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_25.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_26.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_26.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_725.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_726.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_727.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_26.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_728.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_26.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_729.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_730.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_731.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_732.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_733.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_734.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_26.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_735.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_26.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_26.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_26.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_26.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_736.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_26.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_26.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_27.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_27.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_737.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_738.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_739.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_27.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_740.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_27.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_741.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_742.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_743.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_744.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_745.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_746.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_27.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_747.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_27.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_27.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_27.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_27.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_748.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_27.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_27.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_28.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_28.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_749.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_750.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_751.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_28.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_752.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_28.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_753.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_754.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_755.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_756.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_757.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_758.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_28.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_759.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_28.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_28.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_28.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_28.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_760.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_28.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_28.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_29.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_29.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_761.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_762.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_763.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_29.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_764.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_29.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_765.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_766.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_767.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_768.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_769.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_770.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_29.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_771.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_29.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_29.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_29.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_29.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_772.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_29.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_29.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_30.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_30.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_773.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_774.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_775.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_30.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_776.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_30.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_777.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_778.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_779.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_780.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_781.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_782.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_30.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_783.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_30.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_30.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_30.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_30.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_784.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_30.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_30.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_31.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_31.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_785.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_786.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_787.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_31.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_788.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_31.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_789.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_790.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_791.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_792.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_793.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_794.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_31.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_795.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_31.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_31.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_31.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_31.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_796.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_31.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_31.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_32.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_32.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_797.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_798.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_799.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_32.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_800.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_32.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_801.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_802.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_803.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_804.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_805.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_806.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_32.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_807.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_32.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_32.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_32.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_32.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_808.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_32.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_32.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_33.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_33.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_809.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_810.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_811.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_33.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_812.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_33.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_813.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_814.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_815.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_816.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_817.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_818.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_33.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_819.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_33.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_33.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_33.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_33.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_820.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_33.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_33.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_34.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_34.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_821.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_822.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_823.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_34.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_824.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_34.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_825.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_826.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_827.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_828.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_829.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_830.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_34.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_831.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_34.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_34.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_34.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_34.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_832.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_34.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_34.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_35.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_35.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_833.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_834.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_835.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_35.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_836.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_35.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_837.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_838.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_839.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_840.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_841.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_842.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_35.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_843.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_35.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_35.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_35.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_35.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_844.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_35.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_35.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_36.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_36.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_845.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_846.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_847.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_36.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_848.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_36.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_849.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_850.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_851.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_852.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_853.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_854.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_36.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_855.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_36.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_36.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_36.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_36.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_856.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_36.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_36.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_41.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_41.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_905.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_906.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_907.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_41.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_908.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_41.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_909.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_910.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_911.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_912.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_913.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_914.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_41.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_915.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_41.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_41.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_41.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_41.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_916.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_41.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_41.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_42.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_42.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_917.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_918.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_919.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_42.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_920.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_42.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_921.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_922.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_923.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_924.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_925.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_926.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_42.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_927.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_42.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_42.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_42.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_42.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_928.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_42.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_42.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_43.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_43.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_929.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_930.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_931.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_43.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_932.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_43.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_933.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_934.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_935.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_936.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_937.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_938.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_43.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_939.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_43.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_43.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_43.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_43.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_940.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_43.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_43.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_44.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_44.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_941.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_942.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_943.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_44.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_944.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_44.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_945.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_946.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_947.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_948.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_949.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_950.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_44.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_951.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_44.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_44.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_44.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_44.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_952.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_44.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_44.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_45.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_45.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_953.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_954.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_955.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_45.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_956.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_45.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_957.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_958.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_959.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_960.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_961.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_962.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_45.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_963.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_45.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_45.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_45.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_45.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_964.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_45.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_45.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_46.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_46.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_965.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_966.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_967.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_46.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_968.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_46.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_969.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_970.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_971.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_972.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_973.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_974.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_46.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_975.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_46.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_46.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_46.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_46.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_976.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_46.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_46.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_47.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_47.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_977.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_978.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_979.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_47.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_980.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_47.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_981.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_982.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_983.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_984.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_985.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_986.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_47.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_987.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_47.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_47.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_47.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_47.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_988.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_47.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_47.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_48.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_48.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_989.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_990.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_991.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_48.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_992.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_48.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_993.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_994.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_995.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_996.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_997.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_998.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_48.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_999.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_48.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_48.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_48.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_48.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1000.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_48.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_48.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_49.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_49.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1001.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1002.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1003.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_49.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1004.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_49.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1005.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_1006.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_1007.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1008.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1009.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_1010.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_49.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1011.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_49.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_49.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_49.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_49.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1012.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_49.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_49.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_50.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_50.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1013.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1014.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1015.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_50.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1016.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_50.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1017.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_1018.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_1019.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1020.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1021.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_1022.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_50.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1023.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_50.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_50.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_50.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_50.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1024.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_50.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_50.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_51.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_51.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1025.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1026.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1027.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_51.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1028.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_51.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1029.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_1030.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_1031.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1032.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1033.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_1034.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_51.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1035.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_51.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_51.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_51.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_51.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1036.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_51.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_51.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_52.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_52.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1037.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1038.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1039.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_52.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1040.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_52.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1041.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_1042.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_1043.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1044.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1045.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_1046.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_52.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1047.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_52.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_52.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_52.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_52.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1048.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_52.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_52.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_53.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu3usage_53.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1049.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1050.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_1051.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_1052.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_1053.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.cpu_name_1054.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpu_name_1055.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu1usage_53.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.gpu0usage_53.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1056.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1057.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu2usage_53.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1058.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.cpuusage_53.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.clientipaddress_53.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.memoryusage_53.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1059.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1060.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.device1_53.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.elapsedtime_53.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_53.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_54.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_54.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1061.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1062.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1063.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_54.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1064.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_54.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1065.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_1066.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_1067.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1068.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1069.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_1070.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_54.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1071.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_54.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_54.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_54.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_54.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1072.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_54.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_54.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_55.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_55.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1073.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1074.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1075.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_55.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1076.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_55.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1077.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_1078.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_1079.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1080.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1081.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_1082.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_55.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1083.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_55.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_55.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_55.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_55.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1084.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_55.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_55.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_56.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_56.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1085.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1086.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1087.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_56.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1088.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_56.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1089.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_1090.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_1091.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1092.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1093.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_1094.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_56.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1095.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_56.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_56.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_56.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_56.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1096.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_56.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_56.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_57.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_57.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1097.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1098.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1099.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_57.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1100.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_57.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1101.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_1102.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_1103.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1104.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1105.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_1106.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_57.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1107.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_57.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_57.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_57.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_57.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1108.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_57.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_57.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_58.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_58.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1109.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1110.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1111.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_58.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1112.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_58.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1113.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_1114.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_1115.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1116.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1117.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_1118.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_58.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1119.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_58.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_58.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_58.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_58.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1120.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_58.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_58.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_59.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_59.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1121.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1122.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1123.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_59.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1124.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_59.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1125.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_1126.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_1127.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1128.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1129.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_1130.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_59.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1131.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_59.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_59.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_59.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_59.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1132.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_59.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_59.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_60.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_60.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1133.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1134.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1135.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_60.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1136.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_60.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1137.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_1138.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_1139.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1140.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1141.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_1142.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_60.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1143.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_60.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_60.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_60.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_60.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1144.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_60.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_60.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_61.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_61.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1145.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1146.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1147.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_61.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1148.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_61.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1149.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_1150.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_1151.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1152.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1153.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_1154.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_61.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1155.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_61.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_61.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_61.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_61.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1156.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_61.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_61.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_62.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_62.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1157.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1158.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1159.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_62.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1160.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_62.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1161.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_1162.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_1163.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1164.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1165.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_1166.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_62.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1167.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_62.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_62.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_62.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_62.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1168.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_62.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_62.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_63.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_63.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1169.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1170.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1171.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_63.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1172.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_63.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1173.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_1174.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_1175.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1176.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1177.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_1178.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_63.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1179.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_63.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_63.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_63.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_63.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1180.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_63.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_63.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_64.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_64.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1181.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1182.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1183.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_64.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1184.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_64.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1185.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_1186.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_1187.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1188.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1189.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_1190.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_64.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1191.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_64.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_64.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_64.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_64.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1192.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_64.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_64.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_65.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_65.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1193.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1194.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1195.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_65.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1196.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_65.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1197.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_1198.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_1199.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1200.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1201.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_1202.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_65.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1203.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_65.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_65.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_65.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_65.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1204.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_65.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_65.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_66.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_66.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1205.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1206.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1207.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_66.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1208.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_66.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1209.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_1210.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_1211.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1212.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1213.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_1214.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_66.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1215.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_66.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_66.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_66.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_66.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1216.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_66.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_66.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_67.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_67.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1217.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1218.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1219.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_67.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1220.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_67.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1221.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_1222.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_1223.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1224.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1225.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_1226.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_67.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1227.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_67.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_67.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_67.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_67.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1228.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_67.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_67.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.on_Button_68.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.gpu2usage_68.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1229.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1230.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1231.setText(QCoreApplication.translate("MainWindow", u"GPU1", None))
        self.cpuusage_68.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1232.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu0usage_68.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1233.setText(QCoreApplication.translate("MainWindow", u"GPU0", None))
        self.cpu_name_1234.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_name_1235.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1236.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.cpu_name_1237.setText(QCoreApplication.translate("MainWindow", u"MEM", None))
        self.cpu_name_1238.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.gpu3usage_68.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1239.setText(QCoreApplication.translate("MainWindow", u"GPU3", None))
        self.device1_68.setText(QCoreApplication.translate("MainWindow", u"device1", None))
        self.clientipaddress_68.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.gpu1usage_68.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.memoryusage_68.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_name_1240.setText(QCoreApplication.translate("MainWindow", u"GPU2", None))
        self.elapsedtime_68.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.off_Button_68.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
    # retranslateUi


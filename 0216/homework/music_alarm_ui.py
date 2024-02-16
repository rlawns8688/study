# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'music_alarm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

from PySide2.QtWebEngineWidgets import QWebEngineView



class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(659, 610)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.webEngineView = QWebEngineView(Form)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setGeometry(QRect(150, 250, 391, 191))
        self.webEngineView.setUrl(QUrl(u"about:blank"))
        self.pushButton__pause = QPushButton(Form)
        self.pushButton__pause.setObjectName(u"pushButton__pause")
        self.pushButton__pause.setGeometry(QRect(150, 450, 111, 23))
        self.pushButton__pause.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton__change = QPushButton(Form)
        self.pushButton__change.setObjectName(u"pushButton__change")
        self.pushButton__change.setGeometry(QRect(430, 450, 111, 23))
        self.pushButton__change.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 60, 191, 41))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"\n"
"font: 63 italic 24pt \"URW Bookman [urw]\";")
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(290, 140, 256, 91))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton__start = QPushButton(self.layoutWidget)
        self.pushButton__start.setObjectName(u"pushButton__start")
        self.pushButton__start.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.pushButton__start)

        self.pushButton__stop = QPushButton(self.layoutWidget)
        self.pushButton__stop.setObjectName(u"pushButton__stop")
        self.pushButton__stop.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.pushButton__stop)

        self.pushButton__reset = QPushButton(self.layoutWidget)
        self.pushButton__reset.setObjectName(u"pushButton__reset")
        self.pushButton__reset.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.pushButton__reset)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lcdNumber = QLCDNumber(self.layoutWidget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lcdNumber.setSmallDecimalPoint(True)
        self.lcdNumber.setDigitCount(5)
        self.lcdNumber.setMode(QLCDNumber.Dec)
        self.lcdNumber.setSegmentStyle(QLCDNumber.Filled)
        self.lcdNumber.setProperty("value", 15.000000000000000)
        self.lcdNumber.setProperty("intValue", 15)

        self.verticalLayout.addWidget(self.lcdNumber)

        self.layoutWidget1 = QWidget(Form)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(150, 130, 127, 102))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_1 = QLabel(self.layoutWidget1)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.label_1)

        self.lineEdit__URL = QLineEdit(self.layoutWidget1)
        self.lineEdit__URL.setObjectName(u"lineEdit__URL")
        self.lineEdit__URL.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.lineEdit__URL)

        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.label_2)

        self.lineEdit__timerStart = QLineEdit(self.layoutWidget1)
        self.lineEdit__timerStart.setObjectName(u"lineEdit__timerStart")
        self.lineEdit__timerStart.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.lineEdit__timerStart)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton__pause.setText(QCoreApplication.translate("Form", u"pause", None))
        self.pushButton__change.setText(QCoreApplication.translate("Form", u"change", None))
        self.label.setText(QCoreApplication.translate("Form", u"Music Alarm", None))
        self.pushButton__start.setText(QCoreApplication.translate("Form", u"Start", None))
        self.pushButton__stop.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.pushButton__reset.setText(QCoreApplication.translate("Form", u"Reset", None))
        self.label_1.setText(QCoreApplication.translate("Form", u"\ud50c\ub798\uc774 \ub9ac\uc2a4\ud2b8 URL \uc785\ub825", None))
        self.lineEdit__URL.setText(QCoreApplication.translate("Form", u"(https://youtube...)", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\uc7ac\uc0dd \ub300\uae30\uc2dc\uac04 \uc785\ub825", None))
        self.lineEdit__timerStart.setText(QCoreApplication.translate("Form", u"0:00", None))
    # retranslateUi


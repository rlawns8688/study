# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qt_timer.ui'
##
## Created by: Qt User Interface Compiler version 5.15.6
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_Form__timer(object):
    def setupUi(self, Form__timer):
        if not Form__timer.objectName():
            Form__timer.setObjectName(u"Form__timer")
        Form__timer.resize(750, 385)
        self.dial = QDial(Form__timer)
        self.dial.setObjectName(u"dial")
        self.dial.setGeometry(QRect(480, 110, 231, 271))
        self.dial.setBaseSize(QSize(30, 30))
        self.dial.setInvertedAppearance(False)
        self.dial.setInvertedControls(False)
        self.dial.setWrapping(False)
        self.dial.setNotchTarget(5.000000000000000)
        self.dial.setNotchesVisible(True)
        self.textBrowser__log = QTextBrowser(Form__timer)
        self.textBrowser__log.setObjectName(u"textBrowser__log")
        self.textBrowser__log.setGeometry(QRect(10, 270, 441, 71))
        self.label__title = QLabel(Form__timer)
        self.label__title.setObjectName(u"label__title")
        self.label__title.setGeometry(QRect(210, 10, 281, 31))
        font = QFont()
        font.setFamily(u"Source Code Pro Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label__title.setFont(font)
        self.label__title.setLayoutDirection(Qt.LeftToRight)
        self.label__title.setAlignment(Qt.AlignCenter)
        self.layoutWidget = QWidget(Form__timer)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 80, 439, 190))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label__usr_ddi = QLabel(self.layoutWidget)
        self.label__usr_ddi.setObjectName(u"label__usr_ddi")

        self.horizontalLayout.addWidget(self.label__usr_ddi)

        self.comboBox__usr_ddi = QComboBox(self.layoutWidget)
        self.comboBox__usr_ddi.setObjectName(u"comboBox__usr_ddi")

        self.horizontalLayout.addWidget(self.comboBox__usr_ddi)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.frame = QFrame(self.layoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton__start = QPushButton(self.frame)
        self.pushButton__start.setObjectName(u"pushButton__start")

        self.verticalLayout.addWidget(self.pushButton__start)

        self.pushButton__pause = QPushButton(self.frame)
        self.pushButton__pause.setObjectName(u"pushButton__pause")

        self.verticalLayout.addWidget(self.pushButton__pause)

        self.pushButton__reset = QPushButton(self.frame)
        self.pushButton__reset.setObjectName(u"pushButton__reset")

        self.verticalLayout.addWidget(self.pushButton__reset)


        self.gridLayout.addLayout(self.verticalLayout, 1, 3, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_5)

        self.spinBox__sec = QSpinBox(self.frame)
        self.spinBox__sec.setObjectName(u"spinBox__sec")
        font1 = QFont()
        font1.setPointSize(20)
        self.spinBox__sec.setFont(font1)

        self.verticalLayout_4.addWidget(self.spinBox__sec)


        self.gridLayout.addLayout(self.verticalLayout_4, 1, 2, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4)

        self.spinBox__min = QSpinBox(self.frame)
        self.spinBox__min.setObjectName(u"spinBox__min")
        self.spinBox__min.setFont(font1)

        self.verticalLayout_3.addWidget(self.spinBox__min)


        self.gridLayout.addLayout(self.verticalLayout_3, 1, 1, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.spinBox__hour = QSpinBox(self.frame)
        self.spinBox__hour.setObjectName(u"spinBox__hour")
        self.spinBox__hour.setFont(font1)

        self.verticalLayout_2.addWidget(self.spinBox__hour)


        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.label__timer = QLabel(self.frame)
        self.label__timer.setObjectName(u"label__timer")

        self.gridLayout.addWidget(self.label__timer, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.lcdNumber__viewer = QLCDNumber(self.layoutWidget)
        self.lcdNumber__viewer.setObjectName(u"lcdNumber__viewer")
        font2 = QFont()
        font2.setPointSize(28)
        self.lcdNumber__viewer.setFont(font2)

        self.verticalLayout_6.addWidget(self.lcdNumber__viewer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.dateTimeEdit = QDateTimeEdit(Form__timer)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(500, 80, 194, 24))

        self.retranslateUi(Form__timer)

        QMetaObject.connectSlotsByName(Form__timer)
    # setupUi

    def retranslateUi(self, Form__timer):
        Form__timer.setWindowTitle(QCoreApplication.translate("Form__timer", u"Form", None))
        self.label__title.setText(QCoreApplication.translate("Form__timer", u"Alarm for Today's Luck", None))
        self.label__usr_ddi.setText(QCoreApplication.translate("Form__timer", u"\ub098 \uc758  \ub760 ", None))
        self.pushButton__start.setText(QCoreApplication.translate("Form__timer", u"Start", None))
        self.pushButton__pause.setText(QCoreApplication.translate("Form__timer", u"Pause", None))
        self.pushButton__reset.setText(QCoreApplication.translate("Form__timer", u"Reset", None))
        self.label_5.setText(QCoreApplication.translate("Form__timer", u"Sec", None))
        self.label_4.setText(QCoreApplication.translate("Form__timer", u"Min", None))
        self.label_3.setText(QCoreApplication.translate("Form__timer", u"Hour", None))
        self.label__timer.setText(QCoreApplication.translate("Form__timer", u"Timer", None))
    # retranslateUi


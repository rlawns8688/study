# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'timer.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

from timer_observer.resources.rc import icons_rc
from timer_observer.resources.rc import images_rc


class Ui_Form__timer(object):
    def setupUi(self, Form__timer):
        if not Form__timer.objectName():
            Form__timer.setObjectName("Form__timer")
        Form__timer.resize(576, 370)
        icon = QIcon()
        icon.addFile(":/icons/icons/timer-play.png", QSize(), QIcon.Normal, QIcon.Off)
        Form__timer.setWindowIcon(icon)
        self.verticalLayout_4 = QVBoxLayout(Form__timer)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label__jid = QLabel(Form__timer)
        self.label__jid.setObjectName("label__jid")

        self.verticalLayout.addWidget(self.label__jid)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox__link = QComboBox(Form__timer)
        self.comboBox__link.setObjectName("comboBox__link")

        self.horizontalLayout.addWidget(self.comboBox__link)

        self.label = QLabel(Form__timer)
        self.label.setObjectName("label")

        self.horizontalLayout.addWidget(self.label)

        self.lcdNumber__remaining = QLCDNumber(Form__timer)
        self.lcdNumber__remaining.setObjectName("lcdNumber__remaining")
        self.lcdNumber__remaining.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout.addWidget(self.lcdNumber__remaining)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.progressBar__remaining = QProgressBar(Form__timer)
        self.progressBar__remaining.setObjectName("progressBar__remaining")
        self.progressBar__remaining.setValue(0)

        self.verticalLayout.addWidget(self.progressBar__remaining)

        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton__subscribe = QPushButton(Form__timer)
        self.pushButton__subscribe.setObjectName("pushButton__subscribe")
        self.pushButton__subscribe.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.pushButton__subscribe)

        self.label__status = QLabel(Form__timer)
        self.label__status.setObjectName("label__status")

        self.horizontalLayout_3.addWidget(self.label__status)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_2 = QLabel(Form__timer)
        self.label_2.setObjectName("label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(":/icons/icons/clock-check-outline.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.timeEdit__timer = QTimeEdit(Form__timer)
        self.timeEdit__timer.setObjectName("timeEdit__timer")
        self.timeEdit__timer.setCurrentSection(QDateTimeEdit.HourSection)

        self.horizontalLayout_3.addWidget(self.timeEdit__timer)

        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.listWidget__command = QListWidget(Form__timer)
        self.listWidget__command.setObjectName("listWidget__command")

        self.horizontalLayout_4.addWidget(self.listWidget__command)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton__add_item = QPushButton(Form__timer)
        self.pushButton__add_item.setObjectName("pushButton__add_item")
        icon1 = QIcon()
        icon1.addFile(":/icons/icons/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton__add_item.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.pushButton__add_item)

        self.pushButton__del_item = QPushButton(Form__timer)
        self.pushButton__del_item.setObjectName("pushButton__del_item")
        icon2 = QIcon()
        icon2.addFile(":/icons/icons/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton__del_item.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.pushButton__del_item)

        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textEdit__debug = QTextEdit(Form__timer)
        self.textEdit__debug.setObjectName("textEdit__debug")
        self.textEdit__debug.setFrameShape(QFrame.NoFrame)
        self.textEdit__debug.setFrameShadow(QFrame.Plain)
        self.textEdit__debug.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.textEdit__debug)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton__start = QPushButton(Form__timer)
        self.pushButton__start.setObjectName("pushButton__start")
        self.pushButton__start.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.pushButton__start)

        self.pushButton__stop = QPushButton(Form__timer)
        self.pushButton__stop.setObjectName("pushButton__stop")
        icon3 = QIcon()
        icon3.addFile(":/icons/icons/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton__stop.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.pushButton__stop)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.retranslateUi(Form__timer)

        QMetaObject.connectSlotsByName(Form__timer)

    # setupUi

    def retranslateUi(self, Form__timer):
        Form__timer.setWindowTitle(
            QCoreApplication.translate("Form__timer", "Timer", None)
        )
        self.label__jid.setText(
            QCoreApplication.translate("Form__timer", "TextLabel", None)
        )
        self.label.setText(
            QCoreApplication.translate("Form__timer", "Time remaining", None)
        )
        self.pushButton__subscribe.setText(
            QCoreApplication.translate("Form__timer", "\uad6c\ub3c5\ud558\uae30", None)
        )
        self.label__status.setText(
            QCoreApplication.translate("Form__timer", "TextLabel", None)
        )
        self.label_2.setText("")
        self.timeEdit__timer.setDisplayFormat(
            QCoreApplication.translate("Form__timer", "hh:mm:ss", None)
        )
        self.pushButton__add_item.setText(
            QCoreApplication.translate("Form__timer", "Add", None)
        )
        self.pushButton__del_item.setText(
            QCoreApplication.translate("Form__timer", "Remove", None)
        )
        self.pushButton__start.setText(
            QCoreApplication.translate("Form__timer", "Start", None)
        )
        self.pushButton__stop.setText(
            QCoreApplication.translate("Form__timer", "Stop", None)
        )

    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'timer_template.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form__widget(object):
    def setupUi(self, Form__widget):
        if not Form__widget.objectName():
            Form__widget.setObjectName(u"Form__widget")
        Form__widget.resize(374, 114)
        self.verticalLayout = QVBoxLayout(Form__widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.progressBar = QProgressBar(Form__widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.timeEdit__timer = QTimeEdit(Form__widget)
        self.timeEdit__timer.setObjectName(u"timeEdit__timer")

        self.horizontalLayout_3.addWidget(self.timeEdit__timer)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton__start = QPushButton(Form__widget)
        self.pushButton__start.setObjectName(u"pushButton__start")

        self.horizontalLayout.addWidget(self.pushButton__start)

        self.pushButton__stop = QPushButton(Form__widget)
        self.pushButton__stop.setObjectName(u"pushButton__stop")

        self.horizontalLayout.addWidget(self.pushButton__stop)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(Form__widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit = QLineEdit(Form__widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form__widget)

        QMetaObject.connectSlotsByName(Form__widget)
    # setupUi

    def retranslateUi(self, Form__widget):
        Form__widget.setWindowTitle(QCoreApplication.translate("Form__widget", u"Form", None))
        self.timeEdit__timer.setDisplayFormat(QCoreApplication.translate("Form__widget", u"hh:mm:ss", None))
        self.pushButton__start.setText(QCoreApplication.translate("Form__widget", u"start", None))
        self.pushButton__stop.setText(QCoreApplication.translate("Form__widget", u"stop", None))
        self.label.setText(QCoreApplication.translate("Form__widget", u"command", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form__widget", u"ex) /usr/bin/gnome-terminal", None))
    # retranslateUi


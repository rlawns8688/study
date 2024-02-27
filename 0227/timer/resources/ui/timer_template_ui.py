# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'timer_template.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(331, 103)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)

        self.lineEdit__cmd = QLineEdit(Form)
        self.lineEdit__cmd.setObjectName(u"lineEdit__cmd")

        self.verticalLayout.addWidget(self.lineEdit__cmd)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.timeEdit__timer = QTimeEdit(Form)
        self.timeEdit__timer.setObjectName(u"timeEdit__timer")

        self.horizontalLayout_2.addWidget(self.timeEdit__timer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton__start = QPushButton(Form)
        self.pushButton__start.setObjectName(u"pushButton__start")

        self.horizontalLayout.addWidget(self.pushButton__start)

        self.pushButton__stop = QPushButton(Form)
        self.pushButton__stop.setObjectName(u"pushButton__stop")

        self.horizontalLayout.addWidget(self.pushButton__stop)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lineEdit__cmd.setPlaceholderText(QCoreApplication.translate("Form", u"ex) /usr/bin/gnome-terminal", None))
        self.timeEdit__timer.setDisplayFormat(QCoreApplication.translate("Form", u"hh:mm:ss", None))
        self.pushButton__start.setText(QCoreApplication.translate("Form", u"start", None))
        self.pushButton__stop.setText(QCoreApplication.translate("Form", u"stop", None))
    # retranslateUi


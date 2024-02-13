# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(360, 272)
        self.label_value = QLabel(Form)
        self.label_value.setObjectName(u"label_value")
        self.label_value.setGeometry(QRect(140, 20, 181, 41))
        font = QFont()
        font.setFamily(u"URW Gothic [urw]")
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_value.setFont(font)
        self.pushButton_result = QPushButton(Form)
        self.pushButton_result.setObjectName(u"pushButton_result")
        self.pushButton_result.setGeometry(QRect(30, 20, 80, 41))
        font1 = QFont()
        font1.setFamily(u"DejaVu Serif")
        font1.setPointSize(26)
        font1.setBold(True)
        font1.setWeight(75)
        self.pushButton_result.setFont(font1)
        self.pushButton_clear = QPushButton(Form)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setGeometry(QRect(10, 80, 341, 23))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setItalic(True)
        self.pushButton_clear.setFont(font2)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 110, 340, 158))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        font3 = QFont()
        font3.setPointSize(11)
        self.pushButton_5.setFont(font3)

        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.pushButton_mul = QPushButton(self.widget)
        self.pushButton_mul.setObjectName(u"pushButton_mul")
        self.pushButton_mul.setFont(font3)

        self.gridLayout.addWidget(self.pushButton_mul, 2, 3, 1, 1)

        self.pushButton_8 = QPushButton(self.widget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setFont(font3)

        self.gridLayout.addWidget(self.pushButton_8, 0, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font3)

        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_1 = QPushButton(self.widget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setFont(font3)

        self.gridLayout.addWidget(self.pushButton_1, 2, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.widget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font3)

        self.gridLayout.addWidget(self.pushButton_7, 0, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font3)

        self.gridLayout.addWidget(self.pushButton_3, 2, 2, 1, 1)

        self.pushButton_dot = QPushButton(self.widget)
        self.pushButton_dot.setObjectName(u"pushButton_dot")
        self.pushButton_dot.setFont(font3)

        self.gridLayout.addWidget(self.pushButton_dot, 4, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.widget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFont(font3)

        self.gridLayout.addWidget(self.pushButton_9, 0, 2, 1, 1)

        self.pushButton_sum = QPushButton(self.widget)
        self.pushButton_sum.setObjectName(u"pushButton_sum")
        self.pushButton_sum.setFont(font3)

        self.gridLayout.addWidget(self.pushButton_sum, 0, 3, 1, 1)

        self.pushButton_6 = QPushButton(self.widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font3)

        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.pushButton_sub = QPushButton(self.widget)
        self.pushButton_sub.setObjectName(u"pushButton_sub")
        self.pushButton_sub.setFont(font3)

        self.gridLayout.addWidget(self.pushButton_sub, 1, 3, 1, 1)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font3)

        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)

        self.pushButton_0 = QPushButton(self.widget)
        self.pushButton_0.setObjectName(u"pushButton_0")
        self.pushButton_0.setFont(font3)

        self.gridLayout.addWidget(self.pushButton_0, 3, 1, 1, 1)

        self.pushButton_back = QPushButton(self.widget)
        self.pushButton_back.setObjectName(u"pushButton_back")
        self.pushButton_back.setFont(font3)

        self.gridLayout.addWidget(self.pushButton_back, 4, 2, 1, 1)

        self.pushButton_div = QPushButton(self.widget)
        self.pushButton_div.setObjectName(u"pushButton_div")
        self.pushButton_div.setFont(font3)

        self.gridLayout.addWidget(self.pushButton_div, 3, 3, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_value.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.pushButton_result.setText(QCoreApplication.translate("Form", u"=", None))
        self.pushButton_clear.setText(QCoreApplication.translate("Form", u"clear", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.pushButton_mul.setText(QCoreApplication.translate("Form", u"x", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.pushButton_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_dot.setText(QCoreApplication.translate("Form", u".", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.pushButton_sum.setText(QCoreApplication.translate("Form", u"+", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.pushButton_sub.setText(QCoreApplication.translate("Form", u"-", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_back.setText(QCoreApplication.translate("Form", u"<-", None))
        self.pushButton_div.setText(QCoreApplication.translate("Form", u"\u00f7", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'keyPressCal.ui'
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
        Form.resize(194, 213)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 20, 131, 150))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        self.lineEdit.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.lineEdit)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.toolButton = QToolButton(self.layoutWidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setEnabled(True)

        self.horizontalLayout.addWidget(self.toolButton)

        self.toolButton_2 = QToolButton(self.layoutWidget)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setEnabled(True)

        self.horizontalLayout.addWidget(self.toolButton_2)

        self.toolButton_3 = QToolButton(self.layoutWidget)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setEnabled(True)

        self.horizontalLayout.addWidget(self.toolButton_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.toolButton_4 = QToolButton(self.layoutWidget)
        self.toolButton_4.setObjectName(u"toolButton_4")
        self.toolButton_4.setEnabled(True)

        self.horizontalLayout_2.addWidget(self.toolButton_4)

        self.toolButton_5 = QToolButton(self.layoutWidget)
        self.toolButton_5.setObjectName(u"toolButton_5")
        self.toolButton_5.setEnabled(True)

        self.horizontalLayout_2.addWidget(self.toolButton_5)

        self.toolButton_6 = QToolButton(self.layoutWidget)
        self.toolButton_6.setObjectName(u"toolButton_6")
        self.toolButton_6.setEnabled(True)

        self.horizontalLayout_2.addWidget(self.toolButton_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.toolButton_7 = QToolButton(self.layoutWidget)
        self.toolButton_7.setObjectName(u"toolButton_7")
        self.toolButton_7.setEnabled(True)

        self.horizontalLayout_3.addWidget(self.toolButton_7)

        self.toolButton_8 = QToolButton(self.layoutWidget)
        self.toolButton_8.setObjectName(u"toolButton_8")
        self.toolButton_8.setEnabled(True)

        self.horizontalLayout_3.addWidget(self.toolButton_8)

        self.toolButton_9 = QToolButton(self.layoutWidget)
        self.toolButton_9.setObjectName(u"toolButton_9")
        self.toolButton_9.setEnabled(True)

        self.horizontalLayout_3.addWidget(self.toolButton_9)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.toolButton_10 = QToolButton(self.layoutWidget)
        self.toolButton_10.setObjectName(u"toolButton_10")
        self.toolButton_10.setEnabled(True)

        self.horizontalLayout_4.addWidget(self.toolButton_10)

        self.toolButton_11 = QToolButton(self.layoutWidget)
        self.toolButton_11.setObjectName(u"toolButton_11")
        self.toolButton_11.setEnabled(True)

        self.horizontalLayout_4.addWidget(self.toolButton_11)

        self.toolButton_12 = QToolButton(self.layoutWidget)
        self.toolButton_12.setObjectName(u"toolButton_12")
        self.toolButton_12.setEnabled(True)

        self.horizontalLayout_4.addWidget(self.toolButton_12)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.toolButton_13 = QToolButton(self.layoutWidget)
        self.toolButton_13.setObjectName(u"toolButton_13")

        self.verticalLayout.addWidget(self.toolButton_13)

        self.toolButton_14 = QToolButton(self.layoutWidget)
        self.toolButton_14.setObjectName(u"toolButton_14")

        self.verticalLayout.addWidget(self.toolButton_14)

        self.toolButton_15 = QToolButton(self.layoutWidget)
        self.toolButton_15.setObjectName(u"toolButton_15")

        self.verticalLayout.addWidget(self.toolButton_15)

        self.toolButton_16 = QToolButton(self.layoutWidget)
        self.toolButton_16.setObjectName(u"toolButton_16")

        self.verticalLayout.addWidget(self.toolButton_16)


        self.horizontalLayout_5.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.toolButton.setText(QCoreApplication.translate("Form", u"1", None))
        self.toolButton_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.toolButton_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.toolButton_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.toolButton_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.toolButton_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.toolButton_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.toolButton_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.toolButton_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.toolButton_10.setText(QCoreApplication.translate("Form", u"C", None))
        self.toolButton_11.setText(QCoreApplication.translate("Form", u"0", None))
        self.toolButton_12.setText(QCoreApplication.translate("Form", u"=", None))
        self.toolButton_13.setText(QCoreApplication.translate("Form", u"+", None))
        self.toolButton_14.setText(QCoreApplication.translate("Form", u"-", None))
        self.toolButton_15.setText(QCoreApplication.translate("Form", u"*", None))
        self.toolButton_16.setText(QCoreApplication.translate("Form", u"/", None))
    # retranslateUi


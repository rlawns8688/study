# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change_keyword.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_MainWindow__change_keyword(object):
    def setupUi(self, MainWindow__change_keyword):
        if not MainWindow__change_keyword.objectName():
            MainWindow__change_keyword.setObjectName(u"MainWindow__change_keyword")
        MainWindow__change_keyword.resize(438, 209)
        self.centralwidget = QWidget(MainWindow__change_keyword)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit__pdir = QLineEdit(self.centralwidget)
        self.lineEdit__pdir.setObjectName(u"lineEdit__pdir")

        self.horizontalLayout.addWidget(self.lineEdit__pdir)

        self.toolButton__pdir = QToolButton(self.centralwidget)
        self.toolButton__pdir.setObjectName(u"toolButton__pdir")

        self.horizontalLayout.addWidget(self.toolButton__pdir)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.lineEdit__file_ext = QLineEdit(self.centralwidget)
        self.lineEdit__file_ext.setObjectName(u"lineEdit__file_ext")

        self.horizontalLayout_4.addWidget(self.lineEdit__file_ext)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit__change_str = QLineEdit(self.centralwidget)
        self.lineEdit__change_str.setObjectName(u"lineEdit__change_str")

        self.horizontalLayout_2.addWidget(self.lineEdit__change_str)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lineEdit__find_pattern = QLineEdit(self.centralwidget)
        self.lineEdit__find_pattern.setObjectName(u"lineEdit__find_pattern")

        self.horizontalLayout_3.addWidget(self.lineEdit__find_pattern)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton__start = QPushButton(self.centralwidget)
        self.pushButton__start.setObjectName(u"pushButton__start")

        self.horizontalLayout_6.addWidget(self.pushButton__start)

        self.pushButton__stop = QPushButton(self.centralwidget)
        self.pushButton__stop.setObjectName(u"pushButton__stop")

        self.horizontalLayout_6.addWidget(self.pushButton__stop)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        MainWindow__change_keyword.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow__change_keyword)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 438, 20))
        MainWindow__change_keyword.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow__change_keyword)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow__change_keyword.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow__change_keyword)

        QMetaObject.connectSlotsByName(MainWindow__change_keyword)
    # setupUi

    def retranslateUi(self, MainWindow__change_keyword):
        MainWindow__change_keyword.setWindowTitle(QCoreApplication.translate("MainWindow__change_keyword", u"MainWindow", None))
        self.lineEdit__pdir.setPlaceholderText(QCoreApplication.translate("MainWindow__change_keyword", u"/home/rapa", None))
        self.toolButton__pdir.setText(QCoreApplication.translate("MainWindow__change_keyword", u"...", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow__change_keyword", u"\ud30c\uc77c \ud655\uc7a5\uc790", None))
        self.lineEdit__file_ext.setPlaceholderText(QCoreApplication.translate("MainWindow__change_keyword", u".h .cpp", None))
        self.label.setText(QCoreApplication.translate("MainWindow__change_keyword", u"\ubcc0\uacbd\ud560 \ubb38\uc790\uc5f4", None))
        self.lineEdit__change_str.setPlaceholderText(QCoreApplication.translate("MainWindow__change_keyword", u"#include \"PXR2", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow__change_keyword", u"\ucc3e\uc744 \ud328\ud134", None))
        self.lineEdit__find_pattern.setPlaceholderText(QCoreApplication.translate("MainWindow__change_keyword", u"#include \"pxr", None))
        self.pushButton__start.setText(QCoreApplication.translate("MainWindow__change_keyword", u"Start", None))
        self.pushButton__stop.setText(QCoreApplication.translate("MainWindow__change_keyword", u"Stop", None))
    # retranslateUi


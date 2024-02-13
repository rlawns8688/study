# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Sequence_Manager.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_mainWindow__seq(object):
    def setupUi(self, mainWindow__seq):
        if not mainWindow__seq.objectName():
            mainWindow__seq.setObjectName(u"mainWindow__seq")
        mainWindow__seq.resize(526, 522)
        self.actionAbout = QAction(mainWindow__seq)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionExit = QAction(mainWindow__seq)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(mainWindow__seq)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(236, 70, 278, 331))
        self.miss_frame_tab = QWidget()
        self.miss_frame_tab.setObjectName(u"miss_frame_tab")
        self.listWidget_missing = QListWidget(self.miss_frame_tab)
        self.listWidget_missing.setObjectName(u"listWidget_missing")
        self.listWidget_missing.setGeometry(QRect(10, 21, 251, 271))
        self.tabWidget.addTab(self.miss_frame_tab, "")
        self.error_frame_tab = QWidget()
        self.error_frame_tab.setObjectName(u"error_frame_tab")
        self.listWidget_error = QListWidget(self.error_frame_tab)
        self.listWidget_error.setObjectName(u"listWidget_error")
        self.listWidget_error.setGeometry(QRect(10, 21, 251, 271))
        self.tabWidget.addTab(self.error_frame_tab, "")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 30, 421, 27))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_dirpath = QLineEdit(self.layoutWidget)
        self.lineEdit_dirpath.setObjectName(u"lineEdit_dirpath")

        self.horizontalLayout.addWidget(self.lineEdit_dirpath)

        self.toolButton_dirpath = QToolButton(self.layoutWidget)
        self.toolButton_dirpath.setObjectName(u"toolButton_dirpath")

        self.horizontalLayout.addWidget(self.toolButton_dirpath)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_work_filepath = QLineEdit(self.layoutWidget)
        self.lineEdit_work_filepath.setObjectName(u"lineEdit_work_filepath")
        self.lineEdit_work_filepath.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_work_filepath)

        self.toolButton_work_filepath = QToolButton(self.layoutWidget)
        self.toolButton_work_filepath.setObjectName(u"toolButton_work_filepath")

        self.horizontalLayout_2.addWidget(self.toolButton_work_filepath)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 70, 191, 331))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.listWidget = QListWidget(self.layoutWidget1)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)

        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        mainWindow__seq.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow__seq)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 526, 20))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        mainWindow__seq.setMenuBar(self.menubar)
        self.SequnceManager = QStatusBar(mainWindow__seq)
        self.SequnceManager.setObjectName(u"SequnceManager")
        mainWindow__seq.setStatusBar(self.SequnceManager)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(mainWindow__seq)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(mainWindow__seq)
    # setupUi

    def retranslateUi(self, mainWindow__seq):
        mainWindow__seq.setWindowTitle(QCoreApplication.translate("mainWindow__seq", u"MainWindow", None))
        self.actionAbout.setText(QCoreApplication.translate("mainWindow__seq", u"About", None))
        self.actionExit.setText(QCoreApplication.translate("mainWindow__seq", u"Exit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.miss_frame_tab), QCoreApplication.translate("mainWindow__seq", u"Missing_Frame", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.error_frame_tab), QCoreApplication.translate("mainWindow__seq", u"Error_Frame", None))
        self.lineEdit_dirpath.setText(QCoreApplication.translate("mainWindow__seq", u"fsdfsdsf", None))
        self.toolButton_dirpath.setText(QCoreApplication.translate("mainWindow__seq", u"Opendir", None))
        self.lineEdit_work_filepath.setText("")
        self.toolButton_work_filepath.setText(QCoreApplication.translate("mainWindow__seq", u"Open File", None))
        self.label.setText(QCoreApplication.translate("mainWindow__seq", u"TextLabel", None))
        self.menuFile.setTitle(QCoreApplication.translate("mainWindow__seq", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("mainWindow__seq", u"Help", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'my.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 638)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 20, 401, 581))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.labelcontents = QLabel(self.widget)
        self.labelcontents.setObjectName(u"labelcontents")
        font = QFont()
        font.setPointSize(24)
        font.setItalic(True)
        self.labelcontents.setFont(font)

        self.verticalLayout.addWidget(self.labelcontents)

        self.tree_shot = QTreeWidget(self.widget)
        self.tree_shot.setObjectName(u"tree_shot")

        self.verticalLayout.addWidget(self.tree_shot)

        self.progressBar = QProgressBar(self.widget)
        self.progressBar.setObjectName(u"progressBar")
#if QT_CONFIG(accessibility)
        self.progressBar.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout.addWidget(self.progressBar)

        self.btn_run = QPushButton(self.widget)
        self.btn_run.setObjectName(u"btn_run")

        self.verticalLayout.addWidget(self.btn_run)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelcontents.setText(QCoreApplication.translate("MainWindow", u"ShotInfo", None))
        ___qtreewidgetitem = self.tree_shot.headerItem()
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"nk", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"hip", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"mov", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"shot", None));
        self.btn_run.setText(QCoreApplication.translate("MainWindow", u"Run", None))
    # retranslateUi


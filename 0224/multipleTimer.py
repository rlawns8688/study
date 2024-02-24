#!/usr/bin/env python
# encoding=utf-8
# author        :   kim junhyuk
# created date  :   2024.02.24
# modified date  :   2024.02.24
# description  :

import
import pytest
from PySide2 import QtWidgets, QtGui, QtCore
from resources.ui import timer_template_ui

class MutipleTimer(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        w = QtWidgets.QWidget()

        self.vbox = QtWidgets.QVBoxLayout()

        self.__cnt_widgets = 3
        
        self.set_widgets()
        w.setLayout(self.vbox)
        self.setCentralWidget(w)

    def set_widgets(self):
        for i in range(self.__cnt_widgets):
            widget = QtWidgets.QWidget()
            w = timer_template_ui.Ui_Form()
            w.setupUi(widget)
            self.vbox.addWidget(w)
if __name__ == '__main__':
    pass

#!/usr/bin/env python
# encoding=utf-8

# author        : seongcheol jeon
# created date  : 2024.03.05
# modified date : 2024.03.05
# description   :

from PySide2 import QtWidgets, QtGui, QtCore


class Signals(QtCore.QObject):
    certificate = QtCore.Signal(tuple)


class Certification(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__cert_info: tuple = ()
        self.__signals = Signals()
        self.setLayout(self.__setup_ui())
        # vars
        # signal & slot
        self.__connections()

    @property
    def signals(self):
        return self.__signals

    def __connections(self):
        self.__btn_ok.clicked.connect(self.__slot_btn_clk)
        self.__btn_cancel.clicked.connect(self.__slot_btn_clk)

    def __slot_btn_clk(self) -> None:
        btn: QtWidgets.QPushButton = self.sender()
        if btn.text().strip().lower() == 'ok':
            _id = self.__lidt_id.text().strip()
            _pw = self.__lidt_pw.text().strip()
            if len(_id) or len(_pw):
                self.__cert_info = (_id, _pw)
                self.close()
        else:
            self.close()

        # print('certification class: ', self.__cert_info)
        self.__signals.certificate.emit(self.__cert_info)

    def cert_info(self):
        return self.__cert_info

    def __setup_ui(self):
        lbl_id = QtWidgets.QLabel('ID:')
        lbl_pw = QtWidgets.QLabel('PW:')
        self.__lidt_id = QtWidgets.QLineEdit()
        self.__lidt_pw = QtWidgets.QLineEdit()
        self.__lidt_pw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.__btn_ok = QtWidgets.QPushButton('Ok')
        self.__btn_cancel = QtWidgets.QPushButton('Cancel')
        hbox_layout_id = QtWidgets.QHBoxLayout()
        hbox_layout_pw = QtWidgets.QHBoxLayout()
        hbox_layout_btns = QtWidgets.QHBoxLayout()
        vbox_layout = QtWidgets.QVBoxLayout()

        hbox_layout_id.addWidget(lbl_id)
        hbox_layout_id.addWidget(self.__lidt_id)

        hbox_layout_pw.addWidget(lbl_pw)
        hbox_layout_pw.addWidget(self.__lidt_pw)

        hbox_layout_btns.addWidget(self.__btn_ok)
        hbox_layout_btns.addWidget(self.__btn_cancel)

        vbox_layout.addLayout(hbox_layout_id)
        vbox_layout.addLayout(hbox_layout_pw)
        vbox_layout.addLayout(hbox_layout_btns)

        return vbox_layout


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    cert = Certification()
    cert.show()
    app.exec_()

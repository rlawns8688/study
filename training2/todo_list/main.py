#!/usr/bin/env python
# encoding=utf-8

# author        : seongcheol jeon
# created date  : 2024.03.02
# modified date : 2024.03.02
# description   :

import sys
import typing
import datetime
import pydantic

from PySide2 import QtWidgets, QtGui, QtCore

from training2.todo_list.view import todo_view
from model import todo_model
from widget.certification import certification

from libs.qt import library as qt_lib
import constants

from lib import db


# class TodoStatus:
#     status_ids = {
#         'complete': 1,
#         'inprogress': 2,
#         'waiting': 3
#     }
#
#     color = {
#         'complete':     (70, 0, 255, 255),
#         'inprogress':   (255, 70, 0, 255),
#         'waiting':      (0, 255, 70, 255),
#     }


class TodoStatus(pydantic.BaseModel):
    complete: str
    inprogress: str
    waiting: str


class TodoItem(pydantic.BaseModel):
    data_id: int
    todo: str
    save_datetime: datetime.datetime
    deadline: datetime.datetime
    todo_status: typing.Union[str, int, None]
    todo_author: typing.Union[str, int, None]


class TodoList(QtWidgets.QMainWindow):
    TODO_KEY_DATA = [
        "data_id",
        "todo",
        "save_datetime",
        "deadline",
        "todo_status",
        "todo_author",
    ]

    def __init__(self, database, parent=None):
        super().__init__(parent)

        self.__db = database

        self.__todo = list()
        self.__todo_ste = TodoStatus(
            **dict(zip(self.__db.get_todo_status(), self.__db.get_todo_status()))
        )
        self.__init()

        self.__todo_view = todo_view.TodoView()
        self.__todo_model = todo_model.TodoModel(self.__todo)
        self.__todo_view.setModel(self.__todo_model)

        self.__set_ui()

    def __init(self):
        # (55
        # 'coding test practice',
        # datetime.datetime(2023, 12, 15, 0, 0),
        # datetime.datetime(2023, 12, 31, 0, 0),
        # 'inprogress',
        # 'kye')

        todo_list = self.__db.get_todo_list()
        for dat in todo_list:
            todo_item = TodoItem(**dict(zip(TodoList.TODO_KEY_DATA, dat)))
            self.__todo.append(todo_item)

    def __set_ui(self):
        w = QtWidgets.QWidget()
        # v layout
        vbox_layout = QtWidgets.QVBoxLayout()
        vbox_layout.addWidget(self.__todo_view)

        # buttons
        hbox_layout_btns = QtWidgets.QHBoxLayout()
        self.__btn_add = QtWidgets.QPushButton("Add")
        self.__btn_del = QtWidgets.QPushButton("Delete")
        self.__btn_com = QtWidgets.QPushButton("Update")
        hbox_layout_btns.addWidget(self.__btn_add)
        hbox_layout_btns.addWidget(self.__btn_del)
        hbox_layout_btns.addWidget(self.__btn_com)

        vbox_layout.addLayout(hbox_layout_btns)
        w.setLayout(vbox_layout)

        self.setCentralWidget(w)

        self.__connections()

    def __connections(self):
        self.__btn_add.clicked.connect(self.__slot_clicked_add)
        self.__todo_view.clicked.connect(self.__slot_chg_idx_view)
        self.__btn_del.clicked.connect(self.__slot_clicked_del)
        self.__btn_com.clicked.connect(self.__slot_clicked_update)

    def __slot_chg_idx_view(self):
        indexes = self.__todo_view.selectedIndexes()
        if not len(indexes):
            return
        index: QtCore.QModelIndex = indexes[0]
        return index

    def __slot_clicked_update(self):
        index = self.__slot_chg_idx_view()
        if index is None or not index.isValid():
            return
        ok, text = qt_lib.QtLibs.input_dialog("update", "", self)
        if not ok:
            return

        """
        [
            (1, 'todo string', datetime, datetime, 'waiting', 2), 
            (2, 'todo string3', datetime, datetime, 'waiting', 2), 
            (3, 'todo string44', datetime, datetime, 'waiting', 2), 
            ...
        """
        # todo_item_id: int = self.__todo_model.get_data()[index.row()].data_id
        todo_item_id: int = index.data(todo_model.TodoModel.id_role)

        if self.__db.update_todo(todo_item_id, text):
            self.__todo_model.update_status(index.row(), text)

    def __slot_clicked_del(self):
        index = self.__slot_chg_idx_view()
        if index is None or not index.isValid():
            return
        if not qt_lib.QtLibs.question_dialog(
            "Delete Todo",
            f"delete todo item: {index.data(QtCore.Qt.DisplayRole)}",
            self,
        ):
            return

        # todo_item_id: int = self.__todo_model.get_data()[index.row()].data_id
        todo_item_id: int = index.data(todo_model.TodoModel.id_role)

        if self.__db.del_todo(todo_item_id):
            self.__todo_model.del_data(index.row())

    def __slot_clicked_add(self):
        index = self.__slot_chg_idx_view()
        print(index.data(todo_model.TodoModel.test_role))

        ok, text = qt_lib.QtLibs.input_dialog("Add Todo", "adding todo", self)
        if not ok:
            return

        # id, todo string, created date, deadline date, status id, author id
        # (5, 'home tra', '2023/12/15', '2023/12/31', 2, 3);

        print(self.__todo_ste.waiting, type(self.__todo_ste.waiting))

        todo_item = [
            text,
            datetime.datetime.now(),
            datetime.datetime.now(),
            # TodoStatus.status_ids.get('inprogress'),
            self.__todo_ste.waiting,
            1,
        ]

        if self.__db.add_todo(todo_item):
            # self.__todo_model.add_data(TodoItem(text, 0))
            todo_item.insert(0, self.__db.get_id())
            self.__todo_model.add_data(
                TodoItem(**dict(zip(TodoList.TODO_KEY_DATA, todo_item)))
            )

    def input_dialog(self):
        dia = QtWidgets.QDialog()
        vbox_layout = QtWidgets.QVBoxLayout()
        line_edit = QtWidgets.QLineEdit()
        line_edit.setPlaceholderText("ex) programming study")
        hbox_layout = QtWidgets.QHBoxLayout()
        btn_ok = QtWidgets.QPushButton("ok")
        btn_cancel = QtWidgets.QPushButton("cancel")
        # connect
        # btn_ok.clicked.connect()
        # hbox_layout.addWidget(btn_ok, btn_cancel)
        vbox_layout.addWidget(line_edit)
        vbox_layout.addLayout(hbox_layout)
        print("asd")
        dia.show()


class Controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.cert = certification.Certification()
        self.cert.signals.certificate.connect(self.__slot_certificate)

    def __slot_certificate(self, data: tuple):
        try:
            user, passwd = data
            __db = db.DBTodolist(user, passwd)
            if not __db.is_connected_db():
                sys.stderr.write("not connected db...")
                return
            todo_lst = TodoList(__db, self)
            todo_lst.show()

        except constants.CustomExcept as err:
            QtWidgets.QMessageBox.information(self, f"{err.username} 계정 에러", str(err))
        except ValueError as err:
            QtWidgets.QMessageBox.information(self, "", "id & password 비어있습니다.")

    def show(self):
        self.cert.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    c = Controller()
    c.show()
    app.exec_()

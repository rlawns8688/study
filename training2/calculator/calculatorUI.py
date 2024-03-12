#!/usr/bin/env python
# encoding=utf-8

# author        : seongcheol jeon
# created date  : 2024.02.17
# modified date : 2024.02.17
# description   :

# home work: 소수점 되도록


import re
import sys
import importlib
import typing

from PySide2 import QtWidgets, QtGui, QtCore

import qdarktheme

from libs.qt import stylesheet
from libs.algorithm.library import Stack

importlib.reload(stylesheet)


class CalculateExp:
    @staticmethod
    def precedence(op):
        if op == '(' or op == ')':
            return 0
        elif op == '+' or op == '-':
            return 1
        elif op == '*' or op == '/':
            return 2
        else:
            return -1

    @staticmethod
    def is_operator(term):
        return term in ('+', '-', '*', '/')

    @staticmethod
    def has_higher_precedence(op1, op2):
        return CalculateExp.precedence(op1) >= CalculateExp.precedence(op2)

    @staticmethod
    def infix_to_postfix(expression: str) -> typing.List[str]:
        stack = Stack()
        exp_lst = list()

        cotn_num = 0

        for idx in range(len(expression)):
            if cotn_num != 0:
                cotn_num -= 1
                continue

            exp = expression[idx]

            if exp.isnumeric():
                if expression[idx + 1] == '.':
                    next_exp = expression[idx + 1]
                    if next_exp == '.':
                        precsions = ''
                        tmp_idx = idx + 2
                        while expression[tmp_idx].isnumeric():
                            precsions += expression[tmp_idx]
                            cotn_num += 2
                            tmp_idx += 1
                            if (tmp_idx + 1) >= len(expression):
                                break
                        if len(precsions):
                            exp = f'{exp}.{precsions}'
                            exp_lst.append(exp)
                else:
                    cotn_num = 0
                    next_exp = expression[idx + 1]
                    precsions = ''
                    tmp_idx = idx
                    while expression[tmp_idx].isnumeric():
                        precsions += expression[tmp_idx]
                        cotn_num += 1
                        tmp_idx += 1
                    if len(precsions):
                        print(precsions)

                    exp_lst.append(exp)

            elif exp == '(':
                stack.push(exp)
            elif exp == ')':
                while stack.peek() != '(':
                    exp_lst.append(stack.pop())
                stack.pop()
            elif CalculateExp.is_operator(exp):
                if (not stack.is_empty()) and (stack.peek() != '(') and CalculateExp.has_higher_precedence(stack.peek(), exp):
                    exp_lst.append(stack.pop())
                stack.push(exp)

        while not stack.is_empty():
            exp_lst.append(stack.pop())

        return exp_lst

    @staticmethod
    def eval_postfix(expression: typing.List[str]) -> float:
        stack = Stack()

        for exp in expression:
            if CalculateExp.is_number(exp):
                stack.push(float(exp))
            else:
                n2 = stack.pop()
                n1 = stack.pop()

                if exp == '+':
                    res = n1 + n2
                elif exp == '-':
                    res = n1 - n2
                elif exp == '*':
                    res = n1 * n2
                else:
                    res = n1 / n2
                stack.push(res)
        return stack.pop()

    @staticmethod
    def is_number(n: str) -> bool:
        if n.find('.') < 0:
            return n.isnumeric()
        return n.replace('.', '').isnumeric()


class CalculatorUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        qdarktheme.setup_theme()

        # layout
        self.__vbox_layout = QtWidgets.QVBoxLayout(self)
        self.__grid_layout = QtWidgets.QGridLayout()

        # vars
        self.__lineedit_exp = QtWidgets.QLineEdit()
        self.__lineedit_exp.setStyleSheet(stylesheet.LineEdit.get_iphone_style())
        self.__lineedit_exp.setReadOnly(True)
        self.__exp_lst = list()

        self._set_ui_btns()

        self.__vbox_layout.addWidget(self.__lineedit_exp)
        self.__vbox_layout.addLayout(self.__grid_layout)

        self.setLayout(self.__vbox_layout)

    def _set_ui_btns(self):
        btns_str = [
            'AC', '+/-', '%', '/',
            '7',  '8',   '9', '*',
            '4',  '5',   '6', '-',
            '1',  '2',   '3', '+',
            '0',  '',    '.', '='
        ]

        for i, bstr in enumerate(btns_str):
            if bstr == '':
                continue
            btn = QtWidgets.QPushButton(bstr)
            if bstr in ['AC', '+/-', '%']:
                style_str = stylesheet.PushButton.get_iphone_style('#E0E0E0')
            elif bstr in ['/', '*', '-', '+', '=']:
                style_str = stylesheet.PushButton.get_iphone_style('#FF7F00')
            else:
                style_str = stylesheet.PushButton.get_iphone_style('#707070')
            btn.setStyleSheet(style_str)
            btn.setFixedSize(80, 80)
            btn.clicked.connect(self.slot_clicked_btn)
            self.__grid_layout.addWidget(btn, int(i // 4), int(i % 4))

    def slot_clicked_btn(self):
        btn: QtWidgets.QPushButton = self.sender()
        # if not len(btn.text()):
        #     return
        # if re.match(r'[0-9/*.]|^\+$|^-$', btn.text()) is None:
        #     return
        # self.__exp_lst.append(btn.text())

        exp_str = self.__lineedit_exp.text().strip()

        ##
        if btn.text() == '=':
            exp_postfix = CalculateExp.infix_to_postfix(exp_str)
            print(exp_postfix)
            eval_postfix = CalculateExp.eval_postfix(exp_postfix)
            self.__lineedit_exp.setText(str(eval_postfix))
        elif btn.text() == 'AC':
            self.__lineedit_exp.clear()
        else:
            self.__lineedit_exp.setText(exp_str + btn.text())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    calc_ui = CalculatorUI()
    calc_ui.show()
    sys.exit(app.exec_())

    # c = CalculateExp()
    # exp_str = '((12 + 8) - 3) * (11.5 + 1) / 2.2 '
    # exp = c.infix_to_postfix(exp_str)
    # # exp = c.infix_to_postfix('(2 + 1.5) * 1')
    # print(exp)
    # res = c.eval_postfix(exp)
    # print(res)
    # print(res == eval(exp_str))



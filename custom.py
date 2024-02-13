import sys
import importlib
from PySide2 import QtWidgets, QtGui,QtCore
import calculator_ui
importlib.reload(calculator_ui)
#
# class Name:
#     class Number:
#
#


class Calculator(QtWidgets.QWidget, calculator_ui.Ui_Form):
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)
        self.setupUi(self)
        self._signal_func()

    def _signal_func(self):
        self.pushButton_0.clicked.connect(lambda: self.update_label(0))
        self.pushButton_1.clicked.connect(lambda: self.update_label(1))
        self.pushButton_2.clicked.connect(lambda: self.update_label(2))
        self.pushButton_3.clicked.connect(lambda: self.update_label(3))
        self.pushButton_4.clicked.connect(lambda: self.update_label(4))
        self.pushButton_5.clicked.connect(lambda: self.update_label(3))
        self.pushButton_6.clicked.connect(lambda: self.update_label(6))
        self.pushButton_7.clicked.connect(lambda: self.update_label(7))
        self.pushButton_8.clicked.connect(lambda: self.update_label(8))
        self.pushButton_9.clicked.connect(lambda: self.update_label(9))
        self.pushButton_sum.clicked.connect(lambda: self.update_label('+'))
        self.pushButton_sub.clicked.connect(lambda: self.update_label('-'))
        self.pushButton_mul.clicked.connect(lambda: self.update_label('x'))
        self.pushButton_div.clicked.connect(lambda: self.update_label('÷'))
        self.pushButton_dot.clicked.connect(lambda: self.update_label('.'))
        self.pushButton_clear.clicked.connect(self.clear_label)

        self.pushButton_result.clicked.connect(lambda: self.result_value)

    def update_label(self, number):
        current_text = self.label_value.text()
        new_text = current_text + str(number)

        self.label_value.setText(new_text)
    def clear_label(self):
        self.label_value.setText("")

    def result_value(self,num):
        current_text = self.label_value.text()
        clear_text = current_text.replace('x','*')
        clear_text = current_text.replace('÷','//')
        clear_text = eval(clear_text)
        print(clear_text)
        self.label_value.setText(str(clear_text))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    cus = Calculator()
    cus.show()
    sys.exit(app.exec_())

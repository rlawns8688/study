# !/usr/bin/env python
# encoding=utf-8

# author            : jeonghyeon park
# created data      : 2024.02.15
# modified data     : 2024.02.15
# description       :



# TODO : resume > reset > restart 시 스레드 동작 안되는거 고치기

import subprocess
import sys
import time
import datetime
# from builtins import range
from thread_timer.training.libs.algorithm.library import BitMask
from PySide2 import QtWidgets, QtCore, QtGui
import requests
import importlib
import typing
from bs4 import BeautifulSoup

import qt_timer_ui
importlib.reload(qt_timer_ui)
class Anim:
    ddi = {
        'mouse': '쥐띠',
        'cow': '소띠',
        'tiger': '호랑이띠',
        'rabbit': '토끼띠',
        'dragon': '용띠',
        'snake': '뱀띠',
        'horse': '말띠',
        'ramb': '양띠',
        'monkey': '원숭이띠',
        'chicken': '닭띠',
        'dog': '개띠',
        'pig': '돼지띠'
    }
class Constant:
    # read-only로 만들기 위함.
    __slots__ = ()
    # bit index
    START: typing.Final[int] = 1
    PAUSE: typing.Final[int] = 2
    STOP: typing.Final[int] = 4






class Btn_Switch:
    class XXX:
        lst = [False, False, False]
    class OOO:
        lst = [True, True, True]
    class XOO:
        lst = [False, True, True]
    class XXO:
        lst = [False, False, True]
    class XOX:
        lst = [False, True, False]
    class OXX:
        lst = [True, False, False]
    class OOX:
        lst = [True, True, False]
    class OXO:
        lst = [True, False, True]


class Signals(QtCore.QObject):
    time_update = QtCore.Signal(dict)
    dial_update = QtCore.Signal(int)
    pause_signal = QtCore.Signal(bool)
    reset_signal = QtCore.Signal(bool)
    fin_signal = QtCore.Signal(bool)



class Timer_Thread(QtCore.QThread):
    def __init__(self, dict_time, btn_lst=Btn_Switch.OXX.lst):
        super().__init__()
        self.signals = Signals()

        self.__bitfield: BitMask = BitMask()

        self.__btn_lst = btn_lst
        self.__dict_time = dict_time

        self.__is_pause = False
        self.__is_reset = False

        self.__condition = QtCore.QWaitCondition()
        self.__mutex = QtCore.QMutex()


        # init
        self.__bitfield.activate(Constant.STOP)
        self.__bitfield.deactivate(Constant.START | Constant.PAUSE)

    @property
    def bitfield(self):
        return self.__bitfield

    @property
    def dict_time(self):
        return self.__dict_time
    @dict_time.setter
    def dict_time(self, val):
        assert isinstance(val, dict)
        self.__dict_time = val

    @property
    def btn_lst(self):
        return self.__btn_lst
    @btn_lst.setter
    def btn_lst(self, val):
        assert isinstance(val, list)
        self.__btn_lst = val



    def run(self):
        _hour = self.dict_time['hour']
        _min = self.dict_time['min']
        _sec = self.dict_time['sec']
        update_dict = {}
        # cnt = 1

        total_time = _hour*3600 + _min*60 + _sec
        print(f'total sec = {total_time}')

        for t in range(total_time-1, -1, -1):
            print(self.btn_lst)
            dial_num = 100*(t/total_time)
            tick_hour = t // 3600
            temp = t % 3600
            tick_min = temp // 60
            tick_sec = temp % 60

            update_dict['hour'] = tick_hour
            update_dict['min'] = tick_min
            update_dict['sec'] = tick_sec


            # time pause
            if self.is_pause:
                self.__condition.wait(self.__mutex)
                self.signals.pause_signal.emit(True)

            # time reset
            if self.btn_lst[2] is True:
                print('나갑니다.')
                self.signals.reset_signal.emit(True)
                break


            # time ticking emit
            print(f'{tick_hour}h {tick_min}m {tick_sec}')
            self.signals.time_update.emit(update_dict)
            self.signals.dial_update.emit(dial_num)
            # cnt += 1
            time.sleep(1)

        # if reset >> Nothing
        # finish timer -> cmd start
        if not self.is_reset:
            self.signals.fin_signal.emit(True)


class Timer(QtWidgets.QWidget, qt_timer_ui.Ui_Form__timer):
    def __init__(self, parent=None):
        super().__init__(parent)
        # variable
        self.flag_ddi = False
        self.flag_btn = bin(00)
        self.dict_time = {'hour': 0, 'min': 0, 'sec': 0}
        self.__timer_thread = Timer_Thread(self.dict_time)
        self.flag_resume = False
        self.flag_start = False
        self.flag_reset = False

        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)

        self._signal()
        self.set_init()


    def set_init(self):
        self.set_timer(Btn_Switch.XXX.lst)
        self.set_button(Btn_Switch.XXX.lst)

        # LIMIT spin BOX
        self.spinBox__hour.setMaximum(12)
        self.spinBox__min.setMaximum(59)
        self.spinBox__sec.setMaximum(59)

        self.lcdNumber__viewer.display(f'{00:02d}:{00:02d}:{00:02d}')
        self.dial.setEnabled(False)

        self.spinBox__hour.setValue(0)
        self.spinBox__min.setValue(0)
        self.spinBox__sec.setValue(0)

        self.textBrowser__log.setText(f'{0:02d}:{0:02d}:{0:02d}')

        self.flag_resume = False
        self.flag_start = False
        self.flag_reset = False

        # set Time Widget
        _datetime = QtCore.QDateTime.currentDateTime()
        self.dateTimeEdit.setDateTime(_datetime)

        # self.dial.connect(Dial)
        # self.dial.mouseMoveEvent(QtGui.QMouseEvent)

    def _signal(self):
        # ddi setting
        self.comboBox__usr_ddi.addItems(Anim.ddi.values())
        self.comboBox__usr_ddi.activated.connect(self.set_combobox)

        # signal setting [SLOT]
        self.__timer_thread.signals.time_update.connect(self.slot_update_time)
        self.__timer_thread.signals.fin_signal.connect(self.slot_timer_fin)

        self.__timer_thread.signals.dial_update.connect(self.slot_update_dial)

     @QtCore.Slot(dict)
    def slot_update_time(self, val):
        self.spinBox__hour.setEnabled(False)
        self.spinBox__min.setEnabled(False)
        self.spinBox__sec.setEnabled(False)

        self.spinBox__hour.setValue(val['hour'])
        self.spinBox__min.setValue(val['min'])
        self.spinBox__sec.setValue(val['sec'])

        self.textBrowser__log.setText(f'{val["hour"]:02d}:{val["min"]:02d}:{val["sec"]:02d}')
        self.lcdNumber__viewer.display(f'{val["hour"]:02d}:{val["min"]:02d}:{val["sec"]:02d}')

    @QtCore.Slot(int)
    def slot_update_dial(self, val):
        self.dial.setValue(val)



    @QtCore.Slot(bool)
    def slot_timer_fin(self, val):
        if val is True:
            self.get_luck(self.comboBox__usr_ddi.currentText())
            self.set_button(Btn_Switch.XXX.lst)
        # self.set_timer(Btn_Switch.OOO.lst)
        # self.set_button(Btn_Switch.OXX.lst)

    # list to separate each arg and put in pushButton 1 2 3
    def set_timer(self, lst: list):
        self.spinBox__hour.setEnabled(lst[0])
        self.spinBox__min.setEnabled(lst[1])
        self.spinBox__sec.setEnabled(lst[2])

    # list to separate each arg and put in pushButton 1 2 3
    def set_button(self, lst: list):
        self.pushButton__start.setEnabled(lst[0])
        self.pushButton__pause.setEnabled(lst[1])
        self.pushButton__reset.setEnabled(lst[2])

    def set_combobox(self):
        print(self.comboBox__usr_ddi.currentIndex())
        print(self.comboBox__usr_ddi.currentText())
        self.frame.setLineWidth(10)

        self.set_timer(Btn_Switch.OOO.lst)
        self.set_button(Btn_Switch.OXX.lst)



    # TODO - start / when user finish to set the time. then time ticking



    # pause / pause time ticking
    # toggle

    # reset / zero setting

    def set_dial(self):
        self.dial.setValue(i for i in range(100, 1, -1))

    def get_luck(self, ddi='닭띠'):
        cmd = ['notify-send']
        # 웹 페이지에서 데이터 가져오기
        url = requests.get(f'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query={ddi}%20운세')
        html_content = url.text

        # BeautifulSoup 객체 생성
        soup = BeautifulSoup(html_content, 'html.parser')

        # 특정 클래스를 가진 <p> 태그 찾기
        target_p = soup.find('p', class_='text _cs_fortune_text')

        # 텍스트 추출
        if target_p:
            extracted_text = target_p.get_text()
            cmd.append(f'{extracted_text}')
            subprocess.run(cmd)
            print(extracted_text)
        else:
            print("No matching <p> tag found.")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    timer_ui = Timer()
    timer_ui.show()
    sys.exit(app.exec_())


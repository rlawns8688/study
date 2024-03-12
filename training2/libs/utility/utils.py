#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author        : Seongcheol Jeon
# created date  : 2024.02.15
# modified date : 2024.02.15
# description   :

import types
import typing
import functools
import threading
from PySide2 import QtWidgets, QtGui, QtCore

def print_string_void(func: types.FunctionType) -> typing.Callable:
    @functools.wraps(func)
    def __wrapper(*args, **kwargs) -> None:
        print()
        print('[{0}] {1:-^50}'.format('BEGIN', func.__name__), end='\n')
        result = func(*args, **kwargs)
        if result is not None:
            print(result)
        print('[{0}] {1:-^50}'.format('END', func.__name__), end='\n')
    return __wrapper

# 매개변수 타입 체크
class CheckType:
    def __init__(self, var_type: tuple):
        if not isinstance(var_type, tuple):
            raise TypeError('{0}은(는) {1}형식이 아닙니다.'.format(var_type, repr(tuple)))

        self.__var_type: tuple = var_type

    def __call__(self, func: typing.Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if len(self.__var_type) != len(args):
                raise ValueError('매개변수와 형식의 개수가 서로 다릅니다.')
            for i in range(len(args)):
                if not isinstance(args[i], self.__var_type[i]):
                    raise TypeError('{0}은(는) {1}형식이 아닙니다.'.format(args[i], repr(self.__var_type[i])))
            return func(args, kwargs)
        return wrapper


def using_thread(func: typing.Callable):
    def wrapper(*args):
        th = threading.Thread(target=func, args=args)
        th.start()
        return th
    return wrapper

def qtime2sec(qtime) -> int:
    h, m, s = qtime.hour(), qtime.minute(), qtime.second()
    total_sec = h * 3600 + m * 60 + s
    return total_sec

def sec2qtime(sec: int) -> QtCore.QTime:
    h, m = divmod(sec, 3600)
    m = m // 60
    s = sec % 60
    return QtCore.QTime(h, m, s)

def fit(val, smin, smax, dmin, dmax) -> float:
    if val > smax:
        return dmax
    if val < smin:
        return dmin
    return (val / (smax - smin)) + dmin

if __name__ == '__main__':
    pass

#!/usr/bin/env python
# encoding=utf-8

# author        : seongcheol jeon
# created date  : 2024.03.11
# modified date : 2024.03.11
# description   :

class CustomExcept(Exception):
    def __init__(self, *args, **kwargs):
        print('args: ', args)
        print('kwargs: ', kwargs)
        print('custom exception!!!!!!')
        self.username = kwargs.get('_user')


if __name__ == '__main__':
    pass

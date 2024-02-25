#!/usr/bin/env python
# encoding=utf-8

# author        : seongcheol jeon
# created date  : 2024.02.23
# modified date : 2024.02.23
# description   :

import shotgun_api3

class Task:
    def __init__(self, sg):
        self.sg = sg

    def add_version(self, add):
        return self.sg.create("Version", add)


if __name__ == '__main__':
    pass

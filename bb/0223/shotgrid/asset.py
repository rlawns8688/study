#!/usr/bin/env python
# encoding=utf-8
# author        :   kim junhyuk
# created date  :   2024.02.23
# modified date  :   2024.02.23
# description  :   
import os
class Asset:
    def __init__(self, sg, proj):
        self.proj = proj
        self.name = ""
        self.base_path = "/home/rapa/show"
        self.sg = sg
        pass

    def create(self):
        pass

    def make_dirs(self):
        os.makedirs(self.base_path + "/" + self.proj + "/" + self.name)

    # def get_shot_list(self):
    #     shot_list = self.sg.find("Shot", filters, fields)
    #     return shot_list

    def update(self, id, data):
        return self.sg.update('Sequence', id, data)


if __name__ == '__main__':
    pass

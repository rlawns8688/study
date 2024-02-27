#!/usr/bin/env python
# encoding=utf-8

# author        : seongcheol jeon
# created date  : 2024.02.23
# modified date : 2024.02.23
# description   :
import os
class Sequence:
    def __init__(self, sg, proj, seq_data):
        self.proj = proj
        self.id = seq_data['id']
        self.name = seq_data['code']
        self.base_path = "/home/rapa/show"
        self.sg = sg
        pass

    def create(self):
        pass

    def make_dirs(self):
        os.makedirs(self.base_path + "/" + self.proj.name + "/" + self.name)

    def get_shot_list(self):
        filters = [["sg_sequence",
                   "is",
                   {"id": self.id, "type": "Sequence"}
                 ]]
        shot_list = self.sg.find("Shot", filters, ['code'])
        return shot_list

if __name__ == '__main__':
    pass

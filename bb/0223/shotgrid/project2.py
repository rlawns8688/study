#!/usr/bin/env python
# encoding=utf-8
import os

# author        : seongcheol jeon
# created date  : 2024.02.23
# modified date : 2024.02.23
# description   :

import shotgun_api3

class Project:
    def __init__(self, sg):
        self.sg = sg

        self.base_path = "/home/rapa/show"

        pass

    def create(self):
        # self.sg.f
        pass
    def find_one2(self, name):
        filters = [['name', 'is', name]]
        fields = ['shots']
        print(self.sg.find_one('Project',filters,fields))
        return self.sg.find_one('Project',filters,fields)

    def get_seq_list(self):
        pass

    def make_dirs(self):
        os.makedirs(self.base_path + "/" + self.name)
        pass
    def update(self,update_data):
        pass

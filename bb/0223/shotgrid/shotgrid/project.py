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
        self.name = ""
        self.data = {}
        self.base_path = "/home/rapa/show"
        self.sg = sg
        pass

    def create(self):
        pass

    def find_one(self, name):
        self.data = self.sg.find_one('Project', [["name", 'is', name]], ["name"])
        self.id = self.data['id']
        self.name = self.data['name']
        # return self.name

    def get_seq_list(self):
        filters = [["project",
                   "is",
                   {"id": self.id, "type": "Project"}
                 ]]
        seqs = self.sg.find("Sequence", filters, ["code"])
        return seqs

    def make_dirs(self):
        try:
            os.makedirs(self.base_path + "/" + self.name)
        except:
            pass

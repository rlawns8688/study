#!/usr/bin/env python
# encoding=utf-8

# author        : seongcheol jeon
# created date  : 2024.02.23
# modified date : 2024.02.23
# description   :


class Version:
    def __init__(self, sg):
        pass

    def create(self, project, shot, task):
        new_data = {"code": "v02",
                    "project": project.data,
                    "entity": shot.data,
                    "sg_task": task.data}
        sg.create("Version", new_data)
        pass

    def find(self, project, shot, task):
        filter = [["project", "is", project],
                  ["shot", "is", shot],
                  ["task", "is", task]]
        field = []
        vers = sg.find("Version", filter, field)
        return vers
    
    


if __name__ == '__main__':
    pass

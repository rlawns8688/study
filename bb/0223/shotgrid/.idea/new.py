#!/usr/bin/env python
# encoding=utf-8
# author        :   kim junhyuk
# created date  :   2024.02.23
# modified date  :   2024.02.23
# description  :   
import shotgun_api3


class ShotgunEntity:
    def __init__(self, sg):
        self.sg = sg

    def find(self, filters, fields):
        entity_type = self.entity_type
        return self.sg.find(entity_type, filters, fields)

    # 여기에 더 많은 범용 메소드를 정의할 수 있습니다.


class Project(ShotgunEntity):
    entity_type = 'Project'

    # Project 특화 메소드
    def find_active_projects(self):
        filters = [['sg_status', 'is', 'Active']]
        fields = ['id', 'name', 'sg_status']
        return self.find(filters, fields)


class Sequence(ShotgunEntity):
    entity_type = 'Sequence'

    # Sequence 특화 메소드
    def find_sequence_by_code(self, project_id, code):
        filters = [['project', 'is', {'type': 'Project', 'id': project_id}], ['code', 'is', code]]
        fields = ['id', 'code']
        return self.find(filters, fields)


# Shotgun API 인스턴스 생성
sg = shotgun_api3.Shotgun(
    "https://rapa.shotgrid.autodesk.com",
    script_name='your_script_api',
    api_key='your_api_key'
)

# 해당 엔티티 타입 객체 생성 및 사용
project = Project(sg)
active_projects = project.find_active_projects()
print(active_projects)

sequence = Sequence(sg)
specific_sequence = sequence.find_sequence_by_code(project_id=123, code='SQ001')
print(specific_sequence)

if __name__ == '__main__':
    pass

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import shotgun_api3
import pprint

sg = shotgun_api3.Shotgun("https://rapa.shotgrid.autodesk.com",
                          script_name="hoesuk_script_api",
                          api_key="cvMvmpr5pavpuzm(acsggknec")
result = sg.find("Shot",
                 filters=[["sg_status_list", "is", "wtg"],
                          ["project", "is", {"id":123, "type": "Project"}]
                          ],
                 fields=["code", "sg_status_list", "project"])

data = {
    'description': 'Open on a beautiful field with fuzzy bunnies',
    'sg_status_list': 'ip'
    }
# result2 = sg.update('Asset', 1226, data)
#
# filters = [["task_assignees", "is", {"type": "HumanUser", "id": 154}]]
# task = sg.find("Task", filters=filters)
#
# target_task = task[0]
# new_data={"code": "v02",
#           "project": {'type': 'Project', 'id':70},
#           #"entity": {'type': 'Shot', 'id':00},
#           "sg_task": task[0]}
# new_ver = sg.create("Version", new_data)
# print(task)


import project

proj = project.Project(sg)
find = proj.find_one("DEMO: ANIMATION")
print(find)
proj.make_dirs()
seq_list = proj.get_seq_list()
pprint.pp(seq_list)
import sequence
# import shot
for seq_data in seq_list:
    seq = sequence.Sequence(sg, proj, seq_data)
    shot_list = seq.get_shot_list()
    # for shot in shot_list:
    #     shot = shot.Shot()
#

#
# filters = [["task_assignees", "is", {"type": "People", "id": 152}]]
# task = sg.find("Task", filters=filters)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    pass

import shotgun_api3
SERVER_PATH = "https://rapa.shotgrid.autodesk.com"
SCRIPT_NAME = "junhyuk_script_api"
SCRIPT_KEY = "ku@hsncnetgbtgrwwHs8zlxzi"
sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)
my_project = sg.find("Project", [["name","is","junhyuk"]], ["name", "id"])[0]
# print(project)
# project_list = sg.find("Project", [], ["name", "id"])
shot_desc ={
    "project" : my_project,
    "code" : "S004_0010",
    "description" : "This is a test shot",
    "sg_status_list" : "ip"
}

result_shot = sg.create("Shot",shot_desc)
print(result_shot)
version_desc = {
    "project": my_project,
    "code": shot_desc["code"] + "_v001.mov",
    "sg_status_list": "rev",
    "entity": result_shot,
    "sg_path_to_movie": "/home/rapa/Downloads/apples.mov",
}
# result = sg.find("Shot",
#                  filters=[["sg_status_list", "is", "wtg"],
#                           ["project", "is", {"id":123, "type": "Project"}]
#                           ],
#                  fields=["code", "sg_status_list", "project"])
#
# data = {
#     'description': 'Open on a beautiful field with fuzzy bunnies',
#     'sg_status_list': 'ip'
#     }
# result2 = sg.update('Asset', 1226, data)
#



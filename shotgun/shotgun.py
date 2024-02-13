import shotgun_api3
SERVER_PATH = "https://rapa.shotgrid.autodesk.com"
SCRIPT_NAME = "junhyuk_script_api"
SCRIPT_KEY = "ku@hsncnetgbtgrwwHs8zlxzi"
sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)
project = sg.find("Project", [["name","is","junhyuk"]], ["name", "id"])
# print(project)
# project_list = sg.find("Project", [], ["name", "id"])
shot_desc =  {
    "project" : project,
    "code" : "S004_0010",
    "description" : "This is a test shot",
    "sg_status_list" : "ip"
}

result_shot = sg.create("Shot",shot_desc)
print(result_shot)

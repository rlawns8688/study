import shotgun_api3
SERVER_PATH = "https://rapa.shotgrid.autodesk.com"
SCRIPT_NAME = "junhyuk_script_api"
SCRIPT_KEY = "ejpzbooaftirja7smy(Fnnovs"
sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)
my_project = sg.find("Project",[["id","is",127]], ["name", "id"])

# print(project)
# project_list = sg.find("Project", [], ["name", "id"])
shot_desc =  {
    "project" : my_project,
    "code" : "S004_0010",
    "description" : "This is a test shot",
    "sg_status_list" : "ip"
}

result_shot = sg.create("Shot",shot_desc)
print(result_shot)
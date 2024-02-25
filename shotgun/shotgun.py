import shotgun_api3
from pprint import pprint
sg = shotgun_api3.Shotgun(
            "https://rapa.shotgrid.autodesk.com",
                        script_name='junhyuk_script_api',
                        api_key= 'ahywvbPlczeldyxxig2o$kirh')

# result = sg.find_one("Project",
#                  filters=[
#                           ['name', 'is','JUNHYUK']
#                           ], #is는 양옆에 같음
#                  fields=['Project'])
# pprint(result)
#
# result = sg.find('Sequence',
#                  filters=[["project", "is", {"id":123, "type": "Project"}]], #is는 양옆에 같음
#                  fields=['shot'])
pprint(result)
#is는 양옆에 같음
# result = sg.delete("Shot", 865)
# data = {
#     'description': 'hi im junhyuk',
#     'sg_status_list': 'rev'
#     }
# result = sg.update('Version',673, data)



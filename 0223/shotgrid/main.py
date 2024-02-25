# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import shotgun_api3
import pprint
sg = shotgun_api3.Shotgun("https://rapa.shotgrid.autodesk.com",
                          script_name="hoesuk_script_api",
                          api_key="cvMvmpr5pavpuzm(acsggknec")


import project2
import asset
import sequence
import version
proj = project2.Project(sg)
seq =  sequence.Sequence2(sg, 'Demo: Animation')
ver = version.Version(sg)
data = {'description': 'zzz'}
seq.update(23, data)
new_data = {
    'code': 'upupupup',
    'project': {'type': 'Project', 'id': 70},
    'entity': {'type': 'Shot', 'id': 865}}

ver.add(new_data)
# proj.find_one2("Demo: Animation")

# proj.make_dirs()
# seq_list = proj.get_seq_list()
#
# from . import sequence
# for seq_data in seq_list:
#     seq = sequence.Sequence(sg, proj.name, seq_data)
#
# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#

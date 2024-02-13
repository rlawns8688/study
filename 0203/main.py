import sys, os, json
import re
import subprocess
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
from PySide2 import QtUiTools
import hou
class AutoRenderApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.dir_path = '/home/rapa/python/0203'
        self.initUI()
        self.loadData()
        self.qtConnect()

    def loadData(self):
        with open(self.dir_path + '/shotInfo.json', 'r') as openfile:
            self.shotInfo = json.load(openfile)
            print("self.shotInfo", self.shotInfo)
        self.ui.tree_shot.clear()
        for shot in self.shotInfo.keys():
            print(shot)
            child = QTreeWidgetItem(self.ui.tree_shot)
            child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
            child.setText(0, shot)
            child.setToolTip(0, str(self.shotInfo[shot]))
            child.setCheckState(0, Qt.Checked)

    def create_hip(self, shot, data):

        # clear houdini
        hou.hipFile.clear(suppress_save_prompt=True)

        # set frame range
        start_frame = 1001
        end_frame = 1050
        hou.setFps(int(24))
        globFrameSetExpr = "tset `({0}-1)/$FPS` `{1}/$FPS`".format(int(start_frame), int(end_frame))
        hou.hscript(globFrameSetExpr)
        hou.playbar.setPlaybackRange(int(start_frame), int(end_frame))
        n_obj = hou.node("/obj")

        # camera
        n_cam = n_obj.createNode("cam")
        n_cam.parm("tx").set(data['cam_transform'][0])
        n_cam.parm("ty").set(data['cam_transform'][1])
        n_cam.parm("tz").set(data['cam_transform'][2])

        # cam rotation
        n_cam.parm("rx").set(data['cam_rotation'][0])
        n_cam.parm("ry").set(data['cam_rotation'][1])
        n_cam.parm("rz").set(data['cam_rotation'][2])

        # fx geo
        n_fx = n_obj.createNode("geo", "fx")
        self.set_node_pos(n_fx, n_cam.position(), 0, -1)

        # testGeo
        n_testGeo = n_fx.createNode(f"testgeometry_{data['geo_type']}")

        # null out Geo
        n_null_out_geo = n_fx.createNode("null", "OUT_GEO")
        n_null_out_geo.setInput(0, n_testGeo)
        self.set_node_pos(n_null_out_geo, n_testGeo.position(), -2, 0)

        # add otl - ElectrickShock
        n_electricShock = n_fx.createNode("ElectrickShock")
        n_electricShock.setInput(0, n_testGeo)
        self.set_node_pos(n_electricShock, n_testGeo.position(), 0, -1)

        # set key
        u_key_start = hou.Keyframe()
        u_key_start.setFrame(start_frame)
        u_key_start.setValue(0)
        n_electricShock.parm("domainu2").setKeyframe(u_key_start)
        u_key_end = hou.Keyframe()
        u_key_end.setFrame(end_frame)
        u_key_end.setValue(1)
        n_electricShock.parm("domainu2").setKeyframe(u_key_end)

        # null out Geo
        n_null_out_fx = n_fx.createNode("null", "OUT_FX")
        n_null_out_fx.setInput(0, n_electricShock)
        self.set_node_pos(n_null_out_fx, n_electricShock.position(), 2, 0)


        # merge geo with otl
        n_merge = n_fx.createNode("merge")
        n_merge.setInput(0, n_testGeo)
        n_merge.setInput(1, n_electricShock)
        n_merge.setDisplayFlag(True)
        self.set_node_pos(n_merge, n_electricShock.position(), -1, -1)

        # object_merge geo
        n_out_geo = n_obj.createNode("geo", "out_geo")
        n_out_geo.setDisplayFlag(False)
        self.set_node_pos(n_out_geo, n_fx.position(), 0, -1)
        n_out_geo_obj_merge = n_out_geo.createNode("object_merge")
        n_out_geo_obj_merge.parm("objpath1").set(n_null_out_geo.path())
        # object_merge fx
        n_out_fx = n_obj.createNode("geo", "out_fx")
        n_out_fx.setDisplayFlag(False)
        self.set_node_pos(n_out_fx, n_out_geo.position(), 0, -1)
        n_out_fx_obj_merge = n_out_fx.createNode("object_merge")
        n_out_fx_obj_merge.parm("objpath1").set(n_null_out_fx.path())


        # shot dir
        shot_dir_path = os.path.join(self.dir_path, shot)
        # get highest version num
        list_version = []
        for file_name in os.listdir(shot_dir_path):
            res_search = re.match("v\d+(.hip)$", file_name.split("_")[-1])
            if res_search:
                match_string = res_search.group()
                list_version.append(int(re.sub(r'[^0-9]', '', match_string)))
        max_ver = (max(list_version) + 1) if len(list_version) > 0 else 1
        str_ver = "_v" + str(max_ver).zfill(3)
        print("version : ", max_ver)
        hip_path = os.path.join(shot_dir_path, shot + str_ver + ".hip")

        # hip save
        hou.hipFile.save(hip_path)



        # --------- OUT
        # rd geo
        n_out = hou.node("/out")
        n_geo_rd = n_out.createNode("opengl", "rd_geo")
        n_geo_rd.parm("trange").set(1)
        n_geo_rd.parm("f1").set(start_frame)
        n_geo_rd.parm("f2").set(end_frame)
        img_dir = hip_path.replace(".hip", "_geo")
        os.makedirs(img_dir, exist_ok=True)
        img_path = os.path.join(img_dir, os.path.basename(img_dir) + "_$F4.exr")
        n_geo_rd.parm("picture").set(img_path)
        n_geo_rd.parm("vobjects").set("") # candidate obj
        n_geo_rd.parm("forceobjects").set(n_out_geo.path()) # force obj
        print("start render geo!!")
        n_geo_rd.parm("execute").pressButton()
        print("end render geo!!")

        # rd fx
        n_fx_rd = n_out.createNode("ifd", "rd_fx")
        self.set_node_pos(n_fx_rd, n_geo_rd.position(), 0, -1)
        n_fx_rd.parm("trange").set(1)
        img_dir = hip_path.replace(".hip", "_fx")
        os.makedirs(img_dir, exist_ok=True)
        img_path = os.path.join(img_dir, os.path.basename(img_dir) + "_$F4.exr")
        n_fx_rd.parm("vm_picture").set(img_path)
        n_fx_rd.parm("vm_dorayvariance").set(True) # too long time
        n_fx_rd.parm("vm_samplesx").set(5)  # too long time
        n_fx_rd.parm("vm_samplesy").set(5)  # too long time
        n_fx_rd.parm("vobject").set("") # candidate obj
        n_fx_rd.parm("forceobject").set(n_out_fx.path()) # force obj
        n_fx_rd.parm("matte_objects").set(n_out_geo.path()) # matte obj
        print("start render fx!!")
        n_fx_rd.parm("execute").pressButton()
        print("end render fx!!")
        # hip save
        hou.hipFile.save(hip_path)

    def initUI(self):
        self.ui = QtUiTools.QUiLoader().load(os.path.join(self.dir_path, "my.ui"))

        self.setWindowTitle("Auto Render")
        self.resize(460,650)
        header = self.ui.tree_shot.header()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        header.setStretchLastSection(False)
        self.setCentralWidget(self.ui)
        self.show()

    def set_node_pos(self, node, base_pos, add_x, add_y):
        node.setPosition((base_pos[0] + add_x, base_pos[1] + add_y))

    def qtConnect(self):
        self.ui.btn_run.clicked.connect(self.onRun)
    def onRun(self):
        list_works = self.get_checked_words()
        for work_i, dict_data in enumerate(list_works):
            print(list_works)
            for shot, data in dict_data.items():

                print(f'wfefwef{shot}')
                self.create_hip(shot, data)
            self.ui.progressBar.setValue(int((work_i +1) / len(list_works) * 100))
    def get_checked_words(self):
        root = self.ui.tree_shot.invisibleRootItem()
        column = 0
        list_works = []
        for idx in range(root.childCount()):
            tree_item = root.child(idx)
            shot = tree_item.text(column)
            check_state = tree_item.checkState(column)
            if check_state == Qt.Checked:
                dict_data = {shot: self.shotInfo[shot]}
                list_works.append(dict_data)
        return list_works




if __name__ == "__main__":
    app = QApplication(sys.argv)
    myApp = AutoRenderApp()
    app.exec_()

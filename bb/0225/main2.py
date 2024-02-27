import sys, os, json
import re
import subprocess
from datetime import datetime
import requests

sys.path.append("/home/rapa/anaconda3/envs/houdini/lib/python3.9/site-packages")
import pandas as pd
print(pd.__version__)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# pyside2
from PySide2.QtWidgets import *
from PySide2 import QtGui
from PySide2.QtCore import Qt, SIGNAL, QSize
from PySide2 import QtUiTools


import hou

class AutoRenderApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.dir_path = "clas folder dir"
        self.dir_path = os.path.dirname(os.path.abspath(__file__))
        self.shotInfo = None

        self.shot_tree_column = {"shot_code": 0, "mov": 1, "hip": 2, "nk": 3, "start_date": 4, "due_date": 5, "task": 6}

        self.loadData()
        self.initUI()
        self.qtConnect()

        self.onPresetChanged(-1)
        self.onUpdate_shot_tree()
    # ---------------------  ani pub data ---------------------
        self.df_ani_pub = pd.read_csv(os.path.join(self.dir_path, "sg_ani_pub_info.csv"))
        self.df_ani_pub = self.df_ani_pub.dropna(subset=["shot_code"])
        self.df_ani_pub = self.df_ani_pub.loc[self.df_ani_pub.groupby(["shot_code"])["pub_ver"].idxmax()]

        self.df_sg = pd.merge(self.df_sg, self.df_ani_pub, on = 'shot_code', how='left')


         # rename
        dict_rename = {"pub_status": "ani_pub_status"
                        , "pub_ver":"ani_pub_ver"
                        , "updated_at": "ani_pub_updated_time"}
        self.df_ani_pub.rename(columns=dict_rename, inplace=True)
        self.df_ani_pub['ani_pub_updated_time'] = self.df_ani_pub['ani_pub_updated_time'].apply(self.redefine_datetime)
        self.df_ani_pub = self.df_ani_pub[["shot_code", "ani_pub_status", "ani_pub_ver", "ani_pub_updated_time"]]

    # ---------------------  ani status ---------------------
        self.df_ani_status = pd.read_csv(os.path.join(self.dir_path, "sg_ani_status_info.csv"))
        self.df_ani_status = self.df_ani_status.dropna(subset=["shot_code"])

        self.df_ani_status.rename(columns={"status":"ani_status"}, inplace=True)
        self.df_ani_status = self.df_ani_status[["shot_code", "ani_status"]]

        self.df_sg = pd.merge(self.df_sg, self.df_ani_status, on="shot_code", how="left")

        self.load_file_data_info(self.df_sg)

        print(self.df_sg)
        print(self.df_sg.dtypes)

    def loadData(self):
        str_none_date = "1111-11-11"
        self.df_sg = pd.read_csv(os.path.join(self.dir_path, "sg_fx_info.csv"))
        self.df_sg["start_date"] = self.df_sg["start_date"].fillna(str_none_date)
        self.df_sg["due_date"] = self.df_sg["due_date"].fillna(str_none_date)  # change none date

        self.df_sg['isPastStartDate'] = self.df_sg['start_date'].apply(self.redefine_past_start_date)
    def redefine_datetime(self, str_date_time):
        dt_date = datetime.strptime(str(str_date_time), "%Y-%m-%d %H:%M:%S")
        return dt_date

    def onPresetChanged(self, index):
        strPreset = self.ui.cb_preset.currentText().lower().strip()
        print("strPreset", strPreset)
        if strPreset == "preset_todo" or strPreset == "preset_ing":
            # -- Uncheck All Filters
            self.uncheck_all_filters()
            self.onUpdate_shot_tree()

        else:  # custom
            # enable group box
            self.ui.gb_filter_project.setEnabled(True)
            self.ui.gb_filter_shot_status.setEnabled(True)
            self.ui.gb_filter_ani.setEnabled(True)
            self.ui.gb_filter_fx_status.setEnabled(True)

    def uncheck_all_filters(self):
        # uncheck shot status
        self.changeCheckBox(False, self.ui.ck_shot_stat_all, self.onCheckShotStatusChangedAll)
        self.changeCheckBoxGroup(False, self.ui.frame_shot_status_cks, self.onUpdate_shot_tree, False)
        # uncheck ani pub
        self.changeCheckBox(False, self.ui.ck_aniPub_all, self.onCheckAniPubChangedAll)
        self.changeCheckBoxGroup(False, self.ui.frame_aniPub_status_cks, self.onUpdate_shot_tree, False)
        # uncheck ani status
        self.changeCheckBox(False, self.ui.ck_ani_stat_all, self.onCheckAniStatusChangedAll)
        self.changeCheckBoxGroup(False, self.ui.frame_ani_status_cks, self.onUpdate_shot_tree, False)
        # uncheck compare to render log
        self.changeCheckBox(False, self.ui.ck_cmp_render_log_all, self.onCheckCmpRenderLogChangedAll)
        self.changeCheckBoxGroup(False, self.ui.frame_cmp_render_log, self.onUpdate_shot_tree, False)
        # uncheck Compare start date
        self.changeCheckBox(False, self.ui.ck_cmp_startDate, self.onUpdate_shot_tree)
        # uncheck Fx status
        self.changeCheckBox(False, self.ui.ck_fx_stat_all, self.onCheckFxStatusChangedAll)
        self.changeCheckBoxGroup(False, self.ui.frame_fx_status_cks, self.onUpdate_shot_tree, False)

    def onCheckShotStatusChangedAll(self, state):
        self.changeCheckBoxGroup(state, self.ui.frame_shot_status_cks, self.onUpdate_shot_tree)
    def onCheckAniPubChangedAll(self, state):
        self.changeCheckBoxGroup(state, self.ui.frame_aniPub_status_cks, self.onUpdate_shot_tree)
    def onCheckAniStatusChangedAll(self, state):
        self.changeCheckBoxGroup(state, self.ui.frame_ani_status_cks, self.onUpdate_shot_tree)
    def onCheckFxStatusChangedAll(self, state):
        self.changeCheckBoxGroup(state, self.ui.frame_fx_status_cks, self.onUpdate_shot_tree)
    def onCheckCmpRenderLogChangedAll(self, state):
        self.changeCheckBoxGroup(state, self.ui.frame_cmp_render_log, self.onUpdate_shot_tree)




    def changeCheckBoxGroup(self, state ,ui_parent, connectFunc, isNeedUpdate=True):
        for ck_box in ui_parent.findChildren(QCheckBox):
            self.changeCheckBox(state, ck_box, connectFunc)

        if isNeedUpdate == True:
            self.onUpdate_shot_tree()

    def changeCheckBox(self, state, ck_box, connectFunc=None):
        if connectFunc and ck_box.receivers(SIGNAL("stateChanged(int)")) > 0:
            ck_box.stateChanged.disconnect(connectFunc)
        # change status
        ck_box.setCheckState(Qt.Checked if state else Qt.Unchecked)
        if connectFunc:
            ck_box.stateChanged.connect(connectFunc)


    def initUI(self):
        self.ui = QtUiTools.QUiLoader().load(os.path.join(self.dir_path, "auto.ui"))

        # title
        self.setWindowTitle("Auto Render")
        self.resize(400, 700)

        # ---------------------  project comboBox ---------------------
        self.ui.combo_project.addItems(self.get_project())

        # qtree widget header resize
        header = self.ui.tree_shot.header()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        header.setStretchLastSection(False)

        # ---------------------  sync ---------------------
        iconpath = os.path.join(self.dir_path,"ui_resource/sync.png")
        icon_sync = QtGui.QIcon()
        icon_sync.addFile(iconpath, QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.btn_reload_data.setIcon(icon_sync)


        # ---------------------  folding ---------------------
        self.init_fold()

        self.setCentralWidget(self.ui)
        self.show()

    def init_fold(self):
        iconpath = os.path.join(self.dir_path, "ui_resource/arrow_right.png")
        self.icon_arrow_right = QtGui.QIcon()
        self.icon_arrow_right.addFile(iconpath, QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        iconpath = os.path.join(self.dir_path, "ui_resource/arrow_down.png")
        self.icon_arrow_down = QtGui.QIcon()
        self.icon_arrow_down.addFile(iconpath, QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.dict_is_folded = {}
        # ani
        self.ui.btn_fold_ani.setIcon(self.icon_arrow_down)
        self.dict_is_folded[self.ui.btn_fold_ani.objectName()] = False
        # taks
        self.ui.btn_fold_task.setIcon(self.icon_arrow_down)
        self.dict_is_folded[self.ui.btn_fold_task.objectName()] = False
        # user
        self.ui.btn_fold_user.setIcon(self.icon_arrow_down)
        self.dict_is_folded[self.ui.btn_fold_user.objectName()] = False
        # fx
        self.ui.btn_fold_fx.setIcon(self.icon_arrow_down)
        self.dict_is_folded[self.ui.btn_fold_fx.objectName()] = False

        # init fold
        self.onFoldingGroupBox(self.ui.btn_fold_task)
        self.onFoldingGroupBox(self.ui.btn_fold_user)

    def onOpenFolder(self):
        curr_tree_item = self.ui.tree_shot.currentItem()
        shot_code_col = self.shot_tree_column["shot_code"]

        shot = curr_tree_item.text(shot_code_col)

        path_open_dir = os.path.join(self.dir_path, shot)

        if not os.path.exists(path_open_dir):
            path_open_dir = self.dir_path

        os.system("nautilus " +  path_open_dir + " &")



    def onFoldingGroupBox(self, button):
        isFold = not (self.dict_is_folded[button.objectName()])
        groupBox = button.parent()
        parent_groupBox = groupBox.parent()

        if parent_groupBox.__class__.__name__ != "QGroupBox":
            print("onFoldingGroupBox - parent is not QGroupBox :", parent_groupBox.__class__.__name__)
            return

        if isFold == True:
            button.setIcon(self.icon_arrow_right)
        else:
            button.setIcon(self.icon_arrow_down)

        for child in parent_groupBox.children():
            try:
                child.setVisible(not isFold)
            except:
                continue
        # update
        self.dict_is_folded[button.objectName()] = isFold
        # title group box always visible - True
        groupBox.setVisible(True)

    def qtConnect(self):
        self.ui.btn_run.clicked.connect(self.onRun)

        # combobox - preset
        self.ui.cb_preset.currentIndexChanged.connect(self.onPresetChanged)

        # ---------------------  folding ---------------------
        self.ui.btn_fold_ani.clicked.connect(
            lambda state=None, btn_widget=self.ui.btn_fold_ani: self.onFoldingGroupBox(btn_widget))
        self.ui.btn_fold_task.clicked.connect(
            lambda state=None, btn_widget=self.ui.btn_fold_task: self.onFoldingGroupBox(btn_widget))
        self.ui.btn_fold_user.clicked.connect(
            lambda state=None, btn_widget=self.ui.btn_fold_user: self.onFoldingGroupBox(btn_widget))
        self.ui.btn_fold_fx.clicked.connect(
            lambda state=None, btn_widget=self.ui.btn_fold_fx: self.onFoldingGroupBox(btn_widget))

        # ---------------------  shot tree right click menu ---------------------
        self.ui.tree_shot.customContextMenuRequested.connect(self.onTreewidget_menu)

    def onTreewidget_menu(self, position):
        # this function is  qtree widget(shotcode) right mouse click menu
        index = self.ui.tree_shot.indexAt(position)

        # column
        shot_code_col = self.shot_tree_column["shot_code"]
        task_col = self.shot_tree_column["task"]

        if not index.isValid():
            return

        curr_item = self.ui.tree_shot.itemFromIndex(index)
        shot_code = curr_item.text(shot_code_col)
        task = curr_item.text(task_col)

        menu = QMenu(self.ui.tree_shot)

        # ---------------------  open folder ---------------------
        act_open_folder = QAction("Open Folder")
        act_open_folder.triggered.connect(lambda checked=None: self.onOpenFolder())

        menu.addAction(act_open_folder)

        # get dir
        path_job_dir = os.path.join(self.dir_path, shot_code)

        # # ---------------------  mov ---------------------
        # name_mov = self.get_one_df_data(shot_code, task, "last_mov")
        # if name_mov:
        #     path_mov = os.path.join(path_job_dir, name_mov)
        #     act_play_mov = QAction("Play Mov", self)
        #     act_play_mov.triggered.connect(
        #         lambda checked=None, path_mov=path_mov: self.onActPlayMov(path_mov))
        #     menu.addAction(act_play_mov)
        #
        #     # shotgrid upload mov
        #     act_upload_sg = QAction("Upload ShotGrid", self)
        #     menu.addAction(act_upload_sg)
        #
        # # set nk action
        # name_nk = self.get_one_df_data(shot_code, task, "last_nk")
        # if name_nk:
        #     path_nk = os.path.join(path_job_dir, name_nk)
        #     act_open_nk = QAction("Open Nuke", self)
        #     act_open_nk.triggered.connect(
        #         lambda checked=None, path_nk=path_nk: self.onActOpenNk(path_nk))
        #     menu.addAction(act_open_nk)
        #
        # # set hip action
        # name_hip = self.get_one_df_data(shot_code, task, "last_hip")
        # if name_hip:
        #     path_hip = os.path.join(path_job_dir, name_hip)
        #     act_open_hip = QAction("Open Houdini", self)
        #     act_open_hip.triggered.connect(
        #         lambda checked=None, path_hip=path_hip: self.onActOpenHip(path_hip))
        #     menu.addAction(act_open_hip)
        #
        # # the function to display context menu
        menu.exec_(self.ui.tree_shot.mapToGlobal(position))

    def onUpdate_shot_tree(self):
        query = self.getCheckedFiltersQuery()
        # query = None
        # print(query)
        if query:
            self.df_sg_filtered = self.df_sg.query(query)
        else:
            self.df_sg_filtered = self.df_sg
        print(">>>>>>>>> onUpdate")

        shot_col = self.shot_tree_column["shot_code"]
        start_date_col = self.shot_tree_column["start_date"]
        due_date_col = self.shot_tree_column["due_date"]
        task_col = self.shot_tree_column["task"]

        self.ui.tree_shot.clear()
        #ck_state_all = self.ui.ck_all_shotcode.checkState()
        list_filtered_data = self.df_sg_filtered.to_dict("records")

        for dict_data in list_filtered_data:
            task = dict_data["task"]
            shot_code = dict_data["shot_code"]

            child = QTreeWidgetItem(self.ui.tree_shot)
            child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
            child.setCheckState(shot_col, Qt.Unchecked)

            child.setText(shot_col, shot_code)
            child.setText(start_date_col, dict_data["start_date"])  # start_date
            child.setText(due_date_col, dict_data["due_date"])  # due_date
            child.setText(task_col, task)  # task

    def getCheckedFiltersQuery(self):

        list_query = []

        # get checked ani pub status
        ani_pub_query = self.get_checked_query(self.ui.frame_aniPub_status_cks, "ani_pub_status")
        if ani_pub_query:
            list_query.append(ani_pub_query)

        # get checked ani status
        ani_stat_query = self.get_checked_query(self.ui.frame_ani_status_cks, "ani_status")
        if ani_stat_query:
            list_query.append(ani_stat_query)

        # get checked shot status
        shot_stat_query = self.get_checked_query(self.ui.frame_shot_status_cks, "shot_status")
        if shot_stat_query:
            list_query.append(shot_stat_query)

        # get Compare Start Date
        if self.ui.ck_cmp_startDate.checkState() == Qt.Checked:
            list_query.append("(isPastStartDate == True)")

        # get checked fx status
        fx_stat_query = self.get_checked_query(self.ui.frame_fx_status_cks, "status")
        if fx_stat_query:
            list_query.append(fx_stat_query)

        # # get checked cmp render log
        # cmp_render_log_query = self.get_checked_rd_log_query(self.ui.frame_cmp_render_log)
        # if cmp_render_log_query:
        #     list_query.append(cmp_render_log_query)
        #
        # # get checked tasks
        # task_query = self.getCheckedTasksQuery()
        # if task_query:
        #     list_query.append(task_query)
        #
        # # get checked users
        # user_query = self.getCheckedUsersQuery()
        # if user_query:
        #     list_query.append(user_query)
        #
        # combine query
        query = " & ".join(list_query)
        return query

    def get_checked_query(self, ui_parent, column_name):
        list_checked = []
        for ck_box in ui_parent.findChildren(QCheckBox):
            if ck_box.checkState() == Qt.Checked:
                qt_obj_name = ck_box.objectName()
                list_checked.append(qt_obj_name.split("_")[-1])

        query = " | ".join(["{} == '{}'".format(column_name, status) for status in list_checked])
        if query:
            query = "(" + query + ")"
            return query
        else:
            return None

    def get_checked_works(self):
        # 시퀀스 샷 tree 체크 검사.
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
    def get_checked_rd_log_query(self, ui_parent):
       list_query = []
       for ck_box in ui_parent.findChildren(QCheckBox):
           if ck_box.checkState() == Qt.Checked:
               qt_obj_name = ck_box.objectName()

               if qt_obj_name == "ck_cmp_ani_pub_ver":
                   list_query.append("ani_pub_ver > log_last_ani_pub_ver")
               if qt_obj_name == "ck_cmp_ani_update_time":
                   list_query.append("ani_pub_updated_time > log_last_render_time")

       query = " | ".join(list_query)
       if query:
           query = "(" + query + ")"
           return query
       else:
           return None
    def onRun(self):
        list_works = self.get_checked_works()
        for work_i, dict_data in enumerate(list_works):
            for shot, data in dict_data.items():
                print(f"------------ run {shot} -------------")
                self.create_hip(shot, data)
            self.ui.progressBar.setValue(int((work_i + 1) / len(list_works) * 100))

    def redefine_date(self, str_date):
        dt_date = datetime.strptime(str(str_date), "%Y-%m-%d")
        return dt_date

    def redefine_past_start_date(self, start_date):
        dt_start_date = self.redefine_date(start_date)
        if dt_start_date.date() < datetime.now().date():
            return True
        else:
            return False


    def get_project(self):
        return sorted(self.df_sg["project"].drop_duplicates().to_list())

    def set_node_pos(self, node, base_pos, add_x, add_y):
        node.setPosition((base_pos[0] + add_x, base_pos[1] + add_y))

    def create_hip(self, shot, data):
        # clear houdini
        hou.hipFile.clear(suppress_save_prompt=True)

        # set frame range
        start_frame = 1001
        end_frame = 1010

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
        n_electricShock = n_fx.createNode("ElectricShock")
        n_electricShock.setInput(0,n_testGeo)
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
        n_merge.setInput(0,n_testGeo)
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
        shot_dir_path = os.path.join(self.dir_path, shot) # =C:\Class\AAA_001

        # get highest version num
        list_version = []
        for file_name in os.listdir(shot_dir_path):
            res_search = re.match("v\d+(.hip)$", file_name.split("_")[-1])
            if res_search:
                match_string = res_search.group()
                list_version.append(int(re.sub(r'[^0-9]', '', match_string)))
        #TODO max_ver = (max(list_version) + 1) if len(list_version) > 0 else 1
        max_ver = (max(list_version)) if len(list_version) > 0 else 1
        str_ver = "_v" + str(max_ver).zfill(3)
        print("version : ", max_ver)


        hip_path = os.path.join(shot_dir_path, shot + str_ver + ".hip")

        # hip save
        #TODO hou.hipFile.save(hip_path)


        # --------- OUT
        # rd geo
        n_out = hou.node("/out")
        n_geo_rd = n_out.createNode("opengl", "rd_geo")
        n_geo_rd.parm("trange").set(1)
        n_geo_rd.parm("f1").set(start_frame)
        n_geo_rd.parm("f2").set(end_frame)
        img_dir = hip_path.replace(".hip", "_geo")
        os.makedirs(img_dir, exist_ok=True)
        img_path_geo = os.path.join(img_dir, os.path.basename(img_dir) + "_$F4.jpg")
        n_geo_rd.parm("picture").set(img_path_geo)
        n_geo_rd.parm("vobjects").set("")  # candidate obj
        n_geo_rd.parm("forceobjects").set(n_out_geo.path())  # force obj

        print("start render geo!!")
        #TODO n_geo_rd.parm("execute").pressButton()
        print("end render geo!!")

        # rd fx
        n_fx_rd = n_out.createNode("ifd", "rd_fx")
        self.set_node_pos(n_fx_rd, n_geo_rd.position(), 0, -1)
        n_fx_rd.parm("trange").set(1)
        img_dir = hip_path.replace(".hip", "_fx")
        os.makedirs(img_dir, exist_ok=True)
        img_path_fx = os.path.join(img_dir, os.path.basename(img_dir) + "_$F4.jpg")
        n_fx_rd.parm("vm_picture").set(img_path_fx)
        n_fx_rd.parm("vm_dorayvariance").set(False)  # too long time
        n_fx_rd.parm("vm_samplesx").set(1)  # too long time
        n_fx_rd.parm("vm_samplesy").set(1)  # too long time
        n_fx_rd.parm("vobject").set("")  # candidate obj
        n_fx_rd.parm("forceobject").set(n_out_fx.path())  # force obj
        n_fx_rd.parm("matte_objects").set(n_out_geo.path())  # matte obj

        print("start render fx!!")
        #TODO n_fx_rd.parm("execute").pressButton()
        print("end render fx!!")

        # to nk.py argument
        nk_arg = {"start_frame": start_frame ,"end_frame": end_frame
            , "nk_geo": img_path_geo.replace("_$F4.jpg", "_%04d.jpg")
            , "nk_fx": img_path_fx.replace("_$F4.jpg", "_%04d.jpg")
            , "nk_mov": hip_path.replace(".hip", ".mov")
            , "nk_path" : hip_path.replace(".hip",".nk")
        }


        # hip save
        #TODO hou.hipFile.save(hip_path)
        # -E     : ignore PYTHON* environment variables (such as PYTHONPATH)
        cmd = [r'C:\Program Files\Nuke15.0v1\python.exe', '-E', os.path.join(self.dir_path, "nk.py"), json.dumps(nk_arg)]
        p = subprocess.run(cmd)  #  , env={} 환경변수 충돌로 에러가 발생해서 환경 변수를 env={}로 모두 삭제하

        print("def create_hip done ~~~!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myApp = AutoRenderApp()
    app.exec_()
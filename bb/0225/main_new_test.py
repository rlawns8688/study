import file_manager

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1210881532605112363/awDJEzXNBatRT6bg92bN-PqyqClkB7WexkohDUuXvdfJgMmnjWugne5N21g-qExqmQ2w"

# # pyside2
# from PySide2.QtWidgets import *
# from PySide2.QtCore import Qt
# from PySide2 import QtUiTools

# TODO mofiy
# pyside2
from PySide2.QtWidgets import *
from PySide2 import QtGui
from PySide2.QtCore import Qt, SIGNAL, QSize


class AutoRenderApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.dir_path = "clas folder dir"
        self.dir_path = os.path.dirname(os.path.abspath(__file__))
        #self.shotInfo = None
        self.df_sg = None
        self.user_info = {}

        self.loadData()
        self.initUI()
        self.qtConnect()

        self.onPresetChanged(-1)
        #self.onUpdate_shot_tree()

    def loadData(self):
        self.df_sg['isPastStartDate'] = self.df_sg['start_date'].apply(self.redefine_past_start_date)

        # ---------------------  user info ---------------------
        self.df_sg['user'] = self.df_sg['user'].apply(self.redefine_user)

        # ---------------------  ani pub data ---------------------
        self.df_ani_pub = pd.read_csv(os.path.join(self.dir_path, "sg_ani_pub_info.csv"))
        self.df_ani_pub = self.df_ani_pub.dropna(subset=["shot_code"])
        self.df_ani_pub = self.df_ani_pub.loc[self.df_ani_pub.groupby(["shot_code"])["pub_ver"].idxmax()]
         # rename
        dict_rename = {"pub_status": "ani_pub_status"
                        , "pub_ver":"ani_pub_ver"
                        , "updated_at": "ani_pub_updated_time"}
        self.df_ani_pub.rename(columns=dict_rename, inplace=True)
        self.df_ani_pub['ani_pub_updated_time'] = self.df_ani_pub['ani_pub_updated_time'].apply(self.redefine_datetime)
        self.df_ani_pub = self.df_ani_pub[["shot_code", "ani_pub_status", "ani_pub_ver", "ani_pub_updated_time"]]

        self.df_sg = pd.merge(self.df_sg, self.df_ani_pub, on="shot_code", how="left")

        # ---------------------  ani status ---------------------
        self.df_ani_status = pd.read_csv(os.path.join(self.dir_path, "sg_ani_status_info.csv"))
        self.df_ani_status = self.df_ani_status.dropna(subset=["shot_code"])

        self.df_ani_status.rename(columns={"status":"ani_status"}, inplace=True)
        self.df_ani_status = self.df_ani_status[["shot_code", "ani_status"]]

        self.df_sg = pd.merge(self.df_sg, self.df_ani_status, on="shot_code", how="left")

        self.load_file_data_info(self.df_sg)

        print(self.df_sg)
        print(self.df_sg.dtypes)

    def initUI(self):

        # ---------------------  task_tree ---------------------
        list_tasks = sorted(self.df_sg["task"].drop_duplicates().to_list())
        self.setTaksTree(list_tasks)
        # ---------------------  user_tree ---------------------
        list_users = sorted(self.df_sg["user"].drop_duplicates().to_list())
        self.setUserTree(list_users)




        # ---------------------  tree widget header ---------------------
        self.ui.tree_shot.header().setSectionResizeMode(QHeaderView.ResizeToContents)
        # init qtreewidget sort by due date column
        self.ui.tree_shot.header().setSortIndicator(self.shot_tree_column["due_date"], Qt.AscendingOrder)
        self.ui.tree_user.header().setSortIndicator(0, Qt.AscendingOrder)
        self.ui.tree_task.header().setSortIndicator(0, Qt.AscendingOrder)

        self.setCentralWidget(self.ui)
        self.show()

    def qtConnect(self):
        # combobox - preset
        self.ui.cb_preset.currentIndexChanged.connect(self.onPresetChanged)

        self.ui.btn_run.clicked.connect(self.onRun)

        # check / uncheck  all shotcode tree checkbox
        self.ui.ck_all_shotcode.stateChanged.connect(self.onCheckAllShotCodeChanged)

        # ---------------------  tree item change ---------------------
        self.ui.tree_task.itemChanged.connect(self.onUpdate_shot_tree)
        self.ui.tree_user.itemChanged.connect(self.onUpdate_shot_tree)

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

    def get_checked_works(self):
        # 시퀀스 샷 tree 체크 검사.
        root = self.ui.tree_shot.invisibleRootItem()
        column = 0
        list_works = []
        for idx in range(root.childCount()):
            tree_item = root.child(idx)
            shot_code = tree_item.text(column)
            check_state = tree_item.checkState(column)

            if check_state == Qt.Checked:
                # TODO modify
                # dict_data = {shot: self.shotInfo[shot]}
                result_df = self.df_sg_filtered[(self.df_sg_filtered["shot_code"] == shot_code)]
                list_works.extend(result_df.to_dict("records"))

        return list_works

    def onRun(self):
        list_works = self.get_checked_works()
        for work_i, dict_data in enumerate(list_works):
            # TODO modify
            # for shot, data in dict_data.items():
            #     print(f"------------ run {shot} -------------")
            #     self.create_hip(shot, data)
            print(f"------------ run {dict_data['shot_code']} -------------")
            isOK = self.create_hip(dict_data)
            if isOK:
                file_manager.write_log_json(dict_data, self.dir_path)

            self.ui.progressBar.setValue(int((work_i + 1) / len(list_works) * 100))

    # TODO new function add
    def onUpdate_shot_tree(self):

        for dict_data in list_filtered_data:

            child.setCheckState(shot_col, ck_state_all)

            self.create_btn_open_files(child, shot_code, task)

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

        # get checked cmp render log
        cmp_render_log_query = self.get_checked_rd_log_query(self.ui.frame_cmp_render_log)
        if cmp_render_log_query:
            list_query.append(cmp_render_log_query)

        # get checked tasks
        task_query = self.getCheckedTasksQuery()
        if task_query:
            list_query.append(task_query)

        # get checked users
        user_query = self.getCheckedUsersQuery()
        if user_query:
            list_query.append(user_query)

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

    def getCheckedTasksQuery(self):
        # task tree check
        root = self.ui.tree_task.invisibleRootItem()
        column = 0
        list_checked_task = []
        for idx in range(root.childCount()):
            tree_item = root.child(idx)
            check_state = tree_item.checkState(column)
            if check_state == Qt.Checked:
                list_checked_task.append(tree_item.text(column))

        user_query = " | ".join(["task == '{}'".format(user) for user in list_checked_task])
        if user_query:
            return "(" + user_query + ")"
        return None

    # -- For pandas query
    def getCheckedUsersQuery(self):
        # user tree check
        root = self.ui.tree_user.invisibleRootItem()
        column = 0
        list_checked_user = []
        for idx in range(root.childCount()):
            tree_item = root.child(idx)
            check_state = tree_item.checkState(column)
            if check_state == Qt.Checked:
                user_id = tree_item.data(column, Qt.UserRole)
                list_checked_user.append(user_id)

        user_query = " | ".join(["user == '{}'".format(user) for user in list_checked_user])
        if user_query:
            return "(" + user_query + ")"
        return None


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


    def load_file_data_info(self, df):
        list_shot_info = df[["shot_code", "task", "project"]].to_dict('records')

        dict_file_info = file_manager.getFileInfo(self.dir_path, list_shot_info)

        df["log_last_ani_pub_ver"] = pd.Series(dict_file_info["last_ani_pub_ver"])
        df["log_last_render_time"] = pd.Series(dict_file_info["last_render_time"])
        df["last_mov"] = pd.Series(dict_file_info["last_mov"])
        df["last_nk"] = pd.Series(dict_file_info["last_nk"])
        df["last_hip"] = pd.Series(dict_file_info["last_hip"])

    def onPresetChanged(self, index):
        strPreset = self.ui.cb_preset.currentText().lower().strip()

        if strPreset == "preset_todo" or strPreset == "preset_ing":
            # -- Uncheck All Filters
            self.uncheck_all_filters()
            # # ani pub, tpub
            # self.changeCheckBox(True, self.ui.ck_aniPub_pub, self.onUpdate_shot_tree)
            # self.changeCheckBox(True, self.ui.ck_aniPub_tpub, self.onUpdate_shot_tree)
            # # ani status
            # self.changeCheckBox(True, self.ui.ck_ani_stat_done, self.onUpdate_shot_tree)
            # # compare start date
            # self.changeCheckBox(True, self.ui.ck_cmp_startDate, self.onUpdate_shot_tree)
            # if strPreset == "preset_todo":
            #     # uncheck compare to render log
            #     self.changeCheckBox(True, self.ui.ck_cmp_render_log_all, self.onCheckCmpRenderLogChangedAll)
            #     self.changeCheckBoxGroup(True, self.ui.frame_cmp_render_log, self.onUpdate_shot_tree, False)
            #
            # # fx status
            # self.changeCheckBox(True, self.ui.ck_fx_stat_pubr, self.onUpdate_shot_tree)
            # self.changeCheckBox(True, self.ui.ck_fx_stat_wip, self.onUpdate_shot_tree)
            # self.changeCheckBox(True, self.ui.ck_fx_stat_assign, self.onUpdate_shot_tree)
            # self.changeCheckBox(True, self.ui.ck_fx_stat_retake, self.onUpdate_shot_tree)

            # disable group box
            # self.ui.gb_filter_project.setEnabled(False)
            # self.ui.gb_filter_shot_status.setEnabled(False)
            # self.ui.gb_filter_ani.setEnabled(False)
            # self.ui.gb_filter_fx_status.setEnabled(False)

            self.onUpdate_shot_tree()

        else:  # custom
            # enable group box
            self.ui.gb_filter_project.setEnabled(True)
            self.ui.gb_filter_shot_status.setEnabled(True)
            self.ui.gb_filter_ani.setEnabled(True)
            self.ui.gb_filter_fx_status.setEnabled(True)

    def onCheckAllShotCodeChanged(self, state):
        if state == Qt.Checked:
            self.change_check_shotCode(True)
        else:
            self.change_check_shotCode(False)

    def change_check_shotCode(self, isCheck):
        # 샷 코드 트리 전체 선택 또는 전체 해제 기능
        root = self.ui.tree_shot.invisibleRootItem()
        column = self.shot_tree_column["shot_code"]
        for idx in range(root.childCount()):
            seq_tree_item = root.child(idx)
            seq_tree_item.setCheckState(column, Qt.Checked if isCheck else Qt.Unchecked)

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

    def changeCheckBox(self, state, ck_box, connectFunc=None):
        if connectFunc and ck_box.receivers(SIGNAL("stateChanged(int)")) > 0:
            ck_box.stateChanged.disconnect(connectFunc)
        # change status
        ck_box.setCheckState(Qt.Checked if state else Qt.Unchecked)
        if connectFunc:
            ck_box.stateChanged.connect(connectFunc)

    def changeCheckBoxGroup(self, state ,ui_parent, connectFunc, isNeedUpdate=True):
        for ck_box in ui_parent.findChildren(QCheckBox):
            self.changeCheckBox(state, ck_box, connectFunc)

        if isNeedUpdate == True:
            self.onUpdate_shot_tree()

    def setTaksTree(self, prj_fx_tasks, list_do_check=[]):
        self.ui.tree_task.clear()
        for task in prj_fx_tasks:
            child = QTreeWidgetItem(self.ui.tree_task)
            child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
            child.setText(0, task)
            child.setCheckState(0, Qt.Unchecked)
            if task in list_do_check:
                child.setCheckState(0, Qt.Checked)

    def setUserTree(self, prj_fx_users):
        # user 리스트
        self.ui.tree_user.clear()
        column = 0
        for user_id in prj_fx_users:
            child = QTreeWidgetItem(self.ui.tree_user)
            child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
            child.setText(column, self.user_info[user_id])
            child.setData(column, Qt.UserRole, user_id)
            child.setCheckState(column, Qt.Unchecked)

    def redefine_past_start_date(self, start_date):
        dt_start_date = self.redefine_date(start_date)
        if dt_start_date.date() < datetime.now().date():
            return True
        else:
            return False

    def redefine_date(self, str_date):
        dt_date = datetime.strptime(str(str_date), "%Y-%m-%d")
        return dt_date

    def redefine_datetime(self, str_date_time):
        dt_date = datetime.strptime(str(str_date_time), "%Y-%m-%d %H:%M:%S")
        return dt_date

    def redefine_user(self, str_data):
        dict_data = eval(str_data)
        user_id = str(dict_data["id"])
        user_name = dict_data['name']
        self.user_info[user_id] = user_name
        return user_id

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

    def create_btn_open_files(self, treeItem, shot_code, task):
        def create_open_btn(color, shot_code, get_df_column, slot_clicked, idx_column, task):
            w_btn = QPushButton("")
            w_btn.setStyleSheet("QPushButton{ background: "+ color +"; width:1;height:1;border-radius: 3px;}")

            last_file_name = self.get_one_df_data(shot_code, task, get_df_column)
            if last_file_name:
                path_dir = os.path.join(self.dir_path, shot_code)

                path_file = os.path.join(path_dir, last_file_name)
                w_btn.setProperty("path_file", path_file)
                w_btn.clicked.connect(
                    lambda state=None, btn_widget=w_btn: slot_clicked(btn_widget))
                self.ui.tree_shot.setItemWidget(treeItem, idx_column, w_btn)

        # -- mov button
        create_open_btn("#5ba1de", shot_code,"last_mov", self.onOpenMov, 1, task)
        create_open_btn("#eb7826", shot_code,"last_hip", self.onOpenHip, 2, task)
        create_open_btn("#ffd621", shot_code,"last_nk", self.onOpenNuke, 3, task)

    def onOpenMov(self, btn_widget):
        path_mov = btn_widget.property("path_file")
        if path_mov:
            self.onActPlayMov(path_mov)
        else:
            print("err onOpenMov path_mov none :", path_mov)

    def onOpenHip(self, btn_widget):
        path_hip = btn_widget.property("path_file")
        if path_hip:
            self.onActOpenHip(path_hip)
        else:
            print("err onOpenHip path_hip none :", path_hip)

    def onOpenNuke(self, btn_widget):
        path_nk = btn_widget.property("path_file")
        if path_nk:
            self.onActOpenNk(path_nk)
        else:
            print("err onOpenNuke path_nk none :", path_nk)

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

        # ---------------------  mov ---------------------
        name_mov = self.get_one_df_data(shot_code, task, "last_mov")
        if name_mov:
            path_mov = os.path.join(path_job_dir, name_mov)
            act_play_mov = QAction("Play Mov", self)
            act_play_mov.triggered.connect(
                lambda checked=None, path_mov=path_mov: self.onActPlayMov(path_mov))
            menu.addAction(act_play_mov)

            # shotgrid upload mov
            act_upload_sg = QAction("Upload ShotGrid", self)
            menu.addAction(act_upload_sg)


        # set nk action
        name_nk = self.get_one_df_data(shot_code, task, "last_nk")
        if name_nk:
            path_nk = os.path.join(path_job_dir, name_nk)
            act_open_nk = QAction("Open Nuke", self)
            act_open_nk.triggered.connect(
                lambda checked=None, path_nk=path_nk: self.onActOpenNk(path_nk))
            menu.addAction(act_open_nk)

        # set hip action
        name_hip = self.get_one_df_data(shot_code, task, "last_hip")
        if name_hip:
            path_hip = os.path.join(path_job_dir, name_hip)
            act_open_hip = QAction("Open Houdini", self)
            act_open_hip.triggered.connect(
                lambda checked=None, path_hip=path_hip: self.onActOpenHip(path_hip))
            menu.addAction(act_open_hip)

        # the function to display context menu
        menu.exec_(self.ui.tree_shot.mapToGlobal(position))

    def get_one_df_data(self, shot_code, task, column):
        df_shotcode_data = self.df_sg.loc[(self.df_sg.shot_code == shot_code) & (self.df_sg.task == task)]
        list_data = df_shotcode_data[column].values.tolist()
        if len(list_data) > 0 and list_data[0]:
            return list_data[0]
        else:
            return None

    def onOpenFolder(self):
        curr_tree_item = self.ui.tree_shot.currentItem()
        shot_code_col = self.shot_tree_column["shot_code"]

        shot = curr_tree_item.text(shot_code_col)

        path_open_dir = os.path.join(self.dir_path, shot)

        if not os.path.exists(path_open_dir):
            path_open_dir = self.dir_path

        os.system("explorer " +  path_open_dir + " &")

    def onActPlayMov(self, path_mov):
        backup_path = os.getcwd()
        os.chdir(r"C:\Program Files (x86)\VideoLAN\VLC")

        # os.system("vlc.exe " + path_mov + " &")

        cmd = ["vlc.exe", path_mov]
        DETACHED_PROCESS = 0x00000008
        pid = subprocess.Popen(cmd ,creationflags=DETACHED_PROCESS).pid

        os.chdir(backup_path)

    def onActOpenNk(self, path_nk):

        # for ignore hython env -> for nuke
        nk_env = os.environ.copy()
        if "PYTHONPATH" in nk_env.keys():
            del nk_env["PYTHONPATH"]
        if "PYTHONHOME" in nk_env.keys():
            del nk_env["PYTHONHOME"]

        backup_path = os.getcwd()

        # os.system("Nuke15.0.exe " + path_nk + " &")

        os.chdir(r"C:\Program Files\Nuke15.0v1")
        cmd = ["Nuke15.0.exe", path_nk]
        # subprocess.run(cmd, env=nk_env)

        DETACHED_PROCESS = 0x00000008
        pid = subprocess.Popen(cmd, env=nk_env
                               ,creationflags=DETACHED_PROCESS).pid

        os.chdir(backup_path)

    def onActOpenHip(self, path_hip):

        backup_path = os.getcwd()

        # os.system("Nuke15.0.exe " + path_nk + " &")

        os.chdir(r"C:\Program Files\Side Effects Software\Houdini 19.5.435\bin")
        cmd = ["houdini.exe", path_hip]

        DETACHED_PROCESS = 0x00000008
        pid = subprocess.Popen(cmd ,creationflags=DETACHED_PROCESS).pid

        os.chdir(backup_path)

    def get_shot_code(self):
        return sorted(self.df_sg_filtered["shot_code"].drop_duplicates().to_list())


    def send_msg(self, msg):
        message = {"content": msg}
        requests.post(DISCORD_WEBHOOK_URL, data=message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myApp = AutoRenderApp()
    app.exec_()
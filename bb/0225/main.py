import sys, os
from datetime import datetime
import file_manager

sys.path.append('/home/rapa/anaconda3/envs/houdini/lib/python3.9/site-packages')
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
# print(f'complete: {pd}')
# pyside2
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt, SIGNAL
from PySide2 import QtUiTools


class AutoRenderApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.dir_path = "clas folder dir"
        self.df_sg = None
        self.ui = None
        self.dir_path = os.path.dirname(os.path.abspath(__file__))
        self.shotInfo = None

        self.shot_tree_column = {"shot_code": 0, "mov": 1, "hip": 2, "nk": 3, "start_date": 4, "due_date": 5, "task": 6}

        self.loadData()
        self.initUI()
        self.qtConnect()

        self.onPresetChanged(-1)
        # self.onUpdate_shot_tree()

    def loadData(self):
        str_none_date = "1111-11-11"
        self.df_sg = pd.read_csv(os.path.join(self.dir_path, "sg_fx_info.csv"))
        self.df_sg["start_date"] = self.df_sg["start_date"].fillna(str_none_date)
        self.df_sg["due_date"] = self.df_sg["due_date"].fillna(str_none_date)  # change none data

        self.df_sg["isPastStartDate"] = self.df_sg["start_date"].apply(self.redefine_past_start_date)

        # ---------------------  ani pub data ---------------------
        self.df_ani_pub = pd.read_csv(os.path.join(self.dir_path, "sg_ani_pub_info.csv"))
        self.df_ani_pub = self.df_ani_pub.dropna(subset=["shot_code"])
        self.df_ani_pub = self.df_ani_pub.loc[self.df_ani_pub.groupby(["shot_code"])["pub_ver"].idxmax()]
        # rename
        dict_rename = {"pub_status": "ani_pub_status"
            , "pub_ver": "ani_pub_ver"
            , "updated_at": "ani_pub_updated_time"}
        self.df_ani_pub.rename(columns=dict_rename, inplace=True)
        self.df_ani_pub['ani_pub_updated_time'] = self.df_ani_pub['ani_pub_updated_time'].apply(self.redefine_datetime)
        self.df_ani_pub = self.df_ani_pub[["shot_code", "ani_pub_status", "ani_pub_ver", "ani_pub_updated_time"]]

        self.df_sg = pd.merge(self.df_sg, self.df_ani_pub, on="shot_code", how="left")

        # ---------------------  ani status ---------------------
        self.df_ani_status = pd.read_csv(os.path.join(self.dir_path, "sg_ani_status_info.csv"))
        self.df_ani_status = self.df_ani_status.dropna(subset=["shot_code"])

        self.df_ani_status.rename(columns={"status": "ani_status"}, inplace=True)
        self.df_ani_status = self.df_ani_status[["shot_code", "ani_status"]]

        self.df_sg = pd.merge(self.df_sg, self.df_ani_status, on="shot_code", how="left")

        self.load_file_data_info(self.df_sg)

        # print(self.df_sg)
        # print(self.df_sg.dtypes)

    def load_file_data_info(self, df):
        list_shot_info = df[["shot_code", "task", "project"]].to_dict('records')

        dict_file_info = file_manager.getFileInfo(self.dir_path, list_shot_info)

        df["log_last_ani_pub_ver"] = pd.Series(dict_file_info["last_ani_pub_ver"])
        df["log_last_render_time"] = pd.Series(dict_file_info["last_render_time"])
        df["last_mov"] = pd.Series(dict_file_info["last_mov"])
        df["last_nk"] = pd.Series(dict_file_info["last_nk"])
        df["last_hip"] = pd.Series(dict_file_info["last_hip"])

        print("-" * 50, "\n")
        print(df)

    def redefine_datetime(self, str_date_time):
        dt_date = datetime.strptime(str(str_date_time), "%Y-%m-%d %H:%M:%S")
        return dt_date

    def onPresetChanged(self, index):
        strPreset = self.ui.cb_preset.currentText().lower().strip()
        print(strPreset)
        if strPreset == "preset_todo" or strPreset == "preset_ing":
            # -- Uncheck All Filters
            self.uncheck_all_filters()
            self.onUpdate_shot_tree()

        else:  # cunstom
            # enable group box
            self.ui.gb_filter_project.setEnabled(True)
            self.ui.gb_filter_shot_status.setEnabled(True)
            self.ui.gb_filter_ani.setEnabled(True)
            self.ui.gb_filter_fx_status.setEnabled(True)

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

    # def get_checked_rd_log_query(self, ui_parent):
    #    list_query = []
    #    for ck_box in ui_parent.findChildren(QCheckBox):
    #        if ck_box.checkState() == Qt.Checked:
    #            qt_obj_name = ck_box.objectName()
    #
    #            if qt_obj_name == "ck_cmp_ani_pub_ver":
    #                list_query.append("ani_pub_ver > log_last_ani_pub_ver")
    #            if qt_obj_name == "ck_cmp_ani_update_time":
    #                list_query.append("ani_pub_updated_time > log_last_render_time")
    #
    #    query = " | ".join(list_query)
    #    if query:
    #        query = "(" + query + ")"
    #        return query
    #    else:
    #        return None

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

    def changeCheckBoxGroup(self, state, ui_parent, connectFunc, isNeedUpdate=True):
        for ck_box in ui_parent.findChildren(QCheckBox):
            self.changeCheckBox(state, ck_box, connectFunc)

        if isNeedUpdate == True:
            self.onUpdate_shot_tree()

    def changeCheckBox(self, state, ck_box, connectFunc=None):
        if connectFunc and ck_box.receivers(SIGNAL("stateChanged(int)")) > 0:
            ck_box.stateChanged.disconnect(connectFunc)

        ck_box.setCheckState(Qt.Checked if state else Qt.Unchecked)
        if connectFunc:
            ck_box.stateChanged.connect(connectFunc)

    def redefine_date(self, str_date):
        dt_date = datetime.strptime(str(str_date), "%Y-%m-%d")
        return dt_date

    def redefine_past_start_date(self, start_date):
        dt_start_date = self.redefine_date(start_date)
        if dt_start_date.date() < datetime.now().date():
            return True
        else:
            return False

    def initUI(self):
        self.ui = QtUiTools.QUiLoader().load(os.path.join(self.dir_path, "auto.ui"))
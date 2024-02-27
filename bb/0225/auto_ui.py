# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'auto.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import ui_resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1022, 900)
        MainWindow.setMinimumSize(QSize(1022, 700))
        font = QFont()
        font.setFamily(u"\ub098\ub214\uace0\ub515")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"\n"
"QWidget{\n"
"    background: #3A3B3C;\n"
"}\n"
"/*---------------------------  QLabel --------------------------*/\n"
"QLabel{\n"
"    color: rgb(236, 236, 236);\n"
"    font-weight: bold;\n"
"    font-size: 9pt;\n"
"}\n"
"QLabel #label_animation_title #label_task_title{\n"
"    /*color: rgb(236, 236, 236);*/\n"
"    color: red;\n"
"    font-weight: bold;\n"
"    font-size: 11pt;\n"
"}\n"
"\n"
"QLabel:disabled#label_animation_title{\n"
"    color : gray;\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color : gray;\n"
"}\n"
"\n"
"/*---------------------------  QPushButton --------------------------*/\n"
"QPushButton\n"
"{\n"
"    color : rgb(236, 236, 236);\n"
"    background: #0577a8;\n"
"    border: 1px #DADADA solid;\n"
"    padding: 5px 10px;\n"
"    border-radius: 2px;\n"
"    font-weight: bold;\n"
"    font-size: 9pt;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 1px #C6C6C6 sold;\n"
"    background: #0892D0;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color:  #40404"
                        "0;\n"
"    color : gray;\n"
"}\n"
"\n"
"QPushButton:hover#btn_fold_shot_status, :hover#btn_fold_ani{\n"
"    background: #3A3B3C;\n"
"}\n"
"\n"
"QPushButton#btn_fold_shot_status, #btn_fold_ani{\n"
"    background: rgba(255, 255, 255, 0);\n"
"    color: rgb(236, 236, 236);\n"
"}\n"
"\n"
"/*---------------------------  QCheckBox ---------------------------*/\n"
"QCheckBox{\n"
"    color: rgb(236, 236, 236);\n"
"    font-weight: bold;\n"
"    font-size: 9pt;\n"
"}\n"
"QCheckBox:disabled {\n"
"    color : gray;\n"
"}\n"
"\n"
"\n"
"/*---------------------------  QComboBox --------------------------*/\n"
"QComboBox{\n"
"    color : rgb(236, 236, 236);\n"
"    font-weight: bold;\n"
"    font-size: 9pt;\n"
"}\n"
"QComboBox:disabled {\n"
"    background-color:  #404040;\n"
"    color : gray;\n"
"}\n"
"\n"
"/*---------------------------  QProgressBar --------------------------*/\n"
"QProgressBar{\n"
"    color: rgb(236, 236, 236);\n"
"    font-weight: bold;\n"
"    font-size: 9pt\n"
"}\n"
"\n"
"/*-----------------------"
                        "----  QGroupBox --------------------------*/\n"
"QGroupBox{\n"
"    color : rgb(236, 236, 236);\n"
"    font-weight: bold;\n"
"    font-size: 9pt;\n"
"}\n"
"\n"
"QGroupBox#gb_filters,#gb_shotcode{\n"
"    color : rgb(236, 236, 236);\n"
"    font-weight: bold;\n"
"    font-size: 12pt;\n"
"}\n"
"QGroupBox:disabled {\n"
"    background-color:  #404040;\n"
"    color : gray;\n"
"}\n"
"\n"
"/*---------------------------  QListWidget --------------------------*/\n"
"QListWidget{\n"
"    color : rgb(236, 236, 236);\n"
"    font-size: 9pt;;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QListWidget::item{\n"
"    margin:2px;\n"
"}\n"
"\n"
"/*---------------------------  QTreeWidget --------------------------*/\n"
"QTreeWidget{\n"
"    color : rgb(236, 236, 236);\n"
"    font-size: 10pt;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QTreeWidget::item{\n"
"    margin:2px;\n"
"}\n"
"\n"
"/*---------------------------  QSpinBox --------------------------*/\n"
"QSpinBox {\n"
"    color : rgb(236, 236, 236);\n"
"}\n"
"\n"
"/*-------"
                        "--------------------  QLabel --------------------------*/\n"
"\n"
"QLabel#label_animation_title,  #label_task_title, #label_user_title, #label_fx_title{\n"
"    color: rgb(236, 236, 236);\n"
"    font-weight: bold;\n"
"    font-size: 11pt;\n"
"}\n"
"\n"
"QLabel:disabled#label_animation_title, :disabled#label_task_title, :disabled#label_user_title, :disabled#label_fx_title{\n"
"    color : gray;\n"
"}\n"
"\n"
"/*---------------------------  QPushButton --------------------------*/\n"
"QPushButton:hover#btn_fold_ani, :hover#btn_fold_task, :hover#btn_fold_user, :hover#btn_fold_fx{\n"
"    background: #3A3B3C;\n"
"}\n"
"\n"
"QPushButton#btn_fold_ani, #btn_fold_task, #btn_fold_user, #btn_fold_fx{\n"
"    background: rgba(255, 255, 255, 0);\n"
"    color: rgb(236, 236, 236);\n"
"}\n"
"\n"
"/*---------------------------  QGroupBox --------------------------*/\n"
"QGroupBox#gb_filters{\n"
"    color : rgb(236, 236, 236);\n"
"    font-weight: bold;\n"
"    font-size: 12pt;\n"
"}\n"
"\n"
"QGroupBox#gb_task_title, #gb_an"
                        "i_title, #gb_user_title, #gb_fx_title{\n"
"    border: 0px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(7, 7, 7, 7)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_filters = QFrame(self.centralwidget)
        self.frame_filters.setObjectName(u"frame_filters")
        self.frame_filters.setMinimumSize(QSize(500, 0))
        self.frame_filters.setFrameShape(QFrame.NoFrame)
        self.frame_filters.setFrameShadow(QFrame.Plain)
        self.frame_filters.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.frame_filters)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.vlayout_filters = QVBoxLayout()
        self.vlayout_filters.setSpacing(0)
        self.vlayout_filters.setObjectName(u"vlayout_filters")
        self.gb_filters = QGroupBox(self.frame_filters)
        self.gb_filters.setObjectName(u"gb_filters")
        self.gb_filters.setEnabled(True)
        self.gb_filters.setMinimumSize(QSize(500, 0))
        self.gb_filters.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.gb_filters.setCheckable(False)
        self.verticalLayout_4 = QVBoxLayout(self.gb_filters)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_filter_head = QFrame(self.gb_filters)
        self.frame_filter_head.setObjectName(u"frame_filter_head")
        self.frame_filter_head.setFrameShape(QFrame.NoFrame)
        self.frame_filter_head.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_filter_head)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_FilterType = QLabel(self.frame_filter_head)
        self.label_FilterType.setObjectName(u"label_FilterType")

        self.horizontalLayout_9.addWidget(self.label_FilterType)

        self.cb_preset = QComboBox(self.frame_filter_head)
        self.cb_preset.addItem("")
        self.cb_preset.addItem("")
        self.cb_preset.addItem("")
        self.cb_preset.setObjectName(u"cb_preset")

        self.horizontalLayout_9.addWidget(self.cb_preset)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)


        self.verticalLayout_4.addWidget(self.frame_filter_head)

        self.scrollArea = QScrollArea(self.gb_filters)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 461, 963))
        self.verticalLayout_18 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.lyt_vbox_filter = QVBoxLayout()
        self.lyt_vbox_filter.setObjectName(u"lyt_vbox_filter")
        self.gb_filter_project = QGroupBox(self.scrollAreaWidgetContents)
        self.gb_filter_project.setObjectName(u"gb_filter_project")
        self.gb_filter_project.setMaximumSize(QSize(16777215, 60))
        self.gb_filter_project.setFlat(False)
        self.gb_filter_project.setCheckable(False)
        self.horizontalLayout_4 = QHBoxLayout(self.gb_filter_project)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_project = QLabel(self.gb_filter_project)
        self.label_project.setObjectName(u"label_project")
        self.label_project.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_4.addWidget(self.label_project)

        self.combo_project = QComboBox(self.gb_filter_project)
        self.combo_project.setObjectName(u"combo_project")

        self.horizontalLayout_4.addWidget(self.combo_project)


        self.lyt_vbox_filter.addWidget(self.gb_filter_project)

        self.gb_filter_shot_status = QGroupBox(self.scrollAreaWidgetContents)
        self.gb_filter_shot_status.setObjectName(u"gb_filter_shot_status")
        self.gb_filter_shot_status.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.gb_filter_shot_status)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.ck_shot_stat_all = QCheckBox(self.gb_filter_shot_status)
        self.ck_shot_stat_all.setObjectName(u"ck_shot_stat_all")
        self.ck_shot_stat_all.setEnabled(True)
        self.ck_shot_stat_all.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_7.addWidget(self.ck_shot_stat_all)

        self.label_shot_status = QLabel(self.gb_filter_shot_status)
        self.label_shot_status.setObjectName(u"label_shot_status")
        self.label_shot_status.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_7.addWidget(self.label_shot_status)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.frame_shot_status_cks = QFrame(self.gb_filter_shot_status)
        self.frame_shot_status_cks.setObjectName(u"frame_shot_status_cks")
        self.frame_shot_status_cks.setMaximumSize(QSize(16777215, 16777215))
        self.frame_shot_status_cks.setFrameShape(QFrame.StyledPanel)
        self.frame_shot_status_cks.setFrameShadow(QFrame.Plain)
        self.verticalLayout_11 = QVBoxLayout(self.frame_shot_status_cks)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_shot_stat_wip = QLabel(self.frame_shot_status_cks)
        self.label_shot_stat_wip.setObjectName(u"label_shot_stat_wip")

        self.gridLayout.addWidget(self.label_shot_stat_wip, 0, 3, 1, 1, Qt.AlignHCenter)

        self.label_shot_stat_omt = QLabel(self.frame_shot_status_cks)
        self.label_shot_stat_omt.setObjectName(u"label_shot_stat_omt")

        self.gridLayout.addWidget(self.label_shot_stat_omt, 0, 7, 1, 1, Qt.AlignHCenter)

        self.ck_shot_stat_omt = QCheckBox(self.frame_shot_status_cks)
        self.ck_shot_stat_omt.setObjectName(u"ck_shot_stat_omt")

        self.gridLayout.addWidget(self.ck_shot_stat_omt, 1, 7, 1, 1, Qt.AlignHCenter)

        self.ck_shot_stat_wip = QCheckBox(self.frame_shot_status_cks)
        self.ck_shot_stat_wip.setObjectName(u"ck_shot_stat_wip")
        self.ck_shot_stat_wip.setChecked(False)

        self.gridLayout.addWidget(self.ck_shot_stat_wip, 1, 3, 1, 1, Qt.AlignHCenter)

        self.label_shot_stat_retake = QLabel(self.frame_shot_status_cks)
        self.label_shot_stat_retake.setObjectName(u"label_shot_stat_retake")

        self.gridLayout.addWidget(self.label_shot_stat_retake, 0, 5, 1, 1, Qt.AlignHCenter)

        self.label_shot_stat_dir = QLabel(self.frame_shot_status_cks)
        self.label_shot_stat_dir.setObjectName(u"label_shot_stat_dir")

        self.gridLayout.addWidget(self.label_shot_stat_dir, 0, 1, 1, 1, Qt.AlignHCenter)

        self.label_shot_stat_done = QLabel(self.frame_shot_status_cks)
        self.label_shot_stat_done.setObjectName(u"label_shot_stat_done")

        self.gridLayout.addWidget(self.label_shot_stat_done, 0, 0, 1, 1, Qt.AlignHCenter)

        self.ck_shot_stat_dir = QCheckBox(self.frame_shot_status_cks)
        self.ck_shot_stat_dir.setObjectName(u"ck_shot_stat_dir")

        self.gridLayout.addWidget(self.ck_shot_stat_dir, 1, 1, 1, 1, Qt.AlignHCenter)

        self.label_shot_stat_assign = QLabel(self.frame_shot_status_cks)
        self.label_shot_stat_assign.setObjectName(u"label_shot_stat_assign")

        self.gridLayout.addWidget(self.label_shot_stat_assign, 0, 4, 1, 1, Qt.AlignHCenter)

        self.ck_shot_stat_retake = QCheckBox(self.frame_shot_status_cks)
        self.ck_shot_stat_retake.setObjectName(u"ck_shot_stat_retake")

        self.gridLayout.addWidget(self.ck_shot_stat_retake, 1, 5, 1, 1, Qt.AlignHCenter)

        self.ck_shot_stat_done = QCheckBox(self.frame_shot_status_cks)
        self.ck_shot_stat_done.setObjectName(u"ck_shot_stat_done")

        self.gridLayout.addWidget(self.ck_shot_stat_done, 1, 0, 1, 1, Qt.AlignHCenter)

        self.ck_shot_stat_assign = QCheckBox(self.frame_shot_status_cks)
        self.ck_shot_stat_assign.setObjectName(u"ck_shot_stat_assign")

        self.gridLayout.addWidget(self.ck_shot_stat_assign, 1, 4, 1, 1, Qt.AlignHCenter)

        self.label_shot_stat_hld = QLabel(self.frame_shot_status_cks)
        self.label_shot_stat_hld.setObjectName(u"label_shot_stat_hld")

        self.gridLayout.addWidget(self.label_shot_stat_hld, 0, 6, 1, 1, Qt.AlignHCenter)

        self.ck_shot_stat_hld = QCheckBox(self.frame_shot_status_cks)
        self.ck_shot_stat_hld.setObjectName(u"ck_shot_stat_hld")

        self.gridLayout.addWidget(self.ck_shot_stat_hld, 1, 6, 1, 1, Qt.AlignHCenter)

        self.label_shot_stat_out = QLabel(self.frame_shot_status_cks)
        self.label_shot_stat_out.setObjectName(u"label_shot_stat_out")

        self.gridLayout.addWidget(self.label_shot_stat_out, 0, 8, 1, 1, Qt.AlignHCenter)

        self.ck_shot_stat_out = QCheckBox(self.frame_shot_status_cks)
        self.ck_shot_stat_out.setObjectName(u"ck_shot_stat_out")

        self.gridLayout.addWidget(self.ck_shot_stat_out, 1, 8, 1, 1, Qt.AlignHCenter)


        self.verticalLayout_11.addLayout(self.gridLayout)


        self.verticalLayout_6.addWidget(self.frame_shot_status_cks)


        self.lyt_vbox_filter.addWidget(self.gb_filter_shot_status)

        self.gb_filter_ani = QGroupBox(self.scrollAreaWidgetContents)
        self.gb_filter_ani.setObjectName(u"gb_filter_ani")
        self.gb_filter_ani.setEnabled(True)
        self.gb_filter_ani.setMinimumSize(QSize(0, 0))
        self.gb_filter_ani.setMaximumSize(QSize(16777215, 16777215))
        self.gb_filter_ani.setFlat(False)
        self.gb_filter_ani.setCheckable(False)
        self.gb_filter_ani.setChecked(False)
        self.verticalLayout_7 = QVBoxLayout(self.gb_filter_ani)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.gb_ani_title = QGroupBox(self.gb_filter_ani)
        self.gb_ani_title.setObjectName(u"gb_ani_title")
        self.horizontalLayout_3 = QHBoxLayout(self.gb_ani_title)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_fold_ani = QPushButton(self.gb_ani_title)
        self.btn_fold_ani.setObjectName(u"btn_fold_ani")
        self.btn_fold_ani.setMinimumSize(QSize(18, 18))
        self.btn_fold_ani.setMaximumSize(QSize(18, 18))
        icon = QIcon()
        icon.addFile(u":/icon/arrow_down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_fold_ani.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.btn_fold_ani)

        self.label_animation_title = QLabel(self.gb_ani_title)
        self.label_animation_title.setObjectName(u"label_animation_title")
        self.label_animation_title.setEnabled(True)
        self.label_animation_title.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_3.addWidget(self.label_animation_title)


        self.verticalLayout_7.addWidget(self.gb_ani_title)

        self.gb_filter_ani_pub = QGroupBox(self.gb_filter_ani)
        self.gb_filter_ani_pub.setObjectName(u"gb_filter_ani_pub")
        self.gb_filter_ani_pub.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.verticalLayout_5 = QVBoxLayout(self.gb_filter_ani_pub)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.ck_aniPub_all = QCheckBox(self.gb_filter_ani_pub)
        self.ck_aniPub_all.setObjectName(u"ck_aniPub_all")

        self.horizontalLayout_5.addWidget(self.ck_aniPub_all)

        self.label_pub_ani = QLabel(self.gb_filter_ani_pub)
        self.label_pub_ani.setObjectName(u"label_pub_ani")

        self.horizontalLayout_5.addWidget(self.label_pub_ani)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.frame_aniPub_status_cks = QFrame(self.gb_filter_ani_pub)
        self.frame_aniPub_status_cks.setObjectName(u"frame_aniPub_status_cks")
        self.frame_aniPub_status_cks.setFrameShape(QFrame.StyledPanel)
        self.frame_aniPub_status_cks.setFrameShadow(QFrame.Plain)
        self.verticalLayout_13 = QVBoxLayout(self.frame_aniPub_status_cks)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.lyt_grid_ani_pub = QGridLayout()
        self.lyt_grid_ani_pub.setObjectName(u"lyt_grid_ani_pub")
        self.ck_aniPub_tpub = QCheckBox(self.frame_aniPub_status_cks)
        self.ck_aniPub_tpub.setObjectName(u"ck_aniPub_tpub")
        self.ck_aniPub_tpub.setAutoFillBackground(False)
        self.ck_aniPub_tpub.setChecked(True)

        self.lyt_grid_ani_pub.addWidget(self.ck_aniPub_tpub, 1, 1, 1, 1, Qt.AlignHCenter)

        self.ck_aniPub_wtg = QCheckBox(self.frame_aniPub_status_cks)
        self.ck_aniPub_wtg.setObjectName(u"ck_aniPub_wtg")

        self.lyt_grid_ani_pub.addWidget(self.ck_aniPub_wtg, 1, 3, 1, 1, Qt.AlignHCenter)

        self.ck_aniPub_pub = QCheckBox(self.frame_aniPub_status_cks)
        self.ck_aniPub_pub.setObjectName(u"ck_aniPub_pub")
        self.ck_aniPub_pub.setEnabled(True)
        self.ck_aniPub_pub.setLayoutDirection(Qt.LeftToRight)
        self.ck_aniPub_pub.setChecked(True)
        self.ck_aniPub_pub.setTristate(False)

        self.lyt_grid_ani_pub.addWidget(self.ck_aniPub_pub, 1, 0, 1, 1, Qt.AlignHCenter)

        self.label_ani_pub = QLabel(self.frame_aniPub_status_cks)
        self.label_ani_pub.setObjectName(u"label_ani_pub")
        self.label_ani_pub.setLayoutDirection(Qt.LeftToRight)

        self.lyt_grid_ani_pub.addWidget(self.label_ani_pub, 0, 0, 1, 1, Qt.AlignHCenter)

        self.ck_aniPub_retake = QCheckBox(self.frame_aniPub_status_cks)
        self.ck_aniPub_retake.setObjectName(u"ck_aniPub_retake")

        self.lyt_grid_ani_pub.addWidget(self.ck_aniPub_retake, 1, 2, 1, 1, Qt.AlignHCenter)

        self.label_ani_wtg = QLabel(self.frame_aniPub_status_cks)
        self.label_ani_wtg.setObjectName(u"label_ani_wtg")

        self.lyt_grid_ani_pub.addWidget(self.label_ani_wtg, 0, 3, 1, 1, Qt.AlignHCenter)

        self.label_ani_retake = QLabel(self.frame_aniPub_status_cks)
        self.label_ani_retake.setObjectName(u"label_ani_retake")

        self.lyt_grid_ani_pub.addWidget(self.label_ani_retake, 0, 2, 1, 1, Qt.AlignHCenter)

        self.label_ani_tpub = QLabel(self.frame_aniPub_status_cks)
        self.label_ani_tpub.setObjectName(u"label_ani_tpub")

        self.lyt_grid_ani_pub.addWidget(self.label_ani_tpub, 0, 1, 1, 1, Qt.AlignHCenter)


        self.verticalLayout_13.addLayout(self.lyt_grid_ani_pub)


        self.verticalLayout_5.addWidget(self.frame_aniPub_status_cks)


        self.verticalLayout_7.addWidget(self.gb_filter_ani_pub)

        self.gb_filter_ani_status = QGroupBox(self.gb_filter_ani)
        self.gb_filter_ani_status.setObjectName(u"gb_filter_ani_status")
        self.gb_filter_ani_status.setEnabled(True)
        self.gb_filter_ani_status.setCheckable(False)
        self.verticalLayout_8 = QVBoxLayout(self.gb_filter_ani_status)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.ck_ani_stat_all = QCheckBox(self.gb_filter_ani_status)
        self.ck_ani_stat_all.setObjectName(u"ck_ani_stat_all")

        self.horizontalLayout_6.addWidget(self.ck_ani_stat_all)

        self.label_ani_status = QLabel(self.gb_filter_ani_status)
        self.label_ani_status.setObjectName(u"label_ani_status")
        self.label_ani_status.setEnabled(True)

        self.horizontalLayout_6.addWidget(self.label_ani_status)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.frame_ani_status_cks = QFrame(self.gb_filter_ani_status)
        self.frame_ani_status_cks.setObjectName(u"frame_ani_status_cks")
        self.frame_ani_status_cks.setFrameShape(QFrame.StyledPanel)
        self.frame_ani_status_cks.setFrameShadow(QFrame.Plain)
        self.verticalLayout_12 = QVBoxLayout(self.frame_ani_status_cks)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.lyt_grid_ani_status = QGridLayout()
        self.lyt_grid_ani_status.setObjectName(u"lyt_grid_ani_status")
        self.label_ani_stat_assign = QLabel(self.frame_ani_status_cks)
        self.label_ani_stat_assign.setObjectName(u"label_ani_stat_assign")

        self.lyt_grid_ani_status.addWidget(self.label_ani_stat_assign, 0, 4, 1, 1, Qt.AlignHCenter)

        self.ck_ani_stat_retake = QCheckBox(self.frame_ani_status_cks)
        self.ck_ani_stat_retake.setObjectName(u"ck_ani_stat_retake")
        self.ck_ani_stat_retake.setEnabled(True)
        self.ck_ani_stat_retake.setChecked(False)

        self.lyt_grid_ani_status.addWidget(self.ck_ani_stat_retake, 1, 5, 1, 1, Qt.AlignHCenter)

        self.ck_ani_stat_assign = QCheckBox(self.frame_ani_status_cks)
        self.ck_ani_stat_assign.setObjectName(u"ck_ani_stat_assign")
        self.ck_ani_stat_assign.setChecked(False)

        self.lyt_grid_ani_status.addWidget(self.ck_ani_stat_assign, 1, 4, 1, 1, Qt.AlignHCenter)

        self.label_ani_stat_wip = QLabel(self.frame_ani_status_cks)
        self.label_ani_stat_wip.setObjectName(u"label_ani_stat_wip")

        self.lyt_grid_ani_status.addWidget(self.label_ani_stat_wip, 0, 3, 1, 1, Qt.AlignHCenter)

        self.label_ani_stat_retake = QLabel(self.frame_ani_status_cks)
        self.label_ani_stat_retake.setObjectName(u"label_ani_stat_retake")

        self.lyt_grid_ani_status.addWidget(self.label_ani_stat_retake, 0, 5, 1, 1, Qt.AlignHCenter)

        self.label_ani_stat_done = QLabel(self.frame_ani_status_cks)
        self.label_ani_stat_done.setObjectName(u"label_ani_stat_done")

        self.lyt_grid_ani_status.addWidget(self.label_ani_stat_done, 0, 0, 1, 1, Qt.AlignHCenter)

        self.label_ani_stat_omt = QLabel(self.frame_ani_status_cks)
        self.label_ani_stat_omt.setObjectName(u"label_ani_stat_omt")

        self.lyt_grid_ani_status.addWidget(self.label_ani_stat_omt, 0, 8, 1, 1, Qt.AlignHCenter)

        self.label_ani_stat_hld = QLabel(self.frame_ani_status_cks)
        self.label_ani_stat_hld.setObjectName(u"label_ani_stat_hld")

        self.lyt_grid_ani_status.addWidget(self.label_ani_stat_hld, 0, 7, 1, 1, Qt.AlignHCenter)

        self.ck_ani_stat_pubr = QCheckBox(self.frame_ani_status_cks)
        self.ck_ani_stat_pubr.setObjectName(u"ck_ani_stat_pubr")
        self.ck_ani_stat_pubr.setCheckable(True)
        self.ck_ani_stat_pubr.setChecked(False)

        self.lyt_grid_ani_status.addWidget(self.ck_ani_stat_pubr, 1, 1, 1, 1, Qt.AlignHCenter)

        self.ck_ani_stat_wip = QCheckBox(self.frame_ani_status_cks)
        self.ck_ani_stat_wip.setObjectName(u"ck_ani_stat_wip")
        self.ck_ani_stat_wip.setChecked(False)

        self.lyt_grid_ani_status.addWidget(self.ck_ani_stat_wip, 1, 3, 1, 1, Qt.AlignHCenter)

        self.ck_ani_stat_done = QCheckBox(self.frame_ani_status_cks)
        self.ck_ani_stat_done.setObjectName(u"ck_ani_stat_done")
        self.ck_ani_stat_done.setChecked(True)

        self.lyt_grid_ani_status.addWidget(self.ck_ani_stat_done, 1, 0, 1, 1, Qt.AlignHCenter)

        self.label_ani_stat_pubr = QLabel(self.frame_ani_status_cks)
        self.label_ani_stat_pubr.setObjectName(u"label_ani_stat_pubr")

        self.lyt_grid_ani_status.addWidget(self.label_ani_stat_pubr, 0, 1, 1, 1, Qt.AlignHCenter)

        self.ck_ani_stat_hld = QCheckBox(self.frame_ani_status_cks)
        self.ck_ani_stat_hld.setObjectName(u"ck_ani_stat_hld")
        self.ck_ani_stat_hld.setChecked(False)

        self.lyt_grid_ani_status.addWidget(self.ck_ani_stat_hld, 1, 7, 1, 1, Qt.AlignHCenter)

        self.ck_ani_stat_omt = QCheckBox(self.frame_ani_status_cks)
        self.ck_ani_stat_omt.setObjectName(u"ck_ani_stat_omt")

        self.lyt_grid_ani_status.addWidget(self.ck_ani_stat_omt, 1, 8, 1, 1, Qt.AlignHCenter)

        self.label_ani_stat_out = QLabel(self.frame_ani_status_cks)
        self.label_ani_stat_out.setObjectName(u"label_ani_stat_out")

        self.lyt_grid_ani_status.addWidget(self.label_ani_stat_out, 0, 9, 1, 1, Qt.AlignHCenter)

        self.ck_ani_stat_out = QCheckBox(self.frame_ani_status_cks)
        self.ck_ani_stat_out.setObjectName(u"ck_ani_stat_out")
        self.ck_ani_stat_out.setChecked(False)

        self.lyt_grid_ani_status.addWidget(self.ck_ani_stat_out, 1, 9, 1, 1, Qt.AlignHCenter)

        self.label_ani_stat_dir = QLabel(self.frame_ani_status_cks)
        self.label_ani_stat_dir.setObjectName(u"label_ani_stat_dir")

        self.lyt_grid_ani_status.addWidget(self.label_ani_stat_dir, 0, 6, 1, 1, Qt.AlignHCenter)

        self.ck_ani_stat_dir = QCheckBox(self.frame_ani_status_cks)
        self.ck_ani_stat_dir.setObjectName(u"ck_ani_stat_dir")
        self.ck_ani_stat_dir.setChecked(False)

        self.lyt_grid_ani_status.addWidget(self.ck_ani_stat_dir, 1, 6, 1, 1, Qt.AlignHCenter)


        self.verticalLayout_12.addLayout(self.lyt_grid_ani_status)


        self.verticalLayout_8.addWidget(self.frame_ani_status_cks)


        self.verticalLayout_7.addWidget(self.gb_filter_ani_status)

        self.gb_filter_render_log = QGroupBox(self.gb_filter_ani)
        self.gb_filter_render_log.setObjectName(u"gb_filter_render_log")
        self.verticalLayout_14 = QVBoxLayout(self.gb_filter_render_log)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.ck_cmp_render_log_all = QCheckBox(self.gb_filter_render_log)
        self.ck_cmp_render_log_all.setObjectName(u"ck_cmp_render_log_all")
        self.ck_cmp_render_log_all.setChecked(True)

        self.horizontalLayout_8.addWidget(self.ck_cmp_render_log_all)

        self.label_compare_to_rende_log = QLabel(self.gb_filter_render_log)
        self.label_compare_to_rende_log.setObjectName(u"label_compare_to_rende_log")

        self.horizontalLayout_8.addWidget(self.label_compare_to_rende_log)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)


        self.verticalLayout_14.addLayout(self.horizontalLayout_8)

        self.frame_cmp_render_log = QFrame(self.gb_filter_render_log)
        self.frame_cmp_render_log.setObjectName(u"frame_cmp_render_log")
        self.frame_cmp_render_log.setMinimumSize(QSize(0, 0))
        self.frame_cmp_render_log.setFrameShape(QFrame.StyledPanel)
        self.frame_cmp_render_log.setFrameShadow(QFrame.Plain)
        self.verticalLayout_15 = QVBoxLayout(self.frame_cmp_render_log)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_cmp_ani_pub_ver = QLabel(self.frame_cmp_render_log)
        self.label_cmp_ani_pub_ver.setObjectName(u"label_cmp_ani_pub_ver")

        self.gridLayout_6.addWidget(self.label_cmp_ani_pub_ver, 0, 0, 1, 1, Qt.AlignHCenter)

        self.label_cmp_ani_update_time = QLabel(self.frame_cmp_render_log)
        self.label_cmp_ani_update_time.setObjectName(u"label_cmp_ani_update_time")

        self.gridLayout_6.addWidget(self.label_cmp_ani_update_time, 0, 1, 1, 1, Qt.AlignHCenter)

        self.ck_cmp_ani_pub_ver = QCheckBox(self.frame_cmp_render_log)
        self.ck_cmp_ani_pub_ver.setObjectName(u"ck_cmp_ani_pub_ver")
        self.ck_cmp_ani_pub_ver.setChecked(True)

        self.gridLayout_6.addWidget(self.ck_cmp_ani_pub_ver, 1, 0, 1, 1, Qt.AlignHCenter)

        self.ck_cmp_ani_update_time = QCheckBox(self.frame_cmp_render_log)
        self.ck_cmp_ani_update_time.setObjectName(u"ck_cmp_ani_update_time")
        self.ck_cmp_ani_update_time.setChecked(True)

        self.gridLayout_6.addWidget(self.ck_cmp_ani_update_time, 1, 1, 1, 1, Qt.AlignHCenter)


        self.verticalLayout_15.addLayout(self.gridLayout_6)


        self.verticalLayout_14.addWidget(self.frame_cmp_render_log)


        self.verticalLayout_7.addWidget(self.gb_filter_render_log)


        self.lyt_vbox_filter.addWidget(self.gb_filter_ani)

        self.gb_filter_fx_status = QGroupBox(self.scrollAreaWidgetContents)
        self.gb_filter_fx_status.setObjectName(u"gb_filter_fx_status")
        self.gb_filter_fx_status.setEnabled(True)
        self.gb_filter_fx_status.setMaximumSize(QSize(16777215, 16777215))
        self.gb_filter_fx_status.setBaseSize(QSize(0, 0))
        self.verticalLayout_9 = QVBoxLayout(self.gb_filter_fx_status)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.gb_fx_title = QGroupBox(self.gb_filter_fx_status)
        self.gb_fx_title.setObjectName(u"gb_fx_title")
        self.gb_fx_title.setFlat(True)
        self.horizontalLayout_12 = QHBoxLayout(self.gb_fx_title)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.btn_fold_fx = QPushButton(self.gb_fx_title)
        self.btn_fold_fx.setObjectName(u"btn_fold_fx")
        self.btn_fold_fx.setMinimumSize(QSize(18, 18))
        self.btn_fold_fx.setMaximumSize(QSize(18, 18))
        self.btn_fold_fx.setIcon(icon)
        self.btn_fold_fx.setFlat(False)

        self.horizontalLayout_12.addWidget(self.btn_fold_fx)

        self.label_fx_title = QLabel(self.gb_fx_title)
        self.label_fx_title.setObjectName(u"label_fx_title")

        self.horizontalLayout_12.addWidget(self.label_fx_title)


        self.verticalLayout_9.addWidget(self.gb_fx_title)

        self.gb_fx_status = QGroupBox(self.gb_filter_fx_status)
        self.gb_fx_status.setObjectName(u"gb_fx_status")
        self.verticalLayout_17 = QVBoxLayout(self.gb_fx_status)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.ck_fx_stat_all = QCheckBox(self.gb_fx_status)
        self.ck_fx_stat_all.setObjectName(u"ck_fx_stat_all")

        self.horizontalLayout_10.addWidget(self.ck_fx_stat_all)

        self.label_fx_status = QLabel(self.gb_fx_status)
        self.label_fx_status.setObjectName(u"label_fx_status")

        self.horizontalLayout_10.addWidget(self.label_fx_status)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)


        self.verticalLayout_17.addLayout(self.horizontalLayout_10)

        self.frame_fx_status_cks = QFrame(self.gb_fx_status)
        self.frame_fx_status_cks.setObjectName(u"frame_fx_status_cks")
        self.frame_fx_status_cks.setEnabled(True)
        self.frame_fx_status_cks.setMaximumSize(QSize(16777215, 16777215))
        self.frame_fx_status_cks.setFrameShape(QFrame.StyledPanel)
        self.frame_fx_status_cks.setFrameShadow(QFrame.Plain)
        self.frame_fx_status_cks.setLineWidth(0)
        self.verticalLayout_10 = QVBoxLayout(self.frame_fx_status_cks)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_fx_stat_omt = QLabel(self.frame_fx_status_cks)
        self.label_fx_stat_omt.setObjectName(u"label_fx_stat_omt")

        self.gridLayout_2.addWidget(self.label_fx_stat_omt, 0, 7, 1, 1, Qt.AlignHCenter)

        self.label_fx_stat_pubr = QLabel(self.frame_fx_status_cks)
        self.label_fx_stat_pubr.setObjectName(u"label_fx_stat_pubr")

        self.gridLayout_2.addWidget(self.label_fx_stat_pubr, 0, 1, 1, 1, Qt.AlignHCenter)

        self.label_fx_stat_wip = QLabel(self.frame_fx_status_cks)
        self.label_fx_stat_wip.setObjectName(u"label_fx_stat_wip")

        self.gridLayout_2.addWidget(self.label_fx_stat_wip, 0, 2, 1, 1, Qt.AlignHCenter)

        self.label_fx_stat_retake = QLabel(self.frame_fx_status_cks)
        self.label_fx_stat_retake.setObjectName(u"label_fx_stat_retake")

        self.gridLayout_2.addWidget(self.label_fx_stat_retake, 0, 4, 1, 1, Qt.AlignHCenter)

        self.label_fx_stat_done = QLabel(self.frame_fx_status_cks)
        self.label_fx_stat_done.setObjectName(u"label_fx_stat_done")

        self.gridLayout_2.addWidget(self.label_fx_stat_done, 0, 0, 1, 1, Qt.AlignHCenter)

        self.label_fx_stat_out = QLabel(self.frame_fx_status_cks)
        self.label_fx_stat_out.setObjectName(u"label_fx_stat_out")

        self.gridLayout_2.addWidget(self.label_fx_stat_out, 0, 8, 1, 1, Qt.AlignHCenter)

        self.label_fx_stat_assign = QLabel(self.frame_fx_status_cks)
        self.label_fx_stat_assign.setObjectName(u"label_fx_stat_assign")

        self.gridLayout_2.addWidget(self.label_fx_stat_assign, 0, 3, 1, 1, Qt.AlignHCenter)

        self.label_fx_stat_hld = QLabel(self.frame_fx_status_cks)
        self.label_fx_stat_hld.setObjectName(u"label_fx_stat_hld")

        self.gridLayout_2.addWidget(self.label_fx_stat_hld, 0, 6, 1, 1, Qt.AlignHCenter)

        self.ck_fx_stat_done = QCheckBox(self.frame_fx_status_cks)
        self.ck_fx_stat_done.setObjectName(u"ck_fx_stat_done")
        self.ck_fx_stat_done.setChecked(False)

        self.gridLayout_2.addWidget(self.ck_fx_stat_done, 1, 0, 1, 1, Qt.AlignHCenter)

        self.ck_fx_stat_pubr = QCheckBox(self.frame_fx_status_cks)
        self.ck_fx_stat_pubr.setObjectName(u"ck_fx_stat_pubr")
        self.ck_fx_stat_pubr.setChecked(True)

        self.gridLayout_2.addWidget(self.ck_fx_stat_pubr, 1, 1, 1, 1, Qt.AlignHCenter)

        self.ck_fx_stat_wip = QCheckBox(self.frame_fx_status_cks)
        self.ck_fx_stat_wip.setObjectName(u"ck_fx_stat_wip")
        self.ck_fx_stat_wip.setChecked(True)

        self.gridLayout_2.addWidget(self.ck_fx_stat_wip, 1, 2, 1, 1, Qt.AlignHCenter)

        self.ck_fx_stat_assign = QCheckBox(self.frame_fx_status_cks)
        self.ck_fx_stat_assign.setObjectName(u"ck_fx_stat_assign")
        self.ck_fx_stat_assign.setChecked(True)

        self.gridLayout_2.addWidget(self.ck_fx_stat_assign, 1, 3, 1, 1, Qt.AlignHCenter)

        self.ck_fx_stat_retake = QCheckBox(self.frame_fx_status_cks)
        self.ck_fx_stat_retake.setObjectName(u"ck_fx_stat_retake")
        self.ck_fx_stat_retake.setChecked(True)

        self.gridLayout_2.addWidget(self.ck_fx_stat_retake, 1, 4, 1, 1, Qt.AlignHCenter)

        self.ck_fx_stat_hld = QCheckBox(self.frame_fx_status_cks)
        self.ck_fx_stat_hld.setObjectName(u"ck_fx_stat_hld")
        self.ck_fx_stat_hld.setChecked(False)

        self.gridLayout_2.addWidget(self.ck_fx_stat_hld, 1, 6, 1, 1, Qt.AlignHCenter)

        self.ck_fx_stat_omt = QCheckBox(self.frame_fx_status_cks)
        self.ck_fx_stat_omt.setObjectName(u"ck_fx_stat_omt")

        self.gridLayout_2.addWidget(self.ck_fx_stat_omt, 1, 7, 1, 1, Qt.AlignHCenter)

        self.ck_fx_stat_out = QCheckBox(self.frame_fx_status_cks)
        self.ck_fx_stat_out.setObjectName(u"ck_fx_stat_out")

        self.gridLayout_2.addWidget(self.ck_fx_stat_out, 1, 8, 1, 1, Qt.AlignHCenter)

        self.label_fx_stat_dir = QLabel(self.frame_fx_status_cks)
        self.label_fx_stat_dir.setObjectName(u"label_fx_stat_dir")

        self.gridLayout_2.addWidget(self.label_fx_stat_dir, 0, 5, 1, 1, Qt.AlignHCenter)

        self.ck_fx_stat_dir = QCheckBox(self.frame_fx_status_cks)
        self.ck_fx_stat_dir.setObjectName(u"ck_fx_stat_dir")
        self.ck_fx_stat_dir.setChecked(False)

        self.gridLayout_2.addWidget(self.ck_fx_stat_dir, 1, 5, 1, 1, Qt.AlignHCenter)


        self.verticalLayout_10.addLayout(self.gridLayout_2)


        self.verticalLayout_17.addWidget(self.frame_fx_status_cks)


        self.verticalLayout_9.addWidget(self.gb_fx_status)

        self.gb_filter_cmp_time = QGroupBox(self.gb_filter_fx_status)
        self.gb_filter_cmp_time.setObjectName(u"gb_filter_cmp_time")
        self.verticalLayout_16 = QVBoxLayout(self.gb_filter_cmp_time)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.ck_cmp_startDate = QCheckBox(self.gb_filter_cmp_time)
        self.ck_cmp_startDate.setObjectName(u"ck_cmp_startDate")
        self.ck_cmp_startDate.setChecked(True)

        self.horizontalLayout_13.addWidget(self.ck_cmp_startDate)

        self.label_filter_start_time = QLabel(self.gb_filter_cmp_time)
        self.label_filter_start_time.setObjectName(u"label_filter_start_time")

        self.horizontalLayout_13.addWidget(self.label_filter_start_time)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_7)


        self.verticalLayout_16.addLayout(self.horizontalLayout_13)


        self.verticalLayout_9.addWidget(self.gb_filter_cmp_time)


        self.lyt_vbox_filter.addWidget(self.gb_filter_fx_status)

        self.gb_filter_tasks = QGroupBox(self.scrollAreaWidgetContents)
        self.gb_filter_tasks.setObjectName(u"gb_filter_tasks")
        self.gb_filter_tasks.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_19 = QVBoxLayout(self.gb_filter_tasks)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gb_task_title = QGroupBox(self.gb_filter_tasks)
        self.gb_task_title.setObjectName(u"gb_task_title")
        self.gb_task_title.setFlat(True)
        self.horizontalLayout_14 = QHBoxLayout(self.gb_task_title)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_fold_task = QPushButton(self.gb_task_title)
        self.btn_fold_task.setObjectName(u"btn_fold_task")
        self.btn_fold_task.setMinimumSize(QSize(18, 18))
        self.btn_fold_task.setMaximumSize(QSize(18, 18))
        self.btn_fold_task.setIcon(icon)
        self.btn_fold_task.setFlat(False)

        self.horizontalLayout_14.addWidget(self.btn_fold_task)

        self.label_task_title = QLabel(self.gb_task_title)
        self.label_task_title.setObjectName(u"label_task_title")

        self.horizontalLayout_14.addWidget(self.label_task_title)


        self.verticalLayout_19.addWidget(self.gb_task_title)

        self.tree_task = QTreeWidget(self.gb_filter_tasks)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.tree_task.setHeaderItem(__qtreewidgetitem)
        self.tree_task.setObjectName(u"tree_task")
        self.tree_task.setSelectionMode(QAbstractItemView.NoSelection)
        self.tree_task.setIndentation(7)
        self.tree_task.header().setVisible(False)

        self.verticalLayout_19.addWidget(self.tree_task)


        self.lyt_vbox_filter.addWidget(self.gb_filter_tasks)

        self.gb_filter_users = QGroupBox(self.scrollAreaWidgetContents)
        self.gb_filter_users.setObjectName(u"gb_filter_users")
        self.verticalLayout_20 = QVBoxLayout(self.gb_filter_users)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.gb_user_title = QGroupBox(self.gb_filter_users)
        self.gb_user_title.setObjectName(u"gb_user_title")
        self.gb_user_title.setFlat(True)
        self.horizontalLayout_15 = QHBoxLayout(self.gb_user_title)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.btn_fold_user = QPushButton(self.gb_user_title)
        self.btn_fold_user.setObjectName(u"btn_fold_user")
        self.btn_fold_user.setMinimumSize(QSize(18, 18))
        self.btn_fold_user.setMaximumSize(QSize(18, 18))
        self.btn_fold_user.setIcon(icon)
        self.btn_fold_user.setFlat(False)

        self.horizontalLayout_15.addWidget(self.btn_fold_user)

        self.label_user_title = QLabel(self.gb_user_title)
        self.label_user_title.setObjectName(u"label_user_title")

        self.horizontalLayout_15.addWidget(self.label_user_title)


        self.verticalLayout_20.addWidget(self.gb_user_title)

        self.tree_user = QTreeWidget(self.gb_filter_users)
        self.tree_user.setObjectName(u"tree_user")
        self.tree_user.setSelectionMode(QAbstractItemView.NoSelection)
        self.tree_user.setIndentation(7)
        self.tree_user.setSortingEnabled(True)
        self.tree_user.header().setVisible(False)

        self.verticalLayout_20.addWidget(self.tree_user)


        self.lyt_vbox_filter.addWidget(self.gb_filter_users)


        self.verticalLayout_18.addLayout(self.lyt_vbox_filter)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)


        self.vlayout_filters.addWidget(self.gb_filters)


        self.verticalLayout_3.addLayout(self.vlayout_filters)


        self.horizontalLayout.addWidget(self.frame_filters)

        self.gb_shotcode = QGroupBox(self.centralwidget)
        self.gb_shotcode.setObjectName(u"gb_shotcode")
        self.gb_shotcode.setMinimumSize(QSize(500, 0))
        self.gb_shotcode.setCheckable(False)
        self.verticalLayout_2 = QVBoxLayout(self.gb_shotcode)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.ck_all_shotcode = QCheckBox(self.gb_shotcode)
        self.ck_all_shotcode.setObjectName(u"ck_all_shotcode")
        self.ck_all_shotcode.setEnabled(True)

        self.horizontalLayout_11.addWidget(self.ck_all_shotcode)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_8)

        self.btn_reload_data = QPushButton(self.gb_shotcode)
        self.btn_reload_data.setObjectName(u"btn_reload_data")
        icon1 = QIcon()
        icon1.addFile(u":/icon/sync.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_reload_data.setIcon(icon1)
        self.btn_reload_data.setIconSize(QSize(18, 18))
        self.btn_reload_data.setCheckable(False)

        self.horizontalLayout_11.addWidget(self.btn_reload_data)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.tree_shot = QTreeWidget(self.gb_shotcode)
        self.tree_shot.headerItem().setText(1, "")
        self.tree_shot.headerItem().setText(2, "")
        self.tree_shot.headerItem().setText(3, "")
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"shotCode");
        self.tree_shot.setHeaderItem(__qtreewidgetitem1)
        self.tree_shot.setObjectName(u"tree_shot")
        self.tree_shot.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tree_shot.setLineWidth(1)
        self.tree_shot.setAlternatingRowColors(False)
        self.tree_shot.setSelectionMode(QAbstractItemView.NoSelection)
        self.tree_shot.setAutoExpandDelay(-1)
        self.tree_shot.setIndentation(7)
        self.tree_shot.setItemsExpandable(False)
        self.tree_shot.setSortingEnabled(True)
        self.tree_shot.setHeaderHidden(False)
        self.tree_shot.setExpandsOnDoubleClick(False)
        self.tree_shot.setColumnCount(7)
        self.tree_shot.header().setVisible(True)
        self.tree_shot.header().setCascadingSectionResizes(False)
        self.tree_shot.header().setDefaultSectionSize(50)
        self.tree_shot.header().setStretchLastSection(False)

        self.verticalLayout_2.addWidget(self.tree_shot)


        self.horizontalLayout.addWidget(self.gb_shotcode)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_run = QPushButton(self.centralwidget)
        self.btn_run.setObjectName(u"btn_run")

        self.horizontalLayout_2.addWidget(self.btn_run)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)

        self.horizontalLayout_2.addWidget(self.progressBar)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.btn_fold_ani.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Auto Render", None))
        self.gb_filters.setTitle(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.label_FilterType.setText(QCoreApplication.translate("MainWindow", u"Filter Type", None))
        self.cb_preset.setItemText(0, QCoreApplication.translate("MainWindow", u"Preset_Todo", None))
        self.cb_preset.setItemText(1, QCoreApplication.translate("MainWindow", u"Preset_Ing", None))
        self.cb_preset.setItemText(2, QCoreApplication.translate("MainWindow", u"Custom", None))

        self.gb_filter_project.setTitle("")
        self.label_project.setText(QCoreApplication.translate("MainWindow", u"\ud504\ub85c\uc81d\ud2b8", None))
        self.gb_filter_shot_status.setTitle("")
        self.ck_shot_stat_all.setText("")
        self.label_shot_status.setText(QCoreApplication.translate("MainWindow", u"Shot Status", None))
        self.label_shot_stat_wip.setText(QCoreApplication.translate("MainWindow", u"wip", None))
        self.label_shot_stat_omt.setText(QCoreApplication.translate("MainWindow", u"omt", None))
        self.ck_shot_stat_omt.setText("")
        self.ck_shot_stat_wip.setText("")
        self.label_shot_stat_retake.setText(QCoreApplication.translate("MainWindow", u"retake", None))
        self.label_shot_stat_dir.setText(QCoreApplication.translate("MainWindow", u"dir", None))
        self.label_shot_stat_done.setText(QCoreApplication.translate("MainWindow", u"done", None))
        self.ck_shot_stat_dir.setText("")
        self.label_shot_stat_assign.setText(QCoreApplication.translate("MainWindow", u"assign", None))
        self.ck_shot_stat_retake.setText("")
        self.ck_shot_stat_done.setText("")
        self.ck_shot_stat_assign.setText("")
        self.label_shot_stat_hld.setText(QCoreApplication.translate("MainWindow", u"hld", None))
        self.ck_shot_stat_hld.setText("")
        self.label_shot_stat_out.setText(QCoreApplication.translate("MainWindow", u"out", None))
        self.ck_shot_stat_out.setText("")
        self.gb_filter_ani.setTitle("")
        self.gb_ani_title.setTitle("")
        self.btn_fold_ani.setText("")
        self.label_animation_title.setText(QCoreApplication.translate("MainWindow", u"Animation", None))
        self.gb_filter_ani_pub.setTitle("")
        self.ck_aniPub_all.setText("")
        self.label_pub_ani.setText(QCoreApplication.translate("MainWindow", u"Published Ani", None))
        self.ck_aniPub_tpub.setText("")
        self.ck_aniPub_wtg.setText("")
        self.ck_aniPub_pub.setText("")
        self.label_ani_pub.setText(QCoreApplication.translate("MainWindow", u"pub", None))
        self.ck_aniPub_retake.setText("")
        self.label_ani_wtg.setText(QCoreApplication.translate("MainWindow", u"wtg", None))
        self.label_ani_retake.setText(QCoreApplication.translate("MainWindow", u"retake", None))
        self.label_ani_tpub.setText(QCoreApplication.translate("MainWindow", u"tpub", None))
        self.gb_filter_ani_status.setTitle("")
        self.ck_ani_stat_all.setText("")
        self.label_ani_status.setText(QCoreApplication.translate("MainWindow", u"Ani Status", None))
        self.label_ani_stat_assign.setText(QCoreApplication.translate("MainWindow", u"assign", None))
        self.ck_ani_stat_retake.setText("")
        self.ck_ani_stat_assign.setText("")
        self.label_ani_stat_wip.setText(QCoreApplication.translate("MainWindow", u"wip", None))
        self.label_ani_stat_retake.setText(QCoreApplication.translate("MainWindow", u"retake", None))
        self.label_ani_stat_done.setText(QCoreApplication.translate("MainWindow", u"done", None))
        self.label_ani_stat_omt.setText(QCoreApplication.translate("MainWindow", u"omt", None))
        self.label_ani_stat_hld.setText(QCoreApplication.translate("MainWindow", u"hld", None))
        self.ck_ani_stat_pubr.setText("")
        self.ck_ani_stat_wip.setText("")
        self.ck_ani_stat_done.setText("")
        self.label_ani_stat_pubr.setText(QCoreApplication.translate("MainWindow", u"pubr", None))
        self.ck_ani_stat_hld.setText("")
        self.ck_ani_stat_omt.setText("")
        self.label_ani_stat_out.setText(QCoreApplication.translate("MainWindow", u"out", None))
        self.ck_ani_stat_out.setText("")
        self.label_ani_stat_dir.setText(QCoreApplication.translate("MainWindow", u"dir", None))
        self.ck_ani_stat_dir.setText("")
        self.gb_filter_render_log.setTitle("")
        self.ck_cmp_render_log_all.setText("")
        self.label_compare_to_rende_log.setText(QCoreApplication.translate("MainWindow", u"Compare to Render Log", None))
        self.label_cmp_ani_pub_ver.setText(QCoreApplication.translate("MainWindow", u"ani_pub_ver", None))
        self.label_cmp_ani_update_time.setText(QCoreApplication.translate("MainWindow", u"ani_update_time", None))
        self.ck_cmp_ani_pub_ver.setText("")
        self.ck_cmp_ani_update_time.setText("")
        self.gb_filter_fx_status.setTitle("")
        self.gb_fx_title.setTitle("")
        self.btn_fold_fx.setText("")
        self.label_fx_title.setText(QCoreApplication.translate("MainWindow", u"FX", None))
        self.gb_fx_status.setTitle("")
        self.ck_fx_stat_all.setText("")
        self.label_fx_status.setText(QCoreApplication.translate("MainWindow", u"FX Status", None))
        self.label_fx_stat_omt.setText(QCoreApplication.translate("MainWindow", u"omt", None))
        self.label_fx_stat_pubr.setText(QCoreApplication.translate("MainWindow", u"pubr", None))
        self.label_fx_stat_wip.setText(QCoreApplication.translate("MainWindow", u"wip", None))
        self.label_fx_stat_retake.setText(QCoreApplication.translate("MainWindow", u"retake", None))
        self.label_fx_stat_done.setText(QCoreApplication.translate("MainWindow", u"done", None))
        self.label_fx_stat_out.setText(QCoreApplication.translate("MainWindow", u"out", None))
        self.label_fx_stat_assign.setText(QCoreApplication.translate("MainWindow", u"assign", None))
        self.label_fx_stat_hld.setText(QCoreApplication.translate("MainWindow", u"hld", None))
        self.ck_fx_stat_done.setText("")
        self.ck_fx_stat_pubr.setText("")
        self.ck_fx_stat_wip.setText("")
        self.ck_fx_stat_assign.setText("")
        self.ck_fx_stat_retake.setText("")
        self.ck_fx_stat_hld.setText("")
        self.ck_fx_stat_omt.setText("")
        self.ck_fx_stat_out.setText("")
        self.label_fx_stat_dir.setText(QCoreApplication.translate("MainWindow", u"dir", None))
        self.ck_fx_stat_dir.setText("")
        self.gb_filter_cmp_time.setTitle("")
        self.ck_cmp_startDate.setText("")
        self.label_filter_start_time.setText(QCoreApplication.translate("MainWindow", u"Compare (Start Date < Today )", None))
        self.gb_filter_tasks.setTitle("")
        self.gb_task_title.setTitle("")
        self.btn_fold_task.setText("")
        self.label_task_title.setText(QCoreApplication.translate("MainWindow", u"Task", None))
        self.gb_filter_users.setTitle("")
        self.gb_user_title.setTitle("")
        self.btn_fold_user.setText("")
        self.label_user_title.setText(QCoreApplication.translate("MainWindow", u"User", None))
        ___qtreewidgetitem = self.tree_user.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"1", None));
        self.gb_shotcode.setTitle(QCoreApplication.translate("MainWindow", u"ShotCode", None))
        self.ck_all_shotcode.setText(QCoreApplication.translate("MainWindow", u"\uc804\uccb4 \uc120\ud0dd", None))
#if QT_CONFIG(tooltip)
        self.btn_reload_data.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Reload Data</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_reload_data.setText("")
        ___qtreewidgetitem1 = self.tree_shot.headerItem()
        ___qtreewidgetitem1.setText(6, QCoreApplication.translate("MainWindow", u"task", None));
        ___qtreewidgetitem1.setText(5, QCoreApplication.translate("MainWindow", u"due_date", None));
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("MainWindow", u"start_date", None));
        self.btn_run.setText(QCoreApplication.translate("MainWindow", u"Run AutoRender", None))
    # retranslateUi


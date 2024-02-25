#!/usr/bin/env python
# encoding=utf-8
# author        :   kim junhyuk
# created date  :   2024.02.25
# modified date  :   2024.02.25
# description  :   

import os, glob, re
import json
from collections import OrderedDict
from datetime import datetime


g_time_format = '%Y-%m-%d %H:%M:%S'

def get_precomp_dir(prj, seq, shot, task):
    return os.path.join(get_job_dir(prj, seq, shot, task), "precomp")
def get_job_dir(prj, seq, shot, task):
    return os.path.join("/show", prj, "seq", seq, seq + "_" + shot, task, "dev")
def get_shotcode_dir(prj, seq, shot):
    return os.path.join("/show", prj, "seq", seq, seq + "_" + shot)
def get_seq_dir(prj, seq):
    return os.path.join("/show", prj, "seq", seq)
def get_path_log_json(prj, seq, shot, task):
    return os.path.join(get_shotcode_dir(prj, seq, shot), task, "renderLog.json")

def get_file_baseName(seq, shot,task):
    return seq + "_" + shot + "_" +task

def get_highest_version(list_files, v=1):
    name = ""
    for file_name in list_files:
        try:
            vernum = int( re.findall("v\d+", file_name)[-1][1:] )
        except Exception as e:
            print('Error Message:', e)
            continue
        if v > vernum:
            continue
        v = vernum
        name = file_name
    return v, name

def write_log_json(dict_sg_data, dir_path):
    dict_data = dict_sg_data.copy()

    # pop before render log data
    dict_data.pop("log_last_ani_pub_ver")
    dict_data.pop("log_last_render_time")

    shot_code = dict_data["shot_code"]
    task = dict_data["task"]
    job_path = os.path.join(dir_path, shot_code)
    path_json = os.path.join(job_path, "renderLog.json")

    now_time = datetime.now().strftime(g_time_format)

    # read exist json data
    json_data = read_log_json(path_json)

    print("json_data : ", json_data)

    print("1 dict_data :", dict_data)

    dict_data["ani_pub_updated_time"] = dict_data["ani_pub_updated_time"].strftime(g_time_format)


    if json_data:
        json_data[now_time] = dict_data
    else:
        json_data = OrderedDict()
        json_data[now_time] = dict_data

    with open(path_json, "w") as p_json:
        json.dump(json_data, p_json, indent=4)
        print("write jsson file!@#!@#!@")

def read_log_json(path_json):
    if os.path.exists(path_json):
        with open(path_json, "r") as p_json:
            json_data = json.load(p_json, object_pairs_hook=OrderedDict)
        return json_data
    else:
        return None

def getFileInfo(dir_path, list_shot_info):
    dict_result = {"last_ani_pub_ver":[], "last_render_time":[]
        , "last_mov":[], "last_nk":[], "last_hip":[]}
    cnt_json = 0
    none_pub_ver = 0
    dt_none_rd_time = datetime.strptime("1111-11-11 11:11:11", g_time_format)
    for dict_shot_info in list_shot_info:
        shot_code = dict_shot_info["shot_code"]

        job_path = os.path.join(dir_path, shot_code)
        path_json = os.path.join(job_path, "renderLog.json")
        if os.path.exists(path_json):
            # -- read renderLog.json
            json_data = read_log_json(path_json)
            if len(json_data) <= 0:
                dict_result["last_ani_pub_ver"].append(none_pub_ver)
                dict_result["last_render_time"].append(dt_none_rd_time)
            else:
                last_time = list(json_data.keys())[-1]
                dict_result["last_ani_pub_ver"].append(json_data[last_time]["ani_pub_ver"])
                last_datetime = datetime.strptime(last_time, g_time_format)
                dict_result["last_render_time"].append(last_datetime)
                cnt_json += 1
        else:
            dict_result["last_ani_pub_ver"].append(none_pub_ver)
            dict_result["last_render_time"].append(dt_none_rd_time)

        # -- get highest hip file name
        if os.path.exists(job_path):
            list_hip = glob.glob(job_path + f"/{shot_code}_v*.hip")
            if len(list_hip) > 0:
                list_hip_names = [os.path.basename(hip_path) for hip_path in list_hip]
                _, highest_hip_name = get_highest_version(list_hip_names)
                dict_result["last_hip"].append(highest_hip_name)
            else:
                dict_result["last_hip"].append(None)
        else:
            dict_result["last_hip"].append(None)

        if os.path.exists(job_path):
            # -- get highest mov file name
            list_mov = glob.glob(job_path + f"/{shot_code}_v*.mov")
            if len(list_mov) > 0:
                list_mov_names = [os.path.basename(mov_path) for mov_path in list_mov]
                _, highest_mov_name = get_highest_version(list_mov_names)
                dict_result["last_mov"].append(highest_mov_name)
            else:
                dict_result["last_mov"].append(None)

            # -- get highest nk file name
            list_nk = glob.glob(job_path + f"/{shot_code}_v*.nk")
            if len(list_nk) > 0:
                list_nk_names = [os.path.basename(nk_path) for nk_path in list_nk]
                _, highest_nk_name = get_highest_version(list_nk_names)
                dict_result["last_nk"].append(highest_nk_name)
            else:
                dict_result["last_nk"].append(None)
        else:
            dict_result["last_mov"].append(None)
            dict_result["last_nk"].append(None)

    return dict_result
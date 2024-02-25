import pandas as pd


# create pandas data to csv file


# ---------------------- FX ----------------------
if True:
    data = {
        "shot_code": ["AAA_001", "BBB_001", "CCC_001", "DDD_001", "EEE_001", "FFF_001"]
        , "geo_type": ["pighead", "templatebody", "templatehead", "pighead", "templatebody", "templatehead"]

        , "cam_transform_x": [-2.7043, 0.207684, 0.400994, -2.7043, 0.207684, 0.400994]
        , "cam_transform_y": [2.50581, 3.17331, 0.650936,   2.50581, 3.17331, 0.650936]
        , "cam_transform_z": [4.06212, -2.52276, 0.834343, 4.06212, -2.52276, 0.834343]

        , "cam_rotation_x": [-30.4744, -40.0752, -28.456, -30.4744, -40.0752, -28.456]
        , "cam_rotation_y": [-38.8465, 174.118, 28.474, -38.8465, 174.118, 28.474]
        , "cam_rotation_z": [-3.05957e-06, -6.3501e-06, -6.60436e-06, -3.05957e-06, -6.3501e-06, -6.60436e-06]

        , "project": ["R&D", "R&D","R&D","R&D","R&D","R&D"]
        , "status": ["assign", "wip", "retake", "done", "hld", "omt"]
        , "task": ["electric", "electric", "electric", "ocean", "fire", "smoke"]
        , "shot_status": ["assign", "wip", "retake", "done", "dir", "omt"]
        , "user" : [{"id":111, "name":"simon"}, {"id":111, "name":"simon"}, {"id":111, "name":"simon"}, {"id":444, "name":"mendy"}, {"id":555, "name":"silva"}, {"id":666, "name":"luka"}]
        , "start_date": ["2024-02-24", "2024-02-22", "2024-02-20", None, "2024-04-07", "2024-11-11"]
        , "due_date": ["2024-03-20", "2024-03-12", "2024-03-01", None, "2024-05-07", "2024-12-24"]
    }
    df = pd.DataFrame(data)
    df.to_csv("sg_fx_info.csv", index=False)


# ---------------------- ANI STATUS ----------------------
if True:
    data = {
        "shot_code": ["AAA_001", "BBB_001", "CCC_001", "DDD_001", "EEE_001", "FFF_001"]
        , "project":    ["R&D", "R&D","R&D","R&D","R&D","R&D"]
        , "status":  ["assign", "wip", "retake", "done", "hld", "omt"]
    }
    df = pd.DataFrame(data)
    df.to_csv("sg_ani_status_info.csv", index=False)


# ---------------------- ANI PUB STATUS ----------------------
if True:
    data = {
        "shot_code": ["AAA_001", "BBB_001", "CCC_001", "DDD_001", "EEE_001", "FFF_001", "AAA_001", "BBB_001", "CCC_001", "CCC_001"]
        , "project":    ["R&D", "R&D","R&D","R&D","R&D","R&D","R&D","R&D","R&D","R&D"]
        , "pub_status":  ["pub", "pub", "pub", "tpub", "retake", "wtg", "pub", "pub", "pub", "pub"] # wtg waiting to start
        , "pub_ver":[4, 4, 4, 7, 2, 1, 8, 9, 10, 12]
        , "updated_at" : [
            "2024-02-10 10:50:38", "2024-02-12 13:20:38", "2024-02-20 11:10:10"
            , "2024-03-01 11:10:10", "2024-04-02 18:20:10", "2024-04-02 11:15:50"
        , "2024-02-11 13:10:10", "2024-04-02 20:20:10", "2024-04-02 15:15:50", "2024-04-02 20:15:50"]
    }
    df = pd.DataFrame(data)
    df.to_csv("sg_ani_pub_info.csv", index=False)



print("save done ~~!~!")
import os, sys
import subprocess
import json
os.environ["NUKE_INTERACTIVE"] = "1"
nk_argv = sys.argv
#['C:\\Class\\nk.py', '{"nkGeo": "path geo", "nkFX": "path fx path"}']
import nuke

# C:\Program Files\Nuke15.0v1\python.exe
# print("import nuke : ", nuke)
#--------------------------

def createNode(dict_args):
    nuke.scriptClear()

    start_frame = dict_args["start_frame"]
    end_frame = dict_args["end_frame"]

    space = 200

    nuke.root()["first_frame"].setValue(start_frame)
    nuke.root()["last_frame"].setValue(end_frame)

    # shot = "CCC_001"
    # version = "v004"

    # read geo node
    # img_geo_path = f"C:/Class/{shot}/{shot}_{version}_geo/{shot}_{version}_geo_%04d.jpg"
    img_geo_path = dict_args["nk_geo"].replace("\\", "/")
    geo_read = nuke.nodes.Read(file=img_geo_path, format="HD_720", first=start_frame, last=end_frame)

    # read fx node
    # img_fx_path = f"C:/Class/{shot}/{shot}_{version}_fx/{shot}_{version}_fx_%04d.jpg"
    img_fx_path = dict_args["nk_fx"].replace("\\", "/")
    fx_read = nuke.nodes.Read(file=img_fx_path, format="HD_720", first=start_frame, last=end_frame)
    fx_read.setXYpos(geo_read.xpos() + space*2, geo_read.ypos())
    # fx grade
    fx_grade = nuke.nodes.Grade(inputs=[fx_read])
    fx_grade['white'].setValue([0.116431, 0.874786, 1, 1])
    fx_grade.setXYpos(fx_read.xpos() , fx_read.ypos() + space)
    # fx blur1
    fx_blur1 = nuke.nodes.Blur(inputs=[fx_grade], size=16)
    fx_blur1.setXYpos(fx_grade.xpos() + space, fx_grade.ypos())
    # fx blur2
    fx_blur2 = nuke.nodes.Blur(inputs=[fx_grade], size=37)
    fx_blur2.setXYpos(fx_blur1.xpos() + space, fx_blur1.ypos())

    # blur merge
    fx_mg_blur = nuke.nodes.Merge(inputs=[fx_blur1, fx_blur2])
    fx_mg_blur.setXYpos(fx_blur1.xpos() , fx_blur1.ypos()+ space)

    # merge grade & blur
    fx_mg_grade_blur = nuke.nodes.Merge(inputs=[fx_grade,fx_mg_blur])
    fx_mg_grade_blur.setXYpos(fx_grade.xpos() , fx_grade.ypos()+ space*2)

    # merge geo & blur
    mg_geo_blur = nuke.nodes.Merge(inputs=[geo_read,fx_mg_grade_blur])
    mg_geo_blur.setXYpos(geo_read.xpos() , geo_read.ypos()+ space*3)

    # write node
    # mov_path = f"C:/Class/{shot}/{shot}_{version}.mov"
    mov_path = dict_args["nk_mov"].replace("\\", "/")
    # TODO add "MOV"
    write_mov = nuke.nodes.Write(inputs=[mg_geo_blur], file=mov_path, file_type="mov", name="MOV")
    write_mov.setXYpos(mg_geo_blur.xpos() , mg_geo_blur.ypos()+ space)

    # btn_render = write_mov.knob("Render")
    # btn_render.execute()

    # save nk filed
    nuke.scriptSave(dict_args["nk_path"])

    # create mov
    nk_env = os.environ.copy()
    if "PYTHONPATH" in nk_env.keys():
        del nk_env["PYTHONPATH"]
    if "PYTHONHOME" in nk_env.keys():
        del nk_env["PYTHONHOME"]

    """
    -i        with -x or -t use interactive, not render, licens
    -m n      set max number of concurrent threads for rendering to n, where n > 
    --nukex   run as NukeX instead of standard Nuke
    -X nodes  only execute these nodes (comma-separated list)
    """
    # Nuke15.0.exe -i -X MOV -F 1001-1010 .nk
    cmd = [r'C:\Program Files\Nuke15.0v1\Nuke15.0.exe', '-i', '-X', 'MOV', '-F', str(start_frame)+"-"+str(end_frame), dict_args["nk_path"]]
    p = subprocess.run(cmd, env=nk_env)

    print("make mov done~~!~!~")

if __name__ == "__main__":
    if  len(nk_argv) > 1:
        dict_args = json.loads(nk_argv[-1])
        createNode(dict_args)

    print("nk.py done ~!~!")




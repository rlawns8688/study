
start_frame = 1001
end_frame = 1050
space = 200
nuke.root()["first_frame"].setValue(start_frame)
nuke.root()["last_frame"].setValue(end_frame)
shot = "AAA_001"
version = "v001"
# read geo node
img_geo_path = f"/home/rapa/python/0203/{shot}/{shot}_{version}_geo/{shot}_{version}_geo_%04d.exr"
geo_read = nuke.nodes.Read(file=img_geo_path, format="HD_720", first=start_frame, last=end_frame)
# read fx node
img_fx_path = f"/home/rapa/python/0203/{shot}/{shot}_{version}_fx/{shot}_{version}_fx_%04d.exr"
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
mov_path = f"/home/rapa/python/0203/{shot}/{shot}_{version}.mov"
write_mov = nuke.nodes.Write(inputs=[mg_geo_blur], file=mov_path, file_type="mov")
write_mov.setXYpos(mg_geo_blur.xpos() , mg_geo_blur.ypos()+ space)
btn_render = write_mov.knob("Render")
btn_render.execute()

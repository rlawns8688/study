

import maya.cmds as cmds

def create_playblast(output_path):

    render_nodes = cmds.ls(type='renderLayer')
    for node in render_nodes:
        cmds.setAttr(node + ".renderable", True)
    # playblast 실행
    cmds.playblast(
        format='qt',
        sequenceTime=True,
        clearCache=True,
        viewer=True,
        showOrnaments=True,
        fp=4,
        percent=50,
        compression='jpeg',
        quality=100,
        filename=output_path
    )



# 사용 예시
output_path = "/home/rapa/Downloads/test/test.mov"
create_playblast(output_path)

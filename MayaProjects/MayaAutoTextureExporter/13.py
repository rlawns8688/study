import maya.standalone
maya.standalone.initialize(name='python')

import maya.cmds as cmds
cmds.file('test.ma', open=True)  # 'yourSceneFile.mb'를 여러분의 파일 이름으로 변경하세요

# 여기에 코드를 입력하세요

maya.standalone.uninitialize()

import maya.cmds as cmds
import maya.api.OpenMaya as om



import maya.standalone
maya.standalone.initialize()

import maya.cmds as cmds

# 씬 로드
cmds.file("/home/rapa/scene.ma", open=True, f=True)

# 추가적인 작업 수행 가능

# 종료
maya.standalone.uninitialize()
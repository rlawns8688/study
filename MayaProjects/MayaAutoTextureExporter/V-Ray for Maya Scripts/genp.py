import maya.cmds as cmds
import maya.OpenMaya as om


import maya.cmds as cmds

if not cmds.commandPort(":4434", query=True):
    cmds.commandPort(name=":4434")

basePath = '/home/rapa/Downloads/test/texture2'
files = cmds.getFileList(folder=basePath)
meshPath = '/home/rapa/Downloads/test/test.obj'
mesh = cmds.file(meshPath, i=True,  # import true
          ignoreVersion=True,
          ra=True,  # 덮어쓰기 허용
          mergeNamespacesOnClash=True,  # 네임스페이스 충돌시 병합하기
          options="mo=1",  # 모든 개체 가져오기
          pr=True,  # 상대 경로로 가져오기
          importFrameRate=True,  # 프레임 속도 가져오기
          importTimeRange="override"  # 시간 범위 무시하고 가져오기
          )
mesh_names = cmds.ls( type='transform', dag=True, geometry=True)
#mesh 이름 못받아옴
print(mesh_names)
materialList = [] # test
renderPassList = [] # ['BaseColor', 'Metallic', 'Normal', 'Roughness']
# For Loop to fill materialList and renderPassList
for file in files:
    fileNameSplit = file.split(".")[0].split("_")
    extension = file.split(".")[1]
    material = fileNameSplit[0]
    renderPass = fileNameSplit[-1]
    if material not in materialList:
        materialList.append(material)
    if renderPass not in renderPassList:
        renderPassList.append(renderPass)


shader_node = cmds.shadingNode('aiStandardSurface', asShader=True, name='myShader') # 셰이더 생성
shader_group = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='myNewShaderSG') # 셰이더 그룹 생성
cmds.connectAttr('{}.outColor'.format(shader_node), '{}.surfaceShader'.format(shader_group), force=True)# 두개 연결
# print("쉐이더 맞음", new_shader)
# return new_shader, shader_grp
# for material in materialList:
for renderPass in renderPassList:
    texture_node = cmds.shadingNode("file", asTexture=True, name=(material + "_" + renderPass))
    cmds.setAttr(material + "_" + renderPass + ".fileTextureName",
                 basePath + "/" + material + "_" + renderPass + "." + extension, type="string")
    place2d_node = cmds.shadingNode('place2dTexture', asUtility=True)

    cmds.connectAttr(place2d_node + ".outUV", texture_node + ".uvCoord")
    cmds.connectAttr(place2d_node + ".outUvFilterSize", texture_node + ".uvFilterSize")

    if renderPass == "BaseColor":  # setting correct settings and linking nodes up for colour
        cmds.setAttr(material + "_" + renderPass + ".colorSpace", "sRGB", type="string")#속성 설정
        cmds.connectAttr(texture_node + ".outColor", shader_node + ".baseColor", force=True)

    elif renderPass == "Roughness":  # setting correct settings and linking nodes up for roughness
        cmds.setAttr(material + "_" + renderPass + ".colorSpace", "Raw", type="string")#속성 설정
        cmds.setAttr(texture_node + ".alphaIsLuminance", True)#속성 설정
        cmds.connectAttr(texture_node + ".outAlpha", shader_node + ".specularRoughness", force=True)

    elif renderPass == "Metallic":  # setting correct settings and linking nodes up for metalness
        cmds.setAttr(material + "_" + renderPass + ".colorSpace", "Raw", type="string")#속성 설정
        cmds.setAttr(texture_node + ".alphaIsLuminance", True)#속성 설정
        cmds.connectAttr(texture_node + ".outAlpha", shader_node + ".metalness", force=True)

    elif renderPass == "Normal":  # setting correct settings and linking nodes up for normal map
        cmds.setAttr(material + "_" + renderPass + ".colorSpace", "Raw", type="string")#속성 설정
        bump2d = cmds.shadingNode("bump2d", asTexture=True, name=material + "bump2d")#bump2d생성
        cmds.setAttr(material + "bump2d.bumpInterp", 1)#bump2d 연결
        cmds.connectAttr(texture_node + ".outAlpha", material + "bump2d.bumpValue", force=True)#bump2d연결
        cmds.connectAttr(material + "bump2d.outNormal", shader_node + ".normalCamera", force=True)#속성 설정

    elif renderPass == "Height":
        displacementNode = cmds.shadingNode("displacementShader", asTexture=True,
                                            name=(material + "_displacement_shader"))
        cmds.connectAttr(texture_node + ".outAlpha", material + ".displacement",
                         force=True)
        cmds.connectAttr(material + ".displacement", material + "SG.displacementShader",
                         force=True)
    else:
        pass
cmds.select(mesh_names)
cmds.displaySmoothness(divisionsU=3, divisionsV=3, pointsWire=16, pointsShaded=4, polygonObject=3)
cmds.sets('test_test', e=True, forceElement=shader_group)








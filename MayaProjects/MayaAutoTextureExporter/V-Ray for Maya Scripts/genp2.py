import maya.cmds as cmds
import os

basePath = '/home/rapa/Downloads/test/texture3'
files = cmds.getFileList(folder=basePath)
meshPath = '/home/rapa/Downloads/test/test.obj'

# OBJ 파일을 임포트합니다.
cmds.file(meshPath, i=True, ra=True, mergeNamespacesOnClash=True, options="mo=1", pr=True, importFrameRate=True,
          importTimeRange="override")

# 임포트된 메시의 이름을 가져옵니다. 여기서는 예시로 첫 번째 메시를 사용합니다.
mesh_names = cmds.ls(type='mesh')
transform_name = cmds.listRelatives(mesh_names[0], parent=True)[0]

# 재질 리스트와 렌더 패스 리스트를 초기화합니다.
materialList = []
renderPassList = []

# 파일들을 순회하면서 재질과 렌더 패스 리스트를 채웁니다.
for file in files:
    fileNameSplit = file.split(".")[0].split("_")
    material = fileNameSplit[0]
    renderPass = fileNameSplit[-1]
    if material not in materialList:
        materialList.append(material)
    if renderPass not in renderPassList:
        renderPassList.append(renderPass)

# 쉐이더와 쉐이더 그룹을 생성합니다.
shader_node = cmds.shadingNode('aiStandardSurface', asShader=True, name='myShader')
shader_group = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='myShaderSG')
cmds.connectAttr('{}.outColor'.format(shader_node), '{}.surfaceShader'.format(shader_group))

# 재질별로 텍스처를 설정합니다.
for material in materialList:
    for renderPass in renderPassList:
        for file in files:
            if material in file and renderPass in file:
                extension = file.split(".")[-1]
                texture_file = os.path.join(basePath, file)
                texture_node = cmds.shadingNode("file", asTexture=True, name=material + "_" + renderPass)
                cmds.setAttr(texture_node + ".fileTextureName", texture_file, type="string")

                # 여기서 필요한 place2dTexture 노드를 texture_node에 연결합니다.
                place2d_node = cmds.shadingNode('place2dTexture', asUtility=True)
                cmds.connectAttr(place2d_node + ".coverage", texture_node + ".coverage")
                cmds.connectAttr(place2d_node + ".translateFrame", texture_node + ".translateFrame")
                cmds.connectAttr(place2d_node + ".rotateFrame", texture_node + ".rotateFrame")
                cmds.connectAttr(place2d_node + ".mirrorU", texture_node + ".mirrorU")
                cmds.connectAttr(place2d_node + ".mirrorV", texture_node + ".mirrorV")
                cmds.connectAttr(place2d_node + ".stagger", texture_node + ".stagger")
                cmds.connectAttr(place2d_node + ".wrapU", texture_node + ".wrapU")
                cmds.connectAttr(place2d_node + ".wrapV", texture_node + ".wrapV")
                cmds.connectAttr(place2d_node + ".repeatUV", texture_node + ".repeatUV")
                cmds.connectAttr(place2d_node + ".offset", texture_node + ".offset")
                cmds.connectAttr(place2d_node + ".rotateUV", texture_node + ".rotateUV")
                cmds.connectAttr(place2d_node + ".noiseUV", texture_node + ".noiseUV")
                cmds.connectAttr(place2d_node + ".vertexUvOne", texture_node + ".vertexUvOne")
                cmds.connectAttr(place2d_node + ".vertexUvTwo", texture_node + ".vertexUvTwo")
                cmds.connectAttr(place2d_node + ".vertexUvThree", texture_node + ".vertexUvThree")
                cmds.connectAttr(place2d_node + ".vertexCameraOne", texture_node + ".vertexCameraOne")
                cmds.connectAttr(place2d_node + ".outUV", texture_node + ".uvCoord")
                cmds.connectAttr(place2d_node + ".outUvFilterSize", texture_node + ".uvFilterSize")

                # 텍스처 노드를 적절한 쉐이더 속성에 연결합니다.
                if renderPass == "BaseColor":
                    cmds.connectAttr(texture_node + ".outColor", shader_node + ".baseColor", force=True)
                elif renderPass == "Roughness":
                    cmds.connectAttr(texture_node + ".outAlpha", shader_node + ".specularRoughness", force=True)
                elif renderPass == "Metallic":
                    cmds.connectAttr(texture_node + ".outAlpha", shader_node + ".metalness", force=True)
                elif renderPass == "Normal":
                    normal_node = cmds.shadingNode("aiNormalMap", asTexture=True, name=material + "NormalMap")
                    cmds.connectAttr(texture_node + ".outColor", normal_node + ".input", force=True)
                    cmds.connectAttr(normal_node + ".outValue", shader_node + ".normalCamera", force=True)
                elif renderPass == "Height":
                    # 변위 셰이더 생성 및 연결
                    displacement_node = cmds.shadingNode("displacementShader", asShader=True,
                                                         name=material + "_displacementShader")
                    cmds.connectAttr(texture_node + ".outAlpha", displacement_node + ".displacement", force=True)
                    cmds.connectAttr(displacement_node + ".displacement", shader_group + ".displacementShader",
                                     force=True)

# 최종 쉐이더를 메시에 할당합니다.
cmds.select(transform_name)
cmds.hyperShade(assign=shader_node)

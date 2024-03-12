import maya.cmds as cmds
import pathlib
"""try:
    from arnold import *
    from prman import *
except ImportError:
    cmds.warning("Arnold or Renderman was not found")"""

class AutoTexture:
    def renderpath_Importer(self):
    # OBJ 파일을 import합니다.
        file_path = pathlib.Path('/home/rapa/Downloads/test/test.obj')
        assert file_path.exists() is True
        cmds.file(file_path.as_posix(), i=True,  # import true
                  ignoreVersion=True,
                  ra=True,  # 덮어쓰기 허용
                  mergeNamespacesOnClash=False,  # 네임스페이스 충돌해결 false
                  options="mo=1",  # 모든 개체 가져오기
                  pr=True,  # 상대 경로로 가져오기
                  importFrameRate=True,  # 프레임 속도 가져오기
                  importTimeRange="override"  # 시간 범위 무시하고 가져오기
                  )
        # cmds.select('_pCube1', replace=True)#클릭





    def linkBtn(self, *args):
        # Get Files within selected folder
        basePath = cmds.textField(self.txtFieldFolderLocation, query=True, text=True)
        files = cmds.getFileList(folder=basePath)

        # For each file in folder, get the object name and renderpass
        materialList = []
        renderPassList = []

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

        # Checks for the renderer selected
        #     for material in materialList:
                for renderPass in renderPassList:
                    if renderPass == "color": # setting correct settings and linking nodes up for colour
                        fileNode = cmds.shadingNode("file", asTexture=True, name=(material+"_"+renderPass))
                        cmds.setAttr(material+"_"+renderPass+".colorSpace", "sRGB", type = "string")
                        cmds.setAttr(material + "_" + renderPass + ".fileTextureName", basePath+"/"+material+"_shader_"+renderPass+"."+extension, type="string")
                        cmds.connectAttr(material+"_"+renderPass+".outColor", material+"_shader.baseColor", force = True)
                    elif renderPass == "roughness": # setting correct settings and linking nodes up for roughness
                        fileNode = cmds.shadingNode("file", asTexture=True, name=(material + "_" + renderPass))
                        cmds.setAttr(material + "_" + renderPass + ".colorSpace", "Raw", type="string")
                        cmds.setAttr(material + "_" + renderPass + ".fileTextureName", basePath+"/"+material+"_shader_"+renderPass+"."+extension, type="string")
                        cmds.setAttr(material + "_" + renderPass + ".alphaIsLuminance", True)
                        cmds.connectAttr(material + "_" + renderPass + ".outAlpha", material + "_shader.specularRoughness", force=True)
                    elif renderPass == "metalness": # setting correct settings and linking nodes up for metalness
                        fileNode = cmds.shadingNode("file", asTexture=True, name=(material + "_" + renderPass))
                        cmds.setAttr(material + "_" + renderPass + ".colorSpace", "Raw", type="string")
                        cmds.setAttr(material + "_" + renderPass + ".fileTextureName", basePath+"/"+material+"_shader_"+renderPass+"."+extension, type="string")
                        cmds.setAttr(material + "_" + renderPass + ".alphaIsLuminance", True)
                        cmds.connectAttr(material + "_" + renderPass + ".outAlpha", material + "_shader.metalness", force=True)
                    elif renderPass == "normal": # setting correct settings and linking nodes up for normal map
                        fileNode = cmds.shadingNode("file", asTexture=True, name=(material + "_" + renderPass))
                        cmds.setAttr(material + "_" + renderPass + ".colorSpace", "Raw", type="string")
                        cmds.setAttr(material + "_" + renderPass + ".fileTextureName", basePath + "/" + material + "_shader_" + renderPass + "." + extension, type="string")
                        bump2d = cmds.shadingNode("bump2d", asTexture=True, name=material + "_bump2d")
                        cmds.setAttr(material + "_bump2d.bumpInterp", 1)
                        cmds.connectAttr(material + "_" + renderPass + ".outAlpha", material + "_bump2d.bumpValue", force=True)
                        cmds.connectAttr(material + "_bump2d.outNormal", material + "_shader.normalCamera", force=True)
                    elif renderPass == "height": # setting correct settings and linking nodes up for height/displacement map
                        #TODO:
                        displacementNode = cmds.shadingNode("displacementShader", asTexture=True, name=(material + "_displacement_shader"))
                        fileNode = cmds.shadingNode("file", asTexture=True, name=(material + "_" + renderPass))
                        cmds.connectAttr(material + "_" + renderPass + ".outAlpha", material + "_displacement_shader.displacement", force=True)
                        cmds.connectAttr(material + "_displacement_shader.displacement", material + "_shaderSG.displacementShader", force=True)
                    else:
                        pass
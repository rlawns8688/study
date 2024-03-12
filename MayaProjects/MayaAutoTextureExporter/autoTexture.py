import pathlib
import maya.cmds as cmds
import maya.mel as mel
import maya.api.OpenMaya as openMaya
# openMaya.MFnMesh.getAssociatedUVSetInstances()


class FileImporter():
    # OBJ 파일을 import합니다.
    obj_file_path = pathlib.Path('/home/rapa/Downloads/test/test.obj')
    assert obj_file_path.exists() is True
    cmds.file(obj_file_path.as_posix(), i=True,  # import true
              ignoreVersion=True,
              ra=True,  # 덮어쓰기 허용
              mergeNamespacesOnClash=False,  # 네임스페이스 충돌해결 false
              options="mo=1",  # 모든 개체 가져오기
              pr=True,  # 상대 경로로 가져오기
              importFrameRate=True,  # 프레임 속도 가져오기
              importTimeRange="override"  # 시간 범위 무시하고 가져오기
              )
    # cmds.select('_pCube1', replace=True)#클릭


class MakeShader:
    def __init__(self):
        pass
    @staticmethod
    def create_texture_file_node(image_path: pathlib.Path) -> cmds.shadingNode: # 텍스쳐 만들기 : Base Color
        assert image_path.exists() is True
        file_node = cmds.shadingNode('file', at=True, icm=True) # filenode 생성
        cmds.setAttr(file_node + ".fileTextureName", image_path.as_posix(), type="string") # 안에 png넣기
        place2d_node = cmds.shadingNode('place2dTexture', asUtility=True)
        cmds.connectAttr(place2d_node + ".outUV", file_node + ".uvCoord")
        cmds.connectAttr(place2d_node + ".outUvFilterSize", file_node + ".uvFilterSize")
        return file_node

    @staticmethod
    def create_shaders() -> tuple:
        """
        # 쉐이더 만들기 : Arnold Shader
        :return:
        """
        new_shader = cmds.shadingNode('aiStandardSurface', asShader=True, name='myNewShader') # 셰이더 생성
        shader_grp = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='myNewShaderSG') # 셰이더 그룹 생성
        cmds.connectAttr('{}.outColor'.format(new_shader), '{}.surfaceShader'.format(shader_grp), force=True)# 두개 연결
        print("쉐이더 맞음", new_shader)
        return new_shader, shader_grp

    def node_shader_connetor(self): # 위에 두개 연결
        texture_data = {
            'baseColor': pathlib.Path('/home/rapa/Downloads/test/texture1/test_BaseColor.exr'),
            # 'metalness': pathlib.Path('/home/rapa/Downloads/test/texture1/test_Metallic.exr')

        }

        new_shader, shader_grp = MakeShader.create_shaders()

        for k, v in texture_data.items(): # k = texture종류, v = texture경로
            texture = MakeShader.create_texture_file_node(v) # 텍스쳐 노드
            # create shader
            cmds.select('test_test1', replace=True)
            cmds.connectAttr(texture + '.outColor', new_shader + f'.{k}') # 합체
            # 선택된 객체에 새로운 쉐이딩 그룹을 할당하고 쉐이더를 연결
        cmds.sets('test_test1', e=True, forceElement=shader_grp)

if __name__ == "__main__":
    c = MakeShader()
    # c.create_texture_file_node()
    # c.create_shaders()
    c.node_shader_connetor()


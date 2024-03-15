import maya.cmds as cmds
# from main import TextureAssign
import sys
sys.path.append('/home/rapa/myproject')
from assign_shader import ShaderManager

class Exporter:
    def __init__(self):
        pass
    def set_playblast(self, camera='persp'):
        """
        주어진 변환 노드에 카메라를 포커스

        :param transform_node: 카메라를 포커스할 변환 노드 이름
        :param camera: 사용할 카메라 이름
        """
        panels = cmds.getPanel(type='modelPanel')
        for panel in panels:
            cmds.modelEditor(panel, edit=True, displayTextures=True, wireframeOnShaded=False,
                             displayAppearance='smoothShaded')

        transformNode = [cmds.listRelatives(mesh, parent=True)[0]
                         for mesh in cmds.ls(type='mesh') if cmds.listRelatives(mesh, parent=True)]

        cmds.select(transformNode)  # 변환 노드 선택
        cmds.viewFit(camera, fitFactor=1)  # 카메라를 선택된 변환 노드에 포커스

        cmds.setKeyframe(attribute='rotateY', t=1, v=0)
        cmds.setKeyframe(attribute='rotateY', t=300, v=360)
        cmds.select(clear=True)  # 선택 해제

    def create_playblast_from_persp(self, start_frame, end_frame, output_file, width=960, height=540, format='qt',
                                    encoder='H.264'):
        """
        Parameters:
        start_frame (int): 시작 프레임 번호
        end_frame (int): 종료 프레임 번호
        output_file (str): 출력될 파일 경로와 이름
        width (int): 비디오의 너비
        height (int): 비디오의 높이
        format (str): 출력 파일 포맷 ('qt'는 QuickTime을 의미)
        encoder (str): 비디오 인코더
        """
        # 프레임 범위 설정
        cmds.playbackOptions(min=start_frame, max=end_frame)

        # playblast 생성
        cmds.playblast(startTime=start_frame, endTime=end_frame, format=format, filename=output_file,
                       forceOverwrite=True, sequenceTime=0, clearCache=True, viewer=False,
                       showOrnaments=False, offScreen=True, fp=4, percent=100, compression=encoder, quality=100,
                       widthHeight=[width, height])


if __name__ == '__main__':
    e = Exporter()
    obj_file_path = '/home/rapa/myproject/test/test.obj'
    textures_dir = '/home/rapa/myproject/test/texture4'
    # t = TextureAssign(obj_file_path, textures_dir)
    s = ShaderManager(textures_dir)
    output_path = '/home/rapa/myproject/test/test_mov3'

    # t.load_obj_and_assign_textures()
    s.assign_textures(obj_file_path)
    e.set_playblast()

    e.create_playblast_from_persp(1, 400, output_path)

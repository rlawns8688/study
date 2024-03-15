import maya.cmds as cmds
import os

class ShaderManager:
    def __init__(self, textures_dir):
        self.textures_dir = textures_dir

    def create_shader(self, material_name):
        shader_node = cmds.shadingNode('aiStandardSurface', asShader=True, name=f'{material_name}_shader')
        shading_group = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=f'{material_name}_SG')
        cmds.connectAttr(f'{shader_node}.outColor', f'{shading_group}.surfaceShader', force=True)
        return shader_node, shading_group

    def create_texture_node(self, texture_path, material_name, render_pass):
        texture_node = cmds.shadingNode('file', asTexture=True, isColorManaged=True, name=f'{material_name}_{render_pass}')
        cmds.setAttr(f'{texture_node}.fileTextureName', texture_path, type='string')
        return texture_node

    def assign_textures(self, obj_file_path):
        imported_nodes = cmds.file(obj_file_path, i=True, returnNewNodes=True, type="OBJ", options="mo=1", ignoreVersion=True, ra=True, mergeNamespacesOnClash=False, namespace=":")
        transform_nodes = [cmds.listRelatives(node, parent=True)[0] for node in imported_nodes if cmds.nodeType(node) == 'mesh']

        shader_node, shading_group = self.create_shader("sharedMaterial")
        texture_files = [f for f in os.listdir(self.textures_dir) if f.lower().endswith('.exr')]

        for texture_file in texture_files:
            file_full_path = os.path.join(self.textures_dir, texture_file)
            material_name, render_pass = texture_file.rsplit('.', 1)[0].rsplit('_', 1)
            file_node = self.create_texture_node(file_full_path, material_name, render_pass)
            self.connect_texture_to_shader(render_pass, file_node, shader_node, shading_group)


        for transform_node in transform_nodes:
            cmds.select(transform_node)
            cmds.displaySmoothness(transform_node, divisionsU=3, divisionsV=3, pointsWire=16, pointsShaded=4,
                                   polygonObject=3)
            cmds.hyperShade(assign=shader_node)


    def connect_texture_to_shader(self, render_pass, texture_node, shader_node, shading_group):
        if render_pass == "BaseColor":
            cmds.connectAttr(f'{texture_node}.outColor', f'{shader_node}.baseColor', force=True)
        elif render_pass == "Roughness":
            cmds.connectAttr(f'{texture_node}.outAlpha', f'{shader_node}.specularRoughness', force=True)
        elif render_pass == "Metalness":
            cmds.connectAttr(f'{texture_node}.outAlpha', f'{shader_node}.metalness', force=True)
        elif render_pass == "Normal":
            normal_node = cmds.shadingNode("aiNormalMap", asTexture=True, name=f'{texture_node}_normalMap')
            cmds.connectAttr(f'{texture_node}.outColor', f'{normal_node}.input', force=True)
            cmds.connectAttr(f'{normal_node}.outValue', f'{shader_node}.normalCamera', force=True)


if __name__ == '__main__':
    obj_file_path = '/home/rapa/Downloads/test/test.obj'
    textures_dir = '/home/rapa/myproject/test/texture1'
    shader_manager = ShaderManager(textures_dir)
    shader_manager.assign_textures(obj_file_path)

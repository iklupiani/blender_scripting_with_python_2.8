import bpy

bpy.ops.object.mode_set(mode = 'OBJECT')
bpy.ops.object.select_all(action = 'DESELECT')

cube = bpy.context.scene.objects['Cube']
bpy.context.view_layer.objects.active = cube
cube.select_set(True)
bpy.ops.object.mode_set(mode = 'EDIT')
bpy.ops.mesh.select_all(action = 'SELECT')
bpy.context.view_layer.update()

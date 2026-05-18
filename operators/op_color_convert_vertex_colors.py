import bpy

from ..utilities import utilities_color
from ..utilities import utilities_bake


gamma = 2.2



class op(bpy.types.Operator):
	bl_idname = "uv.textools_color_convert_to_vertex_colors"
	bl_label = "Pack Texture"
	bl_description = "Pack ID Colors into single texture and UVs"
	bl_options = {'REGISTER', 'UNDO'}
	
	@classmethod
	def poll(cls, context):
		if bpy.context.area.ui_type != 'UV':
			return False
		if not bpy.context.active_object:
			return False
		if bpy.context.active_object not in bpy.context.selected_objects:
			return False
		if len(bpy.context.selected_objects) != 1:
			return False
		if bpy.context.active_object.type != 'MESH':
			return False
		return True


	def execute(self, context):
		convert_vertex_colors(self, context)
		return {'FINISHED'}



def convert_vertex_colors(self, context):
	obj = bpy.context.active_object
	bpy.ops.object.mode_set(mode='OBJECT')
	layer = utilities_bake.assign_vertex_color(obj)
	if not layer:
		self.report({'ERROR_INVALID_INPUT'}, "Object does not support color attributes")
		return {'CANCELLED'}

	for i in range(len(obj.material_slots)):
		slot = obj.material_slots[i]
		if slot.material:
			color = utilities_color.get_color(i).copy()
			# Fix Gamma
			color[0] = pow(color[0],1/gamma)
			color[1] = pow(color[1],1/gamma)
			color[2] = pow(color[2],1/gamma)

			for polygon in obj.data.polygons:
				if polygon.material_index == i:
					utilities_color.set_polygon_color(layer, polygon, color)

	obj.data.update()

	# Switch Properties Tab
	for area in bpy.context.screen.areas:
		if area.type == 'PROPERTIES':
			for space in area.spaces:
				if space.type == 'PROPERTIES':
					space.context = 'DATA'

	# Switch textured shading
	for area in bpy.context.screen.areas:
		if area.type == 'VIEW_3D':
			for space in area.spaces:
				if space.type == 'VIEW_3D':
					space.shading.type = 'SOLID'

	# Clear materials?
	#bpy.ops.uv.textools_color_clear()

	bpy.ops.ui.textools_popup('INVOKE_DEFAULT', message="Vertex colors assigned")

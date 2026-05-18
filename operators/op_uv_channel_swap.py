import bpy

from ..utilities import utilities_uv



class op(bpy.types.Operator):
	bl_idname = "uv.textools_uv_channel_swap"
	bl_label = "Move UV Channel"
	bl_description = "Move active UV channel up or down in all the selected Objects"
	bl_options = {'REGISTER', 'UNDO'}

	is_down : bpy.props.BoolProperty(default=False, options={'HIDDEN'})

	@classmethod
	def poll(cls, context):
		if bpy.context.active_object == None:
			return False
		if bpy.context.active_object.type != 'MESH':
			return False
		return True


	def execute(self, context):
		premode = bpy.context.active_object.mode
		utilities_uv.multi_object_loop(swapuvs, self, context)
		bpy.ops.object.mode_set(mode=premode)
		return {'FINISHED'}


def swapuvs(self, context):
	uv_layers = bpy.context.object.data.uv_layers
	count = len(uv_layers)

	if count < 2:
		return {'FINISHED'}

	if uv_layers.active_index == 0 and not self.is_down:
		return {'FINISHED'}
	elif uv_layers.active_index == count-1 and self.is_down:
		return {'FINISHED'}

	index_A = uv_layers.active_index
	index_B = index_A + (1 if self.is_down else -1)
	if not hasattr(uv_layers, "move"):
		self.report({'ERROR'}, "UV channel reordering is not available in this Blender version")
		return {'CANCELLED'}

	uv_layers.move(index_A, index_B)
	uv_layers.active_index = index_B
	bpy.context.scene.texToolsSettings.uv_channel = str(index_B)
	return {'FINISHED'}

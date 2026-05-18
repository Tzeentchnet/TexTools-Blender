import bpy

from ..utilities import utilities_color
from ..settings import tt_settings, prefs


gamma = 2.2


class op(bpy.types.Operator):
	bl_idname = "uv.textools_color_assign"
	bl_label = "Assign Color"
	bl_description = "Assign color to selected Objects or faces in Edit Mode"
	bl_options = {'UNDO'}

	index: bpy.props.IntProperty(description="Color Index", default=0)

	@classmethod
	def poll(cls, context):
		if bpy.context.area.ui_type != 'UV':
			return False
		if not bpy.context.active_object:
			return False
		if bpy.context.active_object not in bpy.context.selected_objects:
			return False
		if bpy.context.active_object.type != 'MESH':
			return False
		return True

	def execute(self, context):
		assign_color(self, context, self.index)
		return {'FINISHED'}


def assign_color(self, context, index):
	selected_obj = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']

	previous_mode = 'OBJECT'
	previous_active = bpy.context.view_layer.objects.active
	if previous_active:
		previous_mode = previous_active.mode

	for obj in selected_obj:
		# Select object
		bpy.ops.object.mode_set(mode='OBJECT')
		bpy.ops.object.select_all(action='DESELECT')
		obj.select_set(True)
		bpy.context.view_layer.objects.active = obj

		# Enter Edit mode
		bpy.ops.object.mode_set(mode='EDIT')

		if previous_mode == 'OBJECT':
			bpy.ops.mesh.select_all(action='SELECT')
		
		if tt_settings().color_assign_mode == 'MATERIALS':
			# Verify material slots
			for _ in range(index+1):
				if index >= len(obj.material_slots):
					bpy.ops.object.material_slot_add()

			utilities_color.assign_slot(obj, index)

			# Assign to selection
			obj.active_material_index = index
			bpy.ops.object.material_slot_assign()

		else:  # mode == VERTEXCOLORS
			color = utilities_color.get_color(index).copy()
			if prefs().bool_color_id_vertex_color_gamma:
				# Fix Gamma
				color[0] = pow(color[0], 1/gamma)
				color[1] = pow(color[1], 1/gamma)
				color[2] = pow(color[2], 1/gamma)

			bpy.ops.object.mode_set(mode='OBJECT')
			layer = utilities_color.ensure_color_layer(obj.data, 'TexTools_colorID')
			if not layer:
				self.report({'ERROR_INVALID_INPUT'}, "Object does not support color attributes")
				return {'CANCELLED'}

			for polygon in obj.data.polygons:
				if polygon.select and not polygon.hide:
					utilities_color.set_polygon_color(layer, polygon, color)
			obj.data.update()

	# restore mode
	bpy.ops.object.mode_set(mode='OBJECT')
	bpy.ops.object.select_all(action='DESELECT')
	for obj in selected_obj:
		obj.select_set(True)
	if previous_active:
		bpy.context.view_layer.objects.active = previous_active
	bpy.ops.object.mode_set(mode=previous_mode)

	# Show Material or Data Tab
	utilities_color.update_properties_tab()

	# Change View mode
	utilities_color.update_view_mode()

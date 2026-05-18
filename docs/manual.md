# TexTools Manual

This manual documents the active TexTools operators registered by the Blender extension. Operator IDs are included for search, keymaps, and scripting. Source links point back to the local implementation files.

Most UV layout tools expect a mesh object in Edit Mode with UVs and are intended for use from Blender's UV editor. Texture, bake, Color ID, and support tools note different expectations where they matter.

## UV Channel And Size Tools

| Tool | Operator | Source | What it does |
| --- | --- | --- | --- |
| Add UV Channel | `uv.textools_uv_channel_add` | [op_uv_channel_add.py](../operators/op_uv_channel_add.py) | Adds a new UV channel to all selected mesh objects. |
| Remove UV Channel | `uv.textools_uv_channel_remove` | [op_uv_channel_remove.py](../operators/op_uv_channel_remove.py) | Removes the active UV channel from all selected mesh objects. |
| Move UV Channel | `uv.textools_uv_channel_swap` | [op_uv_channel_swap.py](../operators/op_uv_channel_swap.py) | Moves the active UV channel up or down for all selected mesh objects. The hidden `is_down` option selects the direction. |
| Get Size | `uv.textools_uv_size_get` | [op_uv_size_get.py](../operators/op_uv_size_get.py) | Reads the selected object's texture size into the TexTools size settings. |
| Resize Area | `uv.textools_uv_resize` | [op_uv_resize.py](../operators/op_uv_resize.py) | Resizes the UV work area and active UV editor image. Options include width, height, preset size dropdowns, and anchor direction (`TL`, `TR`, `BL`, `BR`). |

### Blender 5 Native Overlap

- Similar: Add, Remove, and Move UV Channel overlap with Blender's UV Maps controls in Object Data Properties; TexTools applies the action across selected mesh objects and syncs its channel setting.
- Similar: Get Size and Resize Area overlap with Blender's image size and UV editor image controls; TexTools links the size to its texture and texel-density workflow.

## UV Layout Tools

| Tool | Operator | Source | What it does |
| --- | --- | --- | --- |
| Align | `uv.textools_align` | [op_align.py](../operators/op_align.py) | Aligns selected UV vertices, edges, or islands to a chosen side, corner, center, horizontal centerline, or vertical centerline. The hidden `direction` option is set by the UI buttons. |
| Crop | `uv.textools_uv_crop` | [op_uv_crop.py](../operators/op_uv_crop.py) | Frames selected UVs into the 0-1 UV area. |
| Fill | `uv.textools_uv_fill` | [op_uv_fill.py](../operators/op_uv_fill.py) | Scales selected UVs to fill the 0-1 UV area. The `align` option can rotate the selection to a tighter orientation before filling. |
| Rectify | `uv.textools_rectify` | [op_rectify.py](../operators/op_rectify.py) | Aligns selected UV faces or vertices into a rectangular distribution. |
| Relax | `uv.textools_relax` | [op_relax.py](../operators/op_relax.py) | Smooths selected UVs. Options include `iterations` and `area_preservation` to control smoothing strength and shrink compensation. |
| Randomize | `uv.textools_randomize` | [op_randomize.py](../operators/op_randomize.py) | Randomizes selected UV islands or faces. Options control per-face mode, rounding, step size, position strength, rotation range and steps, scale range, bounds handling, and seed. |
| Centralize | `uv.textools_island_centralize` | [op_island_centralize.py](../operators/op_island_centralize.py) | Moves selected faces as close as possible to the 0-1 UV area without changing the textured object. |
| Unwrap | `uv.textools_uv_unwrap` | [op_uv_unwrap.py](../operators/op_uv_unwrap.py) | Unwraps selected UVs while preserving pinned or unselected regions. The hidden `axis` option supports constrained U or V unwrap buttons. |
| Stitch | `uv.textools_stitch` | [op_stitch.py](../operators/op_stitch.py) | Stitches neighboring UV islands to the current selection. |
| Straight Edges Chain | `uv.textools_island_straighten_edge_loops` | [op_island_straighten_edge_loops.py](../operators/op_island_straighten_edge_loops.py) | Straightens a selected edge chain and relaxes the rest of the UV island. |
| Split Bevel | `uv.textools_edge_split_bevel` | [op_edge_split_bevel.py](../operators/op_edge_split_bevel.py) | Splits UVs along selected hard edges and offsets them to create bevel spacing. The `radius` option controls the spacing amount. |

### Blender 5 Native Overlap

- Similar: Align overlaps with `bpy.ops.uv.align`; TexTools adds preset directions and multi-object workflow handling.
- Similar: Crop, Fill, and Centralize overlap with `bpy.ops.uv.pack_islands` plus transform scaling; TexTools adds fixed 0-1 framing, UDIM-aware placement, and fit presets.
- Similar: Relax overlaps with Blender's UV relax and `bpy.ops.uv.minimize_stretch` style workflows; TexTools exposes iterative smoothing and area preservation in one operator.
- Similar: Unwrap overlaps with `bpy.ops.uv.unwrap`; TexTools preserves pinned or unselected regions and supports constrained U or V unwrap actions.
- Same or similar: Stitch wraps `bpy.ops.uv.stitch`; TexTools prepares island outline selections and restores the moved selection.
- Partial: Rectify, Randomize, Straight Edges Chain, and Split Bevel use custom UV geometry logic that has no single matching Blender 5 base operator.

## Island Alignment Tools

| Tool | Operator | Source | What it does |
| --- | --- | --- | --- |
| Align Island by Edge | `uv.textools_island_align_edge` | [op_island_align_edge.py](../operators/op_island_align_edge.py) | Aligns UV islands based on a selected edge. |
| Align World | `uv.textools_island_align_world` | [op_island_align_world.py](../operators/op_island_align_world.py) | Aligns selected UV islands or faces to world direction. Options include per-face processing and axis selection (`Auto`, `X`, `Y`, `Z`). |
| Align And Sort | `uv.textools_island_align_sort` | [op_island_align_sort.py](../operators/op_island_align_sort.py) | Rotates UV islands to minimal bounds and sorts them horizontally or vertically. Options control vertical layout, orientation alignment, and padding. |
| Rotate 90 Degrees | `uv.textools_island_rotate_90` | [op_island_rotate_90.py](../operators/op_island_rotate_90.py) | Rotates the UV selection 90 degrees clockwise or counterclockwise around the global pivot. The hidden `angle` option is set by the UI buttons. |
| Symmetry | `uv.textools_island_mirror` | [op_island_mirror.py](../operators/op_island_mirror.py) | Mirrors selected UV faces around the global pivot. The hidden `is_vertical` option selects horizontal or vertical mirroring. |

### Blender 5 Native Overlap

- Similar: Align World and Align And Sort overlap with Blender UV alignment, rotation, and `bpy.ops.uv.pack_islands` workflows; TexTools combines orientation detection, sorting, and padding presets.
- Similar: Rotate 90 Degrees wraps `bpy.ops.transform.rotate` with fixed UV rotation steps.
- Similar: Symmetry wraps `bpy.ops.transform.mirror` with horizontal and vertical UV presets.
- Partial: Align Island by Edge uses custom selected-edge angle detection before rotating islands, so it only partially overlaps Blender transform tools.

## Island Selection Tools

| Tool | Operator | Source | What it does |
| --- | --- | --- | --- |
| Select Similar | `uv.textools_select_islands_identical` | [op_select_islands_identical.py](../operators/op_select_islands_identical.py) | Selects UV islands with topology similar to the current UV selection. |
| Select Overlap | `uv.textools_select_islands_overlap` | [op_select_islands_overlap.py](../operators/op_select_islands_overlap.py) | Selects overlapping UV islands while leaving one island from each overlap group unselected. |
| Select Island Outline | `uv.textools_select_islands_outline` | [op_select_islands_outline.py](../operators/op_select_islands_outline.py) | Reduces the current UV selection to island boundary edges. |
| Select Flipped | `uv.textools_select_islands_flipped` | [op_select_islands_flipped.py](../operators/op_select_islands_flipped.py) | Detects and selects flipped UV faces across all polygons of the selected objects, including hidden polygons. |
| Select Degenerate | `uv.textools_select_zero` | [op_select_zero.py](../operators/op_select_zero.py) | Detects zero-area UV triangles across selected objects, including hidden polygons. The `precision` option controls the zero-area threshold. |

### Blender 5 Native Overlap

- Similar: Select Overlap wraps `bpy.ops.uv.select_overlap`; TexTools keeps it available in the TexTools island-selection group.
- Similar: Select Island Outline overlaps with `bpy.ops.uv.seams_from_islands`; TexTools turns island boundaries into the active selection and restores prior seams.
- Partial: Select Similar, Select Flipped, and Select Degenerate use custom topology, orientation, and zero-area tests that do not have a single matching Blender 5 UV operator.

## Texel Density And Checker Tools

| Tool | Operator | Source | What it does |
| --- | --- | --- | --- |
| Get Texel Size | `uv.textools_texel_density_get` | [op_texel_density_get.py](../operators/op_texel_density_get.py) | Measures the pixel-per-unit ratio or texel density from the current selection. |
| Set Texel Size | `uv.textools_texel_density_set` | [op_texel_density_set.py](../operators/op_texel_density_set.py) | Scales selected UVs to match the current texel density setting. |
| Checker Map | `uv.textools_texel_checker_map` | [op_texel_checker_map.py](../operators/op_texel_checker_map.py) | Applies checker map material overrides to selected objects and cycles between checker maps and original materials. |
| Checker Map Cleanup | `uv.textools_texel_checker_map_cleanup` | [op_texel_checker_map_cleanup.py](../operators/op_texel_checker_map_cleanup.py) | Removes and unlinks checker map data from selected objects. The `bool_all` option applies cleanup to all objects in the blend file. |

### Blender 5 Native Overlap

- Partial: Get Texel Size and Set Texel Size overlap with manual UV scaling and image-size workflows; Blender 5 does not provide a matching texel-density operator.
- Similar: Checker Map overlaps with applying a material or Geometry Nodes modifier for viewport texture checking; TexTools supplies cycling checker presets and cleanup.

## Texture Management Tools

| Tool | Operator | Source | What it does |
| --- | --- | --- | --- |
| Reload Textures | `uv.textools_texture_reload_all` | [op_texture_reload_all.py](../operators/op_texture_reload_all.py) | Reloads file textures and removes unused image and material data. |
| Preview Texture | `uv.textools_texture_preview` | [op_texture_preview.py](../operators/op_texture_preview.py) | Applies the UV editor background image as a temporary material override on the appropriate selected object. |
| Texture Preview Cleanup | `uv.textools_texture_preview_cleanup` | [op_texture_preview_cleanup.py](../operators/op_texture_preview_cleanup.py) | Removes and unlinks texture preview data from selected objects. The `bool_all` option applies cleanup to all objects in the blend file. |
| Open Texture | `uv.textools_texture_open` | [op_texture_open.py](../operators/op_texture_open.py) | Opens the named Blender image file path in the operating system. |
| Save Texture | `uv.textools_texture_save` | [op_texture_save.py](../operators/op_texture_save.py) | Opens a file browser to save a texture path. It stores the image name, output filepath, and file-browser filters. |
| Select Texture | `uv.textools_texture_select` | [op_texture_select.py](../operators/op_texture_select.py) | Selects a named image, tries to infer the matching bake mode from the image name, and assigns the image to UV editor views. |
| Remove Texture | `uv.textools_texture_remove` | [op_texture_remove.py](../operators/op_texture_remove.py) | Removes the named Blender image datablock and unlinks it from users. |

### Blender 5 Native Overlap

- Similar: Reload Textures overlaps with `bpy.ops.image.reload`; TexTools reloads all file images and also removes unused image and material data.
- Similar: Open Texture and Save Texture overlap with Blender image open/save workflows such as `bpy.ops.image.open` and `bpy.ops.image.save_as`; TexTools targets the selected TexTools image path.
- Partial: Preview Texture, Select Texture, Remove Texture, and Texture Preview Cleanup combine image datablock management with TexTools bake-set and material-preview state.

## Baking Tools

| Tool | Operator | Source | What it does |
| --- | --- | --- | --- |
| Bake | `uv.textools_bake` | [op_bake.py](../operators/op_bake.py) | Bakes selected objects using the active TexTools bake mode, scene bake settings, selected bake sets, and generated output images. |
| Match Names | `uv.textools_bake_organize_names` | [op_bake_organize_names.py](../operators/op_bake_organize_names.py) | Matches high-poly object names to low-poly objects using bounding boxes. |
| Explode | `uv.textools_bake_explode` | [op_bake_explode.py](../operators/op_bake_explode.py) | Explodes selected bake pairs with animation keyframes so baked projection pairs can be separated in space. |

### Blender 5 Native Overlap

- Partial: Bake extends `bpy.ops.object.bake` with bake sets, generated target images, material relinking, Color ID and vertex-color sources, UDIM handling, and composite post-processing.
- None: Match Names and Explode are TexTools bake-set workflow operators with no direct Blender 5 base operator.

### Bake Modes

The Bake operator uses the active bake mode selected in the TexTools UI. Modes are not separate Blender operators, but they materially change what `uv.textools_bake` produces.

- Normal and surface detail: `normal_tangent_bevel`, `normal_object_bevel`, `normal_object`, `normal_tangent`, `curvature`, `bevel_mask`, `wireframe`, `thickness`, `cavity`.
- Selection and ID sources: `selection`, `dust`, `id_element`, `id_material`, `position`, `paint_base`.
- Material channels: `base_color`, `sss_color`, `specular_tint`, `specular`, `sss_strength`, `metallic`, `anisotropic`, `anisotropic_rotation`, `sheen`, `sheen_tint`, `clearcoat`, `clearcoat_roughness`, `transmission_roughness`.
- Blender bake outputs: `ao`, `shadow`, `combined`, `glossiness`, `roughness`, `diffuse`, `environment`, `transmission`, `uv`, `emission`.
- Version-dependent outputs: `emission_strength` and `alpha` are added for supported Blender versions.

## Color ID Tools

| Tool | Operator | Source | What it does |
| --- | --- | --- | --- |
| Assign Color | `uv.textools_color_assign` | [op_color_assign.py](../operators/op_color_assign.py) | Assigns the selected Color ID swatch to selected objects or selected faces in Edit Mode. The `index` option selects the swatch. |
| Clear Colors | `uv.textools_color_clear` | [op_color_clear.py](../operators/op_color_clear.py) | Clears Color ID materials or vertex colors on the active object. |
| Select by Color | `uv.textools_color_select` | [op_color_select.py](../operators/op_color_select.py) | Selects faces that match the selected material Color ID swatch. The `index` option selects the swatch. |
| Select by Vertex Color | `uv.textools_color_select_vertex` | [op_color_select_vertex.py](../operators/op_color_select_vertex.py) | Selects faces that match the selected vertex color swatch. The `index` option selects the swatch. |
| Color Elements | `uv.textools_color_from_elements` | [op_color_from_elements.py](../operators/op_color_from_elements.py) | Assigns a Color ID to each mesh element. |
| Color Materials | `uv.textools_color_from_materials` | [op_color_from_materials.py](../operators/op_color_from_materials.py) | Assigns Color IDs based on mesh material slots. |
| Color Directions | `uv.textools_color_from_directions` | [op_color_from_directions.py](../operators/op_color_from_directions.py) | Assigns Color IDs by face direction. The `directions` option groups faces into 2, 3, 4, or 6 direction buckets. |
| Texture Atlas | `uv.textools_color_convert_to_texture` | [op_color_convert_texture.py](../operators/op_color_convert_texture.py) | Packs Color ID materials into a single texture and matching UV layout. |
| Vertex Colors | `uv.textools_color_convert_to_vertex_colors` | [op_color_convert_vertex_colors.py](../operators/op_color_convert_vertex_colors.py) | Converts Color ID material assignments into a color attribute or vertex color layer. |
| Export Colors | `uv.textools_color_io_export` | [op_color_io_export.py](../operators/op_color_io_export.py) | Exports the current Color ID palette to the clipboard. |
| Import Colors | `uv.textools_color_io_import` | [op_color_io_import.py](../operators/op_color_io_import.py) | Imports hex colors from the clipboard into the current Color ID palette. |

### Blender 5 Native Overlap

- Similar: Assign Color and Select by Color overlap with `bpy.ops.object.material_slot_assign` and material-index selection workflows; TexTools manages Color ID swatches and material slots.
- Partial: Select by Vertex Color and Vertex Colors overlap with Blender color attributes; TexTools adds color averaging, threshold matching, and material-to-color conversion.
- Partial: Texture Atlas overlaps with `bpy.ops.uv.unwrap` and image/material creation; TexTools packs the Color ID palette into a generated atlas workflow.
- None: Clear Colors, Color Elements, Color Materials, Color Directions, Export Colors, and Import Colors are TexTools Color ID palette and assignment workflows without a single matching Blender 5 base operator.

## Mesh Texture Tools

| Tool | Operator | Source | What it does |
| --- | --- | --- | --- |
| UV Mesh | `uv.textools_meshtex_create` | [op_meshtex_create.py](../operators/op_meshtex_create.py) | Creates a new mesh from the selected UVs of the active object. |
| Create Pattern | `uv.textools_meshtex_pattern` | [op_meshtex_pattern.py](../operators/op_meshtex_pattern.py) | Creates mesh patterns such as hexagons, triangles, diamonds, rectangles, stripes, and bricks. Options include mode, repetition size, and scale. |
| Trim | `uv.textools_meshtex_trim` | [op_meshtex_trim.py](../operators/op_meshtex_trim.py) | Trims a mesh texture workflow selection. |
| Collapse | `uv.textools_meshtex_trimcollapse` | [op_meshtex_trim_collapse.py](../operators/op_meshtex_trim_collapse.py) | Collapses trim mesh texture geometry. |
| Wrap Mesh Texture | `uv.textools_meshtex_wrap` | [op_meshtex_wrap.py](../operators/op_meshtex_wrap.py) | Converts UV coordinates into XYZ mesh coordinates for mesh texture workflows. |

### Blender 5 Native Overlap

- Similar: Create Pattern uses Blender mesh primitive operators such as `bpy.ops.mesh.primitive_circle_add` and `bpy.ops.mesh.primitive_plane_add`, then adds modifier presets for repeatable texture patterns.
- Similar: Trim and Collapse overlap with Boolean modifier and `bpy.ops.object.convert` workflows; TexTools packages them for mesh texture trimming.
- Similar: Wrap Mesh Texture uses `bpy.ops.object.surfacedeform_bind`; TexTools sets up the UV mesh target and wrap workflow.
- Partial: UV Mesh converts selected UV coordinates into mesh geometry, which has no single matching Blender 5 base operator.

## Unwrap And Mesh Cleanup Tools

| Tool | Operator | Source | What it does |
| --- | --- | --- | --- |
| Edge Peel | `uv.textools_unwrap_edge_peel` | [op_unwrap_edge_peel.py](../operators/op_unwrap_edge_peel.py) | Unwraps a pipe-like selection along edges selected in 3D space. |
| Iron Faces | `uv.textools_unwrap_faces_iron` | [op_unwrap_faces_iron.py](../operators/op_unwrap_faces_iron.py) | Unwraps selected faces into a single UV island. |
| Sharp Edges from Islands | `uv.textools_smoothing_uv_islands` | [op_smoothing_uv_islands.py](../operators/op_smoothing_uv_islands.py) | Applies smooth normals and sharp edges to mesh borders defined by UV islands. The `soft_self_border` option avoids sharpening borders where an island borders itself. |

### Blender 5 Native Overlap

- Similar: Edge Peel and Iron Faces build on `bpy.ops.uv.unwrap`; TexTools adds seam preparation, island cleanup, and rectification for specific unwrap workflows.
- Similar: Sharp Edges from Islands overlaps with `bpy.ops.uv.seams_from_islands` and `bpy.ops.mesh.faces_shade_smooth`; TexTools automates sharp-edge setup from UV island borders.

## Support And Internal Operators

These operators are registered by the extension but are primarily used by TexTools UI helpers or debugging paths.

| Tool | Operator | Source | What it does |
| --- | --- | --- | --- |
| Debug | `uv.op_debug` | [__init__.py](../__init__.py) | Enables Blender debug display for mesh vertex indices and opens debug behavior used by the TexTools panel when Blender debug mode is active. |
| Select Bake Set | `uv.op_select_bake_set` | [__init__.py](../__init__.py) | Selects the low, high, cage, and related objects that belong to a named bake set. |
| Select Bake Type | `uv.op_select_bake_type` | [__init__.py](../__init__.py) | Selects bake objects by role, such as low, high, cage, float, or issue objects. |
| Message Popup | `ui.textools_popup` | [utilities_ui.py](../utilities/utilities_ui.py) | Shows a small popup message and reports that message to Blender's info log. |

## Inactive Or Commented Operators

The following code exists only as inactive or commented-out implementation and is not registered as active operator behavior.

- `uv.textools_enable_cycles` in [__init__.py](../__init__.py) is inside a quoted block.
- `uv.textools_ui_image_save` in [op_texture_save.py](../operators/op_texture_save.py) is inside a quoted block.
- A duplicate `uv.textools_texture_save` class in [op_texture_save.py](../operators/op_texture_save.py) is commented out.
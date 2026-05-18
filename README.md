# TexTools for Blender #

TexTools is a free Blender extension with a set of professional UV and texture tools for Blender 5 and later, including UV layout tools (Align, Rectify, Sort, Randomize), texture baking modes, texel density tools, smart UV selection operators, Color ID tools, and UV-related mesh creation utilities.

TexTools builds on the classic toolset first created for 3ds Max and later brought to Blender. This version continues that classic workflow as a Blender 5 extension with an updated package layout and compatibility fixes.

## Installation ##

1. Build or download the TexTools extension zip for this project.
2. In Blender 5, open **Edit > Preferences > Extensions**.
3. Remove any older TexTools installation before installing this extension.
4. Use **Install from Disk** and select the TexTools extension zip.
5. Enable TexTools after installation.
6. The TexTools panel is available from Blender's UV editor sidebar.

## Documentation ##

See the local [TexTools Manual](docs/manual.md) for operator descriptions and workflow notes.

## Extension Layout ##

This repository root is the Blender extension root. The extension manifest and registration entry point stay at the top level as `blender_manifest.toml` and `__init__.py`.

- `operators/` contains TexTools operator modules.
- `utilities/` contains shared utility modules and path helpers.
- `assets/` contains icons, thumbnails, and bundled `.blend` resources.
- `vendor/` contains bundled Python dependencies used by the extension.

When Blender 5 is available on PATH, validate the extension from this directory with `blender --command extension validate .`.

## Credits ##

- @renderjs for the classic TexTools foundation.
- @SavMartin for reviving the Blender version for Blender 2.8.
- unclepomedev for Blender compatibility work used as a reference during the Blender 5 update.

import os

PACKAGE_ROOT = os.path.dirname(os.path.dirname(__file__))
ASSETS_ROOT = os.path.join(PACKAGE_ROOT, "assets")
ICONS_ROOT = os.path.join(ASSETS_ROOT, "icons")
ICONS_BIP_ROOT = os.path.join(ASSETS_ROOT, "icons_bip")
RESOURCES_ROOT = os.path.join(ASSETS_ROOT, "resources")
BAKE_MODE_PREVIEWS_ROOT = os.path.join(RESOURCES_ROOT, "bake_modes_bip")


def resource_path(*parts):
	return os.path.join(RESOURCES_ROOT, *parts)

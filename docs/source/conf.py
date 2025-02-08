import os
import sys
sys.path.insert(0, os.path.abspath('../..'))  # Adjust path to match project structure


# Project information
project = "Beanim"
copyright = "2025, Pano"
author = "Pano"

# General configuration
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]

autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show_signature": False,
    "exclude-members": "__init__",
}


# Exclude module contents at the end of each page
toc_object_entries_show_parents = "hide"
add_module_names = False
autodoc_member_order = "bysource"
autodoc_class_signature = "separated"

# HTML output configuration
html_theme = "furo"
html_static_path = ["_static"]


def skip_specific_method(app, what, name, obj, skip, options):
    if name == "animation_overrides":
        return True
    return skip


def setup(app):
    app.connect("autodoc-skip-member", skip_specific_method)

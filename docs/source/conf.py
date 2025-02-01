import os
import sys

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath('../../src'))

# Project information
project = 'Beanim'
copyright = '2025, Pano'
author = 'Pano'

# General configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

# Autodoc configuration
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': False,
    'no-module-index': True,
}


# Remove module names from displayed names
add_module_names = False

# Exclude module contents at the end of each page
autodoc_member_order = 'bysource'

# HTML output configuration
html_theme = 'furo'
html_static_path = ['_static']

def skip_init(app, what, name, obj, skip, options):
    if name == "__init__":
        return True
    return skip

def setup(app):
    app.connect("autodoc-skip-member", skip_init)




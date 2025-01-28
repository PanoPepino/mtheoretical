# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys


sys.path.insert(0, os.path.abspath("../mtheoretical"))

project = 'mtheoretical'
copyright = '2025, Pano'
author = 'Pano'
release = '2.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon'
]
add_module_names = False
add_submodule_names = False
add_package_names = False
toc_object_entries = False
python_use_unqualified_type_names = False

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_theme = 'furo'
html_static_path = ['_static']

# -- Options for HTML output -------------------------------------------------


# -- Extension configuration -------------------------------------------------
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'show-inheritance': True,
    'exclude-members': '__init__'
}

# All these lines is to make the whole web_page more beautiful
autodoc_typehints_format = 'short'
autodoc_class_signature = 'separated'

# Additional configurations
autoclass_content = 'both'

def hide_init_params(cls): # This removes __init__ parameters of classes.
    cls.__init__.__sphinx_signature__ = "()"
    return cls

@hide_init_params
class YourClass:
    def __init__(self, param1, param2):
        pass




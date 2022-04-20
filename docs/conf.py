# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

import datetime

project = "thx"
copyright = f"{datetime.date.today().year}, John Reese"
author = "John Reese"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx_mdinclude",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

autodoc_default_options = {
    "show-inheritance": True,
    "members": True,
    "undoc-members": True,
}
autodoc_member_order = "groupwise"
autodoc_typehints = "description"

highlight_language = "python3"
intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}
master_doc = "index"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"
html_theme_options = {
    "description": "fast command runner",
    "fixed_sidebar": True,
    "badge_branch": "main",
    "github_button": False,
    "github_user": "jreese",
    "github_repo": "thx",
    "show_powered_by": False,
    "sidebar_collapse": False,
    "extra_nav_links": {
        "Report Issues": "https://github.com/jreese/thx/issues",
    },
    "font_family": "lato, Helvetica, sans-serif",
    "code_font_family": (
        "input-mono-narrow, 'Consolas', 'Menlo', 'DejaVu Sans Mono', "
        "'Bitstream Vera Sans Mono', monospace"
    ),
    "head_font_family": "ff-tisa-web-pro, Georgia, serif",
    "head_font_size": "280%",
}

html_sidebars = {
    "**": [
        "about.html",
        "badges.html",
        "navigation.html",
        "relations.html",
        "searchbox.html",
        # "omnilib.html",
    ],
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

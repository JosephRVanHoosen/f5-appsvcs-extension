# -*- coding: utf-8 -*-
#
# F5 Application Services documentation build configuration file, created by
# sphinx-quickstart on Fri Jan 19 13:51:14 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../'))

import f5_sphinx_theme
import re



# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.ifconfig',
    'sphinxjp.themes.basicstrap',
    'cloud_sptheme.ext.table_styling',
    'sphinx.ext.extlinks',
    'sphinx.ext.autosummary',
    'recommonmark',
    'sphinx_copybutton',
]

primary_domain = 'js'
js_source_path = 'docs'

#autosummary_generate = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']

source_suffix = {
  '.rst': 'restructuredtext'
}


# The encoding of source files.
#
source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'F5 BIG-IP AS3'
copyright = u'2024, F5 Networks'
author = u'F5 Networks'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in other places throughout the
# built documents.
#
# The short X.Y version.
version = u''
# The full version, including alpha/beta/rc tags.
release = u'3.49.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via  gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build',
                    'Thumbs.db',
                    '.DS_Store',
                    'venv',
                    '.github',
                    'requirements.txt',
                    'README.rst'
                    ]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'f5_sphinx_theme'
html_theme_path = f5_sphinx_theme.get_html_theme_path()

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'next_prev_link': True,
    'version_selector': True
}

html_context = {
 'version_meta_path': '/products/extensions/f5-appsvcs-extension/versions.json',
 'project_safe': re.sub('[^A-Za-z0-9]+', '', project)
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [ 'searchbox.html', 'localtoc.html', 'globaltoc.html' ]
}

# "<project> v<release> documentation" by default.
#
html_title = "{} {}".format(project, version)

# A shorter title for the navigation bar.  The default is the same as html_title.
#
#html_short_title = u''

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#
html_logo = '_static/f5-logo-solid-rgb_small.png'

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
#
html_last_updated_fmt = '%Y-%m-%d %I:%M:%S'

# Substitutions
rst_epilog = '''
''' % {
    'version': version,
    'base_url': 'http://clouddocs.f5.com'
}

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'F5ApplicationServicesdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'F5ApplicationServices.tex', u'F5 Application Services Documentation',
     u'F5 Networks', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'f5applicationservices', u'F5 Application Services Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'F5ApplicationServices', u'F5 Application Services Documentation',
     author, 'F5ApplicationServices', 'One line description of project.',
     'Miscellaneous'),
]
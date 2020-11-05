# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import datetime
import django
from recommonmark.parser import CommonMarkParser

django_version = ".".join(map(str, django.VERSION[0:2]))
python_version = ".".join(map(str, sys.version_info[0:2]))

sys.path.insert(0, os.path.abspath('..'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'training.settings'
django.setup()

# -- Project information -----------------------------------------------------

# See https://pypi.org/project/sphinxcontrib-django/
project = 'Django {json:api} training'
year = datetime.date.today().year
copyright = '2018-{}, The Trustees of Columbia University in the City of New York. '.format(year)
author = 'Alan Crosswell'

# The short X.Y version
from myapp import VERSION
version = VERSION
# The full version, including alpha/beta/rc tags
release = VERSION
# substitution for |today| in .rst -- the date this documentation was built.
today = datetime.date.today().isoformat()

# Auto-generate API documentation.
#os.environ['SPHINX_APIDOC_OPTIONS'] = "members,undoc-members,show-inheritance"
os.environ['SPHINX_APIDOC_OPTIONS'] = "members,show-inheritance"

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.apidoc',   # runs sphinx-apidoc automatically as part of sphinx-build
    'sphinx.ext.autodoc',     # the autodoc extensions uses files generated by apidoc
    #'sphinxcontrib_django',   # does some nicer django autodoc formatting, but:
                              # https://github.com/edoburu/sphinxcontrib-django/issues/12
    'sphinx.ext.viewcode',    # enable viewing autodoc'd code
    'sphinx.ext.intersphinx', # make links between different sphinx-documented packages
    'sphinx.ext.todo',        # TODO: figure out how to use this;-)
    'sphinx_markdown_tables', # CommonMark doesn't do tables: This extensions does!
    'sphinxcontrib.confluencebuilder', # supposedly installs docs on Confluence
]
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

source_parsers = {
    '.md': CommonMarkParser,
}

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['build']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'default'
html_theme = 'sphinx_rtd_theme'
# html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    # these are for sphinx_rtd_theme:
    'prev_next_buttons_location': 'both',
    'collapse_navigation': True,
    # these are for alabaster:
    # 'show_relbars': True,
    # 'fixed_sidebar': True,
    # 'sidebar_collapse': True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# also for alabaster theme:
# html_sidebars = {
#     '**': [
#         'about.html',
#         'navigation.html',
#         'relations.html',
#         'searchbox.html',
#         'donate.html',
#     ]
# }

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Djangojsonapitrainingdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '10pt',

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
    (master_doc, 'Djangojsonapitraining.tex', 'Django \\{json:api\\} training Documentation',
     'Alan Crosswell', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'djangojsonapitraining', 'Django {json:api} training Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Djangojsonapitraining', 'Django {json:api} training Documentation',
     author, 'Djangojsonapitraining', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# -- Extension configuration -------------------------------------------------

autodoc_member_order = 'bysource'
autodoc_inherit_docstrings = False

# https://stackoverflow.com/questions/10861463/omit-or-format-the-value-of-a-variable-when-documenting-with-sphinx
# from sphinx.ext.autodoc import ModuleLevelDocumenter, DataDocumenter
#
# def add_directive_header(self, sig):
#     ModuleLevelDocumenter.add_directive_header(self, sig)
#     # Rest of original method ignored
#
# DataDocumenter.add_directive_header = add_directive_header

apidoc_module_dir = '../myapp'
apidoc_output_dir = 'apidoc'
apidoc_excluded_paths = ['../myapp/migrations']
apidoc_separate_modules = True
apidoc_toc_file = False
apidoc_module_first = True
apidoc_extra_args = ['-f']

confluence_publish = True
confluence_server_url = os.environ.get('CONFLUENCE_SERVER', "https://confluence.columbia.edu")
confluence_space_name = os.environ.get('CONFLUENCE_SPACE', None)
confluence_parent_page = os.environ.get('CONFLUENCE_PARENT', None)
confluence_server_user = os.environ.get('CONFLUENCE_USER', None)
#confluence_ask_password = True
confluence_server_pass = os.environ.get('CONFLUENCE_PASS', None)

# -- Options for intersphinx extension ---------------------------------------

intersphinx_mapping = {
    'python': ('https://docs.python.org/{}'.format(python_version), None),
    'django': ('https://docs.djangoproject.com/en/{}/'.format(django_version), 
               'https://docs.djangoproject.com/en/{}/_objects/'.format(django_version)),
    # not sure why but the default lookup of objects.inv fails with None
    'djangorestframework-jsonapi': ('https://django-rest-framework-json-api.readthedocs.io/en/stable/',
                                    'https://django-rest-framework-json-api.readthedocs.io/en/stable/objects.inv'),
    # DRF doesn't use sphinx but rather mkdocs:-(
    #'djangorestframework': ('https://django-rest-framework.org/', None),
}

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -*- coding: utf-8 -*-
#
import sys
import os

extensions = [
  'sphinx.ext.autodoc',
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'ReBot Combat API'
copyright = u'2014, docbrown'
version = '0.1'
release = '0.1'
exclude_patterns = ['_build']
default_role = 'obj'
pygments_style = 'sphinx'
html_theme = 'default'
htmlhelp_basename = 'ReBotCombatAPIdoc'
latex_documents = [
  ('index', 'ReBotCombatAPI.tex', u'ReBot Combat API Documentation',
   u'docbrown', 'manual'),
]

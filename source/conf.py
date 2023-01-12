# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'yqlibook'
copyright = '2022, liyongqiang'
author = 'liyongqiang'
release = '0.0.1'
formats:
  - pdf

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser"
]

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'
import myst_parser

source_parsers = {
    '.md': myst_parser
}
source_suffix = ['.rst', '.md']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
#html_static_path = ['_static']
import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
#html_static_path = ['_static']
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_options = {
    'collapse_navigation': False,
    'display_version': False,
    'navigation_depth': 3,
}
html_logo = 'images/logo.png'

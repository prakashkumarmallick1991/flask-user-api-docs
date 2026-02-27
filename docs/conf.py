# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# --------------------------------------------------
# Import system modules
# --------------------------------------------------
import os
import sys

# Add project root directory to Python path
# This allows Sphinx to import your Flask app modules
sys.path.insert(0, os.path.abspath('..'))

# --------------------------------------------------
# Project information
# --------------------------------------------------

project = 'Flask User API'
copyright = '2026, Prakash'
author = 'Prakash'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',      # Auto-generate docs from docstrings
    'sphinx.ext.napoleon',     # Support Google & NumPy style docstrings
    'sphinx.ext.viewcode',     # Add links to highlighted source code
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# --------------------------------------------------
# HTML output configuration
# --------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

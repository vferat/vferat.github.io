# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('_ext'))

# Register custom pybtex style
from pybtex.plugin import register_plugin
from bold_title_style import ModalityStyle, Style as BoldTitleStyle
from modality import ModalityBackend
register_plugin('pybtex.style.formatting', 'bold_title_style', BoldTitleStyle)
register_plugin('pybtex.style.formatting', 'bold_title_modality_style', ModalityStyle)
register_plugin('pybtex.backends', 'docutils', ModalityBackend, force=True)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'sphinx-blog-page'
copyright = '2022–2026, Victor Férat'
author = 'Victor Férat'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_nb']
templates_path = ['_templates']

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist"
]

nb_execution_mode = "auto"

exclude_patterns = ['spelling_wordlist.txt']

# -- Edit Theme -------------------------------------------------
# https://pydata-sphinx-theme.readthedocs.io/en/v0.7.2/user_guide/configuring.html
html_theme = 'pydata_sphinx_theme'

html_theme_options = {
  "github_url": "https://github.com/vferat/",
  "icon_links": [
        {
            "name": "ORCID",
            "url": "https://orcid.org/0000-0003-1952-7657",
            "icon": "fa-brands fa-orcid",
        },
        {
            "name": "LinkedIn",
            "url": "https://www.linkedin.com/in/victor-ferat/",
            "icon": "fa-brands fa-linkedin",
        },        
        ],
  "search_bar_text": "Search this site...",
  "show_prev_next": False,
  "secondary_sidebar_items": {
      "**": ["ablog/postcard.html", "page-toc"],
      "index": [],
  },
}

html_favicon = "_static/favicon.ico"
html_title = "vferat"

html_static_path = ['_static']
html_css_files = [
    'custom.css',
]

# -- Sidebar Options for HTML output -------------------------------------------------
html_sidebars = {'index': [],
                 'about': ['sidebar.html'],
                 'publications': ['sidebar.html'],
                 'projects/**': ['sidebar.html'],
                 'posts/**': [],
                 'wiki/**': [],
                 'wiki/index': ["sidebar-nav-bs.html"],
                 'wiki/basics/index': ["sidebar-nav-bs.html"],
                 'wiki/neuroimaging/index': ["sidebar-nav-bs.html"],
                 'blog': ['ablog/tagcloud.html', 'ablog/archives.html'],
                 'blog/**': [],}

# -- Blog -------------------------------------------------
extensions += ['ablog', 'sphinx.ext.intersphinx']
myst_update_mathjax = False

blog_title = html_title
blog_path = "blog"
fontawesome_included = True
blog_post_pattern = ["posts/*/*.md", "posts/*/*.ipynb"]
post_auto_image = 1 # Index of the image that will be displayed
post_auto_excerpt = 1 # Number of paragraphs (default is ``1``) that will be displayed as an excerpt
post_redirect_refresh = 0 # Old project addresses redirect to their post without waiting

blog_authors = {
    'me': ('Victor Férat', 'https://vferat.github.io/about.html'),}
blog_languages = {
    'en': ('English', None),
    'fr': ('French', None),
}
# -- Bibliography -------------------------------------------------
extensions += ['sphinxcontrib.bibtex']
bibtex_bibfiles = ['bibliography.bib', 'posts/2024/2024-06-17.bib', 'wiki/basics/00_bibliography.bib', 'posts/2026/2026-04-09.bib']
bibtex_default_style = 'bold_title_style'

# -- Markdown syntax extension -------------------------------------------------

# Cards and grid
extensions += ['sphinx_design']

# Colored EEG / fMRI / MEG / neuromod labels
extensions += ['modality']

# toggle
extensions += ['sphinx_togglebutton']

# figures
numfig = True

# Equations
math_numfig = True

# Tabs
extensions += ['sphinx_tabs.tabs']

# Copy button
extensions += ['sphinx_copybutton']

# Spelling
extensions += [ 'sphinxcontrib.spelling' ]
# These pages are mostly author names from bibliographies.
spelling_exclude_patterns = ['publications.md', 'posts/2024/2024-06-17.md']
# The spelling builder cannot render notebook outputs; this does not affect the HTML.
suppress_warnings = ['mystnb.mime_priority']

# Inter sphinx
extensions += ["sphinx.ext.intersphinx"]

# Github context
html_context = {
    # "github_url": "https://github.com", # or your GitHub Enterprise site
    "github_user": "vferat",
    "github_repo": "vferat.github.io",
    "github_version": "main",
    "doc_path": "./source/",
    # Dark by default; visitors can still switch with the theme button.
    "default_mode": "dark",
}
html_theme_options["use_edit_page_button"] = True

# -- Brave Creator --
html_extra_path = ['../.nojekyll', 'extra']

# -- Google analytics --
html_theme_options["analytics"] = {
    "google_analytics_id": "G-FCG0LMTFDL",
}

# -- Referencing --
extensions += ['sphinx_sitemap']
html_baseurl = 'https://vferat.github.io'
html_extra_path += ["extra"]

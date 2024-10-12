# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'sphinx-blog-page'
copyright = '2024, Victor Férat'
author = 'Victor Férat'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']
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
    "tasklist",
]

exclude_patterns = ['spelling_wordlist.txt']
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# -- Edit Theme -------------------------------------------------
# https://pydata-sphinx-theme.readthedocs.io/en/v0.7.2/user_guide/configuring.html
html_theme = 'pydata_sphinx_theme'

html_theme_options = {
  "github_url": "https://github.com/vferat/",
  "icon_links": [
        {
            "name": "Twitter",
            "url": "https://twitter.com/ferat_victor",
            "icon": "fa-brands fa-twitter",
        },
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
}

html_favicon = "_static/favicon.ico"
html_title = "vferat"

html_static_path = ['_static']
html_css_files = [
    'custom.css',
]

# -- Sidebar Options for HTML output -------------------------------------------------
html_sidebars = {'index': ['sidebar.html'],
                 'about': ['sidebar.html'],
                 'publications': ['sidebar.html'],
                 'projects/**': ['sidebar.html', "sidebar-nav-bs.html"],
                 'wiki/**': [],
                 'wiki/index': ["sidebar-nav-bs.html"],
                 'wiki/basics/index': ["sidebar-nav-bs.html"],
                 'wiki/neuroimaging/index': ["sidebar-nav-bs.html"],
                 'blog': ['ablog/tagcloud.html', 'ablog/archives.html'],
                 'blog/**': ['ablog/tagcloud.html', 'ablog/archives.html'],}

# -- Blog -------------------------------------------------
extensions += ['ablog', 'sphinx.ext.intersphinx']
myst_update_mathjax = False

blog_title = html_title
blog_path = "blog"
fontawesome_included = True
blog_post_pattern = "posts/*/*.md"
post_auto_image = 1 # Index of the image that will be displayed
post_auto_excerpt = 1 # Number of paragraphs (default is ``1``) that will be displayed as an excerpt

blog_authors = {
    'me': ('Victor Férat', 'https://vferat.github.io/about.html'),}
blog_languages = {
    'en': ('English', None),
    'fr': ('French', None),
}
# -- Bibliography -------------------------------------------------
extensions += ['sphinxcontrib.bibtex']
bibtex_bibfiles = ['bibliography.bib', 'posts/2024/2024-06-17.bib', 'wiki/basics/00_bibliography.bib']

# -- Markdown syntax extension -------------------------------------------------

# Cards and grid
extensions += ['sphinx_design']
myst_enable_extensions = ["colon_fence"]

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

# Inter sphinx
extensions += ["sphinx.ext.intersphinx"]

# Github context
html_context = {
    # "github_url": "https://github.com", # or your GitHub Enterprise site
    "github_user": "vferat",
    "github_repo": "vferat.github.io",
    "github_version": "main",
    "doc_path": "./source/",
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

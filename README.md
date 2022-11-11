# Portfolio

A repository template to create a Portfolio / blog with Github Pages and Sphinx

https://desktop.github.com/


https://vferat.github.io/about.html


Create a new branch named ```gt-pages```
Go to <kbd>Settings</kbd> -> <kbd>Pages</kbd>

- <kbd>Source</kbd> -> <kbd>deploy from a branch</kbd>

- <kbd>Branch</kbd> -> <kbd>gh-pages</kbd>

## Sphinx

## Create a new environment
```console
conda create -n sphinx python=3.9
conda activate sphinx
```
## install sphinx
```console
pip install sphinx
```
also add it to ```requirements.txt```
```txt
sphinx
```

## Start a new sphinx project
```console
sphinx-quickstart
```

## Build Docs

```console
make html
```

open <kbd>build</kbd>/ <kbd>index.html</kbd>

## Delete Docs

```console
make clean
```

# Configure the website

Edit ```conf.py```

## Use markdown
install myst-parser

```console
pip install --upgrade myst-parser
```
also add it to ```requirements.txt```
```txt
sphinx
myst-parser
```
Add myst_parser to the list of configured extensions:

```python
extensions = ['myst_parser']
```

adjust the source_suffix variable in conf.py
```python
...

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

...
```
## Install a new theme
```console
pip install pydata_sphinx_theme
```

In conf.py
```python
...

html_theme = 'pydata_sphinx_theme'

...
```
## Configure pydata_sphinx_theme

```python
...

html_theme_options = {
  "github_url": "https://github.com/vferat/",
  "twitter_url": "https://twitter.com/ferat_victor",
  "search_bar_text": "Search this site...",
}

html_favicon = "_static/favicon.ico"
html_title = "Pycromancer"

...
```

## Bonus: Adda custom icon link

```python
...

html_theme_options = {
  "github_url": "https://github.com/vferat/",
  "twitter_url": "https://twitter.com/ferat_victor",
  "icon_links": [
        {
            "name": "ORCID",
            "url": "https://orcid.org/0000-0003-1952-7657",
            "icon": "fa-brands fa-orcid",
        },],
  "search_bar_text": "Search this site...",
}
...

```

## Configure the nav bar
- Create a new page ```about.md```
- Create a new page 'blog.md'
- Add a toctree to ```index.md```
``````md
```{toctree}
:maxdepth: 2
:hidden:
about.md
blog.md
```
``````


## Create a sidebar

create ```sidebar.html``` in ```_templates```

```
<div class="profile-pic"><img src="{{ pathto('_static/profil.jfif', 1) }}" /></div>

<div class="bio">
    <div class="name">
        Victor Férat
    </div>
    <div class="title">
        <center>Neurosciences & Python </center>
    </div>
</div>
```

```python
html_sidebars = {'**': ['sidebar.html']}
```

or use the sidebar only for specific pages
```python
...

html_sidebars = {'index': ['sidebar.html'],
                 'about': ['sidebar.html']}

...
```

### Custom the sidebar with css

#### create ```custom.css``` in ```_static```

```css
/* Bio area */
div.profile-pic {
    margin-top: 1em;
}

div.profile-pic img {
    border-radius: 50%;
    width: 200px;
    height: 200px;
    margin: 0 auto;
    display: block;
    filter: grayscale(80%);
}

.title {
    margin: 1em auto;
    max-width: 220px;
    text-align: center;
}

.name {
    font-size: 1.5em;
    text-align: center;
}
```

#### Use css in conf

```python
...

html_css_files = [
    'custom.css',
]

...
```

## Add a blog

https://ablog.readthedocs.io/


### Install
```console
pip install ablog
```

### Configure

```python
...

extensions += ['ablog']

...
```

### Add Content
create post/_year_/yy_mm_dd_title.md

### Edit blog sidebar

```python
...

html_sidebars = {...
                 'blog': ['tagcloud.html', 'archives.html'],}
                 
...
```

## Add Bibliography

```sphinxbibtex```

### Install 

```console
pip install sphinxcontrib-bibtex
```

#### Configure

```python
...

extensions += ['sphinxcontrib.bibtex']
bibtex_bibfiles = ['bibliography.bib']

...
```

### Add content

- Create ```bibliography.bib```

- Create ```publications.md```

- Add it to toctree in ```index.md```

- Insert biblio:

``````md
```{bibliography}
:list: bullet
:filter: author % "Ferat" or "Férat"
```
``````

### Panels with sphinx_design

```console
pip install sphinx_design
```

```python
...

extensions += ['sphinx_design']

...
```

### Twitter

"sphinxcontrib.twitter"

## Edit style

https://pydata-sphinx-theme.readthedocs.io/en/v0.5.2/user_guide/customizing.html

Edit ```conf.py```
```

html_css_files = [
    'custom.css',
]
```

Edit ```custom.css```
```css
/* Theme */
/* https://pydata-sphinx-theme.readthedocs.io/en/v0.7.2/user_guide/customizing.html */
@import "../basic.css";

html[data-theme="light"] {
    --pst-color-primary: rgb(0, 153, 255);
    --pst-color-text-base: rgb(0, 89, 100);
}

html[data-theme="dark"] {
    --pst-color-primary: rgb(68, 180, 255);
    --pst-color-text-base: rgb(7, 226, 255);
}
```

# Bonus

## Using giscus

create layout.html in templates


{%- extends "pydata_sphinx_theme/layout.html" %}

{% block docs_body %}
{{ super() }}
<!-- Add a comment box underneath the page's content -->
<script src="https://giscus.app/client.js"
        data-repo="choldgraf/choldgraf.github.io"
        data-repo-id="MDEwOlJlcG9zaXRvcnk1MTIzNzA1NA=="
        data-category="Blog comments"
        data-category-id="DIC_kwDOAw3Qvs4CAV4E"
        data-mapping="pathname"
        data-reactions-enabled="1"
        data-emit-metadata="0"
        data-theme="light"
        data-lang="en"
        crossorigin="anonymous"
        async>
</script>
{% endblock %}

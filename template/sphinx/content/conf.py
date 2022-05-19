# -*- coding: utf-8 -*-

project = 'Learn MDN'
copyright = '2022, Jim Gao'
author = 'Jim Gao'

extensions = [
    # Sphinx's own extensions
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    # External stuff
    "sphinx_copybutton",
    "myst_parser",
    "sphinxcontrib.mermaid"
]

# Used to extract JSDoc function/class docs from source
# js_language = 'javascript'
# js_source_path = '../src/'
# jsdoc_config_path = '../tsconfig.json'
# primary_domain = 'js'

html_theme = 'furo'
html_title = "Learn MDN"
html_theme_options = {
    "sidebar_hide_name": True,
}

html_static_path = ["_static"]
html_js_files = [
    'https://unpkg.com/mermaid@8.13.10/dist/mermaid.min.js',
    'link.js'
]

extlinks = {
    'MDN_web': ('https://developer.mozilla.org/en-US/docs/Web/%s','web | '),
    'MDN_learn': ('https://developer.mozilla.org/en-US/docs/Learn/%s','learn | ')
}

myst_enable_extensions = [
    "tasklist",
]
"""
Sphinx Documentation Genrator
"""

from datetime import datetime
from pathlib import Path
import sys

_project_path = Path(__file__).resolve().parent.parent.parent
_project_dir = str(_project_path)
sys.path.insert(0, _project_dir)

from lunchable import __lunchable__, __version__

_author = "Justin Flannery"
project = __lunchable__
copyright = f"{datetime.now().year}, {_author}"
author = _author
release = version = __version__

extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",

    "sphinxcontrib.apidoc",
    "sphinxcontrib.autodoc_pydantic",

    "autodocsumm",
    "myst_parser",
    "autoclasstoc",
    "sphinx_copybutton",
    "sphinx_autodoc_typehints",
    "sphinx_autodoc_defaultargs",
    "sphinx_click",
]

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

templates_path = ["_templates"]
html_static_path = ["_static"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "display_version": True,
}
html_show_sphinx = False
html_show_sourcelink = False

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}

autosummary_generate = True
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

autodoc_pydantic_model_show_json = False
autodoc_pydantic_settings_show_json = False

always_document_default_args = True
docstring_default_arg_substitution = "**[Default]:**"

html_favicon = "https://juftin.com/favicon.ico"


import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

logger.info("Hey, I'm the local logger")


"""
Sphinx Documentation Genrator
"""

from datetime import datetime
from pathlib import Path
import sys

_project_dir = str(Path(__file__).resolve().parent.parent.parent)
sys.path.insert(0, _project_dir)

from lunchable import __lunchable__, __version__

_author = "Justin Flannery"
project = __lunchable__
copyright = f"{datetime.now().year}, {_author}"
author = _author
release = __version__

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",

    "sphinxcontrib.autodoc_pydantic",
    "autodocsumm",
    "myst_parser",
    "autoclasstoc",
    "sphinx_copybutton",
    "sphinx_autodoc_defaultargs"
]

templates_path = ["_templates"]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"

html_static_path = ["_static"]

autodoc_pydantic_model_show_json = False
autodoc_pydantic_settings_show_json = False

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}

autosummary_generate = True

intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}

rst_prolog = """
.. |default| raw:: html

    <div class="default-value-section">""" + \
             ' <span class="default-value-label">Default:</span>'

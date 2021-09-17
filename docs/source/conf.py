"""
Sphinx Documentation Genrator
"""

from datetime import datetime
from pathlib import Path
import sys

_project_dir = str(Path(__file__).resolve().parent.parent.parent)
sys.path.insert(0, _project_dir)

from lunchmoney import __lunchmoney__, __version__

_author = "Justin Flannery"
project = __lunchmoney__
copyright = f"{datetime.now().year}, {_author}"
author = _author
release = __version__

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.napoleon",
    "sphinxcontrib.autodoc_pydantic",
    "autodocsumm"
]

templates_path = ["_templates"]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"

html_static_path = ["_static"]

autodoc_pydantic_model_show_json = False
autodoc_pydantic_settings_show_json = False

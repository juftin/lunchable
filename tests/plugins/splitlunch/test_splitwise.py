"""
Run Tests on the Splitwise Plugin
"""

import logging

logger = logging.getLogger(__name__)


def test_import_splitwise():
    """
    Try to import splitwise and succeed since the extra is installed in tox
    """
    test_case = True
    try:
        from lunchmoney.plugins.splitlunch import SplitLunch
    except ImportError:
        test_case = False
    finally:
        assert test_case is True

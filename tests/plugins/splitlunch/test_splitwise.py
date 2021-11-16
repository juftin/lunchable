"""
Run Tests on the Splitwise Plugin
"""

import logging

from lunchable.plugins.splitlunch import SplitLunch
from tests.conftest import lunchable_cassette

logger = logging.getLogger(__name__)


def test_import_splitwise():
    """
    Try to import splitwise and succeed since the extra is installed in tox
    """
    test_case = True
    try:
        from lunchable.plugins.splitlunch import SplitLunch
    except ImportError:
        test_case = False
    finally:
        assert test_case is True


@lunchable_cassette
def test_update_balance():
    """
    Update the Balance
    """
    lunch = SplitLunch()
    lunch.update_splitwise_balance()


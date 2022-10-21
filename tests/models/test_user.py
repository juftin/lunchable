"""
Run Tests on the Miscellaneous Endpoints
"""

import logging

from lunchable import LunchMoney
from tests.conftest import lunchable_cassette

logger = logging.getLogger(__name__)


@lunchable_cassette
def test_get_user(lunch_money_obj: LunchMoney):
    """
    Get Me Object
    """
    me = lunch_money_obj.get_user()
    assert isinstance(me.user_id, int)
    assert isinstance(me.user_email, str)
    assert isinstance(me.budget_name, str)
    assert me.api_key_label == "Lunchable"

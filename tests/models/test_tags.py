"""
Run Tests on the Tags Endpoint
"""

import logging

from lunchable import LunchMoney
from lunchable.models.tags import TagsObject
from tests.conftest import lunchable_cassette

logger = logging.getLogger(__name__)


@lunchable_cassette
def test_get_tags(lunch_money_obj: LunchMoney):
    """
    Get Plaid Account and Assert it's a Plaid Account
    """
    tags = lunch_money_obj.get_tags()
    assert len(tags) >= 1
    for tag in tags:
        assert isinstance(tag, TagsObject)
    logger.info("%s Plaid Accounts returned", len(tags))

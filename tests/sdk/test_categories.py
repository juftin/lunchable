"""
Run Tests on the Categories Endpoint
"""

import logging
from random import choice

from lunchmoney import LunchMoney
from lunchmoney.sdk.categories import CategoriesObject
from tests.conftest import lunchmoney_cassette

logger = logging.getLogger(__name__)


@lunchmoney_cassette
def test_get_categories(lunch_money_obj: LunchMoney):
    """
    Get Categories and Assert that they're categories
    """
    categories = lunch_money_obj.get_categories()
    assert len(categories) >= 1
    for category in categories:
        assert isinstance(category, CategoriesObject)
    logger.info("%s Categories returned", len(categories))
    logger.info(choice(categories))

"""
Run Tests on the Categories Endpoint
"""

import logging

from lunchmoney import LunchMoney
from lunchmoney.models.categories import CategoriesObject
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


@lunchmoney_cassette
def test_create_category(lunch_money_obj: LunchMoney):
    """
    Get Categories and Assert that they're categories
    """
    name = "Test Category"
    category = lunch_money_obj.insert_category(name=name,
                                               description="Test Category Description",
                                               exclude_from_budget=True)
    logger.info("Category ID # %s was just created: %s", category, name)
    assert isinstance(category, int)

"""
Run Tests on the Categories Endpoint
"""

import logging

from lunchable import LunchMoney
from lunchable.models.categories import CategoriesObject
from tests.conftest import lunchable_cassette

logger = logging.getLogger(__name__)


@lunchable_cassette
def test_get_categories(lunch_money_obj: LunchMoney):
    """
    Get Categories and Assert that they're categories
    """
    categories = lunch_money_obj.get_categories()
    assert len(categories) >= 1
    for category in categories:
        assert isinstance(category, CategoriesObject)
    logger.info("%s Categories returned", len(categories))


@lunchable_cassette
def test_create_category(lunch_money_obj: LunchMoney):
    """
    Create A Single Category
    """
    name = "Test Category"
    category = lunch_money_obj.insert_category(
        name=name, description="Test Category Description", exclude_from_budget=True
    )
    logger.info("Category ID # %s was just created: %s", category, name)
    assert isinstance(category, int)


@lunchable_cassette
def test_get_category(lunch_money_obj: LunchMoney):
    """
    Get a Single Category
    """
    category_id = 443128
    category = lunch_money_obj.get_category(category_id=category_id)
    logger.info("Category ID # %s was just fetched: %s", category.id, category.name)
    assert isinstance(category, CategoriesObject)


@lunchable_cassette
def test_delete_category(lunch_money_obj: LunchMoney):
    """
    Delete a Category
    """
    category_id = 343088
    deleted = lunch_money_obj.remove_category(category_id=category_id)
    logger.info("Category ID # %s was just deleted", category_id)
    assert deleted is True


@lunchable_cassette
def test_delete_category_force(lunch_money_obj: LunchMoney):
    """
    Forcefully Delete a Category
    """
    category_id = 343089
    deleted = lunch_money_obj.remove_category_force(category_id=category_id)
    logger.info("Category ID # %s was just deleted", category_id)
    assert deleted is True


@lunchable_cassette
def test_update_category(lunch_money_obj: LunchMoney):
    """
    Update a Single Category
    """
    category_id = 443128
    updated = lunch_money_obj.update_category(
        category_id=category_id, description="Test Category Description Updated"
    )
    assert isinstance(updated, bool)


@lunchable_cassette
def test_create_category_group(lunch_money_obj: LunchMoney):
    """
    Create A Single Category Group
    """
    name = "Test Category Group"
    category_id = lunch_money_obj.insert_category_group(
        name=name, description="Test Category Group!!", exclude_from_budget=True
    )
    logger.info("Category Group ID # %s was just created: %s", category_id, name)
    assert isinstance(category_id, int)


@lunchable_cassette
def test_add_to_category_group(lunch_money_obj: LunchMoney):
    """
    Create A Single Category Group
    """
    name = "Test Category Group"
    category = lunch_money_obj.insert_into_category_group(
        category_group_id=658694,
        new_categories=["Another Another Test Category"],
        category_ids=[443128],
    )
    logger.info("Category Group ID # %s was just created: %s", category.id, name)
    assert isinstance(category, CategoriesObject)


@lunchable_cassette
def test_get_categories_nested(lunch_money_obj: LunchMoney):
    """
    Get Categories and Assert that they're categories
    """
    categories = lunch_money_obj.get_categories(format="nested")
    categories_with_children = list(filter(lambda x: x.children, categories))
    assert len(categories_with_children) >= 1


@lunchable_cassette
def test_get_categories_flattened(lunch_money_obj: LunchMoney):
    """
    Get Categories and Assert that they're categories
    """
    categories = lunch_money_obj.get_categories(format="flattened")
    assert len(categories) >= 1
    for category in categories:
        assert isinstance(category, CategoriesObject)

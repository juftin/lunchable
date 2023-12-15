"""
Run Tests on the Assets Endpoint
"""

import datetime
import logging

import pytest

from lunchable import LunchMoney
from lunchable.models.assets import AssetsObject
from tests.conftest import lunchable_cassette

logger = logging.getLogger(__name__)


@pytest.fixture
def lunchmoney_asset() -> AssetsObject:
    """
    Static lunchable.models.AssetsObject

    Returns
    -------
    AssetsObject
    """
    splitwise_asset = AssetsObject(
        id=78214,
        type_name="cash",
        subtype_name="digital wallet (paypal, venmo)",
        name="Splitwise Balance",
        display_name="Splitwise",
        balance=-1.0,
        balance_as_of=datetime.datetime(
            2021, 8, 28, 16, 6, 35, tzinfo=datetime.timezone.utc
        ),
        closed_on=None,
        currency="usd",
        institution_name="Splitwise",
        created_at=datetime.datetime(
            2021, 8, 28, 16, 6, 2, 701000, tzinfo=datetime.timezone.utc
        ),
    )
    return splitwise_asset


@lunchable_cassette
def test_get_assets(lunch_money_obj: LunchMoney):
    """
    Get Assets and Assert that they're assets
    """
    assets = lunch_money_obj.get_assets()
    assert len(assets) >= 1
    for asset in assets:
        assert isinstance(asset, AssetsObject)
    logger.info("%s Assets returned", len(assets))


@lunchable_cassette
def test_update_asset(lunch_money_obj: LunchMoney, lunchmoney_asset: AssetsObject):
    """
    Update an Asset
    """
    response = lunch_money_obj.update_asset(asset_id=lunchmoney_asset.id, balance=5.20)
    assert isinstance(response, AssetsObject)
    logger.info(response)


@lunchable_cassette
def test_create_asset(lunch_money_obj: LunchMoney):
    """
    Create an Asset
    """
    response = lunch_money_obj.insert_asset(
        type_name="cash",
        name="test-account-1",
        subtype_name=None,
        display_name="Test Account #1",
        balance=4.20,
        currency="usd",
        institution_name="Test Institution",
    )
    assert isinstance(response, AssetsObject)
    logger.info(response)

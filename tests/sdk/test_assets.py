import datetime
import logging

import pytest

from lunchmoney import LunchMoney
from lunchmoney.sdk.assets import AssetsObject
from tests.conftest import lunchmoney_cassette

logger = logging.getLogger(__name__)


@pytest.fixture
def lunchmoney_asset() -> AssetsObject:
    splitwise_asset = AssetsObject(id=21845,
                                   type_name='cash',
                                   subtype_name='digital wallet (paypal, venmo)',
                                   name='Splitwise Balance',
                                   display_name='Splitwise',
                                   balance=-1.0,
                                   balance_as_of=datetime.datetime(2021, 8, 28, 16, 6, 35,
                                                                   tzinfo=datetime.timezone.utc),
                                   closed_on=None,
                                   currency='usd',
                                   institution_name='Splitwise',
                                   created_at=datetime.datetime(2021, 8, 28, 16, 6, 2, 701000,
                                                                tzinfo=datetime.timezone.utc))
    return splitwise_asset


@lunchmoney_cassette
def test_get_assets(lunch_money_obj: LunchMoney):
    """
    Get Assets and Assert that they're assets
    """
    assets = lunch_money_obj.get_assets()
    assert len(assets) >= 1
    for asset in assets:
        assert isinstance(asset, AssetsObject)
    logger.info("%s Assets returned", len(assets))


@lunchmoney_cassette
def test_update_asset(lunch_money_obj: LunchMoney, lunchmoney_asset: AssetsObject):
    """
    Update an Asset
    """
    response = lunch_money_obj.update_asset(asset_id=lunchmoney_asset.id,
                                            balance=5.20)
    assert isinstance(response, AssetsObject)
    logger.info(response)

"""
Run Tests on the Plaid Accounts Endpoint
"""

import logging

from lunchable import LunchMoney
from lunchable.models.plaid_accounts import PlaidAccountObject
from tests.conftest import lunchable_cassette

logger = logging.getLogger(__name__)


@lunchable_cassette
def test_get_plaid_accounts(lunch_money_obj: LunchMoney):
    """
    Get Plaid Account and Assert it's a Plaid Account
    """
    plaid_accounts = lunch_money_obj.get_plaid_accounts()
    assert len(plaid_accounts) >= 1
    for plaid_account in plaid_accounts:
        assert isinstance(plaid_account, PlaidAccountObject)
    logger.info("%s Plaid Accounts returned", len(plaid_accounts))

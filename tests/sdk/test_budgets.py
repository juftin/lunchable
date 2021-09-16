"""
Run Tests on the Budgets Endpoint
"""

import datetime
import logging

from lunchmoney import LunchMoney
from lunchmoney.sdk import BudgetObject
from tests.conftest import beginning_of_this_month, lunchmoney_cassette, obscure_start_date

logger = logging.getLogger(__name__)


@lunchmoney_cassette
def test_upsert_budget(lunch_money_obj: LunchMoney):
    """
    Test upserting some budgets

    Parameters
    ----------
    lunch_money_obj: LunchMoney

    Returns
    -------
    None
    """
    # Ride Sharing
    response = lunch_money_obj.upsert_budget(start_date=obscure_start_date,
                                             category_id=229137,
                                             amount=100.00)
    assert response == dict(category_group=None)


@lunchmoney_cassette
def test_get_budgets(lunch_money_obj: LunchMoney):
    """
    Test Getting some budgets

    Parameters
    ----------
    lunch_money_obj: LunchMoney

    Returns
    -------
    None
    """
    budgets = lunch_money_obj.get_budgets(
        start_date=beginning_of_this_month,
        end_date=beginning_of_this_month + datetime.timedelta(days=28))
    assert len(budgets) >= 1
    for budget in budgets:
        assert isinstance(budget, BudgetObject)
    logger.info("%s Budgets Found", len(budgets))

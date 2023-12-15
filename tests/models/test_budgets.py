"""
Run Tests on the Budgets Endpoint
"""

import datetime
import logging

from lunchable import LunchMoney
from lunchable.models import BudgetObject
from tests.conftest import lunchable_cassette

logger = logging.getLogger(__name__)


@lunchable_cassette
def test_upsert_budget(
    lunch_money_obj: LunchMoney, obscure_start_date: datetime.datetime
):
    """
    Test upserting some budgets
    """
    # Ride Sharing
    response = lunch_money_obj.upsert_budget(
        start_date=obscure_start_date, category_id=443127, amount=100.00
    )
    assert isinstance(response, dict) or response is None


@lunchable_cassette
def test_get_budgets(
    lunch_money_obj: LunchMoney, obscure_start_date: datetime.datetime
):
    """
    Test Getting some budgets
    """
    budgets = lunch_money_obj.get_budgets(
        start_date=obscure_start_date,
        end_date=obscure_start_date + datetime.timedelta(days=28),
    )
    assert len(budgets) >= 1
    for budget in budgets:
        assert isinstance(budget, BudgetObject)
    logger.info("%s Budgets Found", len(budgets))
    logger.info(budgets)


@lunchable_cassette
def test_delete_budget(
    lunch_money_obj: LunchMoney, obscure_start_date: datetime.datetime
):
    """
    Delete a Budget
    """
    deleted = lunch_money_obj.remove_budget(
        start_date=obscure_start_date, category_id=443127
    )
    logger.info("Budget Deleted")
    assert deleted is True

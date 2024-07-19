"""
Run Tests on the Recurring Items Endpoint
"""

import datetime
import logging

from lunchable import LunchMoney
from lunchable.models.recurring_items import RecurringItemsObject
from tests.conftest import lunchable_cassette

logger = logging.getLogger(__name__)


@lunchable_cassette
def test_get_recurring_items(
    lunch_money_obj: LunchMoney, obscure_start_date: datetime.datetime
):
    """
    Get Recurring Items, and ensure they are returned as RecurringItemsObject
    """
    recurring_expenses = lunch_money_obj.get_recurring_items(
        start_date=obscure_start_date
    )
    assert len(recurring_expenses) >= 1
    for recurring_expense in recurring_expenses:
        assert isinstance(recurring_expense, RecurringItemsObject)
    logger.info("%s Recurring Expenses returned", len(recurring_expenses))

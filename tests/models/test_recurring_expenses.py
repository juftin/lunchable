"""
Run Tests on the Recurring Expenses Endpoint
"""

import datetime
import logging

import pytest

from lunchable import LunchMoney
from lunchable.models.recurring_expenses import RecurringExpensesObject
from tests.conftest import lunchable_cassette

logger = logging.getLogger(__name__)


@lunchable_cassette
def test_get_recurring_expenses(
    lunch_money_obj: LunchMoney, obscure_start_date: datetime.datetime
):
    """
    Get Recurring Expense and Assert it's a Recurring Expense
    """
    with pytest.warns(DeprecationWarning):
        recurring_expenses = lunch_money_obj.get_recurring_expenses(
            start_date=obscure_start_date
        )
    assert len(recurring_expenses) >= 1
    for recurring_expense in recurring_expenses:
        assert isinstance(recurring_expense, RecurringExpensesObject)
    logger.info("%s Recurring Expenses returned", len(recurring_expenses))

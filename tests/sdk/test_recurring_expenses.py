"""
Run Tests on the Recurring Expenses Endpoint
"""

import logging

from lunchmoney import LunchMoney
from lunchmoney.sdk.recurring_expenses import RecurringExpensesObject
from tests.conftest import lunchmoney_cassette

logger = logging.getLogger(__name__)


@lunchmoney_cassette
def test_get_recurring_expenses(lunch_money_obj: LunchMoney):
    """
    Get Recurring Expense and Assert it's a Recurring Expense
    """
    recurring_expenses = lunch_money_obj.get_recurring_expenses()
    assert len(recurring_expenses) >= 1
    for recurring_expense in recurring_expenses:
        assert isinstance(recurring_expense, RecurringExpensesObject)
    logger.info("%s Recurring Expenses returned", len(recurring_expenses))

# Author::    Justin Flannery  (mailto:juftin@juftin.com)

"""
Lunch Money - Recurring Expenses

https://lunchmoney.dev/#recurring-expenses
"""

import datetime
import logging
from typing import List, Optional

from pydantic import BaseModel

from lunchmoney.config import APIConfig
from lunchmoney.sdk.core import LunchMoneyCore

logger = logging.getLogger(__name__)


class RecurringExpensesObject(BaseModel):
    """
    https://lunchmoney.dev/#recurring-expenses-object
    """

    id: int
    start_date: Optional[datetime.date]
    end_date: Optional[datetime.date]
    cadence: str
    payee: str
    amount: float
    currency: str
    description: Optional[str]
    billing_date: datetime.date
    type: str
    original_name: Optional[str]
    source: str
    plaid_account_id: Optional[int]
    asset_id: Optional[int]
    transaction_id: Optional[int]
    category_id: Optional[int]


class RecurringExpenseParamsGet(BaseModel):
    """
    https://lunchmoney.dev/#get-recurring-expenses
    """

    start_date: datetime.date
    debit_as_negative: bool


class LunchMoneyRecurringExpenses(LunchMoneyCore):
    """
    Lunch Money Recurring Expenses Interactions
    """

    def get_recurring_expenses(self, start_date: Optional[datetime.date] = None,
                               debit_as_negative: bool = False) -> List[RecurringExpensesObject]:
        """
        Retrieve a list of recurring expenses to expect for a specified period.

        Every month, a different set of recurring expenses is expected. This is because recurring
        expenses can be once a year, twice a year, every 4 months, etc.

        If a recurring expense is listed as “twice a month”, then that recurring expense will be
        returned twice, each with a different billing date based on when the system believes that
        recurring expense transaction is to be expected. If the recurring expense is listed as
        “once a week”, then that recurring expense will be returned in this list as many times as
        there are weeks for the specified month.

        In the same vein, if a recurring expense that began last month is set to “Every 3
        months”, then that recurring expense will not show up in the results for this month.

        Parameters
        ----------
        start_date : Optional[datetime.date]
            Date to search. By default will return the first day of the current month
        debit_as_negative: bool
            Pass in true if you’d like expenses to be returned as negative amounts and credits as
            positive amounts.

        Returns
        -------
        List[RecurringExpensesObject]
        """
        if start_date is None:
            start_date = datetime.datetime.now().date().replace(day=1)
        params = RecurringExpenseParamsGet(start_date=start_date,
                                           debit_as_negative=debit_as_negative).dict()
        response_data = self._make_request(method="GET",
                                           url_path=[APIConfig.LUNCH_MONEY_RECURRING_EXPENSES],
                                           params=params)
        recurring_expenses = response_data.get(APIConfig.LUNCH_MONEY_RECURRING_EXPENSES)
        recurring_expenses_objects = [RecurringExpensesObject(**item) for item in
                                      recurring_expenses]
        logger.debug("%s RecurringExpensesObjects retrieved", len(recurring_expenses_objects))
        return recurring_expenses_objects

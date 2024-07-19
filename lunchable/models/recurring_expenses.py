"""
Lunch Money - Recurring Expenses

https://lunchmoney.dev/#recurring-expenses
"""

import datetime
import logging
import warnings
from typing import List, Optional

from pydantic import Field

from lunchable._config import APIConfig
from lunchable.models._base import LunchableModel
from lunchable.models._core import LunchMoneyAPIClient
from lunchable.models._descriptions import _RecurringExpensesDescriptions

logger = logging.getLogger(__name__)


class RecurringExpensesObject(LunchableModel):
    """
    Recurring Expenses Object

    https://lunchmoney.dev/#recurring-expenses-object
    """

    id: int = Field(description=_RecurringExpensesDescriptions.id)
    start_date: Optional[datetime.date] = Field(
        None, description=_RecurringExpensesDescriptions.start_date
    )
    end_date: Optional[datetime.date] = Field(
        None, description=_RecurringExpensesDescriptions.end_date
    )
    cadence: str = Field(description=_RecurringExpensesDescriptions.cadence)
    payee: str = Field(description="Payee of the recurring expense")
    amount: float = Field(description=_RecurringExpensesDescriptions.amount)
    currency: str = Field(
        max_length=3, description=_RecurringExpensesDescriptions.currency
    )
    description: Optional[str] = Field(
        None, description=_RecurringExpensesDescriptions.description
    )
    billing_date: datetime.date = Field(
        description=_RecurringExpensesDescriptions.billing_date
    )
    type: str = Field(description=_RecurringExpensesDescriptions.type)
    original_name: Optional[str] = Field(
        None, description=_RecurringExpensesDescriptions.original_name
    )
    source: str = Field(description=_RecurringExpensesDescriptions.source)
    plaid_account_id: Optional[int] = Field(
        None, description=_RecurringExpensesDescriptions.plaid_account_id
    )
    asset_id: Optional[int] = Field(
        None, description=_RecurringExpensesDescriptions.asset_id
    )
    category_id: Optional[int] = Field(
        None, description=_RecurringExpensesDescriptions.category_id
    )


class RecurringExpenseParamsGet(LunchableModel):
    """
    https://lunchmoney.dev/#get-recurring-expenses
    """

    start_date: datetime.date
    debit_as_negative: Optional[bool] = None


class RecurringExpensesClient(LunchMoneyAPIClient):
    """
    Lunch Money Recurring Expenses Interactions
    """

    def get_recurring_expenses(
        self,
        start_date: Optional[datetime.date] = None,
        debit_as_negative: Optional[bool] = None,
    ) -> List[RecurringExpensesObject]:
        """
        Get Recurring Expenses

        **DEPRECATED** - Use [LunchMoney.get_recurring_items()][lunchable.LunchMoney.get_recurring_items]
        instead.

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
            Pass in true if you'd like expenses to be returned as negative amounts and credits as
            positive amounts.

        Returns
        -------
        List[RecurringExpensesObject]
        """
        warnings.warn(
            message=(
                "`LunchMoney.get_recurring_expenses` is deprecated, "
                "use `LunchMoney.get_recurring_items` instead"
            ),
            category=DeprecationWarning,
            stacklevel=2,
        )
        if start_date is None:
            start_date = datetime.datetime.now().date().replace(day=1)
        params = RecurringExpenseParamsGet(
            start_date=start_date, debit_as_negative=debit_as_negative
        ).model_dump(exclude_none=True)
        response_data = self.make_request(
            method=self.Methods.GET,
            url_path=[APIConfig.LUNCH_MONEY_RECURRING_EXPENSES],
            params=params,
        )
        recurring_expenses = response_data.get(APIConfig.LUNCH_MONEY_RECURRING_EXPENSES)
        recurring_expenses_objects = [
            RecurringExpensesObject.model_validate(item) for item in recurring_expenses
        ]
        logger.debug(
            "%s RecurringExpensesObjects retrieved", len(recurring_expenses_objects)
        )
        return recurring_expenses_objects

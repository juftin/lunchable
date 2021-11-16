"""
Lunch Money - Recurring Expenses

https://lunchmoney.dev/#recurring-expenses
"""

import datetime
import logging
from typing import List, Optional

from pydantic import BaseModel, Field

from lunchable._config import APIConfig
from lunchable.models._core import LunchMoneyAPIClient

logger = logging.getLogger(__name__)


class RecurringExpensesObject(BaseModel):
    """
    Recurring Expenses Object

    https://lunchmoney.dev/#recurring-expenses-object
    """

    _id_description = "Unique identifier for recurring expense"
    _start_date_description = """
    Denotes when recurring expense starts occurring in ISO 8601 format. 
    If null, then this recurring expense will show up for all time 
    before end_date
    """
    _end_date_description = """
    Denotes when recurring expense stops occurring in ISO 8601 format. 
    If null, then this recurring expense has no set end date and will 
    show up for all months after start_date
    """
    _cadence_description = """
    One of: [monthly, twice a month, once a week, every 3 months, every 4 months, 
    twice a year, yearly]
    """
    _amount_description = "Amount of the recurring expense in numeric format to 4 decimal places"
    _currency_description = """
    Three-letter lowercase currency code for the recurring expense in ISO 4217 format
    """
    _description_description = """
    If any, represents the user-entered description of the recurring expense
    """
    _billing_date_description = """
    Expected billing date for this recurring expense for this month in ISO 8601 format
    """
    _type_description = """"
    This can be one of two values: cleared (The recurring expense has been reviewed 
    by the user), suggested (The recurring expense is suggested by the system; 
    the user has yet to review/clear it)
    """
    _original_name_description = """
    If any, represents the original name of the recurring expense as
    denoted by the transaction that triggered its creation
    """
    _source_description = """
    This can be one of three values: manual (User created this recurring expense 
    manually from the Recurring Expenses page), transaction (User created this by 
    converting a transaction from the Transactions page), system (Recurring expense 
    was created by the system on transaction import). Some older recurring expenses 
    may not have a source.
    """
    _plaid_account_id_description = """
    If any, denotes the plaid account associated with the creation of this "
    recurring expense (see Plaid Accounts)"
    """
    _asset_id_description = """
    If any, denotes the manually-managed account (i.e. asset) associated with the 
    creation of this recurring expense (see Assets)
    """
    _transaction_id_description = """
    If any, denotes the unique identifier for the associated transaction matching 
    this recurring expense for the current time period
    """
    _category_id_description = """
    If any, denotes the unique identifier for the associated category to this recurring expense
    """

    id: int = Field(description=_id_description)
    start_date: Optional[datetime.date] = Field(description=_start_date_description)
    end_date: Optional[datetime.date] = Field(description=_end_date_description)
    cadence: str = Field(description=_cadence_description)
    payee: str = Field(description="Payee of the recurring expense")
    amount: float = Field(description=_amount_description)
    currency: str = Field(max_length=3, description=_currency_description)
    description: Optional[str] = Field(description=_description_description)
    billing_date: datetime.date = Field(description=_billing_date_description)
    type: str = Field(description=_type_description)
    original_name: Optional[str] = Field(description=_original_name_description)
    source: str = Field(description=_source_description)
    plaid_account_id: Optional[int] = Field(description=_plaid_account_id_description)
    asset_id: Optional[int] = Field(description=_asset_id_description)
    transaction_id: Optional[int] = Field(description=_transaction_id_description)
    category_id: Optional[int] = Field(description=_category_id_description)


class RecurringExpenseParamsGet(BaseModel):
    """
    https://lunchmoney.dev/#get-recurring-expenses
    """

    start_date: datetime.date
    debit_as_negative: bool


class _LunchMoneyRecurringExpenses(LunchMoneyAPIClient):
    """
    Lunch Money Recurring Expenses Interactions
    """

    def get_recurring_expenses(self, start_date: Optional[datetime.date] = None,
                               debit_as_negative: bool = False) -> List[RecurringExpensesObject]:
        """
        Get Recurring Expenses

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

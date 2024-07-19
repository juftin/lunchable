"""
Lunch Money - Recurring Expenses

https://lunchmoney.dev/#recurring-expenses
"""

from __future__ import annotations

import datetime
import logging
from typing import Any, Dict, List, Optional

from pydantic import Field

from lunchable._config import APIConfig
from lunchable.models._base import LunchableModel
from lunchable.models._core import LunchMoneyAPIClient
from lunchable.models._descriptions import (
    _RecurringItemsDescriptions,
    _SummarizedTransactionDescriptions,
)

logger = logging.getLogger(__name__)


class SummarizedTransactionObject(LunchableModel):
    """
    Summarized Transaction Object
    """

    id: int = Field(description=_SummarizedTransactionDescriptions.id)
    date: datetime.date = Field(description=_SummarizedTransactionDescriptions.date)
    amount: float = Field(description=_SummarizedTransactionDescriptions.amount)
    currency: str = Field(
        max_length=3, description=_SummarizedTransactionDescriptions.currency
    )
    payee: str = Field(description=_SummarizedTransactionDescriptions.payee)
    category_id: Optional[int] = Field(
        None, description=_SummarizedTransactionDescriptions.category_id
    )
    recurring_id: Optional[int] = Field(
        None, description=_SummarizedTransactionDescriptions.recurring_id
    )
    to_base: float = Field(description=_SummarizedTransactionDescriptions.to_base)


class RecurringItemsObject(LunchableModel):
    """
    Recurring Expenses Object
    """

    id: int = Field(description=_RecurringItemsDescriptions.id)
    start_date: Optional[datetime.date] = Field(
        None, description=_RecurringItemsDescriptions.start_date
    )
    end_date: Optional[datetime.date] = Field(
        None, description=_RecurringItemsDescriptions.end_date
    )
    payee: str = Field(description=_RecurringItemsDescriptions.payee)
    currency: str = Field(
        max_length=3, description=_RecurringItemsDescriptions.currency
    )
    created_by: int = Field(description=_RecurringItemsDescriptions.created_by)
    created_at: datetime.datetime = Field(
        description=_RecurringItemsDescriptions.created_at
    )
    updated_at: datetime.datetime = Field(
        description=_RecurringItemsDescriptions.updated_at
    )
    billing_date: datetime.date = Field(
        description=_RecurringItemsDescriptions.billing_date
    )
    original_name: Optional[str] = Field(
        None, description=_RecurringItemsDescriptions.original_name
    )
    description: Optional[str] = Field(
        None, description=_RecurringItemsDescriptions.description
    )
    plaid_account_id: Optional[int] = Field(
        None, description=_RecurringItemsDescriptions.plaid_account_id
    )
    asset_id: Optional[int] = Field(
        None, description=_RecurringItemsDescriptions.asset_id
    )
    source: str = Field(description=_RecurringItemsDescriptions.source)
    notes: Optional[str] = Field(None, description=_RecurringItemsDescriptions.notes)
    amount: float = Field(description=_RecurringItemsDescriptions.amount)
    category_id: Optional[int] = Field(
        None, description=_RecurringItemsDescriptions.category_id
    )
    category_group_id: Optional[int] = Field(
        None, description=_RecurringItemsDescriptions.category_group_id
    )
    is_income: bool = Field(description=_RecurringItemsDescriptions.is_income)
    exclude_from_totals: bool = Field(
        description=_RecurringItemsDescriptions.exclude_from_totals
    )
    granularity: str = Field(description=_RecurringItemsDescriptions.granularity)
    cadence: Optional[str] = Field(None)
    quantity: Optional[int] = Field(
        None, description=_RecurringItemsDescriptions.quantity
    )
    occurrences: Dict[datetime.date, List[SummarizedTransactionObject]] = Field(
        description=_RecurringItemsDescriptions.occurrences
    )
    transactions_within_range: Optional[List[SummarizedTransactionObject]] = Field(
        None, description=_RecurringItemsDescriptions.transactions_within_range
    )
    missing_dates_within_range: Optional[List[Any]] = Field(
        None, description=_RecurringItemsDescriptions.missing_dates_within_range
    )
    date: Optional[datetime.date] = Field(
        None, description=_RecurringItemsDescriptions.date
    )
    to_base: float = Field(description=_RecurringItemsDescriptions.to_base)


class RecurringItemsParamsGet(LunchableModel):
    """
    https://lunchmoney.dev/#get-recurring-items
    """

    start_date: datetime.date
    debit_as_negative: Optional[bool] = None


class RecurringItemsClient(LunchMoneyAPIClient):
    """
    Lunch Money Recurring Items Interactions
    """

    def get_recurring_items(
        self,
        start_date: Optional[datetime.date] = None,
        debit_as_negative: Optional[bool] = None,
    ) -> List[RecurringItemsObject]:
        """
        Get Recurring Items

        Use this to retrieve a list of recurring items to expect for a specified month.

        A different set of recurring items is expected every month. These can be once a year,
        twice a year, every four months, etc.

        If a recurring item is listed as “twice a month,” then the recurring item object returned
        will have an occurrences attribute populated by the different billing dates the system believes
        recurring transactions should occur, including the two dates in the current month, the last
        transaction date prior to the month, and the next transaction date after the month.

        If the recurring item is listed as “once a week,” then the recurring item object returned will
        have an occurrences object populated with as many times as there are weeks for the specified
        month, along with the last transaction from the previous month and the next transaction for
        the next month.

        In the same vein, if a recurring item that began last month is set to “Every 3 months”,
        then that recurring item object that occurred will not include any dates for this month.

        Parameters
        ----------
        start_date : Optional[datetime.date]
            Date to search. Whatever your start date, the system will automatically
            return recurring items expected for that month. For instance, if you
            input 2020-01-25, the system will return recurring items which are to
            be expected between 2020-01-01 to 2020-01-31. By default will return
            the first day of the current month
        debit_as_negative: bool
            Pass in true if you'd like items to be returned as negative amounts
            and credits as positive amounts. Defaults to false.

        Returns
        -------
        List[RecurringItemsObject]
        """
        if start_date is None:
            start_date = datetime.datetime.now().date().replace(day=1)
        params = RecurringItemsParamsGet(
            start_date=start_date, debit_as_negative=debit_as_negative
        ).model_dump(exclude_none=True)
        response_data = self.make_request(
            method=self.Methods.GET,
            url_path=[APIConfig.LUNCH_MONEY_RECURRING_ITEMS],
            params=params,
        )
        recurring_expenses_objects = [
            RecurringItemsObject.model_validate(item) for item in response_data
        ]
        logger.debug(
            "%s RecurringExpensesObjects retrieved", len(recurring_expenses_objects)
        )
        return recurring_expenses_objects

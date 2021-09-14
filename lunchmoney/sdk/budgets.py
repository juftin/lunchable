# Author::    Justin Flannery  (mailto:juftin@juftin.com)

"""
Lunch Money - Budgets

https://lunchmoney.dev/#budget
"""

import datetime
import logging
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, validator

from lunchmoney.config import APIConfig
from lunchmoney.sdk.core import LunchMoneyCore

logger = logging.getLogger(__name__)


class BudgetDataObject(BaseModel):
    budget_amount: Optional[float]
    budget_currency: Optional[str]
    budget_to_base: Optional[float]
    spending_to_base: float = 0.00
    num_transactions: int = 0


class BudgetConfigObject(BaseModel):
    config_id: int
    cadence: str
    amount: Optional[float]
    currency: Optional[str]
    to_base: Optional[float]
    auto_suggest: str


class BudgetObject(BaseModel):
    category_name: str
    category_id: Optional[int]
    category_group_name: Optional[str]
    group_id: Optional[int]
    is_group: Optional[bool]
    is_income: bool
    exclude_from_budget: bool
    exclude_from_totals: bool
    data: Dict[datetime.date, BudgetDataObject]
    config: Optional[BudgetConfigObject]


class BudgetParamsGet(BaseModel):
    """
    https://lunchmoney.dev/#get-budget-summary
    """

    start_date: datetime.date
    end_date: datetime.date


class BudgetParamsPut(BaseModel):
    """
    https://lunchmoney.dev/#upsert-budget
    """

    start_date: datetime.date
    category_id: int
    amount: float
    currency: Optional[str]

    @validator("start_date")
    def result_check(cls, x):
        return str(x)


class BudgetParamsRemove(BaseModel):
    """
    https://lunchmoney.dev/#remove-budget
    """

    start_date: datetime.date
    category_id: int


class _LunchMoneyBudgets(LunchMoneyCore):
    """
    Lunch Money Budget Interactions
    """

    def get_budgets(self, start_date: datetime.date,
                    end_date: datetime.date) -> List[BudgetObject]:
        """
        Get full details on the budgets for all categories between a certain time
        period. The budgeted and spending amounts will be an aggregate across this
        time period. (https://lunchmoney.dev/#plaid-accounts-object)

        Returns
        -------
        List[BudgetObject]
        """
        params = BudgetParamsGet(start_date=start_date, end_date=end_date).dict()
        response_data = self._make_request(method="GET",
                                           url_path=[APIConfig.LUNCHMONEY_BUDGET],
                                           params=params)
        budget_objects = [BudgetObject(**item) for item in response_data]
        return budget_objects

    def upsert_budget(self,
                      start_date: datetime.date,
                      category_id: int,
                      amount: float,
                      currency: Optional[str] = None
                      ) -> Dict[str, Dict[str, Any]]:
        """
        Use this method to update an existing budget or insert a new budget for a particular
        category and date.

        Note: Lunch Money currently only supports monthly budgets, so your date must always be
        the start of a month (eg. 2021-04-01)

        If this is a sub-category, the response will include the updated category group's budget.
        This is because setting a sub-category may also update the category group's overall budget.

        Parameters
        ----------
        start_date : date
            Start date for the budget period. Lunch Money currently only supports monthly budgets,
            so your date must always be the start of a month (eg. 2021-04-01)
        category_id: int
            Unique identifier for the category
        amount: float
            Amount for budget
        currency: Optional[str]
            Currency for the budgeted amount (optional). If empty, will default to your primary
            currency

        Returns
        -------
        Dict[str, Dict[str, Any]]
        """
        body = BudgetParamsPut(start_date=start_date, category_id=category_id,
                               amount=amount, currency=currency).dict(exclude_none=True)
        response_data = self._make_request(method="PUT",
                                           url_path=[APIConfig.LUNCHMONEY_BUDGET],
                                           json=body)
        return response_data

    def remove_budget(self,
                      start_date: datetime.date,
                      category_id: int
                      ) -> bool:
        """
        Use this endpoint to unset an existing budget for a particular category in a
        particular month.

        Parameters
        ----------
        start_date : date
            Start date for the budget period. Lunch Money currently only supports monthly budgets,
            so your date must always be the start of a month (eg. 2021-04-01)
        category_id: int
            Unique identifier for the category

        Returns
        -------
        bool
        """
        params = BudgetParamsRemove(start_date=start_date, category_id=category_id).dict()
        response_data = self._make_request(method="DELETE",
                                           url_path=[APIConfig.LUNCHMONEY_BUDGET],
                                           params=params)
        return response_data

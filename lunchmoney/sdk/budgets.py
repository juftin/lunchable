# Author::    Justin Flannery  (mailto:juftin@juftin.com)

"""
Lunch Money - Budgets

https://lunchmoney.dev/#budget
"""

import datetime
import logging
from typing import Dict, List, Optional

from pydantic import BaseModel

from lunchmoney.config import APIConfig
from lunchmoney.sdk.core import LunchMoneyCore

logger = logging.getLogger(__name__)


class BudgetDataObject(BaseModel):
    budget_month: datetime.date
    budget_amount: Optional[float]
    budget_currency: Optional[str]
    budget_to_base: Optional[float]
    spending_to_base: float
    num_transactions: int


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


class BudgetParamsGet(BaseModel):
    """
    https://lunchmoney.dev/#get-budget-summary
    """

    start_date: datetime.date
    end_date: datetime.date


class LunchMoneyBudgets(LunchMoneyCore):
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

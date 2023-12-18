"""
Lunch Money - Budgets

https://lunchmoney.dev/#budget
"""

import datetime
import logging
from typing import Any, Dict, List, Optional

from pydantic import Field

from lunchable._config import APIConfig
from lunchable.models._base import LunchableModel
from lunchable.models._core import LunchMoneyAPIClient
from lunchable.models._descriptions import _BudgetDescriptions

logger = logging.getLogger(__name__)


class BudgetDataObject(LunchableModel):
    """
    Data Object within a Budget
    """

    budget_amount: Optional[float] = None
    budget_currency: Optional[str] = None
    budget_to_base: Optional[float] = None
    spending_to_base: float = 0.00
    num_transactions: int = 0


class BudgetConfigObject(LunchableModel):
    """
    Budget Configuration Object
    """

    config_id: int
    cadence: str
    amount: Optional[float] = None
    currency: Optional[str] = None
    to_base: Optional[float] = None
    auto_suggest: str


class BudgetObject(LunchableModel):
    """
    Monthly Budget Per Category Object

    https://lunchmoney.dev/#budget-object
    """

    category_name: str = Field(description="Name of the category")
    category_id: Optional[int] = Field(
        None, description="Unique identifier for category"
    )
    category_group_name: Optional[str] = Field(
        None, description=_BudgetDescriptions.category_group_name
    )
    group_id: Optional[int] = Field(
        None, description="Unique identifier for category group"
    )
    is_group: Optional[bool] = Field(
        None, description="If true, this category is a group"
    )
    is_income: bool = Field(description=_BudgetDescriptions.is_income)
    exclude_from_budget: bool = Field(
        description=_BudgetDescriptions.exclude_from_budget
    )
    exclude_from_totals: bool = Field(
        description=_BudgetDescriptions.exclude_from_totals
    )
    data: Dict[datetime.date, BudgetDataObject] = Field(
        description=_BudgetDescriptions.data
    )
    config: Optional[BudgetConfigObject] = Field(
        None, description=_BudgetDescriptions.config
    )


class BudgetParamsGet(LunchableModel):
    """
    https://lunchmoney.dev/#get-budget-summary
    """

    start_date: datetime.date
    end_date: datetime.date


class BudgetParamsPut(LunchableModel):
    """
    https://lunchmoney.dev/#upsert-budget
    """

    start_date: datetime.date
    category_id: int
    amount: float
    currency: Optional[str] = None


class BudgetParamsRemove(LunchableModel):
    """
    https://lunchmoney.dev/#remove-budget
    """

    start_date: datetime.date
    category_id: int


class BudgetsClient(LunchMoneyAPIClient):
    """
    Lunch Money Budget Interactions
    """

    def get_budgets(
        self, start_date: datetime.date, end_date: datetime.date
    ) -> List[BudgetObject]:
        """
        Get Monthly Budgets

        Get full details on the budgets for all categories between a certain time
        period. The budgeted and spending amounts will be an aggregate across this
        time period. (https://lunchmoney.dev/#plaid-accounts-object)

        Returns
        -------
        List[BudgetObject]
        """
        params = BudgetParamsGet(start_date=start_date, end_date=end_date).model_dump()
        response_data = self.make_request(
            method=self.Methods.GET,
            url_path=[APIConfig.LUNCHMONEY_BUDGET],
            params=params,
        )
        budget_objects = [BudgetObject.model_validate(item) for item in response_data]
        return budget_objects

    def upsert_budget(
        self,
        start_date: datetime.date,
        category_id: int,
        amount: float,
        currency: Optional[str] = None,
    ) -> Optional[Dict[str, Any]]:
        """
        Upsert a Budget for a Category and Date

        Use this endpoint to update an existing budget or insert a new budget for
        a particular category and date.

        Note: Lunch Money currently only supports monthly budgets, so your date must
        always be the start of a month (eg. 2021-04-01)

        If this is a sub-category, the response will include the updated category
        group's budget. This is because setting a sub-category may also update
        the category group's overall budget.

        https://lunchmoney.dev/#upsert-budget

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
        Optional[Dict[str, Any]]
        """
        body = BudgetParamsPut(
            start_date=start_date,
            category_id=category_id,
            amount=amount,
            currency=currency,
        ).model_dump(exclude_none=True)
        response_data = self.make_request(
            method=self.Methods.PUT,
            url_path=[APIConfig.LUNCHMONEY_BUDGET],
            payload=body,
        )

        return response_data["category_group"]

    def remove_budget(self, start_date: datetime.date, category_id: int) -> bool:
        """
        Unset an Existing Budget for a Particular Category in a Particular Month

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
        params = BudgetParamsRemove(
            start_date=start_date, category_id=category_id
        ).model_dump()
        response_data = self.make_request(
            method=self.Methods.DELETE,
            url_path=[APIConfig.LUNCHMONEY_BUDGET],
            params=params,
        )
        return response_data

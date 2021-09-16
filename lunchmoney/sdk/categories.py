"""
Lunch Money - Categories

https://lunchmoney.dev/#categories
"""

import datetime
import logging
from typing import List, Optional

from pydantic import BaseModel

from lunchmoney.config import APIConfig
from lunchmoney.sdk._core import LunchMoneyAPIClient

logger = logging.getLogger(__name__)


class ModelCreateCategory(BaseModel):
    """
    https://lunchmoney.dev/#create-category
    """

    name: str
    description: Optional[str]
    is_income: Optional[bool] = False
    exclude_from_budget: Optional[bool] = False
    exclude_from_totals: Optional[bool] = False


class CategoriesObject(BaseModel):
    """
    https://lunchmoney.dev/#categories-object
    """

    id: int
    name: str
    description: Optional[str]
    is_income: str
    exclude_from_budget: bool
    exclude_from_totals: bool
    updated_at: datetime.datetime
    created_at: datetime.datetime
    is_group: bool
    group_id: Optional[int]


class _LunchMoneyCategories(LunchMoneyAPIClient):
    """
    Lunch Money Categories Interactions
    """

    def get_categories(self) -> List[CategoriesObject]:
        """
        Get all categories

        Use this endpoint to get a list of all categories associated with the user's account.
        https://lunchmoney.dev/#get-all-categories

        Returns
        -------
        List[CategoriesObject]
        """
        response_data = self._make_request(method=self.methods.GET,
                                           url_path=APIConfig.LUNCHMONEY_CATEGORIES)
        categories = response_data["categories"]
        budget_objects = [CategoriesObject(**item) for item in categories]
        return budget_objects

    def create_category(self, name: str,
                        description: Optional[str] = None,
                        is_income: Optional[bool] = False,
                        exclude_from_budget: Optional[bool] = False,
                        exclude_from_totals: Optional[bool] = False) -> int:
        """
        Create Category

        Use this to create a single category
        https://lunchmoney.dev/#create-category

        Parameters
        ----------
        name: str
            Name of category. Must be between 1 and 40 characters.
        description: Optional[str]
            Description of category. Must be less than 140 categories. Defaults to None.
        is_income: Optional[bool]
            Whether or not transactions in this category should be treated as income.
            Defaults to False.
        exclude_from_budget: Optional[bool]
            Whether or not transactions in this category should be excluded from budgets.
            Defaults to False.
        exclude_from_totals: Optional[bool]
            Whether or not transactions in this category should be excluded from
            calculated totals. Defaults to False.

        Returns
        -------
        int
            ID of the newly created category
        """

        category_body = ModelCreateCategory(
            name=name,
            description=description,
            is_income=is_income,
            exclude_from_budget=exclude_from_budget,
            exclude_from_totals=exclude_from_totals).dict(exclude_none=True)
        response_data = self._make_request(method=self.methods.POST,
                                           url_path=APIConfig.LUNCHMONEY_CATEGORIES,
                                           payload=category_body)
        return response_data["category_id"]

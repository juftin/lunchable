"""
Lunch Money - Categories

https://lunchmoney.dev/#categories
"""

import datetime
import logging
from typing import List, Optional

from pydantic import BaseModel, Field

from lunchable._config import APIConfig
from lunchable.models._core import LunchMoneyAPIClient

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
    Lunch Money Spending Categories

    https://lunchmoney.dev/#categories-object
    """

    _name_description = "The name of the category. Must be between 1 and 40 characters."
    _description_description = "The description of the category. Must not exceed 140 characters."
    _is_income_description = "If true, the transactions in this category will be treated as income."
    _exclude_from_budget_description = """
    If true, the transactions in this category will be excluded from the budget.
    """
    _exclude_from_totals_description = """
    If true, the transactions in this category will be excluded from totals.
    """
    _updated_at_description = """
    The date and time of when the category was last updated (in the ISO 8601 extended format).
    """
    _created_at_description = """
    The date and time of when the category was created (in the ISO 8601 extended format).
    """
    _is_group_description = """
    If true, the category is a group that can be a parent to other categories.
    """
    _group_id_description = """
    The ID of a category group (or null if the category doesn't belong to a category group).
    """

    id: int = Field(description="A unique identifier for the category.")
    name: str = Field(min_length=1, max_length=40, description=_name_description)
    description: Optional[str] = Field(max_length=140, description=_description_description)
    is_income: str = Field(description=_is_income_description)
    exclude_from_budget: bool = Field(description=_exclude_from_budget_description)
    exclude_from_totals: bool = Field(description=_exclude_from_totals_description)
    updated_at: datetime.datetime = Field(description=_updated_at_description)
    created_at: datetime.datetime = Field(description=_created_at_description)
    is_group: bool = Field(description=_is_group_description)
    group_id: Optional[int] = Field(description=_group_id_description)


class _LunchMoneyCategories(LunchMoneyAPIClient):
    """
    Lunch Money Categories Interactions
    """

    def get_categories(self) -> List[CategoriesObject]:
        """
        Get Spending categories

        Use this endpoint to get a list of all categories associated with the user's account.
        https://lunchmoney.dev/#get-all-categories

        Returns
        -------
        List[CategoriesObject]
        """
        response_data = self._make_request(method=self.Methods.GET,
                                           url_path=APIConfig.LUNCHMONEY_CATEGORIES)
        categories = response_data["categories"]
        budget_objects = [CategoriesObject(**item) for item in categories]
        return budget_objects

    def insert_category(self, name: str,
                        description: Optional[str] = None,
                        is_income: Optional[bool] = False,
                        exclude_from_budget: Optional[bool] = False,
                        exclude_from_totals: Optional[bool] = False) -> int:
        """
        Create a Spending Category

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
        response_data = self._make_request(method=self.Methods.POST,
                                           url_path=APIConfig.LUNCHMONEY_CATEGORIES,
                                           payload=category_body)
        return response_data["category_id"]

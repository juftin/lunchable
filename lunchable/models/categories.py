"""
Lunch Money - Categories

https://lunchmoney.dev/#categories
"""

import datetime
import json
import logging
from typing import List, Optional

from pydantic import Field

from lunchable._config import APIConfig
from lunchable.exceptions import LunchMoneyError
from lunchable.models._base import LunchableModel
from lunchable.models._core import LunchMoneyAPIClient

logger = logging.getLogger(__name__)


class ModelCreateCategory(LunchableModel):
    """
    https://lunchmoney.dev/#create-category
    """

    name: str
    description: Optional[str]
    is_income: Optional[bool] = False
    exclude_from_budget: Optional[bool] = False
    exclude_from_totals: Optional[bool] = False


class CategoryChild(LunchableModel):
    """
    Child Entry on the Category Object
    """

    id: int
    name: str = Field(min_length=1, max_length=40)
    description: Optional[str] = Field(max_length=140)
    created_at: Optional[datetime.datetime]


class CategoriesObject(LunchableModel):
    """
    Lunch Money Spending Categories

    https://lunchmoney.dev/#categories-object
    """

    _name_description = "The name of the category. Must be between 1 and 40 characters."
    _description_description = (
        "The description of the category. Must not exceed 140 characters."
    )
    _is_income_description = (
        "If true, the transactions in this category will be treated as income."
    )
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
    _children_description = (
        "For category groups, this will populate with the "
        "categories nested within and include id, name, "
        "description and created_at fields."
    )

    id: int = Field(description="A unique identifier for the category.")
    name: str = Field(min_length=1, max_length=40, description=_name_description)
    description: Optional[str] = Field(
        max_length=140, description=_description_description
    )
    is_income: str = Field(description=_is_income_description)
    exclude_from_budget: bool = Field(description=_exclude_from_budget_description)
    exclude_from_totals: bool = Field(description=_exclude_from_totals_description)
    updated_at: Optional[datetime.datetime] = Field(description=_updated_at_description)
    created_at: Optional[datetime.datetime] = Field(description=_created_at_description)
    is_group: bool = Field(description=_is_group_description)
    group_id: Optional[int] = Field(description=_group_id_description)
    children: Optional[List[CategoryChild]] = Field(description=_children_description)


class _CategoriesParamsPut(LunchableModel):
    """
    https://lunchmoney.dev/#update-category
    """

    name: Optional[str] = Field(min_length=1, max_length=40)
    description: Optional[str] = Field(max_length=140)
    is_income: Optional[bool]
    exclude_from_budget: Optional[bool]
    exclude_from_totals: Optional[bool]
    group_id: Optional[int]


class _CategoriesParamsPost(LunchableModel):
    """
    https://lunchmoney.dev/#create-category-group
    """

    name: str
    description: Optional[str]
    is_income: Optional[bool] = False
    exclude_from_budget: Optional[bool] = False
    exclude_from_totals: Optional[bool] = False
    category_ids: Optional[List[int]]
    new_categories: Optional[List[str]]


class _CategoriesAddParamsPost(LunchableModel):
    """
    https://lunchmoney.dev/#add-to-category-group
    """

    category_ids: Optional[List[int]]
    new_categories: Optional[List[str]]


class CategoriesClient(LunchMoneyAPIClient):
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
        response_data = self._make_request(
            method=self.Methods.GET, url_path=APIConfig.LUNCHMONEY_CATEGORIES
        )
        categories = response_data["categories"]
        category_objects = [CategoriesObject(**item) for item in categories]
        return category_objects

    def insert_category(
        self,
        name: str,
        description: Optional[str] = None,
        is_income: Optional[bool] = False,
        exclude_from_budget: Optional[bool] = False,
        exclude_from_totals: Optional[bool] = False,
    ) -> int:
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
            exclude_from_totals=exclude_from_totals,
        ).dict(exclude_none=True)
        response_data = self._make_request(
            method=self.Methods.POST,
            url_path=APIConfig.LUNCHMONEY_CATEGORIES,
            payload=category_body,
        )
        return response_data["category_id"]

    def get_category(self, category_id: int) -> CategoriesObject:
        """
        Get single category

        Use this endpoint to get hydrated details on a single category. Note that if
        this category is part of a category group, its properties (is_income,
        exclude_from_budget, exclude_from_totals) will inherit from the category group.

        https://lunchmoney.dev/#get-single-category

        Parameters
        ----------
        category_id : int
            Id of the Lunch Money Category

        Returns
        -------
        CategoriesObject
        """
        response_data = self._make_request(
            method=self.Methods.GET,
            url_path=[APIConfig.LUNCHMONEY_CATEGORIES, category_id],
        )
        return CategoriesObject(**response_data)

    def remove_category(self, category_id: int) -> bool:
        """
        Delete a single category

        Use this endpoint to delete a single category or category group. This will
        only work if there are no dependencies, such as existing budgets for the
        category, categorized transactions, categorized recurring items, etc. If
        there are dependents, this endpoint will return what the dependents are
        and how many there are.

        https://lunchmoney.dev/#delete-category

        Parameters
        ----------
        category_id : int
            Id of the Lunch Money Category

        Returns
        -------
        bool
        """
        response_data = self._make_request(
            method=self.Methods.DELETE,
            url_path=[APIConfig.LUNCHMONEY_CATEGORIES, category_id],
        )
        if response_data is not True:
            raise LunchMoneyError(
                f"That Category ({category_id}) has Dependents: "
                f"{json.dumps(response_data, indent=4)}"
            )
        return response_data

    def remove_category_force(self, category_id: int) -> bool:
        """
        Forcefully delete a single category

        Use this endpoint to force delete a single category or category group and
        along with it, disassociate the category from any transactions, recurring
        items, budgets, etc.

        Note: it is best practice to first try the Delete Category endpoint to ensure
        you don't accidentally delete any data. Disassociation/deletion of the data
        arising from this endpoint is irreversible!

        https://lunchmoney.dev/#force-delete-category

        Parameters
        ----------
        category_id : int
            Id of the Lunch Money Category

        Returns
        -------
        bool
        """
        response_data = self._make_request(
            method=self.Methods.DELETE,
            url_path=[APIConfig.LUNCHMONEY_CATEGORIES, category_id, "force"],
        )
        return response_data

    def update_category(
        self,
        category_id: int,
        name: Optional[str] = None,
        description: Optional[str] = None,
        is_income: Optional[bool] = None,
        exclude_from_budget: Optional[bool] = None,
        exclude_from_totals: Optional[bool] = None,
        group_id: Optional[int] = None,
    ) -> bool:
        """
        Update a single category

        Use this endpoint to update the properties for a single category or category group

        https://lunchmoney.dev/#update-category

        Parameters
        ----------
        category_id : int
            Id of the Lunch Money Category
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
        group_id: Optional[int]
            For a category, set the group_id to include it in a category group

        Returns
        -------
        bool
        """
        payload = _CategoriesParamsPut(
            name=name,
            description=description,
            is_income=is_income,
            exclude_from_budget=exclude_from_budget,
            exclude_from_totals=exclude_from_totals,
            group_id=group_id,
        ).dict(exclude_none=True)
        response_data = self._make_request(
            method=self.Methods.PUT,
            url_path=[APIConfig.LUNCHMONEY_CATEGORIES, category_id],
            payload=payload,
        )
        return response_data

    def insert_category_group(
        self,
        name: str,
        description: Optional[str] = None,
        is_income: Optional[bool] = False,
        exclude_from_budget: Optional[bool] = False,
        exclude_from_totals: Optional[bool] = False,
        category_ids: Optional[List[int]] = None,
        new_categories: Optional[List[str]] = None,
    ) -> int:
        """
        Create a Spending Category Group

        Use this endpoint to create a single category group
        https://lunchmoney.dev/#create-category-group

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
        category_ids: Optional[List[int]]
            Array of category_id to include in the category group.
        new_categories: Optional[List[str]]
            Array of strings representing new categories to create and subsequently
            include in the category group.

        Returns
        -------
        int
            ID of the newly created category group
        """
        payload = _CategoriesParamsPost(
            name=name,
            description=description,
            is_income=is_income,
            exclude_from_budget=exclude_from_budget,
            exclude_from_totals=exclude_from_totals,
            category_ids=category_ids,
            new_categories=new_categories,
        ).dict(exclude_none=True)
        response_data = self._make_request(
            method=self.Methods.POST,
            url_path=[APIConfig.LUNCHMONEY_CATEGORIES, "group"],
            payload=payload,
        )
        return response_data["category_id"]

    def insert_into_category_group(
        self,
        category_group_id: int,
        category_ids: Optional[List[int]] = None,
        new_categories: Optional[List[str]] = None,
    ) -> CategoriesObject:
        """
        Add to a Category Group

        Use this endpoint to add categories (either existing or new) to a single
        category group

        https://lunchmoney.dev/#add-to-category-group

        Parameters
        ----------
        category_group_id: int
            Id of the Lunch Money Category Group
        category_ids: Optional[List[int]]
            Array of category_id to include in the category group.
        new_categories: Optional[List[str]]
            Array of strings representing new categories to create and subsequently
            include in the category group.

        Returns
        -------
        CategoriesObject
        """
        payload = _CategoriesAddParamsPost(
            category_ids=category_ids, new_categories=new_categories
        ).dict(exclude_none=True)
        response_data = self._make_request(
            method=self.Methods.POST,
            url_path=[
                APIConfig.LUNCHMONEY_CATEGORIES,
                "group",
                category_group_id,
                "add",
            ],
            payload=payload,
        )
        return CategoriesObject(**response_data)

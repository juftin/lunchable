"""
Lunch Money - Categories

https://lunchmoney.dev/#categories
"""

import datetime
import logging
from typing import List, Optional

from pydantic import BaseModel

from lunchmoney.config import APIConfig
from lunchmoney.sdk._core import LunchMoneyCore

logger = logging.getLogger(__name__)


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


class _LunchMoneyCategories(LunchMoneyCore):
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
        response_data = self._make_request(method="GET",
                                           url_path=[APIConfig.LUNCHMONEY_CATEGORIES])
        categories = response_data["categories"]
        budget_objects = [CategoriesObject(**item) for item in categories]
        return budget_objects

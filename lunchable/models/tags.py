"""
Lunch Money - Tags

https://lunchmoney.dev/#tags
"""

import logging
from typing import List, Optional

from pydantic import BaseModel, Field

from lunchable._config import APIConfig
from lunchable.models._core import LunchMoneyAPIClient

logger = logging.getLogger(__name__)


class TagsObject(BaseModel):
    """
    Lunchmoney Tags object

    https://lunchmoney.dev/#tags-object
    """

    id: int = Field(description="Unique identifier for tag")
    name: str = Field(description="User-defined name of tag", min_length=1)
    description: Optional[str] = Field(description="User-defined description of tag")


class _LunchMoneyTags(LunchMoneyAPIClient):
    """
    Lunch Money Tag Interactions
    """

    def get_tags(self) -> List[TagsObject]:
        """
        Get Spending Tags

        Use this endpoint to get a list of all tags associated with the
        user's account.

        https://lunchmoney.dev/#get-all-tags

        Returns
        -------
        List[TagsObject]
        """
        response_data = self._make_request(method=self.Methods.GET,
                                           url_path=APIConfig.LUNCHMONEY_TAGS)
        tag_objects = [TagsObject(**item) for item in response_data]
        return tag_objects

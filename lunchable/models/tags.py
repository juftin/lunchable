"""
Lunch Money - Tags

https://lunchmoney.dev/#tags
"""

import logging
from typing import List, Optional

from pydantic import BaseModel, Field, validator

from lunchable.config import APIConfig
from lunchable.models._core import LunchMoneyAPIClient

logger = logging.getLogger(__name__)


class TagsObject(BaseModel):
    """
    Lunchmoney Tags object

    https://lunchmoney.dev/#tags-object
    """

    id: int = Field(description="Unique identifier for tag")
    name: str = Field(description="User-defined name of tag")
    description: Optional[str] = Field(description="User-defined description of tag")

    @validator("name", pre=True)
    def none_str(cls, v):
        """
        Convert None to Empty Str
        """
        if v is None:
            return ""
        else:
            return v


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
        response_data = self._make_request(method=self.methods.GET,
                                           url_path=APIConfig.LUNCHMONEY_TAGS)
        tag_objects = [TagsObject(**item) for item in response_data]
        return tag_objects

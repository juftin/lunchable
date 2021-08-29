# Author::    Justin Flannery  (mailto:juftin@juftin.com)

"""
Lunch Money - Assets

https://lunchmoney.dev/#assets
"""

import datetime
import logging
from typing import List, Optional

from pydantic import BaseModel

from lunchmoney.config import APIConfig
from lunchmoney.sdk.core import LunchMoneyCore

logger = logging.getLogger(__name__)


class AssetsObject(BaseModel):
    """
    https://lunchmoney.dev/#assets-object
    """
    id: int
    type_name: str
    subtype_name: str
    name: str
    display_name: str
    balance: float
    balance_as_of: datetime.datetime
    closed_on: Optional[datetime.date]
    currency: str
    institution_name: str
    created_at: datetime.datetime


class LunchMoneyAssets(LunchMoneyCore):
    """
    Lunch Money Assets Interactions
    """

    def get_assets(self) -> List[AssetsObject]:
        """
        Get a list of all manually-managed assets associated with the user's account.

        (https://lunchmoney.dev/#assets-object)

        Returns
        -------
        List[AssetsObject]
        """
        response_data = self._make_request(method="GET",
                                           url_path=[APIConfig.LUNCHMONEY_ASSETS])
        assets = response_data.get(APIConfig.LUNCHMONEY_ASSETS)
        asset_objects = [AssetsObject(**item) for item in assets]
        return asset_objects

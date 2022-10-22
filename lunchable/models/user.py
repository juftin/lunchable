"""
Lunch Money - User

https://lunchmoney.dev/#user
"""

import logging
from typing import Optional

from pydantic import Field

from lunchable._config import APIConfig
from lunchable.models._base import LunchableModel
from lunchable.models._core import LunchMoneyAPIClient

logger = logging.getLogger(__name__)


class UserObject(LunchableModel):
    """
    The LunchMoney `User` object

    https://lunchmoney.dev/#user-object
    """

    user_id: int = Field(description="Unique identifier for user")
    user_name: str = Field(description="User's' name")
    user_email: str = Field(description="User's' Email")
    account_id: int = Field(
        description="Unique identifier for the associated budgeting account"
    )
    budget_name: str = Field(description="Name of the associated budgeting account")
    api_key_label: Optional[str] = Field(
        description="User-defined label of the developer API key used. "
        "Returns null if nothing has been set."
    )


class UserClient(LunchMoneyAPIClient):
    """
    Lunch Money Interactions for Non Finance Operations
    """

    def get_user(self) -> UserObject:
        """
        Get Personal User Details

        Use this endpoint to get details on the current user.

        https://lunchmoney.dev/#get-user

        Returns
        -------
        UserObject
        """
        response_data = self._make_request(
            method=self.Methods.GET, url_path=APIConfig.LUNCHMONEY_ME
        )
        me = UserObject(**response_data)
        return me

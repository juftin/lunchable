"""
Lunch Money - Plaid Accounts

https://lunchmoney.dev/#plaid-accounts
"""

import datetime
import logging
from typing import List, Optional

from pydantic import Field

from lunchable._config import APIConfig
from lunchable.models._base import LunchableModel
from lunchable.models._core import LunchMoneyAPIClient
from lunchable.models._descriptions import _PlaidAccountDescriptions

logger = logging.getLogger(__name__)


class PlaidAccountObject(LunchableModel):
    """
    Assets synced from Plaid

    Similar to AssetObjects, these accounts are linked to remote sources in Plaid.

    https://lunchmoney.dev/#plaid-accounts-object
    """

    id: int = Field(description="Unique identifier of Plaid account")
    date_linked: datetime.date = Field(
        description=_PlaidAccountDescriptions.date_linked
    )
    name: str = Field(description=_PlaidAccountDescriptions.name)
    type: str = Field(description=_PlaidAccountDescriptions.type)
    subtype: str = Field(description=_PlaidAccountDescriptions.subtype)
    mask: Optional[str] = Field(None, description=_PlaidAccountDescriptions.mask)
    institution_name: str = Field(
        description=_PlaidAccountDescriptions.institution_name
    )
    status: str = Field(description=_PlaidAccountDescriptions.status)
    last_import: Optional[datetime.datetime] = Field(
        None, description=_PlaidAccountDescriptions.last_import
    )
    balance: Optional[float] = Field(
        None, description=_PlaidAccountDescriptions.balance
    )
    currency: str = Field(description=_PlaidAccountDescriptions.currency)
    balance_last_update: datetime.datetime = Field(
        description=_PlaidAccountDescriptions.balance_last_update
    )
    limit: Optional[int] = Field(None, description=_PlaidAccountDescriptions.limit)


class PlaidAccountsClient(LunchMoneyAPIClient):
    """
    Lunch Money Plaid Accounts Interactions
    """

    def get_plaid_accounts(self) -> List[PlaidAccountObject]:
        """
        Get Plaid Synced Assets

        Get a list of all synced Plaid accounts associated with the user's account.

        Plaid Accounts are individual bank accounts that you have linked to Lunch Money via Plaid.
        You may link one bank but one bank might contain 4 accounts. Each of these
        accounts is a Plaid Account. (https://lunchmoney.dev/#plaid-accounts-object)

        Returns
        -------
        List[PlaidAccountObject]
        """
        response_data = self.make_request(
            method=self.Methods.GET, url_path=APIConfig.LUNCHMONEY_PLAID_ACCOUNTS
        )
        accounts = response_data.get(APIConfig.LUNCHMONEY_PLAID_ACCOUNTS)
        account_objects = [PlaidAccountObject.model_validate(item) for item in accounts]
        return account_objects

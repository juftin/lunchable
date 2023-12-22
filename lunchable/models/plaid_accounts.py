"""
Lunch Money - Plaid Accounts

https://lunchmoney.dev/#plaid-accounts
"""

from __future__ import annotations

import datetime
import logging
from typing import List, Optional

from pydantic import Field

from lunchable._config import APIConfig
from lunchable.models._base import LunchableModel
from lunchable.models._core import LunchMoneyAPIClient
from lunchable.models._descriptions import _PlaidAccountDescriptions

logger = logging.getLogger(__name__)


class _PlaidFetchRequest(LunchableModel):
    """
    Trigger Fetch from Plaid

    https://lunchmoney.dev/#trigger-fetch-from-plaid
    """

    start_date: Optional[datetime.date] = None
    end_date: Optional[datetime.date] = None
    plaid_account_id: Optional[int] = None


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

    def trigger_fetch_from_plaid(
        self,
        start_date: Optional[datetime.date] = None,
        end_date: Optional[datetime.date] = None,
        plaid_account_id: Optional[int] = None,
    ) -> bool:
        """
        Trigger Fetch from Plaid

        ** This is an experimental endpoint and parameters and/or response may change. **

        Use this endpoint to trigger a fetch for latest data from Plaid.

        Returns true if there were eligible Plaid accounts to trigger a fetch for. Eligible
        accounts are those who last_fetch value is over 1 minute ago. (Although the limit
        is every minute, please use this endpoint sparingly!)

        Note that fetching from Plaid is a background job. This endpoint simply queues up
        the job. You may track the plaid_last_successful_update, last_fetch and last_import
        properties to verify the results of the fetch.

        Parameters
        ----------
        start_date: Optional[datetime.date]
            Start date for fetch (ignored if end_date is null)
        end_date: Optional[datetime.date]
            End date for fetch (ignored if start_date is null)
        plaid_account_id: Optional[int]
            Specific ID of a plaid account to fetch. If left empty,
            endpoint will trigger a fetch for all eligible accounts

        Returns
        -------
        bool
            Returns true if there were eligible Plaid accounts to trigger a fetch for.
        """
        fetch_request = _PlaidFetchRequest(
            start_date=start_date, end_date=end_date, plaid_account_id=plaid_account_id
        )
        response: bool = self.make_request(
            method=self.Methods.POST,
            url_path=[APIConfig.LUNCHMONEY_PLAID_ACCOUNTS, "fetch"],
            data=fetch_request.model_dump(exclude_none=True),
        )
        return response

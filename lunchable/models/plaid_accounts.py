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

logger = logging.getLogger(__name__)


class PlaidAccountObject(LunchableModel):
    """
    Assets synced from Plaid

    Similar to AssetObjects, these accounts are linked to remote sources in Plaid.

    https://lunchmoney.dev/#plaid-accounts-object
    """

    _date_linked_description = (
        "Date account was first linked in ISO 8601 extended format"
    )
    _name_description = """
    Name of the account. Can be overridden by the user. Field is originally set by Plaid")
    """
    _type_description = """
    Primary type of account. Typically one of: [credit, depository, brokerage, cash,
    loan, investment]. This field is set by Plaid and cannot be altered.
    """
    _subtype_description = """
    Optional subtype name of account. This field is set by Plaid and cannot be altered
    """
    _mask_description = """
    Mask (last 3 to 4 digits of account) of account. This field is set by
    Plaid and cannot be altered
    """
    _institution_name_description = """
    Name of institution associated with account. This field is set by
    Plaid and cannot be altered
    """
    _status_description = """
    Denotes the current status of the account within Lunch Money. Must be one of:
    active (Account is active and in good state),
    inactive (Account marked inactive from user. No transactions fetched or
    balance update for this account),
    relink (Account needs to be relinked with Plaid),
    syncing (Account is awaiting first import of transactions),
    error (Account is in error with Plaid),
    not found (Account is in error with Plaid),
    not supported (Account is in error with Plaid)
    """
    _last_import_description = """
    Date of last imported transaction in ISO 8601 extended format (not necessarily
    date of last attempted import)
    """
    _balance_description = """
    Current balance of the account in numeric format to 4 decimal places. This field is
    set by Plaid and cannot be altered
    """
    _currency_description = """
    Currency of account balance in ISO 4217 format. This field is set by Plaid
    and cannot be altered
    """
    _balance_last_update_description = """
    Date balance was last updated in ISO 8601 extended format. This field is set
    by Plaid and cannot be altered
    """
    _limit_description = """
    Optional credit limit of the account. This field is set by Plaid and cannot be altered
    """

    id: int = Field(description="Unique identifier of Plaid account")
    date_linked: datetime.date = Field(description=_date_linked_description)
    name: str = Field(description=_name_description)
    type: str = Field(description=_type_description)
    subtype: str = Field(description=_subtype_description)
    mask: str = Field(description=_mask_description)
    institution_name: str = Field(description=_institution_name_description)
    status: str = Field(description=_status_description)
    last_import: Optional[datetime.datetime] = Field(
        description=_last_import_description
    )
    balance: Optional[float] = Field(description=_balance_description)
    currency: str = Field(description=_currency_description)
    balance_last_update: datetime.datetime = Field(
        description=_balance_last_update_description
    )
    limit: Optional[int] = Field(description=_limit_description)


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
        response_data = self._make_request(
            method=self.Methods.GET, url_path=APIConfig.LUNCHMONEY_PLAID_ACCOUNTS
        )
        accounts = response_data.get(APIConfig.LUNCHMONEY_PLAID_ACCOUNTS)
        account_objects = [PlaidAccountObject(**item) for item in accounts]
        return account_objects

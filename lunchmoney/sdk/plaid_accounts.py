# Author::    Justin Flannery  (mailto:juftin@juftin.com)

"""
Lunch Money - Plaid Accounts

https://lunchmoney.dev/#plaid-accounts
"""
import datetime
import logging
from typing import List, Optional

from pydantic import BaseModel

from lunchmoney.config import APIConfig
from lunchmoney.sdk.core import LunchMoneyCore

logger = logging.getLogger(__name__)


class RecurringExpenseObject(BaseModel):
    id: int
    start_date: datetime.datetime
    end_date: datetime.datetime
    cadence: str
    payee: str
    amount: float
    currency: str
    description: str
    billing_date: datetime.datetime
    type: str
    original_name: str
    source: str
    plaid_account_id: int
    asset_id: int
    transaction_id: int
    category_id: int


class PlaidAccountObject(BaseModel):
    id: int
    date_linked: datetime.date
    name: str
    type: str
    subtype: str
    mask: str
    institution_name: str
    status: str
    last_import: Optional[datetime.datetime]
    balance: float
    currency: str
    balance_last_update: datetime.datetime
    limit: Optional[int]


class LunchMoneyPlaidAccounts(LunchMoneyCore):
    """
    Lunch Money Plaid Accounts Interactions
    """

    def get_plaid_accounts(self) -> List[PlaidAccountObject]:
        """
        Get a list of all synced Plaid accounts associated with the user's account.

        Plaid Accounts are individual bank accounts that you have linked to Lunch Money via Plaid.
        You may link one bank but one bank might contain 4 accounts. Each of these
        accounts is a Plaid Account. (https://lunchmoney.dev/#plaid-accounts-object)

        Returns
        -------
        List[PlaidAccountObject]
        """
        response_data = self._make_request(method="GET",
                                           url_path=[APIConfig.LUNCHMONEY_PLAID_ACCOUNTS])
        accounts = response_data.get(APIConfig.LUNCHMONEY_PLAID_ACCOUNTS)
        account_objects = [PlaidAccountObject(**item) for item in accounts]
        return account_objects

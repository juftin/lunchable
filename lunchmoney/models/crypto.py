"""
Lunch Money - Crypto

https://lunchmoney.dev/#crypto
"""
import datetime
import logging
from typing import List, Optional

from pydantic import BaseModel

from lunchmoney.config import APIConfig
from lunchmoney.models._core import LunchMoneyAPIClient

logger = logging.getLogger(__name__)


class CryptoObject(BaseModel):
    """
    Lunchmoney Crypto object

    https://lunchmoney.dev/#crypto-object
    """

    id: int
    zabo_account_id: Optional[int]
    source: str
    name: str
    display_name: Optional[str]
    balance: float
    balance_as_of: datetime.datetime
    status: str
    institution_name: str
    created_at: datetime.datetime


class _LunchMoneyCrypto(LunchMoneyAPIClient):
    """
    Lunch Money Tag Interactions
    """

    def get_crypto(self) -> List[CryptoObject]:
        """
        Get All Crypto

        Use this endpoint to get a list of all cryptocurrency assets associated
        with the user's account. Both crypto balances from synced and manual
        accounts will be returned.

        https://lunchmoney.dev/#get-all-crypto

        Returns
        -------
        List[CryptoObject]
        """
        response_data = self._make_request(method=self.methods.GET,
                                           url_path=APIConfig.LUNCHMONEY_CRYPTO)
        crypto_data = response_data["crypto"]
        crypto_objects = [CryptoObject(**item) for item in crypto_data]

        return crypto_objects

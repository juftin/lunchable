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
    balance_as_of: Optional[datetime.datetime]
    status: Optional[str]
    institution_name: str
    created_at: datetime.datetime


class CryptoParamsPut(BaseModel):
    """
    https://lunchmoney.dev/#update-manual-crypto-asset
    """

    name: Optional[str]
    display_name: Optional[str]
    institution_name: Optional[str]
    balance: Optional[float]
    currency: Optional[str]


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

    def update_crypto(self, crypto_id: int,
                      name: Optional[str] = None,
                      display_name: Optional[str] = None,
                      institution_name: Optional[str] = None,
                      balance: Optional[float] = None,
                      currency: Optional[str] = None) -> CryptoObject:
        """
        Update Manual Crypto Asset

        Use this endpoint to update a single manually-managed crypto asset (does not include
        assets received from syncing with your wallet/exchange/etc). These are denoted by
        source: manual from the GET call above.

        https://lunchmoney.dev/#update-manual-crypto-asset

        Parameters
        ----------
        crypto_id: int
            ID of the crypto asset to update
        name: Optional[str]
            Official or full name of the account. Max 45 characters
        display_name: Optional[str]
            Display name for the account. Max 25 characters
        institution_name: Optional[str]
            Name of provider that holds the account. Max 50 characters
        balance: Optional[float]
            Numeric value of the current balance of the account. Do not include any
            special characters aside from a decimal point!
        currency: Optional[str]
            Cryptocurrency that is supported for manual tracking in our database

        Returns
        -------
        CryptoObject
        """
        crypto_body = CryptoParamsPut(name=name, display_name=display_name,
                                      institution_name=institution_name, balance=balance,
                                      currency=currency).dict(exclude_none=True)
        response_data = self._make_request(method=self.methods.PUT,
                                           url_path=[APIConfig.LUNCHMONEY_CRYPTO,
                                                     APIConfig.LUNCHMONEY_CRYPTO_MANUAL,
                                                     crypto_id],
                                           payload=crypto_body)
        crypto = CryptoObject(**response_data)
        return crypto

"""
Lunch Money - Crypto

https://lunchmoney.dev/#crypto
"""

import datetime
import logging
from typing import List, Optional

from pydantic import BaseModel, Field

from lunchable.config import APIConfig
from lunchable.models._core import LunchMoneyAPIClient

logger = logging.getLogger(__name__)


class CryptoObject(BaseModel):
    """
    Crypto Asset Object

    https://lunchmoney.dev/#crypto-object
    """

    _id_description = "Unique identifier for a manual crypto account (no ID for synced accounts)"
    _zabo_account_id_description = """
    Unique identifier for a synced crypto account (no ID for manual accounts, 
    multiple currencies may have the same zabo_account_id)
    """
    _source_description = """
    `synced` (this account is synced via a wallet, exchange, etc.) or `manual` (this account 
    balance is managed manually)
    """
    _display_name_description = "Display name of the crypto asset (as set by user)"
    _balance_as_of_description = """
    Date/time the balance was last updated in ISO 8601 extended format
    """
    _status_description = "The current status of the crypto account. Either active or in error."
    _created_at_description = "Date/time the asset was created in ISO 8601 extended format"

    id: int = Field(description=_id_description)
    zabo_account_id: Optional[int] = Field(description=_zabo_account_id_description)
    source: str = Field(description=_source_description)
    name: str = Field(description="Name of the crypto asset")
    display_name: Optional[str] = Field(description=_display_name_description)
    balance: float = Field(description="Current balance")
    balance_as_of: Optional[datetime.datetime] = Field(description=_balance_as_of_description)
    currency: Optional[str] = Field(description="Abbreviation for the cryptocurrency")
    status: Optional[str] = Field(description=_status_description)
    institution_name: str = Field(description="Name of provider holding the asset")
    created_at: datetime.datetime = Field(description=_created_at_description)


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
        Get Crypto Assets

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
        Update a Manual Crypto Asset

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

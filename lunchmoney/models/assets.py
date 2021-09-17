"""
Lunch Money - Assets

https://lunchmoney.dev/#assets
"""

import datetime
import logging
from typing import List, Optional

from pydantic import BaseModel, validator

from lunchmoney.config import APIConfig
from lunchmoney.models._core import LunchMoneyAPIClient

logger = logging.getLogger(__name__)


class AssetsObject(BaseModel):
    """
    https://lunchmoney.dev/#assets-object
    """

    id: int
    type_name: str
    subtype_name: str
    name: str
    display_name: Optional[str]
    balance: float
    balance_as_of: datetime.datetime
    closed_on: Optional[datetime.date]
    currency: str
    institution_name: Optional[str]
    created_at: datetime.datetime


class AssetsParamsPut(BaseModel):
    """
    https://lunchmoney.dev/#update-asset
    """

    type_name: Optional[str]
    subtype_name: Optional[str]
    name: Optional[str]
    balance: Optional[str]
    balance_as_of: Optional[datetime.datetime]
    currency: Optional[str]
    institution_name: Optional[str]

    @classmethod
    @validator("balance", pre=True)
    def result_check(cls, x):
        """
        Check a result
        """
        return round(x, 2)


class _LunchMoneyAssets(LunchMoneyAPIClient):
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

    def update_asset(self, asset_id: int,
                     type_name: Optional[str] = None,
                     subtype_name: Optional[str] = None,
                     name: Optional[str] = None,
                     balance: Optional[float] = None,
                     balance_as_of: Optional[datetime.datetime] = None,
                     currency: Optional[str] = None,
                     institution_name: Optional[str] = None) -> AssetsObject:
        """
        Use this method to update a single asset.

        Parameters
        ----------
        asset_id: int
            Asset Identifier
        type_name: Optional[str]
            Must be one of: cash, credit, investment, other, real estate, loan, vehicle,
            cryptocurrency, employee compensation
        subtype_name: Optional[str]
            Max 25 characters
        name: Optional[str]
            Max 45 characters
        balance: Optional[float]
            Numeric value of the current balance of the account. Do not include any special
            characters aside from a decimal point!
        balance_as_of: Optional[datetime.datetime]
            Has no effect if balance is not defined. If balance is defined, but balance_as_of
            is not supplied or is invalid, current timestamp will be used.
        currency: Optional[str]
            Three-letter lowercase currency in ISO 4217 format. The code sent must exist in
            our database. Defaults to asset's currency.
        institution_name: Optional[str]
            Max 50 characters

        Returns
        -------
        AssetsObject
        """
        payload = AssetsParamsPut(type_name=type_name,
                                  subtype_name=subtype_name,
                                  name=name, balance=balance,
                                  balance_as_of=balance_as_of,
                                  currency=currency,
                                  institution_name=institution_name).dict(exclude_none=True)
        response_data = self._make_request(method="PUT",
                                           url_path=[APIConfig.LUNCHMONEY_ASSETS,
                                                     asset_id],
                                           payload=payload)
        asset = AssetsObject(**response_data)
        return asset

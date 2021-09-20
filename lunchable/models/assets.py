"""
Lunch Money - Assets

https://lunchmoney.dev/#assets
"""

import datetime
import logging
from typing import List, Optional

from pydantic import BaseModel, Field, validator

from lunchable.config import APIConfig
from lunchable.models._core import LunchMoneyAPIClient

logger = logging.getLogger(__name__)


class AssetsObject(BaseModel):
    """
    Manually Managed Asset Objects

    Assets in Lunch Money are similar to `plaid-accounts` except that they are manually managed.

    https://lunchmoney.dev/#assets-object
    """

    _type_name_description = """
    Primary type of the asset. Must be one of: [employee compensation, cash, vehicle, loan, 
    cryptocurrency, investment, other, credit, real estate]
    """
    _subtype_name_description = """
    Optional asset subtype. Examples include: [retirement, checking, savings, prepaid credit card]
    """
    _balance_description = "Current balance of the asset in numeric format to 4 decimal places"
    _balance_as_of_description = """
    Date/time the balance was last updated in ISO 8601 extended format
    """
    _closed_on_description = "The date this asset was closed (optional)"
    _currency_description = "Three-letter lowercase currency code of the balance in ISO 4217 format"
    _created_at_description = "Date/time the asset was created in ISO 8601 extended format"

    id: int = Field(description="Unique identifier for asset")
    type_name: str = Field(description=_type_name_description)
    subtype_name: str = Field(description=_subtype_name_description)
    name: str = Field(description="Name of the asset")
    display_name: Optional[str] = Field(description="Display name of the asset (as set by user)")
    balance: float = Field(description=_balance_description)
    balance_as_of: datetime.datetime = Field(description=_balance_as_of_description)
    closed_on: Optional[datetime.date] = Field(description=_closed_on_description)
    currency: str = Field(description=_currency_description)
    institution_name: Optional[str] = Field(description="Name of institution holding the asset")
    created_at: datetime.datetime = Field(description=_created_at_description)


class _AssetsParamsPut(BaseModel):
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
        Get Manually Managed Assets

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
        Update a Single Asset

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
        payload = _AssetsParamsPut(type_name=type_name,
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

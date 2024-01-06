"""
Lunch Money - Assets

https://lunchmoney.dev/#assets
"""

import datetime
import logging
from typing import List, Optional, Union

from pydantic import Field, field_validator

from lunchable._config import APIConfig
from lunchable.models._base import LunchableModel
from lunchable.models._core import LunchMoneyAPIClient
from lunchable.models._descriptions import _AssetsDescriptions

logger = logging.getLogger(__name__)


class AssetsObject(LunchableModel):
    """
    Manually Managed Asset Objects

    Assets in Lunch Money are similar to `plaid-accounts` except that they are manually managed.

    https://lunchmoney.dev/#assets-object
    """

    id: int = Field(description="Unique identifier for asset")
    type_name: str = Field(description=_AssetsDescriptions.type_name)
    subtype_name: Optional[str] = Field(
        None, description=_AssetsDescriptions.subtype_name
    )
    name: str = Field(description="Name of the asset")
    display_name: Optional[str] = Field(
        None, description="Display name of the asset (as set by user)"
    )
    balance: float = Field(description=_AssetsDescriptions.balance)
    balance_as_of: Optional[datetime.datetime] = Field(
        None, description=_AssetsDescriptions.balance_as_of
    )
    closed_on: Optional[datetime.date] = Field(
        None, description=_AssetsDescriptions.closed_on
    )
    currency: str = Field(description=_AssetsDescriptions.currency)
    institution_name: Optional[str] = Field(
        None, description="Name of institution holding the asset"
    )
    exclude_transactions: bool = Field(
        default=False, description=_AssetsDescriptions.exclude_transactions
    )
    created_at: datetime.datetime = Field(description=_AssetsDescriptions.created_at)


class _AssetsParamsPut(LunchableModel):
    """
    https://lunchmoney.dev/#update-asset
    """

    type_name: Optional[str] = None
    subtype_name: Optional[str] = None
    name: Optional[str] = None
    balance: Optional[float] = None
    balance_as_of: Optional[datetime.datetime] = None
    currency: Optional[str] = None
    institution_name: Optional[str] = None

    @field_validator("balance", mode="before")
    @classmethod
    def result_check(cls, x: Union[float, int]) -> float:
        """
        Check a result
        """
        return round(x, 2)


class _AssetsParamsPost(LunchableModel):
    """
    https://lunchmoney.dev/#create-asset
    """

    type_name: str
    subtype_name: Optional[str] = None
    name: str
    display_name: Optional[str] = None
    balance: float
    balance_as_of: Optional[datetime.datetime] = None
    currency: Optional[str] = None
    institution_name: Optional[str] = None
    closed_on: Optional[datetime.date] = None
    exclude_transactions: Optional[bool] = None

    @field_validator("balance", mode="before")
    @classmethod
    def result_check(cls, x: Union[float, int]) -> float:
        """
        Check a result
        """
        return round(x, 2)


class AssetsClient(LunchMoneyAPIClient):
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
        response_data = self.make_request(
            method=self.Methods.GET, url_path=[APIConfig.LUNCHMONEY_ASSETS]
        )
        assets = response_data.get(APIConfig.LUNCHMONEY_ASSETS)
        asset_objects = [AssetsObject.model_validate(item) for item in assets]
        return asset_objects

    def update_asset(
        self,
        asset_id: int,
        type_name: Optional[str] = None,
        subtype_name: Optional[str] = None,
        name: Optional[str] = None,
        balance: Optional[float] = None,
        balance_as_of: Optional[datetime.datetime] = None,
        currency: Optional[str] = None,
        institution_name: Optional[str] = None,
    ) -> AssetsObject:
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
        payload = _AssetsParamsPut(
            type_name=type_name,
            subtype_name=subtype_name,
            name=name,
            balance=balance,
            balance_as_of=balance_as_of,
            currency=currency,
            institution_name=institution_name,
        ).model_dump(exclude_none=True)
        response_data = self.make_request(
            method=self.Methods.PUT,
            url_path=[APIConfig.LUNCHMONEY_ASSETS, asset_id],
            payload=payload,
        )
        asset = AssetsObject.model_validate(response_data)
        return asset

    def insert_asset(
        self,
        type_name: str,
        name: Optional[str] = None,
        subtype_name: Optional[str] = None,
        display_name: Optional[str] = None,
        balance: float = 0.00,
        balance_as_of: Optional[datetime.datetime] = None,
        currency: Optional[str] = None,
        institution_name: Optional[str] = None,
        closed_on: Optional[datetime.date] = None,
        exclude_transactions: Optional[bool] = None,
    ) -> AssetsObject:
        """
        Create a single (manually-managed) asset.

        Parameters
        ----------
        type_name: Optional[str]
            Must be one of: cash, credit, investment, other, real estate, loan, vehicle,
            cryptocurrency, employee compensation
        name: Optional[str]
            Max 45 characters
        subtype_name: Optional[str]
            Max 25 characters
        display_name: Optional[str]
            Display name of the asset (as set by user)
        balance: float
            Numeric value of the current balance of the account. Do not include any
            special characters aside from a decimal point! Defaults to `0.00`
        balance_as_of: Optional[datetime.datetime]
            Has no effect if balance is not defined. If balance is defined, but
            balance_as_of is not supplied or is invalid, current timestamp will be used.
        currency: Optional[str]
            Three-letter lowercase currency in ISO 4217 format. The code sent must exist
            in our database. Defaults to user's primary currency.
        institution_name: Optional[str]
            Max 50 characters
        closed_on: Optional[datetime.date]
            The date this asset was closed
        exclude_transactions: bool
            If true, this asset will not show up as an option for assignment when
            creating transactions manually. Defaults to False

        Returns
        -------
        AssetsObject
        """
        payload = _AssetsParamsPost(
            type_name=type_name,
            subtype_name=subtype_name,
            name=name,
            display_name=display_name,
            balance=balance,
            balance_as_of=balance_as_of,
            currency=currency,
            institution_name=institution_name,
            closed_on=closed_on,
            exclude_transactions=exclude_transactions,
        ).model_dump(exclude_none=True)
        response_data = self.make_request(
            method=self.Methods.POST,
            url_path=[APIConfig.LUNCHMONEY_ASSETS],
            payload=payload,
        )
        asset = AssetsObject.model_validate(response_data)
        return asset

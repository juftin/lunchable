"""
Base Classes for lunchable-app
"""

from __future__ import annotations

import datetime
import functools
import logging
from abc import ABC, abstractmethod
from typing import Any, Callable, ClassVar, Dict, List, Tuple, Type, TypeVar, overload

from pydantic import BaseModel, Field

from lunchable import LunchMoney
from lunchable.models import (
    AssetsObject,
    CategoriesObject,
    CryptoObject,
    LunchableModel,
    PlaidAccountObject,
    TagsObject,
    TransactionObject,
    UserObject,
)

logger = logging.getLogger(__name__)

LunchableModelType = TypeVar("LunchableModelType", bound=LunchableModel)


class LunchableData(BaseModel):
    """
    Data Container for Lunchable App Data
    """

    plaid_accounts: Dict[int, PlaidAccountObject] = Field(
        default_factory=dict, description="Plaid Accounts"
    )
    transactions: Dict[int, TransactionObject] = Field(
        default_factory=dict, description="Transactions"
    )
    categories: Dict[int, CategoriesObject] = Field(
        default_factory=dict, description="Categories"
    )
    assets: Dict[int, AssetsObject] = Field(default_factory=dict, description="Assets")
    tags: Dict[int, TagsObject] = Field(default_factory=dict, description="Tags")
    crypto: Dict[int, CryptoObject] = Field(default_factory=dict, description="Crypto")
    user: UserObject = Field(
        UserObject(
            user_id=0, user_name="", user_email="", account_id=0, budget_name=""
        ),
        description="User",
    )

    @property
    def asset_map(self) -> Dict[int, PlaidAccountObject | AssetsObject]:
        """
        Asset Mapping Across Plaid Accounts and Assets

        Returns
        -------
        Dict[int, Union[PlaidAccountObject, AssetsObject]]
        """
        return {
            **self.plaid_accounts,
            **self.assets,
        }

    @property
    def plaid_accounts_list(self) -> List[PlaidAccountObject]:
        """
        List of Plaid Accounts

        Returns
        -------
        List[PlaidAccountObject]
        """
        return list(self.plaid_accounts.values())

    @property
    def assets_list(self) -> List[AssetsObject]:
        """
        List of Assets

        Returns
        -------
        List[AssetsObject]
        """
        return list(self.assets.values())

    @property
    def transactions_list(self) -> List[TransactionObject]:
        """
        List of Transactions

        Returns
        -------
        List[TransactionObject]
        """
        return list(self.transactions.values())

    @property
    def categories_list(self) -> List[CategoriesObject]:
        """
        List of Categories

        Returns
        -------
        List[CategoriesObject]
        """
        return list(self.categories.values())

    @property
    def tags_list(self) -> List[TagsObject]:
        """
        List of Tags

        Returns
        -------
        List[TagsObject]
        """
        return list(self.tags.values())

    @property
    def crypto_list(self) -> List[CryptoObject]:
        """
        List of Crypto

        Returns
        -------
        List[CryptoObject]
        """
        return list(self.crypto.values())


class BaseLunchableApp(ABC):
    """
    Abstract Base Class for Lunchable Apps
    """

    @property
    def _lunchable_data_mapping(
        self,
    ) -> Dict[
        Type[LunchableModel],
        Tuple[str, Callable[[], List[LunchableModel] | LunchableModel]],
    ]:
        """
        Mapping of Lunchable Objects to their Data Collecting Info
        """
        return {
            PlaidAccountObject: ("plaid_accounts", self.lunch.get_plaid_accounts),
            TransactionObject: ("transactions", self.lunch.get_transactions),
            CategoriesObject: ("categories", self.lunch.get_categories),
            AssetsObject: ("assets", self.lunch.get_assets),
            TagsObject: ("tags", self.lunch.get_tags),
            UserObject: ("user", self.lunch.get_user),
            CryptoObject: ("crypto", self.lunch.get_crypto),
        }

    def __init__(self, access_token: str | None = None):
        """
        Lunchable App Initialization

        Parameters
        ----------
        access_token: Optional[str]
            Lunchmoney Developer API Access Token. Inherited from
            `LUNCHMONEY_ACCESS_TOKEN` environment variable if not provided
        """
        self.lunch = LunchMoney(access_token=access_token)
        self.data = LunchableData()

    @property
    @abstractmethod
    def lunchable_models(self) -> List[Type[LunchableModel]]:
        """
        Every LunchableApp should define which data objects it depends on

        Returns
        -------
        List[LunchableDataModel]
        """

    @overload
    def refresh(self, model: Type[UserObject], **kwargs: Any) -> UserObject:
        ...

    @overload
    def refresh(
        self, model: Type[LunchableModelType], **kwargs: Any
    ) -> Dict[int, LunchableModelType]:
        ...

    def refresh(
        self, model: Type[LunchableModel], **kwargs: Any
    ) -> LunchableModel | Dict[int, LunchableModel]:
        """
        Refresh a Lunchable Model

        Parameters
        ----------
        model: Type[LunchableModel]
            Type of Lunchable Model to refresh
        kwargs: Any
            Additional keyword arguments to pass to the function that
            fetches the data.

        Returns
        -------
        LunchableModel | Dict[int, LunchableModel]
            Unless you're requesting the `UserObject`, this method will return a
            dictionary of the refreshed data, keyed by the object's ID.

        Examples
        --------
        ```python
        from typing import Dict

        from lunchable.models import CategoriesObject
        from lunchable.plugins import LunchableApp

        app = LunchableApp()
        categories: Dict[int, CategoriesObject] = app.refresh(CategoriesObject)
        ```
        """
        try:
            attr_name, data_getter = self._lunchable_data_mapping[model]
            fetch_data_function = functools.partial(data_getter, **kwargs)
        except KeyError as e:
            msg = f"Model not supported by Lunchable App: {model.__name__}"
            raise NotImplementedError(msg) from e
        fetched_data = fetch_data_function()
        if isinstance(fetched_data, UserObject):
            data_mapping = fetched_data
        else:
            data_mapping = {item.id: item for item in fetched_data}  # type: ignore[assignment]
        setattr(self.data, attr_name, data_mapping)
        return data_mapping

    def refresh_data(self, models: List[Type[LunchableModel]] | None = None) -> None:
        """
        Refresh the data in the Lunchable App

        Parameters
        ----------
        models: List[Type[LunchableModel]] | None
            Explicit list of Lunchable Models to refresh. If not provided,
            all models defined in will be refreshed (which by default is
            all of them except for transactions)

        Examples
        --------
        ```python
        from typing import Dict

        from lunchable.models import PlaidAccountObject
        from lunchable.plugins import LunchableApp

        app = LunchableApp()
        app.refresh_data()
        plaid_accounts: Dict[int, PlaidAccountObject] = app.data.plaid_accounts
        ```

        ```python
        from typing import Dict

        from lunchable.models import AssetsObject
        from lunchable.plugins import LunchableApp

        app = LunchableApp()
        app.refresh_data(models=[AssetsObject])
        assets: Dict[int, AssetsObject] = app.data.assets
        ```
        """
        refresh_models = models or self.lunchable_models
        for model in refresh_models:
            self.refresh(model)

    def refresh_transactions(
        self,
        start_date: datetime.date | datetime.datetime | str | None = None,
        end_date: datetime.date | datetime.datetime | str | None = None,
        tag_id: int | None = None,
        recurring_id: int | None = None,
        plaid_account_id: int | None = None,
        category_id: int | None = None,
        asset_id: int | None = None,
        group_id: int | None = None,
        is_group: bool | None = None,
        status: str | None = None,
        debit_as_negative: bool | None = None,
        pending: bool | None = None,
        params: Dict[str, Any] | None = None,
    ) -> Dict[int, TransactionObject]:
        """
        Refresh App data with the latest transactions

        Parameters
        ----------
        start_date: Optional[Union[datetime.date, datetime.datetime, str]]
            Denotes the beginning of the time period to fetch transactions for.
            Defaults to beginning of current month. Required if end_date exists.
            Format: YYYY-MM-DD.
        end_date: Optional[Union[datetime.date, datetime.datetime, str]]
            Denotes the end of the time period you'd like to get transactions for.
            Defaults to end of current month. Required if start_date exists.
        tag_id: Optional[int]
            Filter by tag. Only accepts IDs, not names.
        recurring_id: Optional[int]
            Filter by recurring expense
        plaid_account_id: Optional[int]
            Filter by Plaid account
        category_id: Optional[int]
            Filter by category. Will also match category groups.
        asset_id: Optional[int]
            Filter by asset
        group_id: Optional[int]
            Filter by group_id (if the transaction is part of a specific group)
        is_group: Optional[bool]
            Filter by group (returns transaction groups)
        status: Optional[str]
            Filter by status (Can be cleared or uncleared. For recurring
            transactions, use recurring)
        debit_as_negative: Optional[bool]
            Pass in true if you'd like expenses to be returned as negative amounts and
            credits as positive amounts. Defaults to false.
        pending: Optional[bool]
            Pass in true if you'd like to include imported transactions with a
            pending status.
        params: Optional[dict]
            Additional Query String Params

        Returns
        -------
        Dict[int, TransactionObject]

        Examples
        --------
        ```python
        from typing import Dict

        from lunchable.models import TransactionObject
        from lunchable.plugins import LunchableApp

        app = LunchableApp()
        transactions: Dict[int, TransactionObject] = app.refresh_transactions(
            start_date="2021-01-01", end_date="2021-01-31"
        )
        ```
        """
        transactions = self.lunch.get_transactions(
            start_date=start_date,
            end_date=end_date,
            tag_id=tag_id,
            recurring_id=recurring_id,
            plaid_account_id=plaid_account_id,
            category_id=category_id,
            asset_id=asset_id,
            group_id=group_id,
            is_group=is_group,
            status=status,
            debit_as_negative=debit_as_negative,
            pending=pending,
            params=params,
        )
        transaction_map = {item.id: item for item in transactions}
        self.data.transactions.update(transaction_map)
        return transaction_map

    def clear_transactions(self) -> None:
        """
        Clear Transactions from the App
        """
        self.data.transactions.clear()


class LunchableApp(BaseLunchableApp):
    """
    Pre-Built Lunchable App

    This app comes with a `data` property which represents all the base data
    the app should need.

    This app comes with a `refresh_data` method which will refresh all of the
    data in the app, except for transactions. To refresh transactions, use the
    `refresh_transactions` method.
    """

    lunchable_models: ClassVar[List[Type[LunchableModel]]] = [
        PlaidAccountObject,
        CategoriesObject,
        AssetsObject,
        TagsObject,
        UserObject,
        CryptoObject,
    ]

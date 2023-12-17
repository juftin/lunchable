"""
Base App Class
"""

import base64
import datetime
import json
import logging
import shutil
from abc import ABC, abstractmethod
from hashlib import sha256
from typing import Any, Callable, Dict, List, Optional, Type, TypeVar, Union

from pydantic import BaseModel
from pydantic.json import pydantic_encoder

from lunchable import LunchMoney
from lunchable._config import FileConfig
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


class LunchableDataModel(LunchableModel):
    """
    Core Data Model Defining App Dependencies
    """

    model: Type[LunchableModel]
    function: Callable[[Any], Any]
    kwargs: Dict[str, Any] = {}


class LunchableDataContainer(BaseModel):
    """
    Data Container for Lunchable App Data
    """

    plaid_accounts: Dict[int, PlaidAccountObject] = {}
    transactions: Dict[int, TransactionObject] = {}
    categories: Dict[int, CategoriesObject] = {}
    assets: Dict[int, AssetsObject] = {}
    tags: Dict[int, TagsObject] = {}
    user: UserObject = UserObject(
        user_id=0, user_name="", user_email="", account_id=0, budget_name=""
    )
    crypto: Dict[int, CryptoObject] = {}

    @property
    def asset_map(self) -> Dict[int, Union[PlaidAccountObject, AssetsObject]]:
        """
        Asset Mapping Across Plaid Accounts and Assets

        Returns
        -------
        Dict[int, Union[PlaidAccountObject, AssetsObject]]
        """
        asset_map: Dict[int, Union[PlaidAccountObject, AssetsObject]] = {}
        asset_map.update(self.plaid_accounts)
        asset_map.update(self.assets)
        return asset_map

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

    __lunchable_object_mapping__: Dict[str, str] = {
        PlaidAccountObject.__name__: "plaid_accounts",
        TransactionObject.__name__: "transactions",
        CategoriesObject.__name__: "categories",
        AssetsObject.__name__: "assets",
        TagsObject.__name__: "tags",
        UserObject.__name__: "user",
        CryptoObject.__name__: "crypto",
    }

    @property
    @abstractmethod
    def lunchable_models(self) -> List[LunchableDataModel]:
        """
        Every LunchableApp should define which data objects it depends on

        Returns
        -------
        List[LunchableDataModel]
        """

    @property
    @abstractmethod
    def __builtin_data_models__(self) -> List[LunchableDataModel]:
        """
        Every LunchableApp should define which data objects are built-in

        Returns
        -------
        List[LunchableDataModel]
        """

    def __init__(self, cache_time: int = 0, access_token: Optional[str] = None):
        """
        Lunchable App Initialization

        Parameters
        ----------
        cache_time: int
            Amount of time until the cache should be refreshed
            (in seconds). Defaults to 0 which always polls for the latest data
        access_token: Optional[str]
            Lunchmoney Developer API Access Token
        """
        self.lunch = LunchMoney(access_token=access_token)
        self.lunch_data = LunchableDataContainer()
        self.data_dir = FileConfig.DATA_DIR.joinpath(self.__class__.__name__).joinpath(
            sha256(self.lunch.access_token.encode("utf-8")).hexdigest()
        )
        self.cache_time = cache_time
        if self.cache_time > 0:
            self.data_dir.mkdir(exist_ok=True, parents=True)

    def _cache_single_object(
        self,
        model: Type[LunchableModelType],
        function: Callable[[Any], Any],
        kwargs: Optional[Dict[str, Any]] = None,
        force: bool = False,
    ) -> Union[LunchableModelType, List[LunchableModelType]]:
        """
        Cache a Core Lunchable Data Object

        Parameters
        ----------
        model: Type[LunchableModel]
        function: Callable
        kwargs: Optional[Dict[str, Any]]
        force: bool

        Returns
        -------
        Any
        """
        if kwargs is None:
            kwargs = {}
        data_file = self.data_dir.joinpath(f"{model.__name__}.lunch")
        if force is True:
            refresh = True
        elif self.cache_time > 0 and data_file.exists():
            modified_time = datetime.datetime.fromtimestamp(
                data_file.stat().st_mtime, tz=datetime.timezone.utc
            )
            current_time = datetime.datetime.now(tz=datetime.timezone.utc)
            file_age = current_time - modified_time
            refresh = file_age > datetime.timedelta(seconds=self.cache_time)
        else:
            refresh = True
        if refresh is True:
            data_objects = function(**kwargs)  # type: ignore[call-arg]
            if self.cache_time > 0:
                plain_data: str = json.dumps(data_objects, default=pydantic_encoder)
                base64_data: bytes = base64.b64encode(plain_data.encode("utf-8"))
                data_file.write_bytes(base64_data)
        else:
            file_text: bytes = data_file.read_bytes()
            json_body: bytes = base64.b64decode(file_text)
            json_data: Union[Dict[str, Any], List[Dict[str, Any]]] = json.loads(
                json_body.decode("utf-8")
            )
            if isinstance(json_data, dict):
                data_objects = model.model_validate(json_data)
            else:
                data_objects = [model.model_validate(item) for item in json_data]
        return data_objects

    def get_latest_cache(
        self,
        include: Optional[List[Type[LunchableModel]]] = None,
        exclude: Optional[List[Type[LunchableModel]]] = None,
        force: bool = False,
    ) -> None:
        """
        Cache the Underlying Data Objects

        Parameters
        ----------
        include : Optional[List[Type[LunchableModel]]]
            Models to refresh cache for (instead of all of them)
        exclude : Optional[List[Type[LunchableModel]]]
            Models to skip cache refreshing
        force: bool
            Whether to force the cache

        Returns
        -------
        None
        """
        models_to_process = self.lunchable_models + self.__builtin_data_models__
        if include is not None:
            new_models_to_process: List[LunchableDataModel] = []
            data_model_mapping = {item.model: item for item in models_to_process}
            for model_class in include:
                new_models_to_process.append(data_model_mapping[model_class])
            models_to_process = new_models_to_process
        exclusions = exclude if exclude is not None else []
        for data_model in models_to_process:
            if data_model.model in exclusions:
                continue
            cache = self._cache_single_object(
                model=data_model.model,
                function=data_model.function,
                kwargs=data_model.kwargs,
                force=force,
            )
            cache_attribute: Union[Dict[int, LunchableModel], LunchableModel]
            if isinstance(cache, list):
                cache_attribute = {item.id: item for item in cache}
            else:
                cache_attribute = cache
            setattr(
                self.lunch_data,
                self.__lunchable_object_mapping__[data_model.model.__name__],
                cache_attribute,
            )

    def refresh_transactions(
        self,
        start_date: Optional[Union[datetime.date, datetime.datetime, str]] = None,
        end_date: Optional[Union[datetime.date, datetime.datetime, str]] = None,
        tag_id: Optional[int] = None,
        recurring_id: Optional[int] = None,
        plaid_account_id: Optional[int] = None,
        category_id: Optional[int] = None,
        asset_id: Optional[int] = None,
        group_id: Optional[int] = None,
        is_group: Optional[bool] = None,
        status: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        debit_as_negative: Optional[bool] = None,
        pending: Optional[bool] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> Dict[int, TransactionObject]:
        """
        Refresh App data with the latest transactions

        Parameters
        ----------
        start_date: Optional[Union[datetime.date, datetime.datetime, str]]
            Denotes the beginning of the time period to fetch transactions for. Defaults
            to beginning of current month. Required if end_date exists. Format: YYYY-MM-DD.
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
        offset: Optional[int]
            Sets the offset for the records returned
        limit: Optional[int]
            Sets the maximum number of records to return. Note: The server will not
            respond with any indication that there are more records to be returned.
            Please check the response length to determine if you should make another
            call with an offset to fetch more transactions.
        debit_as_negative: Optional[bool]
            Pass in true if you'd like expenses to be returned as negative amounts and
            credits as positive amounts. Defaults to false.
        pending: Optional[bool]
            Pass in true if you'd like to include imported transactions with a pending status.
        params: Optional[dict]
            Additional Query String Params

        Returns
        -------
        Dict[int, TransactionObject]
        """
        transactions = self.lunch.get_transactions(
            start_date=start_date, end_date=end_date, status=status
        )
        transaction_map = {item.id: item for item in transactions}
        self.lunch_data.transactions = transaction_map
        return transaction_map

    def delete_cache(self) -> None:
        """
        Delete any corresponding cache files
        """
        if self.data_dir.exists():
            shutil.rmtree(self.data_dir)


class LunchableApp(BaseLunchableApp):
    """
    Pre-Built Lunchable App

    This app comes with a `data` property which represents all the base data
    the app should need. Extend the `data_models` property to items like
    `TransactionObject`s to interact with transactions
    """

    @property
    def lunchable_models(self) -> List[LunchableDataModel]:
        """
        Which Data Should this app get
        """
        return []

    @property
    def __builtin_data_models__(self) -> List[LunchableDataModel]:
        """
        Built-In Models to Populate Most LunchableApp instances

        Returns
        -------
        List[LunchableDataModel]
        """
        return [
            LunchableDataModel(
                model=CategoriesObject, function=self.lunch.get_categories
            ),
            LunchableDataModel(
                model=PlaidAccountObject,
                function=self.lunch.get_plaid_accounts,
            ),
            LunchableDataModel(
                model=AssetsObject,
                function=self.lunch.get_assets,
            ),
            LunchableDataModel(
                model=TagsObject,
                function=self.lunch.get_tags,
            ),
            LunchableDataModel(
                model=UserObject,
                function=self.lunch.get_user,
            ),
            LunchableDataModel(
                model=CryptoObject,
                function=self.lunch.get_crypto,
            ),
        ]


class LunchableTransactionsBaseApp(LunchableApp, ABC):
    """
    LunchableApp supporting transactions
    """

    data_models: List[LunchableDataModel] = []

    @property
    @abstractmethod
    def start_date(self) -> datetime.date:
        """
        LunchableTransactionsApp requires a Start Date

        Returns
        -------
        datetime.date
        """

    @property
    @abstractmethod
    def end_date(self) -> datetime.date:
        """
        LunchableTransactionsApp requires a End Date

        Returns
        -------
        datetime.date
        """

    @property
    def __builtin_data_models__(self) -> List[LunchableDataModel]:
        """
        Which Data Should this app get
        """
        return [
            *super().__builtin_data_models__,
            LunchableDataModel(
                model=TransactionObject,
                function=self.lunch.get_transactions,
                kwargs={"start_date": self.start_date, "end_date": self.end_date},
            ),
        ]

    def refresh_transactions(  # type: ignore[override]
        self,
        start_date: Optional[datetime.date] = None,
        end_date: Optional[datetime.date] = None,
    ) -> Dict[int, TransactionObject]:
        """
        Refresh App data with the latest transactions

        Returns
        -------
        Dict[int, TransactionObject]
        """
        transactions = self.lunch.get_transactions(
            start_date=start_date if start_date is not None else self.start_date,
            end_date=end_date if end_date is not None else self.end_date,
        )
        transaction_map = {item.id: item for item in transactions}
        self.lunch_data.transactions = transaction_map
        return transaction_map


class LunchableTransactionsApp(LunchableTransactionsBaseApp):
    """
    Pre-Built Lunchable App with the last 365 days worth of transactions
    """

    @property
    def start_date(self) -> datetime.date:
        """
        LunchableTransactionsApp requires a Start Date

        Returns
        -------
        datetime.date
        """
        today = datetime.date.today()
        return today.replace(year=today.year - 100)

    @property
    def end_date(self) -> datetime.date:
        """
        LunchableTransactionsApp requires a End Date

        Returns
        -------
        datetime.date
        """
        today = datetime.date.today()
        return today.replace(year=today.year + 100)

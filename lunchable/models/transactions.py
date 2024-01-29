"""
Lunch Money - Transactions

https://lunchmoney.dev/#transactions
"""

import datetime
import logging
from enum import Enum
from typing import Any, Dict, List, Optional, Union

import pydantic_core
from pydantic import Field, field_validator

from lunchable import LunchMoneyError
from lunchable._config import APIConfig
from lunchable.models._base import LunchableModel
from lunchable.models._core import LunchMoneyAPIClient
from lunchable.models._descriptions import (
    _TransactionDescriptions,
    _TransactionInsertDescriptions,
    _TransactionSplitDescriptions,
    _TransactionUpdateDescriptions,
)
from lunchable.models.tags import TagsObject

logger = logging.getLogger(__name__)


class TransactionBaseObject(LunchableModel):
    """
    Base Model For All Transactions to Inherit From
    """

    pass


class TransactionInsertObject(TransactionBaseObject):
    """
    Object For Creating New Transactions

    https://lunchmoney.dev/#insert-transactions
    """

    class StatusEnum(str, Enum):
        """
        Status Options, must be "cleared" or "uncleared"
        """

        cleared = "cleared"
        uncleared = "uncleared"

    date: datetime.date = Field(description=_TransactionInsertDescriptions.date)
    amount: float = Field(description=_TransactionInsertDescriptions.amount)
    category_id: Optional[int] = Field(
        None, description=_TransactionInsertDescriptions.category_id
    )
    payee: Optional[str] = Field(None, description="Max 140 characters", max_length=140)
    currency: Optional[str] = Field(
        None, description=_TransactionInsertDescriptions.currency, max_length=3
    )
    asset_id: Optional[int] = Field(
        None, description=_TransactionInsertDescriptions.asset_id
    )
    recurring_id: Optional[int] = Field(
        None, description=_TransactionInsertDescriptions.recurring_id
    )
    notes: Optional[str] = Field(None, description="Max 350 characters", max_length=350)
    status: Optional[StatusEnum] = Field(
        None, description=_TransactionInsertDescriptions.status
    )
    external_id: Optional[str] = Field(
        None, description=_TransactionInsertDescriptions.external_id, max_length=75
    )
    tags: Optional[List[Union[str, int]]] = Field(
        None, description=_TransactionInsertDescriptions.tags
    )


class TransactionUpdateObject(TransactionBaseObject):
    """
    Object For Updating Existing Transactions

    https://lunchmoney.dev/#update-transaction
    """

    class StatusEnum(str, Enum):
        """
        Status Options, must be "cleared" or "uncleared"
        """

        cleared = "cleared"
        uncleared = "uncleared"

    date: Optional[datetime.date] = Field(
        None, description=_TransactionUpdateDescriptions.date
    )
    category_id: Optional[int] = Field(
        None, description=_TransactionUpdateDescriptions.category_id
    )
    payee: Optional[str] = Field(None, description="Max 140 characters", max_length=140)
    amount: Optional[float] = Field(
        None, description=_TransactionUpdateDescriptions.amount
    )
    currency: Optional[str] = Field(
        None, description=_TransactionUpdateDescriptions.currency
    )
    asset_id: Optional[int] = Field(
        None, description=_TransactionUpdateDescriptions.asset_id
    )
    recurring_id: Optional[int] = Field(
        None, description=_TransactionUpdateDescriptions.recurring_id
    )
    notes: Optional[str] = Field(None, description="Max 350 characters", max_length=350)
    status: Optional[StatusEnum] = Field(
        None, description=_TransactionUpdateDescriptions.status
    )
    external_id: Optional[str] = Field(
        None, description=_TransactionUpdateDescriptions.external_id
    )
    tags: Optional[List[Union[int, str]]] = Field(
        None, description=_TransactionUpdateDescriptions.tags
    )


class TransactionSplitObject(TransactionBaseObject):
    """
    Object for Splitting Transactions

    https://lunchmoney.dev/#split-object
    """

    date: datetime.date = Field(description=_TransactionSplitDescriptions.date)
    category_id: Optional[int] = Field(
        default=None, description=_TransactionSplitDescriptions.category_id
    )
    notes: Optional[str] = Field(None, description=_TransactionSplitDescriptions.notes)
    amount: float = Field(description=_TransactionSplitDescriptions.amount)


class FullStatusEnum(str, Enum):
    """
    Status Options
    """

    cleared = "cleared"
    uncleared = "uncleared"
    recurring = "recurring"
    recurring_suggested = "recurring_suggested"
    pending = "pending"


class TransactionChildObject(TransactionBaseObject):
    """
    Child Transaction Object for Transaction Groups
    """

    id: int = Field(description=_TransactionDescriptions.id)
    amount: float = Field(description=_TransactionDescriptions.amount)
    payee: Optional[str] = Field(None, description=_TransactionDescriptions.payee)
    date: datetime.date = Field(description=_TransactionDescriptions.date)
    formatted_date: Optional[str] = Field(
        None, description=_TransactionDescriptions.formatted_date
    )
    notes: Optional[str] = Field(None, description=_TransactionDescriptions.notes)
    currency: Optional[str] = Field(None, description=_TransactionDescriptions.currency)
    asset_id: Optional[int] = Field(None, description=_TransactionDescriptions.asset_id)
    plaid_account_id: Optional[int] = Field(
        None, description=_TransactionDescriptions.plaid_account_id
    )
    to_base: Optional[float] = Field(None, description=_TransactionDescriptions.to_base)


class TransactionObject(TransactionBaseObject):
    """
    Universal Lunch Money Transaction Object

    https://lunchmoney.dev/#transaction-object
    """

    id: int = Field(description=_TransactionDescriptions.id)
    date: datetime.date = Field(description=_TransactionDescriptions.date)
    payee: Optional[str] = Field(None, description=_TransactionDescriptions.payee)
    amount: float = Field(description=_TransactionDescriptions.amount)
    currency: Optional[str] = Field(
        None, max_length=3, description=_TransactionDescriptions.currency
    )
    to_base: Optional[float] = Field(None, description=_TransactionDescriptions.to_base)
    category_id: Optional[int] = Field(
        None, description=_TransactionDescriptions.category_id
    )
    category_name: Optional[str] = Field(
        None, description=_TransactionDescriptions.category_name
    )
    category_group_id: Optional[int] = Field(
        None, description=_TransactionDescriptions.category_group_id
    )
    category_group_name: Optional[str] = Field(
        None, description=_TransactionDescriptions.category_group_name
    )
    is_income: Optional[bool] = Field(
        None, description=_TransactionDescriptions.is_income
    )
    exclude_from_budget: Optional[bool] = Field(
        None, description=_TransactionDescriptions.exclude_from_budget
    )
    exclude_from_totals: Optional[bool] = Field(
        None, description=_TransactionDescriptions.exclude_from_totals
    )
    created_at: datetime.datetime = Field(
        description=_TransactionDescriptions.created_at
    )
    updated_at: datetime.datetime = Field(
        description=_TransactionDescriptions.updated_at
    )
    status: Optional[str] = Field(None, description=_TransactionDescriptions.status)
    is_pending: Optional[bool] = Field(
        None, description=_TransactionDescriptions.is_pending
    )
    notes: Optional[str] = Field(None, description=_TransactionDescriptions.notes)
    original_name: Optional[str] = Field(
        None, description=_TransactionDescriptions.original_name
    )
    recurring_id: Optional[int] = Field(
        None, description=_TransactionDescriptions.recurring_id
    )
    recurring_payee: Optional[str] = Field(
        None, description=_TransactionDescriptions.recurring_payee
    )
    recurring_description: Optional[str] = Field(
        None, description=_TransactionDescriptions.recurring_description
    )
    recurring_cadence: Optional[str] = Field(
        None, description=_TransactionDescriptions.recurring_cadence
    )
    recurring_type: Optional[str] = Field(
        None, description=_TransactionDescriptions.recurring_type
    )
    recurring_amount: Optional[float] = Field(
        None, description=_TransactionDescriptions.recurring_amount
    )
    recurring_currency: Optional[str] = Field(
        None, description=_TransactionDescriptions.recurring_currency
    )
    parent_id: Optional[int] = Field(
        None, description=_TransactionDescriptions.parent_id
    )
    has_children: Optional[bool] = Field(
        None, description=_TransactionDescriptions.has_children
    )
    group_id: Optional[int] = Field(None, description=_TransactionDescriptions.group_id)
    is_group: Optional[bool] = Field(
        None, description=_TransactionDescriptions.is_group
    )
    asset_id: Optional[int] = Field(None, description=_TransactionDescriptions.asset_id)
    asset_institution_name: Optional[str] = Field(
        None, description=_TransactionDescriptions.asset_institution_name
    )
    asset_name: Optional[str] = Field(
        None, description=_TransactionDescriptions.asset_name
    )
    asset_display_name: Optional[str] = Field(
        None, description=_TransactionDescriptions.asset_display_name
    )
    asset_status: Optional[str] = Field(
        None, description=_TransactionDescriptions.asset_status
    )
    plaid_account_id: Optional[int] = Field(
        None, description=_TransactionDescriptions.plaid_account_id
    )
    plaid_account_name: Optional[str] = Field(
        None, description=_TransactionDescriptions.plaid_account_name
    )
    plaid_account_mask: Optional[str] = Field(
        None, description=_TransactionDescriptions.plaid_account_mask
    )
    institution_name: Optional[str] = Field(
        None, description=_TransactionDescriptions.institution_name
    )
    plaid_account_display_name: Optional[str] = Field(
        None, description=_TransactionDescriptions.plaid_account_display_name
    )
    plaid_metadata: Optional[Dict[str, Any]] = Field(
        None, description=_TransactionDescriptions.plaid_metadata
    )
    source: Optional[str] = Field(None, description=_TransactionDescriptions.source)
    display_name: Optional[str] = Field(
        None, description=_TransactionDescriptions.display_name
    )
    display_notes: Optional[str] = Field(
        None, description=_TransactionDescriptions.display_notes
    )
    account_display_name: Optional[str] = Field(
        None, description=_TransactionDescriptions.account_display_name
    )
    tags: Optional[List[TagsObject]] = Field(None, description="Array of Tag objects")
    external_id: Optional[str] = Field(
        None, max_length=75, description=_TransactionDescriptions.external_id
    )
    children: Optional[List[TransactionChildObject]] = Field(
        None, description=_TransactionDescriptions.children
    )

    @field_validator("plaid_metadata", mode="before")
    def to_json(cls, x: Optional[str]) -> Optional[Dict[str, Any]]:
        """
        Check a result
        """
        if x is None:
            return None
        elif isinstance(x, dict):
            return x
        else:
            return pydantic_core.from_json(x)

    def get_update_object(self) -> TransactionUpdateObject:
        """
        Return a TransactionUpdateObject

        Return a TransactionUpdateObject to update an expense. Simply
        change one of the properties and perform an `update_transaction` with
        your Lunchable object.

        Returns
        -------
        TransactionUpdateObject
        """
        update_dict = self.model_dump()
        try:
            TransactionUpdateObject.StatusEnum(self.status)
        except ValueError:
            update_dict["status"] = None
        update_object = TransactionUpdateObject.model_validate(update_dict)
        if update_object.tags is not None:
            tags = [] if self.tags is None else self.tags
            update_object.tags = [tag.name for tag in tags]
        return update_object

    def get_insert_object(self) -> TransactionInsertObject:
        """
        Return a TransactionInsertObject

        Return a TransactionInsertObject to update an expense. Simply
        change some of the properties and perform an `insert_transactions` with
        your Lunchable object.

        Returns
        -------
        TransactionInsertObject
        """
        insert_dict = self.model_dump()
        try:
            TransactionInsertObject.StatusEnum(self.status)
        except ValueError:
            insert_dict["status"] = None
        insert_object = TransactionInsertObject.model_validate(insert_dict)
        if insert_object.tags is not None:
            tags = [] if self.tags is None else self.tags
            insert_object.tags = [tag.name for tag in tags]
        return insert_object


class _TransactionsResponse(LunchableModel):
    """
    HTTP Response for Transactions
    """

    transactions: List[TransactionObject]
    has_more: bool = False


class _TransactionParamsGet(LunchableModel):
    """
    https://lunchmoney.dev/#get-all-transactions
    """

    tag_id: Optional[int] = None
    recurring_id: Optional[int] = None
    plaid_account_id: Optional[int] = None
    category_id: Optional[int] = None
    asset_id: Optional[int] = None
    group_id: Optional[int] = None
    is_group: Optional[bool] = None
    status: Optional[FullStatusEnum] = None
    offset: Optional[int] = None
    limit: Optional[int] = None
    start_date: Optional[datetime.date] = None
    end_date: Optional[datetime.date] = None
    debit_as_negative: Optional[bool] = None
    pending: Optional[bool] = None


class _TransactionInsertParamsPost(LunchableModel):
    """
    https://lunchmoney.dev/#insert-transactions
    """

    transactions: List[TransactionInsertObject]
    apply_rules: Optional[bool] = None
    skip_duplicates: Optional[bool] = None
    check_for_recurring: Optional[bool] = None
    debit_as_negative: Optional[bool] = None
    skip_balance_update: Optional[bool] = None


class _TransactionGroupParamsPost(LunchableModel):
    """
    https://lunchmoney.dev/#create-transaction-group
    """

    date: datetime.date
    payee: str
    category_id: Optional[int] = None
    notes: Optional[str] = None
    tags: Optional[List[int]] = None
    transactions: List[int]


class _TransactionUpdateParamsPut(LunchableModel):
    """
    https://lunchmoney.dev/#update-transaction
    """

    split: Optional[List[TransactionSplitObject]] = None
    transaction: Optional[TransactionUpdateObject] = None
    debit_as_negative: Optional[bool] = None
    skip_balance_update: Optional[bool] = None


class _TransactionsUnsplitPost(LunchableModel):
    """
    https://lunchmoney.dev/#unsplit-transactions
    """

    parent_ids: List[int]
    remove_parents: Optional[bool] = None


class TransactionsClient(LunchMoneyAPIClient):
    """
    Lunch Money Transactions Interactions
    """

    def get_transactions(
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
    ) -> List[TransactionObject]:
        """
        Get Transactions Using Criteria

        Use this to retrieve all transactions between a date range (this method handles
        pagination automatically unless you specify a limit / offset argument). Returns
        list of Transaction objects. If no query parameters are set, this will return
        transactions for the current calendar month. If either start_date or end_date are
        datetime.datetime objects, they will be reduced to dates. If a string is provided,
        it will be attempted to be parsed as YYYY-MM-DD format.

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
            Sets the offset for the records returned (disables
            automatic pagination)
        limit: Optional[int]
            Sets the maximum number of records to return. Defaults to 1000
             (disables automatic pagination)
        debit_as_negative: Optional[bool]
            Pass in true if you'd like expenses to be returned as negative amounts and
            credits as positive amounts. Defaults to false.
        pending: Optional[bool]
            Pass in true if you'd like to include imported transactions with a pending status.
        params: Optional[dict]
            Additional Query String Params

        Returns
        -------
        List[TransactionObject]
            A list of transactions

        Examples
        --------
        Retrieve a list of
        [TransactionObject][lunchable.models.transactions.TransactionObject]

        ```python
        from lunchable import LunchMoney

        lunch = LunchMoney(access_token="xxxxxxx")
        transactions = lunch.get_transactions(start_date="2020-01-01",
                                              end_date="2020-01-31")
        ```
        """
        search_params = _TransactionParamsGet(
            tag_id=tag_id,
            recurring_id=recurring_id,
            plaid_account_id=plaid_account_id,
            category_id=category_id,
            asset_id=asset_id,
            group_id=group_id,
            is_group=is_group,
            status=status,
            offset=offset,
            limit=limit,
            start_date=start_date,
            end_date=end_date,
            debit_as_negative=debit_as_negative,
            pending=pending,
        ).model_dump(exclude_none=True)
        search_params.update(params if params is not None else {})
        auto_paginate = all(
            [
                offset is None,
                search_params.get("offset") is None,
                limit is None,
                search_params.get("limit") is None,
            ]
        )
        transactions = self._get_transactions(
            search_params=search_params,
            paginate=auto_paginate,
        )
        return transactions

    def _get_transactions(
        self,
        search_params: Dict[str, Any],
        existing_transactions: Optional[List[TransactionObject]] = None,
        paginate: bool = True,
    ) -> List[TransactionObject]:
        """
        Paginate Transactions
        """
        existing_transactions = existing_transactions or []
        transaction_response = self.make_request(
            method=self.Methods.GET,
            url_path=APIConfig.LUNCHMONEY_TRANSACTIONS,
            params=search_params,
        )
        transaction_response = _TransactionsResponse.model_validate(
            transaction_response
        )
        existing_transactions.extend(transaction_response.transactions)
        if transaction_response.has_more and paginate:
            search_params["offset"] = len(existing_transactions)
            return self._get_transactions(
                existing_transactions=existing_transactions,
                search_params=search_params,
                paginate=True,
            )
        return existing_transactions

    def get_transaction(
        self, transaction_id: int, debit_as_negative: Optional[bool] = None
    ) -> TransactionObject:
        """
        Get a Transaction by ID

        Parameters
        ----------
        transaction_id: int
            Lunch Money Transaction ID
        debit_as_negative: Optional[bool]
            Pass in true if you'd like expenses to be returned as negative
            amounts and credits as positive amounts. Defaults to false.

        Returns
        -------
        TransactionObject

        Examples
        --------
        Retrieve a single transaction by its ID

        ```python
        from lunchable import LunchMoney

        lunch = LunchMoney(access_token="xxxxxxx")
        transaction = lunch.get_transaction(transaction_id=1234)
        ```

        The above code returns a
        [TransactionObject][lunchable.models.transactions.TransactionObject]
        with ID # 1234 (assuming it exists)
        """
        response_data = self.make_request(
            method=self.Methods.GET,
            url_path=[APIConfig.LUNCHMONEY_TRANSACTIONS, transaction_id],
            params={"debit_as_negative": debit_as_negative}
            if debit_as_negative is not None
            else {},
        )
        return TransactionObject.model_validate(response_data)

    ListOrSingleTransactionUpdateObject = Optional[
        Union[TransactionUpdateObject, TransactionObject]
    ]

    ListOrSingleTransactionInsertObject = Union[
        TransactionObject,
        TransactionInsertObject,
        List[TransactionObject],
        List[TransactionInsertObject],
        List[Union[TransactionObject, TransactionInsertObject]],
    ]

    def update_transaction(
        self,
        transaction_id: int,
        transaction: ListOrSingleTransactionUpdateObject = None,
        split: Optional[List[TransactionSplitObject]] = None,
        debit_as_negative: Optional[bool] = None,
        skip_balance_update: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """
        Update a Transaction

        Use this endpoint to update a single transaction. You may also use this
        to split an existing transaction. If a TransactionObject is provided it will be
        converted into a TransactionUpdateObject.

        PUT https://dev.lunchmoney.app/v1/transactions/:transaction_id

        Parameters
        ----------
        transaction_id: int
            Lunch Money Transaction ID
        transaction: ListOrSingleTransactionUpdateObject
            Object to update with
        split: Optional[List[TransactionSplitObject]]
            Defines the split of a transaction. You may not split an already-split
            transaction, recurring transaction, or group transaction.
        debit_as_negative: Optional[bool]
            If true, will assume negative amount values denote expenses and
            positive amount values denote credits. Defaults to false.
        skip_balance_update: Optional[bool]
            If false, will skip updating balance if an asset_id
            is present for any of the transactions.

        Returns
        -------
        Dict[str, Any]

        Examples
        --------
        Update a transaction with a
        [TransactionUpdateObject][lunchable.models.transactions.TransactionUpdateObject]

        ```python
        from datetime import datetime

        from lunchable import LunchMoney, TransactionUpdateObject

        lunch = LunchMoney(access_token="xxxxxxx")
        transaction_note = f"Updated on {datetime.now()}"
        notes_update = TransactionUpdateObject(notes=transaction_note)
        response = lunch.update_transaction(transaction_id=1234,
                                            transaction=notes_update)
        ```

        Update a
        [TransactionObject][lunchable.models.transactions.TransactionObject]
        with itself

        ```python
        from datetime import datetime, timedelta

        from lunchable import LunchMoney

        lunch = LunchMoney(access_token="xxxxxxx")
        transaction = lunch.get_transaction(transaction_id=1234)

        transaction.notes = f"Updated on {datetime.now()}"
        transaction.date = transaction.date + timedelta(days=1)
        response = lunch.update_transaction(transaction_id=transaction.id,
                                            transaction=transaction)
        ```
        """
        payload = _TransactionUpdateParamsPut(
            split=split,
            debit_as_negative=debit_as_negative,
            skip_balance_update=skip_balance_update,
        ).model_dump(exclude_none=True)
        if transaction is None and split is None:
            raise LunchMoneyError("You must update the transaction or provide a split")
        elif transaction is not None:
            if isinstance(transaction, TransactionObject):
                transaction = transaction.get_update_object()
            payload["transaction"] = transaction.model_dump(exclude_unset=True)
        response_data = self.make_request(
            method=self.Methods.PUT,
            url_path=[APIConfig.LUNCHMONEY_TRANSACTIONS, transaction_id],
            payload=payload,
        )
        return response_data

    def insert_transactions(
        self,
        transactions: ListOrSingleTransactionInsertObject,
        apply_rules: Optional[bool] = None,
        skip_duplicates: Optional[bool] = None,
        debit_as_negative: Optional[bool] = None,
        check_for_recurring: Optional[bool] = None,
        skip_balance_update: Optional[bool] = None,
    ) -> List[int]:
        """
        Create One or Many Lunch Money Transactions

        Use this endpoint to insert many transactions at once. Also accepts
        a single transaction as well. If a TransactionObject is provided it will be
        converted into a TransactionInsertObject.

        https://lunchmoney.dev/#insert-transactions

        Parameters
        ----------
        transactions: ListOrSingleTransactionTypeObject
            Transactions to insert. Either a single TransactionInsertObject object or
            a list of them
        apply_rules: Optional[bool]
            If true, will apply account's existing rules to the inserted transactions.
            Defaults to false.
        skip_duplicates: Optional[bool]
            If true, the system will automatically dedupe based on transaction date,
            payee and amount. Note that deduping by external_id will occur regardless
            of this flag.
        check_for_recurring: Optional[bool]
            if true, will check new transactions for occurrences of new monthly expenses.
            Defaults to false.
        debit_as_negative: Optional[bool]
            If true, will assume negative amount values denote expenses and
            positive amount values denote credits. Defaults to false.
        skip_balance_update: Optional[bool]
            If false, will skip updating balance if an asset_id
            is present for any of the transactions.

        Returns
        -------
        List[int]

        Examples
        --------
        Create a new transaction with a
        [TransactionInsertObject][lunchable.models.transactions.TransactionInsertObject]

        ```python
        from lunchable import LunchMoney, TransactionInsertObject

        lunch = LunchMoney(access_token="xxxxxxx")

        new_transaction = TransactionInsertObject(payee="Example Restaurant",
                                                  amount=120.00,
                                                  notes="Saturday Dinner")
        new_transaction_ids = lunch.insert_transactions(transactions=new_transaction)
        ```
        """
        insert_objects = []
        if not isinstance(transactions, list):
            transactions = [transactions]
        for item in transactions:
            if isinstance(item, TransactionObject):
                insert_objects.append(item.get_insert_object())
            elif isinstance(item, TransactionInsertObject):
                insert_objects.append(item)
            else:
                raise LunchMoneyError(
                    "Only TransactionObjects or TransactionInsertObjects are "
                    "supported by this function."
                )
        payload = _TransactionInsertParamsPost(
            transactions=insert_objects,
            apply_rules=apply_rules,
            skip_duplicates=skip_duplicates,
            check_for_recurring=check_for_recurring,
            debit_as_negative=debit_as_negative,
            skip_balance_update=skip_balance_update,
        ).model_dump(exclude_none=True)
        response_data = self.make_request(
            method=self.Methods.POST,
            url_path=APIConfig.LUNCHMONEY_TRANSACTIONS,
            payload=payload,
        )
        ids: List[int] = response_data["ids"] if response_data else []
        return ids

    def insert_transaction_group(
        self,
        date: datetime.date,
        payee: str,
        transactions: List[int],
        category_id: Optional[int] = None,
        notes: Optional[str] = None,
        tags: Optional[List[int]] = None,
    ) -> int:
        """
        Create a Transaction Group of Two or More Transactions

        Returns the ID of the newly created transaction group

        Parameters
        ----------
        date: datetime.date
            Date for the grouped transaction
        payee: str
            Payee name for the grouped transaction
        category_id: Optional[int]
            Category for the grouped transaction
        notes: Optional[str]
            Notes for the grouped transaction
        tags: Optional[List[int]]
            Array of tag IDs for the grouped transaction
        transactions: Optional[List[int]]
            Array of transaction IDs to be part of the transaction group

        Returns
        -------
        int
        """
        if len(transactions) < 2:
            raise LunchMoneyError(
                "You must include 2 or more transactions " "in the Transaction Group"
            )
        transaction_params = _TransactionGroupParamsPost(
            date=date,
            payee=payee,
            category_id=category_id,
            notes=notes,
            tags=tags,
            transactions=transactions,
        ).model_dump(exclude_none=True)
        response_data = self.make_request(
            method=self.Methods.POST,
            url_path=[
                APIConfig.LUNCHMONEY_TRANSACTIONS,
                APIConfig.LUNCHMONEY_TRANSACTION_GROUPS,
            ],
            payload=transaction_params,
        )
        return response_data

    def remove_transaction_group(self, transaction_group_id: int) -> List[int]:
        """
        Delete a Transaction Group

        Use this method to delete a transaction group. The transactions within the
        group will not be removed.

        Returns the IDs of the transactions that were part of the deleted group

        https://lunchmoney.dev/#delete-transaction-group

        Parameters
        ----------
        transaction_group_id: int
            Transaction Group Identifier

        Returns
        -------
        List[int]
        """
        response_data = self.make_request(
            method=self.Methods.DELETE,
            url_path=[
                APIConfig.LUNCHMONEY_TRANSACTIONS,
                APIConfig.LUNCHMONEY_TRANSACTION_GROUPS,
                transaction_group_id,
            ],
        )
        return response_data["transactions"]

    def unsplit_transactions(
        self, parent_ids: List[int], remove_parents: Optional[bool] = None
    ) -> List[int]:
        """
        Unsplit Transactions

        Use this endpoint to unsplit one or more transactions.

        Returns an array of IDs of deleted transactions

        https://lunchmoney.dev/#unsplit-transactions

        Parameters
        ----------
        parent_ids: List[int]
            Array of transaction IDs to unsplit. If one transaction is unsplittable,
            no transaction will be unsplit.
        remove_parents: Optional[bool]
            If true, deletes the original parent transaction as well. Note,
            this is unreversable!

        Returns
        -------
        List[int]
        """
        response_data = self.make_request(
            method=self.Methods.POST,
            url_path=[APIConfig.LUNCHMONEY_TRANSACTIONS, "unsplit"],
            payload=_TransactionsUnsplitPost(
                parent_ids=parent_ids, remove_parents=remove_parents
            ).model_dump(exclude_none=True),
        )
        return response_data

    def get_transaction_group(self, transaction_id: int) -> TransactionObject:
        """
        Get a Transaction Group

        Parameters
        ----------
        transaction_id: int
            Transaction ID of either the parent or any of the children
            in the transaction group

        Returns
        -------
        TransactionObject
            The transaction group as a `TransactionObject`
        """
        response_data = self.make_request(
            method=self.Methods.GET,
            params={"transaction_id": transaction_id},
            url_path=[
                APIConfig.LUNCHMONEY_TRANSACTIONS,
                APIConfig.LUNCHMONEY_TRANSACTION_GROUPS,
            ],
        )
        return TransactionObject.model_validate(response_data)

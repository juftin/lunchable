"""
Lunch Money - Transactions

https://lunchmoney.dev/#transactions
"""

import datetime
import logging
from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from lunchable import LunchMoneyError
from lunchable._config import APIConfig
from lunchable.models._base import LunchableModel
from lunchable.models._core import LunchMoneyAPIClient
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

    _date_description = """
    Must be in ISO 8601 format (YYYY-MM-DD).
    """
    _amount_description = """
    Numeric value of amount. i.e. $4.25 should be denoted as 4.25.
    """
    _category_id_description = """
    Unique identifier for associated category_id. Category must be associated with
    the same account and must not be a category group.
    """
    _currency_description = """
    Three-letter lowercase currency code in ISO 4217 format. The code sent must exist
    in our database. Defaults to user account's primary currency.
    """
    _asset_id_description = """
    Unique identifier for associated asset (manually-managed account). Asset must be
    associated with the same account.
    """
    _recurring_id = """
    Unique identifier for associated recurring expense. Recurring expense must be associated
    with the same account.
    """
    _status_description = """
    Must be either cleared or uncleared. If recurring_id is provided, the status will
    automatically be set to recurring or recurring_suggested depending on the type of
    recurring_id. Defaults to uncleared.
    """
    _external_id_description = """
    User-defined external ID for transaction. Max 75 characters. External IDs must be
    unique within the same asset_id.
    """
    _tags_description = """
    Passing in a number will attempt to match by ID. If no matching tag ID is found, an error
    will be thrown. Passing in a string will attempt to match by string. If no matching tag
    name is found, a new tag will be created.
    """

    class StatusEnum(str, Enum):
        """
        Status Options, must be "cleared" or "uncleared"
        """

        cleared = "cleared"
        uncleared = "uncleared"

    date: datetime.date = Field(description=_date_description)
    amount: float = Field(description=_amount_description)
    category_id: Optional[int] = Field(description=_category_id_description)
    payee: Optional[str] = Field(description="Max 140 characters", max_length=140)
    currency: Optional[str] = Field(description=_currency_description, max_length=3)
    asset_id: Optional[int] = Field(description=_asset_id_description)
    recurring_id: Optional[int] = Field(description=_recurring_id)
    notes: Optional[str] = Field(description="Max 350 characters", max_length=350)
    status: Optional[StatusEnum] = Field(description=_status_description)
    external_id: Optional[str] = Field(
        description=_external_id_description, max_length=75
    )
    tags: Optional[List[Union[str, int]]] = Field(description=_tags_description)


class TransactionUpdateObject(TransactionBaseObject):
    """
    Object For Updating Existing Transactions

    https://lunchmoney.dev/#update-transaction
    """

    _date_description = """
    Must be in ISO 8601 format (YYYY-MM-DD).
    """
    _category_id_description = """
    Unique identifier for associated category_id. Category must be associated
    with the same account and must not be a category group.
    """
    _amount_description = """
    You may only update this if this transaction was not created from an automatic
    import, i.e. if this transaction is not associated with a plaid_account_id
    """
    _currency_description = """
    You may only update this if this transaction was not created from an automatic
    import, i.e. if this transaction is not associated with a plaid_account_id.
    Defaults to user account's primary currency.
    """
    _asset_id_description = """
    Unique identifier for associated asset (manually-managed account). Asset must be
    associated with the same account. You may only update this if this transaction was
    not created from an automatic import, i.e. if this transaction is not associated
    with a plaid_account_id
    """
    _recurring_id_description = """
    Unique identifier for associated recurring expense. Recurring expense must
    be associated with the same account.
    """
    _status_description = """
    Must be either cleared or uncleared. Defaults to uncleared If recurring_id is
    provided, the status will automatically be set to recurring or recurring_suggested
    depending on the type of recurring_id. Defaults to uncleared.
    """
    _external_id_description = """
    User-defined external ID for transaction. Max 75 characters. External IDs must be
    unique within the same asset_id. You may only update this if this transaction was
    not created from an automatic import, i.e. if this transaction is not associated
    with a plaid_account_id
    """
    _tags_description = """
    Passing in a number will attempt to match by ID. If no matching tag ID is found,
    an error will be thrown. Passing in a string will attempt to match by string.
    If no matching tag name is found, a new tag will be created.
    """

    class StatusEnum(str, Enum):
        """
        Status Options, must be "cleared" or "uncleared"
        """

        cleared = "cleared"
        uncleared = "uncleared"

    date: Optional[datetime.date] = Field(description=_date_description)
    category_id: Optional[int] = Field(description=_category_id_description)
    payee: Optional[str] = Field(description="Max 140 characters", max_length=140)
    amount: Optional[float] = Field(description=_amount_description)
    currency: Optional[str] = Field(description=_currency_description)
    asset_id: Optional[int] = Field(description=_asset_id_description)
    recurring_id: Optional[int] = Field(description=_recurring_id_description)
    notes: Optional[str] = Field(description="Max 350 characters", max_length=350)
    status: Optional[StatusEnum] = Field(description=_status_description)
    external_id: Optional[str] = Field(description=_external_id_description)
    tags: Optional[List[Union[int, str]]] = Field(description=_tags_description)


class TransactionSplitObject(TransactionBaseObject):
    """
    Object for Splitting Transactions

    https://lunchmoney.dev/#split-object
    """

    _date_description = "Must be in ISO 8601 format (YYYY-MM-DD)."
    _category_id_description = """
    Unique identifier for associated category_id. Category must be associated
    with the same account.
    """
    _notes_description = "Transaction Split Notes."
    _amount_description = """
    Individual amount of split. Currency will inherit from parent transaction. All
    amounts must sum up to parent transaction amount.
    """

    date: datetime.date = Field(description=_date_description)
    category_id: int = Field(description=_category_id_description)
    notes: Optional[str] = Field(description=_notes_description)
    amount: float = Field(description=_amount_description)


class FullStatusEnum(str, Enum):
    """
    Status Options
    """

    cleared = "cleared"
    uncleared = "uncleared"
    recurring = "recurring"
    recurring_suggested = "recurring_suggested"
    pending = "pending"


class TransactionObject(TransactionBaseObject):
    """
    Universal Lunch Money Transaction Object

    https://lunchmoney.dev/#transaction-object
    """

    _amount_description = """
    Amount of the transaction in numeric format to 4 decimal places
    """
    _payee_description = """
    Name of payee If recurring_id is not null, this field will show the payee
    of associated recurring expense instead of the original transaction payee
    """
    _currency_description = """
    Three-letter lowercase currency code of the transaction in ISO 4217 format
    """
    _notes_description = """
    User-entered transaction notes If recurring_id is not null, this field will
    be description of associated recurring expense
    """
    _category_description = """
    Unique identifier of associated category (see Categories)
    """
    _asset_id_description = """
    Unique identifier of associated manually-managed account (see Assets)
    Note: plaid_account_id and asset_id cannot both exist for a transaction
    """
    _plaid_account_id_description = """
    Unique identifier of associated Plaid account (see Plaid Accounts) Note:
    plaid_account_id and asset_id cannot both exist for a transaction
    """
    _status_description = """
    One of the following: cleared: User has reviewed the transaction | uncleared:
    User has not yet reviewed the transaction | recurring: Transaction is linked
    to a recurring expense | recurring_suggested: Transaction is listed as a
    suggested transaction for an existing recurring expense | pending: Imported
    transaction is marked as pending. This should be a temporary state. User intervention
    is required to change this to recurring.
    """
    _parent_id_description = """
    Exists if this is a split transaction. Denotes the transaction ID of the original
    transaction. Note that the parent transaction is not returned in this call.
    """
    _is_group_description = """
    True if this transaction represents a group of transactions. If so, amount
    and currency represent the totalled amount of transactions bearing this
    transaction’s id as their group_id. Amount is calculated based on the
    user’s primary currency.
    """
    _group_id_description = """
    Exists if this transaction is part of a group. Denotes the parent’s transaction ID
    """
    _external_id_description = """
    User-defined external ID for any manually-entered or imported transaction.
    External ID cannot be accessed or changed for Plaid-imported transactions.
    External ID must be unique by asset_id. Max 75 characters.
    """
    _original_name_description = """
    The transactions original name before any payee name updates. For synced transactions,
    this is the raw original payee name from your bank.
    """
    _type_description = """
    (for synced investment transactions only) The transaction type as set by
    Plaid for investment transactions. Possible values include: buy, sell, cash,
    transfer and more
    """
    _subtype_description = """
    (for synced investment transactions only) The transaction type as set by Plaid
    for investment transactions. Possible values include: management fee, withdrawal,
    dividend, deposit and more
    """
    _fees_description = """
    (for synced investment transactions only) The fees as set by Plaid for investment
    transactions.
    """
    _price_description = """
    (for synced investment transactions only) The price as set by Plaid for investment
    transactions.
    """
    _quantity_description = """
    (for synced investment transactions only) The quantity as set by Plaid for investment
    transactions.
    """

    id: int = Field(description="Unique identifier for transaction")
    date: datetime.date = Field(description="Date of transaction in ISO 8601 format")
    payee: Optional[str] = Field(description=_payee_description)
    amount: float = Field(description=_amount_description)
    currency: Optional[str] = Field(max_length=3, description=_currency_description)
    notes: Optional[str] = Field(description=_notes_description)
    category_id: Optional[int] = Field(description=_category_description)
    asset_id: Optional[int] = Field(description=_asset_id_description)
    plaid_account_id: Optional[int] = Field(description=_plaid_account_id_description)
    status: Optional[str] = Field(description=_status_description)
    parent_id: Optional[int] = Field(description=_parent_id_description)
    is_group: Optional[bool] = Field(description=_is_group_description)
    group_id: Optional[int] = Field(description=_group_id_description)
    tags: Optional[List[TagsObject]] = Field(description="Array of Tag objects")
    external_id: Optional[str] = Field(
        max_length=75, description=_external_id_description
    )
    original_name: Optional[str] = Field(description=_original_name_description)
    type: Optional[str] = Field(description=_type_description)
    subtype: Optional[str] = Field(description=_subtype_description)
    fees: Optional[str] = Field(description=_fees_description)
    price: Optional[str] = Field(description=_price_description)
    quantity: Optional[str] = Field(description=_quantity_description)

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
        update_dict = self.dict()
        try:
            TransactionUpdateObject.StatusEnum(self.status)
        except ValueError:
            update_dict["status"] = None
        update_object = TransactionUpdateObject(**update_dict)
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
        insert_dict = self.dict()
        try:
            TransactionInsertObject.StatusEnum(self.status)
        except ValueError:
            insert_dict["status"] = None
        insert_object = TransactionInsertObject(**insert_dict)
        if insert_object.tags is not None:
            tags = [] if self.tags is None else self.tags
            insert_object.tags = [tag.name for tag in tags]
        return insert_object


class _TransactionParamsGet(LunchableModel):
    """
    https://lunchmoney.dev/#get-all-transactions
    """

    tag_id: Optional[int]
    recurring_id: Optional[int]
    plaid_account_id: Optional[int]
    category_id: Optional[int]
    asset_id: Optional[int]
    group_id: Optional[int]
    is_group: Optional[bool]
    status: Optional[FullStatusEnum]
    offset: Optional[int]
    limit: Optional[int]
    start_date: Optional[datetime.date]
    end_date: Optional[datetime.date]
    debit_as_negative: Optional[bool]
    pending: Optional[bool]


class _TransactionInsertParamsPost(LunchableModel):
    """
    https://lunchmoney.dev/#insert-transactions
    """

    transactions: List[TransactionInsertObject]
    apply_rules: bool = False
    skip_duplicates: bool = False
    check_for_recurring: bool = False
    debit_as_negative: bool = False
    skip_balance_update: bool = True


class _TransactionGroupParamsPost(LunchableModel):
    """
    https://lunchmoney.dev/#create-transaction-group
    """

    date: datetime.date
    payee: str
    category_id: Optional[int]
    notes: Optional[str]
    tags: Optional[List[int]]
    transactions: List[int]


class _TransactionUpdateParamsPut(LunchableModel):
    """
    https://lunchmoney.dev/#update-transaction
    """

    split: Optional[List[TransactionSplitObject]] = None
    transaction: Optional[TransactionUpdateObject] = None
    debit_as_negative: bool = False
    skip_balance_update: bool = True


class _TransactionsUnsplitPost(LunchableModel):
    """
    https://lunchmoney.dev/#unsplit-transactions
    """

    parent_ids: List[int]
    remove_parents: bool = False


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
        params: Optional[dict] = None,
    ) -> List[TransactionObject]:
        """
        Get Transactions Using Criteria

        Use this to retrieve all transactions between a date range. Returns list of Transaction
        objects. If no query parameters are set, this will return transactions for the
        current calendar month. If either start_date or end_date are datetime.datetime objects,
        they will be reduced to dates. If a string is provided, it will be attempted to be parsed
        as YYYY-MM-DD format.

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
            Pass in true if you’d like expenses to be returned as negative amounts and
            credits as positive amounts. Defaults to false.
        pending: Optional[bool]
            Pass in true if you’d like to include imported transactions with a pending status.
        params: Optional[dict]
            Additional Query String Params

        Returns
        -------
        List[TransactionObject]
            A list of transactions

        Examples
        --------
        Retrieve a list of :class:`.TransactionObject` ::

            from lunchable import LunchMoney

            lunch = LunchMoney(access_token="xxxxxxx")
            transactions = lunch.get_transactions(start_date="2020-01-01",
                                                  end_date="2020-01-31")
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
        ).dict(exclude_none=True)
        search_params.update(params if params is not None else {})
        response_data = self._make_request(
            method=self.Methods.GET,
            url_path=APIConfig.LUNCHMONEY_TRANSACTIONS,
            params=search_params,
        )
        transactions = response_data[APIConfig.LUNCHMONEY_TRANSACTIONS]
        transaction_objects = [TransactionObject(**item) for item in transactions]
        return transaction_objects

    def get_transaction(self, transaction_id: int) -> TransactionObject:
        """
        Get a Transaction by ID

        Parameters
        ----------
        transaction_id: int
            Lunch Money Transaction ID

        Returns
        -------
        TransactionObject

        Examples
        --------
        Retrieve a single transaction by its ID ::

            from lunchable import LunchMoney

            lunch = LunchMoney(access_token="xxxxxxx")
            transaction = lunch.get_transaction(transaction_id=1234)

        The above code returns a :class:`.TransactionObject` with ID # 1234 (assuming
        it exists)
        """
        response_data = self._make_request(
            method=self.Methods.GET,
            url_path=[APIConfig.LUNCHMONEY_TRANSACTIONS, transaction_id],
        )
        return TransactionObject(**response_data)

    ListOrSingleTransactionUpdateObject = Optional[
        Union[TransactionUpdateObject, TransactionObject]
    ]

    ListOrSingleTransactionInsertObject = Union[
        TransactionObject,
        TransactionInsertObject,
        List[TransactionObject],
        List[TransactionInsertObject],
        List[
            Union[TransactionObject, TransactionInsertObject],
        ],
    ]

    def update_transaction(
        self,
        transaction_id: int,
        transaction: ListOrSingleTransactionUpdateObject = None,
        split: Optional[List[TransactionSplitObject]] = None,
        debit_as_negative: bool = False,
        skip_balance_update: bool = True,
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
        debit_as_negative: bool
            If true, will assume negative amount values denote expenses and
            positive amount values denote credits. Defaults to false.
        skip_balance_update: bool
            If false, will skip updating balance if an asset_id
            is present for any of the transactions.

        Returns
        -------
        Dict[str, Any]

        Examples
        --------
        Update a transaction with a :class:`.TransactionUpdateObject` ::

            from datetime import datetime

            from lunchable import LunchMoney, TransactionUpdateObject

            lunch = LunchMoney(access_token="xxxxxxx")
            transaction_note = f"Updated on {datetime.now()}"
            notes_update = TransactionUpdateObject(notes=transaction_note)
            response = lunch.update_transaction(transaction_id=1234,
                                                transaction=notes_update)

        Update a :class:`.TransactionObject` with itself ::

            from datetime import datetime, timedelta

            from lunchable import LunchMoney

            lunch = LunchMoney(access_token="xxxxxxx")
            transaction = lunch.get_transaction(transaction_id=1234)

            transaction.notes = f"Updated on {datetime.now()}"
            transaction.date = transaction.date + timedelta(days=1)
            response = lunch.update_transaction(transaction_id=transaction.id,
                                                transaction=transaction)
        """
        payload = _TransactionUpdateParamsPut(
            split=split,
            debit_as_negative=debit_as_negative,
            skip_balance_update=skip_balance_update,
        ).dict(exclude_none=True)
        if transaction is None and split is None:
            raise LunchMoneyError("You must update the transaction or provide a split")
        elif transaction is not None:
            if isinstance(transaction, TransactionObject):
                transaction = transaction.get_update_object()
            payload["transaction"] = transaction.dict(exclude_unset=True)
        response_data = self._make_request(
            method=self.Methods.PUT,
            url_path=[APIConfig.LUNCHMONEY_TRANSACTIONS, transaction_id],
            payload=payload,
        )
        return response_data

    def insert_transactions(
        self,
        transactions: ListOrSingleTransactionInsertObject,
        apply_rules: bool = False,
        skip_duplicates: bool = True,
        debit_as_negative: bool = False,
        check_for_recurring: bool = False,
        skip_balance_update: bool = True,
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
        apply_rules: bool
            If true, will apply account’s existing rules to the inserted transactions.
            Defaults to false.
        skip_duplicates: bool
            If true, the system will automatically dedupe based on transaction date,
            payee and amount. Note that deduping by external_id will occur regardless
            of this flag.
        check_for_recurring: bool
            if true, will check new transactions for occurrences of new monthly expenses.
            Defaults to false.
        debit_as_negative: bool
            If true, will assume negative amount values denote expenses and
            positive amount values denote credits. Defaults to false.
        skip_balance_update: bool
            If false, will skip updating balance if an asset_id
            is present for any of the transactions.

        Returns
        -------
        List[int]

        Examples
        --------
        Create a new transaction with a :class:`.TransactionInsertObject` ::

            from lunchable import LunchMoney, TransactionInsertObject

            lunch = LunchMoney(access_token="xxxxxxx")

            new_transaction = TransactionInsertObject(payee="Example Restaurant",
                                                      amount=120.00,
                                                      notes="Saturday Dinner")
            new_transaction_ids = lunch.insert_transactions(transactions=new_transaction)
        """
        insert_objects = list()
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
        ).dict(exclude_unset=True)
        response_data = self._make_request(
            method=self.Methods.POST,
            url_path=APIConfig.LUNCHMONEY_TRANSACTIONS,
            payload=payload,
        )
        ids: List[int] = response_data["ids"]
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
        ).dict(exclude_none=True)
        response_data = self._make_request(
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
        response_data = self._make_request(
            method=self.Methods.DELETE,
            url_path=[
                APIConfig.LUNCHMONEY_TRANSACTIONS,
                APIConfig.LUNCHMONEY_TRANSACTION_GROUPS,
                transaction_group_id,
            ],
        )
        return response_data["transactions"]

    def unsplit_transactions(
        self, parent_ids: List[int], remove_parents: bool = False
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
        remove_parents: bool
            If true, deletes the original parent transaction as well. Note,
            this is unreversable!

        Returns
        -------
        List[int]
        """
        response_data = self._make_request(
            method=self.Methods.POST,
            url_path=[APIConfig.LUNCHMONEY_TRANSACTIONS, "unsplit"],
            payload=_TransactionsUnsplitPost(
                parent_ids=parent_ids, remove_parents=remove_parents
            ).dict(exclude_none=True),
        )
        return response_data

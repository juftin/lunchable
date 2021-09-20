"""
Lunch Money - Transactions

https://lunchmoney.dev/#transactions
"""

import datetime
import logging
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field

from lunchable import LunchMoneyError
from lunchable.config import APIConfig
from lunchable.models._core import LunchMoneyAPIClient

logger = logging.getLogger(__name__)


class TransactionObject(BaseModel):
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
    One of the following: cleared: User has reviewed the transaction uncleared: 
    User has not yet reviewed the transaction recurring: Transaction is linked 
    to a recurring expense recurring_suggested: Transaction is listed as a 
    suggested transaction for an existing recurring expense. User intervention 
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

    id: Optional[int] = Field(description="Unique identifier for transaction")
    date: str = Field(description="Date of transaction in ISO 8601 format")
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
    tags: Optional[List[str]] = Field(description="Array of Tag objects")
    external_id: Optional[str] = Field(max_length=75,
                                       description=_external_id_description)
    original_name: str = Field(description=_original_name_description)
    type: Optional[str] = Field(description=_type_description)
    subtype: Optional[str] = Field(description=_subtype_description)
    fees: Optional[str] = Field(description=_fees_description)
    price: Optional[str] = Field(description=_price_description)
    quantity: Optional[str] = Field(description=_quantity_description)


class TransactionInsertObject(BaseModel):
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

    date: datetime.date = Field(description=_date_description)
    amount: float = Field(description=_amount_description)
    category_id: Optional[int] = Field(description=_category_id_description)
    payee: Optional[str] = Field(description="Max 140 characters", max_length=140)
    currency: Optional[str] = Field(description=_currency_description, max_length=3)
    asset_id: Optional[int] = Field(description=_asset_id_description)
    recurring_id: Optional[int] = Field(description=_recurring_id)
    notes: Optional[str] = Field(description="Max 350 characters", max_length=350)
    status: Optional[str] = Field(description=_status_description)
    external_id: Optional[str] = Field(description=_external_id_description, max_length=75)
    tags: Optional[List[Any]] = Field(description=_tags_description)


class TransactionUpdateObject(BaseModel):
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

    date: Optional[datetime.date] = Field(description=_date_description)
    category_id: Optional[int] = Field(description=_category_id_description)
    payee: Optional[str] = Field(description="Max 140 characters", max_length=140)
    amount: Optional[float] = Field(description=_amount_description)
    currency: Optional[str] = Field(description=_currency_description)
    asset_id: Optional[int] = Field(description=_asset_id_description)
    recurring_id: Optional[int] = Field(description=_recurring_id_description)
    notes: Optional[str] = Field(description="Max 350 characters", max_length=350)
    status: Optional[str] = Field(description=_status_description)
    external_id: Optional[str] = Field(description=_external_id_description)
    tags: Optional[List[Any]] = Field(description=_tags_description)


class TransactionParamsGet(BaseModel):
    """
    https://lunchmoney.dev/#get-all-transactions
    """

    start_date: Optional[datetime.date]
    end_date: Optional[datetime.date]


class TransactionInsertParamsPost(BaseModel):
    """
    https://lunchmoney.dev/#insert-transactions
    """

    transactions: List[TransactionInsertObject]
    apply_rules: bool = False
    skip_duplicates: bool = False
    check_for_recurring: bool = False
    debit_as_negative: bool = False
    skip_balance_update: bool = True


class TransactionGroupParamsPost(BaseModel):
    """
    https://lunchmoney.dev/#create-transaction-group
    """

    date: datetime.date
    payee: str
    category_id: Optional[int]
    notes: Optional[str]
    tags: Optional[List[int]]
    transactions: List[int]


class TransactionSplitObject(BaseModel):
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


class TransactionUpdateParamsPut(BaseModel):
    """
    https://lunchmoney.dev/#update-transaction
    """

    split: Optional[TransactionSplitObject]
    transaction: TransactionUpdateObject
    debit_as_negative: bool = False
    skip_balance_update: bool = True


class _LunchMoneyTransactions(LunchMoneyAPIClient):
    """
    Lunch Money Transactions Interactions
    """

    def get_transactions(self,
                         start_date: Optional[Union[datetime.date, datetime.datetime, str]] = None,
                         end_date: Optional[Union[datetime.date, datetime.datetime, str]] = None,
                         params: Optional[dict] = None
                         ) -> List[TransactionObject]:
        """
        Get Transactions Using Criteria

        Use this to retrieve all transactions between a date range. Returns list of Transaction
        objects. If no query parameters are set, this will return transactions for the
        current calendar month. If either start_date or _end_date are datetime.datetime objects,
        they will be reduced to dates. If a string is provided, it will be attempted to be parsed
        as YYYY-MM-DD format

        Parameters
        ----------
        start_date: Optional[Union[datetime.date, datetime.datetime, str]]:
            start date for search
        end_date: Optional[Union[datetime.date, datetime.datetime, str]]
            end date for search
        params: Optional[dict]
            additional parameters to pass to the API

        Returns
        -------
        List[TransactionObject]

        Examples
        --------
        Retrieve a list of :class:`.TransactionObject` ::

            from lunchable import LunchMoney

            lunch = LunchMoney(access_token="xxxxxxx")
            transactions = lunch.get_transactions(start_date="2020-01-01",
                                                  end_date="2020-01-31")
        """
        search_params = TransactionParamsGet(start_date=start_date,
                                             end_date=end_date).dict(exclude_none=True)
        if params is not None:
            search_params.update(params)
        response_data = self._make_request(method=self.methods.GET,
                                           url_path=APIConfig.LUNCHMONEY_TRANSACTIONS,
                                           params=search_params)
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
        Dict[str, Any]

        Examples
        --------
        Retrieve a single transaction by its ID ::

            from lunchable import LunchMoney

            lunch = LunchMoney(access_token="xxxxxxx")
            transaction = lunch.get_transaction(transaction_id=1234)

        The above code returns a :class:`.TransactionObject` with ID # 1234 (assuming
        it exists)
        """
        response_data = self._make_request(method=self.methods.GET,
                                           url_path=[APIConfig.LUNCHMONEY_TRANSACTIONS,
                                                     transaction_id])
        return TransactionObject(**response_data)

    def update_transaction(self, transaction_id: int,
                           transaction: TransactionUpdateObject,
                           split: Optional[TransactionSplitObject] = None,
                           debit_as_negative: bool = False,
                           skip_balance_update: bool = True) -> Dict[str, Any]:
        """
        Update a Transaction

        Use this endpoint to update a single transaction. You may also use this
        to split an existing transaction.

        PUT https://dev.lunchmoney.app/v1/transactions/:transaction_id

        Parameters
        ----------
        transaction_id: int
            Lunch Money Transaction ID
        transaction: TransactionUpdateObject
            Object to update with
        split: Optional[TransactionSplitObject]
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
        """
        payload = TransactionUpdateParamsPut(transaction=transaction,
                                             split=split,
                                             debit_as_negative=debit_as_negative,
                                             skip_balance_update=skip_balance_update
                                             ).dict(exclude_unset=True)
        response_data = self._make_request(method=self.methods.PUT,
                                           url_path=[APIConfig.LUNCHMONEY_TRANSACTIONS,
                                                     transaction_id],
                                           payload=payload)
        return response_data

    def insert_transactions(
            self,
            transactions: Union[TransactionInsertObject, List[TransactionInsertObject]],
            apply_rules: bool = False,
            skip_duplicates: bool = True,
            debit_as_negative: bool = False,
            check_for_recurring: bool = False,
            skip_balance_update: bool = True
    ) -> List[int]:
        """
        Create One or Many Lunch Money Transactions

        Use this endpoint to insert many transactions at once.

        https://lunchmoney.dev/#insert-transactions

        Parameters
        ----------
        transactions: Union[TransactionInsertObject, List[TransactionInsertObject]]
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
        if isinstance(transactions, TransactionInsertObject):
            transactions = [transactions]
        payload = TransactionInsertParamsPost(transactions=transactions,
                                              apply_rules=apply_rules,
                                              skip_duplicates=skip_duplicates,
                                              check_for_recurring=check_for_recurring,
                                              debit_as_negative=debit_as_negative,
                                              skip_balance_update=skip_balance_update
                                              ).dict(exclude_unset=True)
        response_data = self._make_request(method=self.methods.POST,
                                           url_path=APIConfig.LUNCHMONEY_TRANSACTIONS,
                                           payload=payload)
        ids: List[int] = response_data["ids"]
        return ids

    def insert_transaction_group(self,
                                 date: datetime.date,
                                 payee: str,
                                 transactions: List[int],
                                 category_id: Optional[int] = None,
                                 notes: Optional[str] = None,
                                 tags: Optional[List[int]] = None) -> int:
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
            raise LunchMoneyError("You must include 2 or more transactions "
                                  "in the Transaction Group")
        transaction_params = TransactionGroupParamsPost(
            date=date, payee=payee, category_id=category_id,
            notes=notes, tags=tags, transactions=transactions).dict(exclude_none=True)
        response_data = self._make_request(method=self.methods.POST,
                                           url_path=[APIConfig.LUNCHMONEY_TRANSACTIONS,
                                                     APIConfig.LUNCHMONEY_TRANSACTION_GROUPS],
                                           payload=transaction_params)
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
        response_data = self._make_request(method=self.methods.DELETE,
                                           url_path=[APIConfig.LUNCHMONEY_TRANSACTIONS,
                                                     APIConfig.LUNCHMONEY_TRANSACTION_GROUPS,
                                                     transaction_group_id])
        return response_data["transactions"]

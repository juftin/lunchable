# Author::    Justin Flannery  (mailto:juftin@juftin.com)

"""
Lunch Money - Transactions

https://lunchmoney.dev/#transactions
"""

import datetime
import logging
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel

from lunchmoney.config import APIConfig
from lunchmoney.sdk.core import LunchMoneyCore

logger = logging.getLogger(__name__)


class TransactionsObject(BaseModel):
    """
    https://lunchmoney.dev/#transaction-object
    """

    id: Optional[int]
    date: str
    amount: float
    payee: Optional[str]
    currency: Optional[str]
    status: Optional[str]
    category_id: Optional[int]
    asset_id: Optional[int]
    parent_id: Optional[int]
    plaid_account_id: Optional[int]
    is_group: Optional[bool]
    group_id: Optional[int]
    external_id: Optional[str]
    tags: Optional[List[str]]
    notes: Optional[str]


class TransactionInsertObject(BaseModel):
    """
    https://lunchmoney.dev/#insert-transactions
    """

    date: datetime.date
    amount: float
    category_id: Optional[int]
    payee: Optional[str]
    currency: Optional[str]
    asset_id: Optional[int]
    recurring_id: Optional[int]
    notes: Optional[str]
    status: Optional[str]
    external_id: Optional[str]
    tags: Optional[List[Any]]


class TransactionUpdateObject(BaseModel):
    """
    https://lunchmoney.dev/#update-transaction
    """

    date: Optional[datetime.date]
    amount: Optional[float]
    category_id: Optional[int]
    payee: Optional[str]
    currency: Optional[str]
    asset_id: Optional[int]
    recurring_id: Optional[int]
    notes: Optional[str]
    status: Optional[str]
    external_id: Optional[str]
    tags: Optional[List[Any]]


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


class TransactionUpdateParamsPut(BaseModel):
    """
    https://lunchmoney.dev/#update-transaction
    """

    split: Optional[bool]
    transaction: TransactionUpdateObject
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
    transactions: Optional[List[int]]


class LunchMoneyTransactions(LunchMoneyCore):
    """
    Lunch Money Transactions Interactions
    """

    def get_transactions(self,
                         start_date: Optional[Union[datetime.date, datetime.datetime, str]] = None,
                         end_date: Optional[Union[datetime.date, datetime.datetime, str]] = None,
                         params: Optional[dict] = None
                         ) -> List[TransactionsObject]:
        """
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
        List[TransactionsObject]
        """
        search_params = TransactionParamsGet(start_date=start_date,
                                             end_date=end_date).dict(exclude_none=True)
        if params is not None:
            search_params.update(params)
        response_data = self._make_request(method="GET",
                                           url_path=APIConfig.LUNCHMONEY_TRANSACTIONS,
                                           params=search_params)
        transactions = response_data[APIConfig.LUNCHMONEY_TRANSACTIONS]
        transaction_objects = [TransactionsObject(**item) for item in transactions]
        return transaction_objects

    def get_transaction(self, transaction_id: int) -> TransactionsObject:
        """
        Returns a single Transaction object

        Parameters
        ----------
        transaction_id: int
            Lunch Money Transaction ID

        Returns
        -------
        Dict[str, Any]
        """
        response_data = self._make_request(method="GET",
                                           url_path=[APIConfig.LUNCHMONEY_TRANSACTIONS,
                                                     transaction_id])
        return TransactionsObject(**response_data)

    def update_transaction(self, transaction_id: int,
                           transaction: TransactionUpdateObject,
                           split: Optional[object] = None,
                           debit_as_negative: bool = False,
                           skip_balance_update: bool = True) -> Dict[str, Any]:
        """
        Returns a single Transaction object

        Parameters
        ----------
        transaction_id: int
            Lunch Money Transaction ID
        transaction: TransactionUpdateObject
            Object to update with
        split: object
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
        """
        response_data = TransactionUpdateParamsPut(transaction=transaction,
                                                   split=split,
                                                   debit_as_negative=debit_as_negative,
                                                   skip_balance_update=skip_balance_update
                                                   ).dict(exclude_unset=True)
        response_data = self._make_request(method="PUT",
                                           url_path=[APIConfig.LUNCHMONEY_TRANSACTIONS,
                                                     transaction_id],
                                           json=response_data)
        return response_data

    def insert_transactions(
            self,
            transactions: Union[TransactionInsertObject, List[TransactionInsertObject]],
            apply_rules: bool = False,
            skip_duplicates: bool = True,
            debit_as_negative: bool = False,
            check_for_recurring: bool = False,
            skip_balance_update: bool = True
    ) -> Dict[str, Any]:
        """
        Returns a single Transaction object

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
        Dict[str, Any]
        """
        if isinstance(transactions, TransactionInsertObject):
            transactions = [transactions]
        response_data = TransactionInsertParamsPost(transactions=transactions,
                                                    apply_rules=apply_rules,
                                                    skip_duplicates=skip_duplicates,
                                                    check_for_recurring=check_for_recurring,
                                                    debit_as_negative=debit_as_negative,
                                                    skip_balance_update=skip_balance_update
                                                    ).json(exclude_unset=True)
        response_data = self._make_request(method="POST",
                                           url_path=APIConfig.LUNCHMONEY_TRANSACTIONS,
                                           data=response_data)
        return response_data

    def create_transaction_group(self,
                                 date: datetime.date,
                                 payee: str,
                                 category_id: Optional[int] = None,
                                 notes: Optional[str] = None,
                                 tags: Optional[List[id]] = None,
                                 transactions: Optional[List[id]] = None) -> int:
        """
        Use this endpoint to create a transaction group of two or more transactions.

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
        tags: Optional[List[id]]
            Array of tag IDs for the grouped transaction
        transactions: Optional[List[id]]
            Array of transaction IDs to be part of the transaction group

        Returns
        -------
        int
        """
        transaction_params = TransactionGroupParamsPost(
            date=date, payee=payee, category_id=category_id,
            notes=notes, tags=tags, transactions=transactions).dict(exclude_none=True)
        response_data = self._make_request(method="POST",
                                           url_path=[APIConfig.LUNCHMONEY_TRANSACTIONS,
                                                     APIConfig.LUNCHMONEY_TRANSACTION_GROUPS],
                                           params=transaction_params)
        return response_data

    def delete_transaction_group(self, transaction_group_id: int) -> List[int]:
        """
        Use this method to delete a transaction group. The transactions within the
        group will not be removed.

        Returns the IDs of the transactions that were part of the deleted group

        Parameters
        ----------
        transaction_group_id: int
            Transaction Group Identifier

        Returns
        -------
        List[int]
        """
        response_data = self._make_request(method="DELETE",
                                           url_path=[APIConfig.LUNCHMONEY_TRANSACTIONS,
                                                     APIConfig.LUNCHMONEY_TRANSACTION_GROUPS,
                                                     transaction_group_id])
        return response_data

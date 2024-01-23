"""
Run Tests on the Transactions Endpoint
"""

import datetime
import logging
from time import sleep
from typing import List

from lunchable import LunchMoney
from lunchable.models.transactions import (
    TransactionChildObject,
    TransactionInsertObject,
    TransactionObject,
    TransactionSplitObject,
    TransactionUpdateObject,
)
from tests.conftest import lunchable_cassette

logger = logging.getLogger(__name__)


@lunchable_cassette
def test_get_transactions(lunch_money_obj: LunchMoney):
    """
    Get Transactions and assert they're Transactions
    """
    transactions = lunch_money_obj.get_transactions()
    assert len(transactions) >= 1
    for transaction in transactions:
        assert isinstance(transaction, TransactionObject)
    logger.info("%s Transactions returned", len(transactions))


@lunchable_cassette
def test_get_transaction(lunch_money_obj: LunchMoney):
    """
    Get Transaction (singular) and assert it's a Transaction
    """
    transaction = lunch_money_obj.get_transaction(transaction_id=546434806)
    assert isinstance(transaction, TransactionObject)
    logger.info("Transaction returned: %s", transaction.id)


@lunchable_cassette
def test_insert_transactions(
    lunch_money_obj: LunchMoney, test_transactions: List[TransactionObject]
):
    """
    Insert a Transaction into Lunch Money
    """
    random_note = f"Random Test Description: {datetime.datetime.now()}"
    new_transaction = TransactionInsertObject(
        date=datetime.datetime.now().date(),
        payee="Random Test",
        notes=random_note,
        amount=3.50,
        asset_id=test_transactions[0].asset_id,
    )
    response = lunch_money_obj.insert_transactions(transactions=new_transaction)
    string_ints = [str(integer) for integer in response]
    logger.info("Transactions(s) Created: %s", ", ".join(string_ints))
    for transaction_id in response:
        assert isinstance(transaction_id, int)


@lunchable_cassette
def test_update_transaction(
    lunch_money_obj: LunchMoney, test_transactions: List[TransactionObject]
):
    """
    Update a Transaction in Lunch Money
    """
    transaction_note = f"Updated on {datetime.datetime.now()}"
    transaction_update_obj = TransactionUpdateObject(notes=transaction_note)
    response = lunch_money_obj.update_transaction(
        transaction_id=test_transactions[1].id, transaction=transaction_update_obj
    )
    assert response["updated"] is True


@lunchable_cassette
def test_create_and_delete_transaction_group(
    lunch_money_obj: LunchMoney, test_transactions: List[TransactionObject]
):
    """
    Create a transaction group
    """
    group_id = lunch_money_obj.insert_transaction_group(
        date=datetime.datetime.now().date(),
        payee="Test",
        notes="Test Transaction Group",
        transactions=[test_transactions[1].id, test_transactions[2].id],
    )
    assert isinstance(group_id, int)
    logger.info("Transaction Group created, ID# %s", group_id)
    sleep(1)
    response = lunch_money_obj.remove_transaction_group(transaction_group_id=group_id)
    for transaction_id in response:
        assert isinstance(transaction_id, int)
    logger.info("Transactions part of group: %s", response)


@lunchable_cassette
def test_split_transaction(lunch_money_obj: LunchMoney):
    """
    Try to split a transaction
    """
    transaction_to_split = lunch_money_obj.get_transaction(179018320)
    amount_1 = transaction_to_split.amount / 2
    split_object = TransactionSplitObject(
        date=transaction_to_split.date,
        category_id=transaction_to_split.category_id,
        notes=transaction_to_split.notes,
        amount=amount_1,
    )
    split_object_2 = split_object.model_copy()
    new_split = lunch_money_obj.update_transaction(
        transaction_id=transaction_to_split.id, split=[split_object, split_object_2]
    )
    assert len(new_split["split"]) == 2


@lunchable_cassette
def test_unsplit_transaction(lunch_money_obj: LunchMoney):
    """
    Try to unsplit a transaction
    """
    transaction_ids = [179018299]
    response = lunch_money_obj.unsplit_transactions(
        parent_ids=transaction_ids, remove_parents=True
    )
    assert len(response) == 3


@lunchable_cassette
def test_get_uncleared_transactions(lunch_money_obj: LunchMoney) -> None:
    """
    Get uncleared transactions

    Enum values previously weren't getting JSON encoded
    """
    uncleared_transactions = lunch_money_obj.get_transactions(status="uncleared")
    assert len(uncleared_transactions) >= 1
    for transaction in uncleared_transactions:
        assert isinstance(transaction, TransactionObject)


@lunchable_cassette
def test_204_response(lunch_money_obj: LunchMoney) -> None:
    """
    Test that a 204 response is handled correctly

    This test includes a hand-edited cassette to simulate a 204 response
    """
    test_transaction = TransactionInsertObject(
        date=datetime.date.today(),
        payee="Test",
        notes="Test Transaction Group",
        amount=3.50,
    )
    response = lunch_money_obj.insert_transactions(transactions=test_transaction)
    assert response == []


@lunchable_cassette
def test_get_transaction_group(lunch_money_obj: LunchMoney) -> None:
    """
    Test get_transaction_group
    """
    transaction_group = lunch_money_obj.get_transaction_group(transaction_id=856827078)
    assert isinstance(transaction_group, TransactionObject)
    assert transaction_group.is_group is True
    assert isinstance(transaction_group.children[0], TransactionChildObject)


@lunchable_cassette
def test_get_transactions_no_paginate(lunch_money_obj: LunchMoney) -> None:
    """
    Test get_transactions with no pagination
    """
    transactions = lunch_money_obj.get_transactions(limit=5)
    assert len(transactions) >= 1
    for transaction in transactions:
        assert isinstance(transaction, TransactionObject)

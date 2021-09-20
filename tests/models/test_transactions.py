"""
Run Tests on the Transactions Endpoint
"""

import datetime
import logging
from time import sleep
from typing import List

from lunchmoney import LunchMoney
from lunchmoney.models.transactions import (TransactionInsertObject,
                                            TransactionObject,
                                            TransactionUpdateObject)
from tests.conftest import lunchmoney_cassette

logger = logging.getLogger(__name__)


@lunchmoney_cassette
def test_get_transactions(lunch_money_obj: LunchMoney):
    """
    Get Transactions and assert they're Transactions
    """
    transactions = lunch_money_obj.get_transactions()
    assert len(transactions) >= 1
    for transaction in transactions:
        assert isinstance(transaction, TransactionObject)
    logger.info("%s Transactions returned", len(transactions))


@lunchmoney_cassette
def test_get_transaction(lunch_money_obj: LunchMoney):
    """
    Get Transaction (singular) and assert it's a Transaction
    """
    transaction = lunch_money_obj.get_transaction(transaction_id=53725270)
    assert isinstance(transaction, TransactionObject)
    logger.info("Transaction returned: %s", transaction.id)


@lunchmoney_cassette
def test_insert_transactions(lunch_money_obj: LunchMoney,
                             test_transactions: List[TransactionObject]):
    """
    Insert a Transaction into Lunch Money
    """
    random_note = f"Random Test Description: {datetime.datetime.now()}"
    new_transaction = TransactionInsertObject(date=datetime.datetime.now().date(),
                                              payee="Random Test",
                                              notes=random_note,
                                              amount=3.50,
                                              asset_id=test_transactions[0].asset_id)
    response = lunch_money_obj.insert_transactions(transactions=new_transaction)
    string_ints = [str(integer) for integer in response]
    logger.info("Transactions(s) Created: %s", ", ".join(string_ints))
    for transaction_id in response:
        assert isinstance(transaction_id, int)


@lunchmoney_cassette
def test_update_transaction(lunch_money_obj: LunchMoney,
                            test_transactions: List[TransactionObject]):
    """
    Update a Transaction in Lunch Money
    """
    transaction_note = f"Updated on {datetime.datetime.now()}"
    transaction_update_obj = TransactionUpdateObject(notes=transaction_note)
    response = lunch_money_obj.update_transaction(transaction_id=test_transactions[1].id,
                                                  transaction=transaction_update_obj)
    assert response["updated"] is True


@lunchmoney_cassette
def test_create_and_delete_transaction_group(lunch_money_obj: LunchMoney,
                                             test_transactions: List[TransactionObject]):
    """
    Create a transaction group
    """
    group_id = lunch_money_obj.insert_transaction_group(
        date=datetime.datetime.now().date(),
        payee="Test",
        notes="Test Transaction Group",
        transactions=[test_transactions[1].id, test_transactions[2].id])
    assert isinstance(group_id, int)
    logger.info("Transaction Group created, ID# %s", group_id)
    sleep(1)
    response = lunch_money_obj.remove_transaction_group(transaction_group_id=group_id)
    for transaction_id in response:
        assert isinstance(transaction_id, int)
    logger.info("Transactions part of group: %s", response)

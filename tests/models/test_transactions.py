"""
Run Tests on the Transactions Endpoint
"""

import datetime
import logging

from lunchmoney import LunchMoney
from lunchmoney.models.transactions import (TransactionInsertObject,
                                            TransactionsObject,
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
        assert isinstance(transaction, TransactionsObject)
    logger.info("%s Transactions returned", len(transactions))


@lunchmoney_cassette
def test_get_transaction(lunch_money_obj: LunchMoney):
    """
    Get Transaction (singular) and assert it's a Transaction
    """
    transaction = lunch_money_obj.get_transaction(transaction_id=53725270)
    assert isinstance(transaction, TransactionsObject)
    logger.info("Transaction returned: %s", transaction.id)


@lunchmoney_cassette
def test_insert_transactions(lunch_money_obj: LunchMoney):
    """
    Insert a Transaction into Lunch Money
    """
    new_transaction = TransactionInsertObject(date=datetime.datetime.now().date(),
                                              payee="Test",
                                              notes="Test Description",
                                              amount=3.50)
    response = lunch_money_obj.insert_transactions(transactions=new_transaction)
    string_ints = [str(integer) for integer in response]
    logger.info("Transactions(s) Created: %s", ", ".join(string_ints))
    for transaction_id in response:
        assert isinstance(transaction_id, int)


@lunchmoney_cassette
def test_update_transaction(lunch_money_obj: LunchMoney):
    """
    Update a Transaction in Lunch Money
    """
    transaction_note = f"Updated on {datetime.datetime.now()}"
    transaction_update_obj = TransactionUpdateObject(notes=transaction_note)
    response = lunch_money_obj.update_transaction(transaction_id=55330396,
                                                  transaction=transaction_update_obj)
    assert response["updated"] is True


@lunchmoney_cassette
def test_create_transaction_group(lunch_money_obj: LunchMoney):
    """
    Create a transaction group
    """
    group_id = lunch_money_obj.create_transaction_group(
        date=datetime.datetime.now().date(),
        payee="Test",
        notes="Test Transaction Group",
        transactions=[55330396, 55335002])
    assert isinstance(group_id, int)
    logger.info("Transaction Group created, ID# %s", group_id)


@lunchmoney_cassette
def test_delete_transaction_group(lunch_money_obj: LunchMoney):
    """
    Update a Transaction in Lunch Money
    """
    response = lunch_money_obj.delete_transaction_group(transaction_group_id=55335945)
    for transaction_id in response:
        assert isinstance(transaction_id, int)
    logger.info("Transactions part of group: %s", response)

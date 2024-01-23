"""
Pytest Fixtures Shared Across all Unit Tests
"""

import datetime
import os
import pathlib
from typing import List

import pytest
from vcr import VCR

from lunchable import LunchMoney
from lunchable.models import TransactionObject

obscure_start_date_object = datetime.datetime(year=2022, month=11, day=1)
beginning_of_this_month = datetime.datetime.now().replace(day=1)
module_scope = pytest.fixture(scope="module")


@pytest.fixture(autouse=True)
def set_test_env_vars(monkeypatch: pytest.MonkeyPatch) -> None:
    """
    Set Environment Variables for Testing if they are not already set
    """
    testing_env_vars = [
        "LUNCHMONEY_ACCESS_TOKEN",
        "PUSHOVER_USER_KEY",
        "SPLITWISE_API_KEY",
        "SPLITWISE_CONSUMER_KEY",
        "SPLITWISE_CONSUMER_SECRET",
    ]
    for env_var in testing_env_vars:
        if not os.getenv(env_var):
            monkeypatch.setenv(env_var, f"{env_var}_PLACEHOLDER")


@pytest.fixture
def obscure_start_date() -> datetime.datetime:
    """
    An Obscure Hardcoded Date

    Returns
    -------
    datetime.datetime
    """
    return obscure_start_date_object


@pytest.fixture
def lunch_money_obj() -> LunchMoney:
    """
    Static LunchMoney Instance

    Returns
    -------
    LunchMoney
    """
    lunch_money_obj = LunchMoney()
    assert isinstance(lunch_money_obj, LunchMoney)
    return lunch_money_obj


@pytest.fixture
def test_transactions() -> List[TransactionObject]:
    """
    Load some example transactions
    """
    transaction_dict_1 = {
        "amount": 1.0,
        "asset_id": 49335,
        "category_id": 658761,
        "currency": "usd",
        "date": "2021-09-19",
        "external_id": None,
        "fees": None,
        "group_id": None,
        "id": 546434801,
        "is_group": False,
        "notes": "Test Transaction 1",
        "original_name": "Test 1",
        "parent_id": None,
        "payee": "Test 1",
        "plaid_account_id": None,
        "price": None,
        "quantity": None,
        "status": "uncleared",
        "subtype": None,
        "tags": None,
        "type": None,
        "created_at": "2021-09-19T20:00:00.000Z",
        "updated_at": "2021-09-19T20:00:00.000Z",
    }
    transaction_dict_2 = {
        "amount": 2.0,
        "asset_id": 23043,
        "category_id": 229146,
        "currency": "usd",
        "date": "2021-09-19",
        "external_id": None,
        "fees": None,
        "group_id": None,
        "id": 546452296,
        "is_group": False,
        "notes": "Test Transaction 2",
        "original_name": "Test 2",
        "parent_id": None,
        "payee": "Test 2",
        "plaid_account_id": None,
        "price": None,
        "quantity": None,
        "status": "uncleared",
        "subtype": None,
        "tags": None,
        "type": None,
        "created_at": "2021-09-19T20:00:00.000Z",
        "updated_at": "2021-09-19T20:00:00.000Z",
    }
    transaction_dict_3 = {
        "amount": 3.0,
        "asset_id": 23043,
        "category_id": 229140,
        "currency": "usd",
        "date": "2021-09-19",
        "external_id": None,
        "fees": None,
        "group_id": None,
        "id": 546434806,
        "is_group": False,
        "notes": "Test Transaction 3",
        "original_name": "Test 3",
        "parent_id": None,
        "payee": "Test 3",
        "plaid_account_id": None,
        "price": None,
        "quantity": None,
        "status": "uncleared",
        "subtype": None,
        "tags": None,
        "type": None,
        "created_at": "2021-09-19T20:00:00.000Z",
        "updated_at": "2021-09-19T20:00:00.000Z",
    }
    transaction_1 = TransactionObject.model_validate(transaction_dict_1)
    transaction_2 = TransactionObject.model_validate(transaction_dict_2)
    transaction_3 = TransactionObject.model_validate(transaction_dict_3)
    return [transaction_1, transaction_2, transaction_3]


###########################################################
# VCR Configuration : Offload Epic API Calls to Cassettes #
###########################################################


def path_transformer(path: str) -> str:
    """
    Cassette Path Transformer
    """
    suffix = ".yaml"
    if not path.endswith(suffix):
        path = path + suffix
    cassette_path = pathlib.Path(path)
    cassette_path = cassette_path.parent / "cassettes" / cassette_path.name
    return str(cassette_path)


vcr = VCR(
    filter_headers=(("authorization", "XXXXXXXXXX"),),
    filter_query_parameters=(("user", "XXXXXXXXXX"), ("token", "XXXXXXXXXX")),
    path_transformer=path_transformer,
    record_mode=os.getenv("VCR_RECORD_MODE", "once"),
)

# Decorator Object to Use pyvcr Cassettes on Unit Tests
# pass `--vcr-record=none` to pytest CI runs to ensure new cassettes are generated
lunchable_cassette = vcr.use_cassette

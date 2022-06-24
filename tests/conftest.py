"""
Pytest Fixtures Shared Across all Unit Tests
"""

import datetime
from os import getenv
from typing import Dict, List

import pytest

from lunchable import LunchMoney
from lunchable.models import TransactionObject

obscure_start_date_object = datetime.datetime(year=2022, month=11, day=1)
beginning_of_this_month = datetime.datetime.now().replace(day=1)
module_scope = pytest.fixture(scope="module")


@pytest.fixture
def obscure_start_date() -> datetime.datetime:
    """
    An Obscure Hardcoded Date

    Returns
    -------
    datetime.datetime
    """
    return obscure_start_date_object


def scrub_string(string, replacement=""):
    """
    Nested Scrubbing Function
    """

    def before_record_response(response):
        body = response["body"]["string"]
        sensitive_strings = string.split(",")
        try:
            sensitive_strings.remove("<LUNCH>")
        except ValueError:
            pass
        for string_part in sensitive_strings:
            string_part = string_part.strip()
            if isinstance(body, bytes):
                try:
                    body = body.decode("utf-8").replace(string_part, replacement)
                    body = str.encode(body)
                except UnicodeDecodeError:
                    pass
            else:
                body = body.replace(string, replacement)
        response["body"]["string"] = body
        return response

    return before_record_response


@module_scope
def vcr_config() -> Dict[str, list]:
    """
    VCR Cassette Privacy Enforcer

    This fixture ensures the API Credentials are obfuscated

    Returns
    -------
    Dict[str, list]:
    """
    return {
        "filter_headers": [("authorization", "XXXXXXXXXX")],
        "filter_query_parameters": [("user", "XXXXXXXXXX"), ("token", "XXXXXXXXXX")],
        "before_record_response": scrub_string(
            getenv("SENSITIVE_REQUEST_STRINGS", "<LUNCH>"), "XXXXXXXXXX"
        ),
    }


# Decorator Object to Use pyvcr Cassettes on Unit Tests (see `pytest-vcr`)
# pass `--vcr-record=none` to pytest CI runs to ensure new cassettes are generated
lunchable_cassette = pytest.mark.vcr(scope="module")


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
        "asset_id": 23043,
        "category_id": 229134,
        "currency": "usd",
        "date": "2021-09-19",
        "external_id": None,
        "fees": None,
        "group_id": None,
        "id": 55907882,
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
        "id": 55907976,
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
        "id": 55907977,
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
    }
    transaction_1 = TransactionObject(**transaction_dict_1)
    transaction_2 = TransactionObject(**transaction_dict_2)
    transaction_3 = TransactionObject(**transaction_dict_3)
    return [transaction_1, transaction_2, transaction_3]

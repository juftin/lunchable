"""
Pytest Fixtures Shared Across all Unit Tests
"""

import datetime
from typing import Dict

import pytest

from lunchmoney import LunchMoney

obscure_start_date = datetime.datetime(year=2022, month=11, day=1)
beginning_of_this_month = datetime.datetime.now().replace(day=1)
module_scope = pytest.fixture(scope="module")


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
    }


# Decorator Object to Use pyvcr Cassettes on Unit Tests (see `pytest-vcr`)
# pass `--vcr-record=none` to pytest CI runs to ensure new cassettes are generated
lunchmoney_cassette = pytest.mark.vcr(scope="module")


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

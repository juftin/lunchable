import pytest

from lunchmoney import LunchMoney


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": [("authorization", "XXXXXXXXXX")],
    }


@pytest.fixture
def lunch_money_obj() -> LunchMoney:
    lunch_money_obj = LunchMoney()
    assert isinstance(lunch_money_obj, LunchMoney)
    return lunch_money_obj

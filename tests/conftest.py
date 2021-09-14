import pytest

from lunchmoney import LunchMoney

module_scope = pytest.fixture(scope="module")


@module_scope
def vcr_config():
    return {
        "filter_headers": [("authorization", "XXXXXXXXXX")],
    }


# Decorator Object to Use pyvcr Cassettes on Unit Tests (see `pytest-vcr`)
# pass `--vcr-record=none` to pytest CI runs to ensure new cassettes are generated
lunchmoney_cassette = pytest.mark.vcr(scope="module")


@pytest.fixture
def lunch_money_obj() -> LunchMoney:
    lunch_money_obj = LunchMoney()
    assert isinstance(lunch_money_obj, LunchMoney)
    return lunch_money_obj

import datetime
import logging
from random import choice

import pytest

from lunchmoney import LunchMoney

logger = logging.getLogger(__name__)


@pytest.fixture
def lunch_money_obj():
    lunch_money_obj = LunchMoney()
    return lunch_money_obj


def test_budgets(lunch_money_obj):
    budgets = lunch_money_obj.get_budgets(start_date=datetime.date(2021, 7, 1),
                                          end_date=datetime.date(2021, 7, 31))
    logger.info("%s Budgets Found", len(budgets))
    logger.info("Example Budget: %s", choice(budgets))

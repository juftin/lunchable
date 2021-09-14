import datetime
import logging
from random import choice

from lunchmoney import LunchMoney
from tests.conftest import lunchmoney_cassette

logger = logging.getLogger(__name__)


@lunchmoney_cassette
def test_budgets(lunch_money_obj: LunchMoney):
    budgets = lunch_money_obj.get_budgets(start_date=datetime.date(2021, 7, 1),
                                          end_date=datetime.date(2021, 7, 31))
    logger.info("%s Budgets Found", len(budgets))
    logger.info("Example Budget: %s", choice(budgets))

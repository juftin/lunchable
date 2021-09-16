"""
Run Tests on the Crypto Endpoint
"""

import logging

from lunchmoney import LunchMoney
from lunchmoney.models.crypto import CryptoObject
from tests.conftest import lunchmoney_cassette

logger = logging.getLogger(__name__)


@lunchmoney_cassette
def test_get_crypto(lunch_money_obj: LunchMoney):
    """
    Get Crypto and assert its Crypto
    """
    cryptos = lunch_money_obj.get_crypto()
    assert len(cryptos) >= 1
    for crypto in cryptos:
        assert isinstance(crypto, CryptoObject)
    logger.info("%s Crypto Accounts returned", len(cryptos))

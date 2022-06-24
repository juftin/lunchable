"""
Run Tests on the Pushover Plugin
"""

import logging
from typing import List

from lunchable.models import TransactionObject
from lunchable.plugins.pushlunch import PushLunch
from tests.conftest import lunchable_cassette

logger = logging.getLogger(__name__)


@lunchable_cassette
def test_send_notification():
    """
    Send a Generic Notification
    """
    pusher = PushLunch()
    pusher.send_notification(
        message="This is a test notification from lunchable.", title="Test"
    )


@lunchable_cassette
def test_post_transaction(test_transactions: List[TransactionObject]):
    """
    Send
    """
    pusher = PushLunch()
    example_notification = test_transactions[0]
    example_notification.payee = "Test"
    example_notification.notes = "Example Test Notification from lunchable"
    pusher.post_transaction(transaction=example_notification)

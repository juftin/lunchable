"""
Pushover Notifications via lunchable
"""

import logging
from base64 import b64decode
from json import loads
from os import getenv
from textwrap import dedent
from time import sleep
from typing import Any, Dict, List, Optional

import httpx

from lunchable.models import (
    AssetsObject,
    CategoriesObject,
    PlaidAccountObject,
    TransactionObject,
)
from lunchable.plugins import LunchableApp

logger = logging.getLogger(__name__)


class PushLunchError(Exception):
    """
    PushLunch Exception
    """

    pass


class PushLunch(LunchableApp):
    """
    Lunch Money Pushover Notifications via Lunchable
    """

    pushover_endpoint = "https://api.pushover.net/1/messages.json"

    def __init__(
        self,
        user_key: Optional[str] = None,
        app_token: Optional[str] = None,
        lunchmoney_access_token: Optional[str] = None,
    ):
        """
        Initialize

        Parameters
        ----------
        user_key : Optional[str]
            Pushover User Key. Will attempt to inherit from `PUSHOVER_USER_KEY`  environment
            variable if none defined
        app_token: Optional[str]
            Pushover app token, will attempt to inherit from `PUSHOVER_APP_TOKEN`  environment
            variable. If no token available, the official lunchable app token will be provided
        lunchmoney_access_token: Optional[str]
            LunchMoney Access Token. Will be inherited from `LUNCHMONEY_ACCESS_TOKEN`
            environment variable.
        """
        super().__init__(access_token=lunchmoney_access_token)
        self.pushover_session = httpx.Client()
        self.pushover_session.headers.update({"Content-Type": "application/json"})

        _courtesy_token = b"YXpwMzZ6MjExcWV5OGFvOXNicWF0cmdraXc4aGVz"
        if app_token is None:
            app_token = getenv("PUSHOVER_APP_TOKEN", None)
        token = app_token or b64decode(_courtesy_token).decode("utf-8")
        user_key = user_key or getenv("PUSHOVER_USER_KEY", None)
        if user_key in [None, ""]:
            raise PushLunchError(
                "You must provide a Pushover User Key or define it with "
                "a `PUSHOVER_USER_KEY` environment variable"
            )
        self._params = {"user": user_key, "token": token}
        self.get_latest_cache(
            include=[AssetsObject, PlaidAccountObject, CategoriesObject]
        )
        self.notified_transactions: List[int] = []

    def send_notification(
        self,
        message: str,
        attachment: Optional[object] = None,
        device: Optional[str] = None,
        title: Optional[str] = None,
        url: Optional[str] = None,
        url_title: Optional[str] = None,
        priority: Optional[int] = None,
        sound: Optional[str] = None,
        timestamp: Optional[str] = None,
        html: bool = False,
    ) -> httpx.Response:
        """
        Send a Pushover Notification

        Parameters
        ----------
        message: Optional[str]
            your message
        attachment: Optional[object]
            an image attachment to send with the message; see attachments for more information
            on how to upload files
        device: Optional[str]
            your user's device name to send the message directly to that device, rather than
            all of the user's devices (multiple devices may be separated by a comma)
        title: Optional[str]
            your message's title, otherwise your app's name is used
        url: Optional[str]
            a supplementary URL to show with your message
        url_title: Optional[str]
            a title for your supplementary URL, otherwise just the URL is shown
        priority: Optional[int]
            send as -2 to generate no notification/alert, -1 to always send as a quiet
            notification, 1 to display as high-priority and bypass the user's quiet hours,
            or 2 to also require confirmation from the user
        sound: Optional[str]
            the name of one of the sounds supported by device clients to override the
            user's default sound choice
        timestamp: Optional[str]
            a Unix timestamp of your message's date and time to display to the user, rather
            than the time your message is received by our API
        html: Union[None, 1]
            Pass 1 if message contains HTML contents

        Returns
        -------
        httpx.Response
        """
        html_param = 1 if html not in [None, False] else None
        params_dict = {
            "message": message,
            "attachment": attachment,
            "device": device,
            "title": title,
            "url": url,
            "url_title": url_title,
            "priority": priority,
            "sound": sound,
            "timestamp": timestamp,
            "html": html_param,
        }
        params: Dict[str, Any] = {
            key: value for key, value in params_dict.items() if value is not None
        }
        params.update(self._params)
        response = self.pushover_session.post(url=self.pushover_endpoint, params=params)
        response.raise_for_status()
        return response

    def post_transaction(
        self, transaction: TransactionObject
    ) -> Optional[Dict[str, Any]]:
        """
        Post a Lunch Money Transaction as a Pushover Notification

        Assuming the instance of the
        class hasn't already posted this particular notification

        Parameters
        ----------
        transaction: TransactionObject

        Returns
        -------
        Dict[str, Any]
        """
        if transaction.id in self.notified_transactions:
            return None
        if transaction.category_id is None:
            category = "N/A"
        else:
            category = self.lunch_data.categories[transaction.category_id].name
        account_id = transaction.plaid_account_id or transaction.asset_id
        assert account_id is not None
        account = self.lunch_data.asset_map[account_id]
        if isinstance(account, AssetsObject):
            account_name = account.display_name or account.name
        else:
            account_name = account.name
        transaction_formatted = dedent(
            f"""
        <b>Payee:</b> <i>{transaction.payee}</i>
        <b>Amount:</b> <i>{self._format_float(transaction.amount)}</i>
        <b>Date:</b> <i>{transaction.date.strftime("%A %B %-d, %Y")}</i>
        <b>Category:</b> <i>{category}</i>
        <b>Account:</b> <i>{account_name}</i>
        """
        ).strip()
        if transaction.currency is not None:
            transaction_formatted += (
                f"\n<b>Currency:</b> <i>{transaction.currency.upper()}</i>"
            )
        if transaction.status is not None:
            transaction_formatted += (
                f"\n<b>Status:</b> <i>{transaction.status.title()}</i>"
            )
        if transaction.notes is not None:
            note = f"<b>Notes:</b> <i>{transaction.notes}</i>"
            transaction_formatted += f"\n{note}"
        if transaction.status == "uncleared":
            url = (
                '<a href="https://my.lunchmoney.app/transactions/'
                f'{transaction.date.year}/{transaction.date.strftime("%m")}?status=unreviewed">'
                "<b>Uncleared Transactions from this Period</b></a>"
            )
            transaction_formatted += f"\n\n{url}"

        response = self.send_notification(
            message=transaction_formatted, title="Lunch Money Transaction", html=True
        )
        self.notified_transactions.append(transaction.id)
        return loads(response.content)

    @classmethod
    def _format_float(cls, amount: float) -> str:
        """
        Format Floats to be pleasant and human readable

        Parameters
        ----------
        amount: float
            Float Amount to be converted into a string

        Returns
        -------
        str
        """
        if amount < 0:
            float_string = f"$ ({float(amount):,.2f})".replace("-", "")
        else:
            float_string = f"$ {float(amount):,.2f}"
        return float_string

    def notify_uncleared_transactions(
        self, continuous: bool = False, interval: Optional[int] = None
    ) -> List[TransactionObject]:
        """
        Get the Current Period's Uncleared Transactions and Send a Notification for each

        Parameters
        ----------
        continuous : bool
            Whether to continuously check for more uncleared transactions,
            waiting a fixed amount in between checks.
        interval: Optional[int]
            Sleep Interval in Between Tries - only applies if `continuous` is set.
            Defaults to 60 (minutes). Cannot be less than 5 (minutes)

        Returns
        -------
        List[TransactionObject]
        """
        if interval is None:
            interval = 60
        if continuous is True and interval < 5:
            logger.warning(
                "Check interval cannot be less than 5 minutes. Defaulting to 5."
            )
            interval = 5
        if continuous is True:
            logger.info("Continuous Notifications Enabled. Beginning PushLunch.")

        uncleared_transactions = []
        continuous_search = True

        while continuous_search is True:
            found_transactions = len(self.notified_transactions)
            uncleared_transactions += self.lunch.get_transactions(status="uncleared")
            for transaction in uncleared_transactions:
                self.post_transaction(transaction=transaction)
            if continuous is True:
                notified = len(self.notified_transactions)
                new_transactions = notified - found_transactions
                logger.info(
                    "%s new transactions pushed. %s total.", new_transactions, notified
                )
                sleep(interval * 60)
            else:
                continuous_search = False

        return uncleared_transactions

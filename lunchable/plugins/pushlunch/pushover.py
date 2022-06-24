"""
Pushover Notifications via lunchable
"""

import datetime
import logging
from base64 import b64decode
from json import loads
from os import getenv
from textwrap import dedent
from time import sleep
from typing import Any, Dict, List, Optional

import requests

from lunchable import LunchMoney
from lunchable.models import AssetsObject, PlaidAccountObject, TransactionObject

logger = logging.getLogger(__name__)


class PushLunchError(Exception):
    """
    PushLunch Exception
    """

    pass


class PushLunch:
    """
    Lunch Money Pushover Notifications via Lunchable
    """

    pushover_endpoint = "https://api.pushover.net/1/messages.json"

    def __init__(
        self,
        user_key: Optional[str] = None,
        app_token: Optional[str] = None,
        lunchmoney_access_token: Optional[str] = None,
        lunchable_client: Optional[LunchMoney] = None,
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
        lunchable_client: Optional[LunchMoney]
            lunchable client to use. One will be created if none provided.
        """
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

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
        self._params = dict(user=user_key, token=token)
        self.lunchable = lunchable_client or LunchMoney(
            access_token=lunchmoney_access_token
        )
        self.asset_mapping = self._get_assets()
        self.category_mapping = self._get_categories()
        self.notified_transactions: List[int] = list()

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
    ) -> requests.Response:
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
        requests.Response
        """
        html_param = 1 if html not in [None, False] else None
        params_dict = dict(
            message=message,
            attachment=attachment,
            device=device,
            title=title,
            url=url,
            url_title=url_title,
            priority=priority,
            sound=sound,
            timestamp=timestamp,
            html=html_param,
        )
        params: Dict[str, Any] = {
            key: value for key, value in params_dict.items() if value is not None
        }
        params.update(self._params)
        response = self.session.post(url=self.pushover_endpoint, params=params)
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
            category = self.category_mapping[transaction.category_id]
        account_id = transaction.plaid_account_id or transaction.asset_id
        assert account_id is not None
        transaction_formatted = dedent(
            f"""
        <b>Payee:</b> <i>{transaction.payee}</i>
        <b>Amount:</b> <i>{self._format_float(transaction.amount)}</i>
        <b>Date:</b> <i>{transaction.date.strftime("%A %B %-d, %Y")}</i>
        <b>Category:</b> <i>{category}</i>
        <b>Account:</b> <i>{self.asset_mapping[account_id]}</i>
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

    def _get_assets(self) -> Dict[int, str]:
        """
        Get Mapping Of Asset ID -> Asset Name

        Returns
        -------
        Dict[int, str]
        """
        manual_assets = self.lunchable.get_assets()
        plaid_account = self.lunchable.get_plaid_accounts()
        assets = [*manual_assets, *plaid_account]
        asset_mapping = dict()
        for account in assets:
            if isinstance(account, AssetsObject):
                if account.display_name is None:
                    name = account.name
                else:
                    name = account.display_name
                asset_mapping[account.id] = name
            elif isinstance(account, PlaidAccountObject):
                asset_mapping[account.id] = account.name
        return asset_mapping

    def _get_categories(self) -> Dict[int, str]:
        """
        Get Mapping Of Category ID -> Category Name

        Returns
        -------
        Dict[int, str]
        """
        categories = self.lunchable.get_categories()
        category_mapping = dict()
        for category in categories:
            category_mapping[category.id] = category.name
        return category_mapping

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
            float_string = "$ ({:,.2f})".format(float(amount)).replace("-", "")
        else:
            float_string = "$ {:,.2f}".format(float(amount))
        return float_string

    def _get_uncleared_transactions(
        self,
        start_date: Optional[datetime.datetime] = None,
        end_date: Optional[datetime.datetime] = None,
    ) -> List[TransactionObject]:
        """
        Get Uncleared Transactions

        Returns
        -------
        List[TransactionObject]
        """
        uncleared_transactions = self.lunchable.get_transactions(
            start_date=start_date, end_date=end_date, status="uncleared"
        )
        return uncleared_transactions

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

        uncleared_transactions = list()
        continuous_search = True

        while continuous_search is True:
            found_transactions = len(self.notified_transactions)
            uncleared_transactions += self._get_uncleared_transactions()
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

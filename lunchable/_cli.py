"""
Lunchmoney CLI
"""

import logging
from json import JSONDecodeError
from typing import Optional

import click
import requests
from pydantic.json import pydantic_encoder
from rich import print, print_json, traceback

import lunchable
from lunchable import LunchMoney
from lunchable.models._base import LunchableModel
from lunchable.plugins.pushlunch import PushLunch

logger = logging.getLogger(__name__)


class LunchMoneyContext(LunchableModel):
    """
    Context Object to PAss Around CLI
    """

    debug: bool
    access_token: Optional[str]


debug_option = click.option(
    "--debug/--no-debug", default=False, help="Enable extra debugging output"
)
access_token_option = click.option(
    "--access-token",
    default=None,
    help="LunchMoney Developer API Access Token",
    envvar="LUNCHMONEY_ACCESS_TOKEN",
)


@click.group()
@click.version_option(
    version=lunchable.__version__, prog_name=lunchable.__application__
)
@access_token_option
@debug_option
@click.pass_context
def cli(ctx: click.core.Context, debug: bool, access_token: str) -> None:
    """
    Interactions with Lunch Money via lunchable 🍱
    """
    ctx.obj = LunchMoneyContext(debug=debug, access_token=access_token)
    traceback.install(show_locals=debug)
    if debug is True:
        logging.basicConfig(
            level=logging.DEBUG, format="%(asctime)s [%(levelname)8s]: %(message)s"
        )


@cli.group()
def transactions():
    """
    Interact with Lunch Money transactions
    """


@cli.group()
def plugins():
    """
    Interact with Lunchable Plugins
    """


@transactions.command("get")
@click.option(
    "--start-date",
    default=None,
    help="Denotes the beginning of the time period to fetch transactions for. Defaults"
    "to beginning of current month. Required if end_date exists. "
    "Format: YYYY-MM-DD.",
)
@click.option(
    "--end-date",
    default=None,
    help="Denotes the end of the time period you'd like to get transactions for. "
    "Defaults to end of current month. Required if start_date exists."
    "Format: YYYY-MM-DD.",
)
@click.option(
    "--tag-id", default=None, help="Filter by tag. Only accepts IDs, not names."
)
@click.option("--recurring-id", default=None, help="Filter by recurring expense")
@click.option("--plaid-account-id", default=None, help="Filter by Plaid account")
@click.option(
    "--category-id",
    default=None,
    help="Filter by category. Will also match category groups.",
)
@click.option("--asset-id", default=None, help="Filter by asset")
@click.option(
    "--group-id",
    default=None,
    help="Filter by group_id (if the transaction is part of a specific group)",
)
@click.option(
    "--is-group", default=None, help="Filter by group (returns transaction groups)"
)
@click.option(
    "--status",
    default=None,
    help="Filter by status (Can be cleared or uncleared. For recurring "
    "transactions, use recurring)",
)
@click.option("--offset", default=None, help="Sets the offset for the records returned")
@click.option(
    "--limit",
    default=None,
    help="Sets the maximum number of records to return. Note: The server will not "
    "respond with any indication that there are more records to be returned. "
    "Please check the response length to determine if you should make another "
    "call with an offset to fetch more transactions.",
)
@click.option(
    "--debit-as-negative",
    default=None,
    help="Pass in true if you’d like expenses to be returned as negative amounts and "
    "credits as positive amounts. Defaults to false.",
)
@click.option(
    "--pending",
    is_flag=True,
    default=None,
    help="Pass in true if you’d like to include imported transactions with a pending status.",
)
@click.pass_obj
def lunchmoney_transactions(context: LunchMoneyContext, **kwargs):
    """
    Retrieve Lunch Money Transactions
    """
    lunch = LunchMoney(access_token=context.access_token)
    transactions = lunch.get_transactions(**kwargs)
    print_json(data=transactions, default=pydantic_encoder)


@plugins.group()
def splitlunch():
    """
    Splitwise Plugin for lunchable, SplitLunch 💲🍱
    """
    pass


@splitlunch.command("expenses")
@click.option(
    "--limit", default=None, help="Limit the amount of Results. 0 returns everything."
)
@click.option("--offset", default=None, help="Number of expenses to be skipped")
@click.option("--limit", default=None, help="Number of expenses to be returned")
@click.option("--group-id", default=None, help="GroupID of the expenses")
@click.option("--friendship-id", default=None, help="FriendshipID of the expenses")
@click.option(
    "--dated-after",
    default=None,
    help="ISO 8601 Date time. Return expenses later that this date",
)
@click.option(
    "--dated-before",
    default=None,
    help="ISO 8601 Date time. Return expenses earlier than this date",
)
@click.option(
    "--updated-after",
    default=None,
    help="ISO 8601 Date time. Return expenses updated after this date",
)
@click.option(
    "--updated-before",
    default=None,
    help="ISO 8601 Date time. Return expenses updated before this date",
)
def splitlunch_expenses(**kwargs):
    """
    Retrieve Splitwise Expenses
    """
    from lunchable.plugins.splitlunch import SplitLunch

    splitlunch = SplitLunch()
    if set(kwargs.values()) == {None}:
        kwargs["limit"] = 5
    expenses = splitlunch.get_expenses(**kwargs)
    print_json(data=expenses, default=pydantic_encoder)


tag_transactions = click.option(
    "--tag-transactions",
    is_flag=True,
    help="Tag the resulting transactions with a `Splitwise` tag.",
)
financial_partner_id = click.option(
    "--financial-partner-id",
    default=None,
    type=click.INT,
    help="Splitwise ID of your financial partner.",
)
financial_partner_email = click.option(
    "--financial-partner-email",
    default=None,
    help="Splitwise Email Address of your financial partner.",
)
financial_partner_group_id = click.option(
    "--financial-partner-group-id",
    default=None,
    type=click.INT,
    help="Splitwise Group ID for financial partner transactions.",
)


@splitlunch.command("splitlunch")
@tag_transactions
def make_splitlunch(**kwargs):
    """
    Split all `SplitLunch` tagged transactions in half.

    One of these new splits will be recategorized to `Reimbursement`.
    """
    from lunchable.plugins.splitlunch import SplitLunch

    splitlunch = SplitLunch()
    results = splitlunch.make_splitlunch(**kwargs)
    print_json(data=results, default=pydantic_encoder)


@splitlunch.command("splitlunch-import")
@tag_transactions
@financial_partner_id
@financial_partner_email
@financial_partner_group_id
def make_splitlunch_import(**kwargs):
    """
    Import `SplitLunchImport` tagged transactions to Splitwise and Split them in Lunch Money

    Send a transaction to Splitwise and then split the original transaction in Lunch Money.
    One of these new splits will be recategorized to `Reimbursement`. Any tags will be
    reapplied.
    """
    from lunchable.plugins.splitlunch import SplitLunch

    financial_partner_id = kwargs.pop("financial_partner_id")
    financial_partner_email = kwargs.pop("financial_partner_email")
    financial_partner_group_id = kwargs.pop("financial_partner_group_id")
    splitlunch = SplitLunch(
        financial_partner_id=financial_partner_id,
        financial_partner_email=financial_partner_email,
        financial_partner_group_id=financial_partner_group_id,
    )
    results = splitlunch.make_splitlunch_import(**kwargs)
    print_json(data=results, default=pydantic_encoder)


@splitlunch.command("splitlunch-direct-import")
@tag_transactions
@financial_partner_id
@financial_partner_email
@financial_partner_group_id
def make_splitlunch_direct_import(**kwargs):
    """
    Import `SplitLunchDirectImport` tagged transactions to Splitwise and Split them in Lunch Money

    Send a transaction to Splitwise and then split the original transaction in Lunch Money.
    One of these new splits will be recategorized to `Reimbursement`. Any tags will be
    reapplied.
    """
    from lunchable.plugins.splitlunch import SplitLunch

    financial_partner_id = kwargs.pop("financial_partner_id")
    financial_partner_email = kwargs.pop("financial_partner_email")
    financial_partner_group_id = kwargs.pop("financial_partner_group_id")
    splitlunch = SplitLunch(
        financial_partner_id=financial_partner_id,
        financial_partner_email=financial_partner_email,
        financial_partner_group_id=financial_partner_group_id,
    )
    results = splitlunch.make_splitlunch_direct_import(**kwargs)
    print_json(data=results, default=pydantic_encoder)


@splitlunch.command("update-balance")
def update_splitwise_balance(**kwargs):
    """
    Update the Splitwise Asset Balance
    """
    from lunchable.plugins.splitlunch import SplitLunch

    splitlunch = SplitLunch()
    updated_asset = splitlunch.update_splitwise_balance()
    print_json(data=updated_asset, default=pydantic_encoder)


@splitlunch.command("refresh")
def refresh_splitwise_transactions(**kwargs):
    """
    Import New Splitwise Transactions to Lunch Money and

    This function gets all transactions from Splitwise, all transactions from
    your Lunch Money Splitwise account and compares the two. This also updates
    the account balance.
    """
    from lunchable.plugins.splitlunch import SplitLunch

    splitlunch = SplitLunch()
    response = splitlunch.refresh_splitwise_transactions()
    print_json(data=response, default=pydantic_encoder)


@plugins.group()
def pushlunch():
    """
    Push Notifications for Lunch Money: PushLunch 📲
    """
    pass


@pushlunch.command("notify")
@click.option(
    "--continuous",
    is_flag=True,
    help="Whether to continuously check for more uncleared transactions, "
    "waiting a fixed amount in between checks.",
)
@click.option(
    "--interval",
    default=None,
    help="Sleep Interval in Between Tries - only applies if `continuous` is set. "
    "Defaults to 60 (minutes). Cannot be less than 5 (minutes)",
)
@click.option(
    "--user-key",
    default=None,
    help="Pushover User Key. Defaults to `PUSHOVER_USER_KEY` env var",
)
def notify(continuous: bool, interval: int, user_key: str):
    """
    Send a Notification for each Uncleared Transaction
    """
    push = PushLunch(user_key=user_key)
    if interval is not None:
        interval = int(interval)
    if continuous is not None:
        logging.basicConfig(
            level=logging.INFO, format="%(asctime)s [%(levelname)8s]: %(message)s"
        )
    push.notify_uncleared_transactions(continuous=continuous, interval=interval)


@cli.command()
@click.argument("URL")
@click.option("-X", "--request", default="GET", help="Specify request command to use")
@click.option("-d", "--data", default=None, help="HTTP POST data")
@click.pass_obj
def http(context: LunchMoneyContext, url: str, request: str, data: str):
    """
    Interact with the LunchMoney API

    lunchable http /v1/transactions
    """
    lunch = LunchMoney(access_token=context.access_token)
    if not url.startswith("http"):
        url = url.lstrip("/")
        url_request = f"https://dev.lunchmoney.app/{url}"
    else:
        url_request = url
    resp = lunch.make_http_request(
        method=request,
        url=url_request,
        data=data,
    )
    try:
        resp.raise_for_status()
    except requests.HTTPError:
        logger.error(resp)
        print(resp.text)
        exit(1)
    try:
        response = resp.json()
    except JSONDecodeError:
        response = resp.text
    print_json(data=response, default=pydantic_encoder)

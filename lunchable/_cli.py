"""
Lunchmoney CLI
"""

import json
import logging
from typing import List

import click
from pydantic.json import pydantic_encoder

import lunchable
from lunchable import LunchMoney
from lunchable.plugins.splitlunch import SplitLunch

logger = logging.getLogger(__name__)


@click.group()
@click.version_option(lunchable.__version__)
@click.option("--json/--no-json", default=False, help="Disable Logging Output for pure JSON")
@click.option("--debug/--no-debug", default=False, help="Enable Debugging (verbose) output")
@click.pass_context
def cli(ctx, **kwargs):
    """
    lunchable interactions with Lunch Money 🍱
    """
    ctx.ensure_object(dict)
    ctx.obj["DEBUG"] = kwargs["debug"]
    ctx.obj["JSON"] = kwargs["json"]


@cli.group()
def transactions():
    """
    Interact with Lunch Money transactions
    """


@transactions.command("get")
@click.option("--start-date", default=None,
              help="Denotes the beginning of the time period to fetch transactions for. Defaults"
                   "to beginning of current month. Required if end_date exists. "
                   "Format: YYYY-MM-DD.")
@click.option("--end-date", default=None,
              help="Denotes the end of the time period you'd like to get transactions for. "
                   "Defaults to end of current month. Required if start_date exists."
                   "Format: YYYY-MM-DD.")
@click.option("--tag-id", default=None,
              help="Filter by tag. Only accepts IDs, not names.")
@click.option("--recurring-id", default=None, help="Filter by recurring expense")
@click.option("--plaid-account-id", default=None, help="Filter by Plaid account")
@click.option("--category-id", default=None,
              help="Filter by category. Will also match category groups.")
@click.option("--asset-id", default=None, help="Filter by asset")
@click.option("--group-id", default=None,
              help="Filter by group_id (if the transaction is part of a specific group)")
@click.option("--is-group", default=None, help="Filter by group (returns transaction groups)")
@click.option("--status", default=None,
              help="Filter by status (Can be cleared or uncleared. For recurring "
                   "transactions, use recurring)")
@click.option("--offset", default=None, help="Sets the offset for the records returned")
@click.option("--limit", default=None,
              help="Sets the maximum number of records to return. Note: The server will not "
                   "respond with any indication that there are more records to be returned. "
                   "Please check the response length to determine if you should make another "
                   "call with an offset to fetch more transactions.")
@click.option("--debit-as-negative", default=None,
              help="Pass in true if you’d like expenses to be returned as negative amounts and "
                   "credits as positive amounts. Defaults to false.")
def lunchmoney_transactions(**kwargs):
    """
    Retrieve Lunch Money Transactions
    """
    lunch = LunchMoney()
    transactions = lunch.get_transactions(**kwargs)
    click.echo(json.dumps(transactions, default=pydantic_encoder, indent=2))


@cli.group()
@click.pass_context
def splitlunch(ctx):
    """
    Interact with the Splitwise Plugin for lunchable, SplitLunch 💲🍱
    """
    pass


@splitlunch.command("expenses")
@click.option("--limit", default=None, help="Limit the amount of Results. 0 returns everything.")
@click.option("--offset", default=None,
              help="Number of expenses to be skipped")
@click.option("--limit", default=None,
              help="Number of expenses to be returned")
@click.option("--group-id", default=None,
              help="GroupID of the expenses")
@click.option("--friendship-id", default=None,
              help="FriendshipID of the expenses")
@click.option("--dated-after", default=None,
              help="ISO 8601 Date time. Return expenses later that this date")
@click.option("--dated-before", default=None,
              help="ISO 8601 Date time. Return expenses earlier than this date")
@click.option("--updated-after", default=None,
              help="ISO 8601 Date time. Return expenses updated after this date")
@click.option("--updated-before", default=None,
              help="ISO 8601 Date time. Return expenses updated before this date")
def splitlunch_expenses(**kwargs):
    """
    Retrieve Splitwise Expenses
    """
    splitlunch = SplitLunch()
    expenses = splitlunch.get_expenses(**kwargs)
    click.echo(json.dumps(expenses, default=pydantic_encoder, indent=2))


@splitlunch.command("make-splitlunch")
@click.option("--tag-transactions", is_flag=True,
              help="Tag the resulting transactions with a `Splitwise` tag.")
def make_splitlunch(**kwargs) -> List[int]:
    """
    Split all `SplitLunch` tagged transactions in half.

    One of these new splits will be recategorized to `Reimbursement`.
    """
    splitlunch = SplitLunch()
    results = splitlunch.make_splitlunch(**kwargs)
    click.echo(json.dumps(results, default=pydantic_encoder))


@splitlunch.command("make-splitlunch-import")
@click.option("--tag-transactions", is_flag=True,
              help="Tag the resulting transactions with a `Splitwise` tag.")
def make_splitlunch_import(**kwargs) -> List[int]:
    """
    Import `SplitLunchImport` tagged transactions to Splitwise and Split them in Lunch Money

    Send a transaction to Splitwise and then split the original transaction in Lunch Money.
    One of these new splits will be recategorized to `Reimbursement`. Any tags will be
    reapplied.
    """
    splitlunch = SplitLunch()
    results = splitlunch.make_splitlunch_import(**kwargs)
    click.echo(json.dumps(results, default=pydantic_encoder))


@splitlunch.command("update-splitwise-balance")
def update_splitwise_balance():
    """
    Update the Splitwise Asset Balance
    """
    splitlunch = SplitLunch()
    updated_asset = splitlunch.update_splitwise_balance()
    click.echo(json.dumps(updated_asset, default=pydantic_encoder, indent=2))

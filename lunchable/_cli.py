"""
Lunchmoney CLI
"""

import logging
import sys
from json import JSONDecodeError
from typing import Any, Dict, Optional

import click
import httpx
from click_plugins import with_plugins
from importlib_metadata import entry_points
from pydantic_core import to_jsonable_python
from rich import print, print_json, traceback

import lunchable
from lunchable import LunchMoney
from lunchable._config.logging_config import set_up_logging
from lunchable.models import LunchableModel

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


@click.group(invoke_without_command=True)
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
    set_up_logging(log_level=logging.DEBUG if debug is True else logging.INFO)
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


@cli.group()
def transactions() -> None:
    """
    Interact with Lunch Money transactions
    """


@cli.group()
def plugins() -> None:
    """
    Interact with Lunchable Plugins

    Install lunchable with the "plugins" extra to get
    all the known plugins

    pipx install "lunchable[plugins]"
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
def lunchmoney_transactions(
    context: LunchMoneyContext, **kwargs: Dict[str, Any]
) -> None:
    """
    Retrieve Lunch Money Transactions
    """
    lunch = LunchMoney(access_token=context.access_token)
    transactions = lunch.get_transactions(**kwargs)  # type: ignore[arg-type]
    json_data = to_jsonable_python(transactions)
    print_json(data=json_data)


@cli.command()
@click.argument("URL")
@click.option("-X", "--request", default="GET", help="Specify request command to use")
@click.option("-d", "--data", default=None, help="HTTP POST data")
@click.pass_obj
def http(context: LunchMoneyContext, url: str, request: str, data: str) -> None:
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
    resp = lunch.request(
        method=request,
        url=url_request,
        content=data,
    )
    try:
        resp.raise_for_status()
    except httpx.HTTPError:
        logger.error(resp)
        print(resp.text)
        sys.exit(1)
    try:
        response = resp.json()
    except JSONDecodeError:
        response = resp.text
    json_data = to_jsonable_python(response)
    print_json(data=json_data)


discovered_plugins = entry_points(group="lunchable.cli")
with_plugins(discovered_plugins)(plugins)

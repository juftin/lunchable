"""
Lunchmoney CLI
"""

import json
import logging
from typing import List

import click
from pydantic.json import pydantic_encoder

import lunchable
from lunchable.plugins.splitlunch import SplitLunch

logger = logging.getLogger(__name__)


@click.group()
@click.version_option(lunchable.__version__)
@click.option("--json/--no-json", default=False, help="Disable Logging Output for pure JSON")
@click.option("--debug/--no-debug", default=False, help="Enable Debugging (verbose) output")
@click.pass_context
def cli(ctx, debug, json):
    """
    lunchable interactions with Lunch Money 🍱
    """
    ctx.ensure_object(dict)
    ctx.obj["DEBUG"] = debug
    ctx.obj["JSON"] = json


@cli.group()
@click.pass_context
def splitlunch(ctx):
    """
    Interact with the Splitwise Plugin for lunchable, SplitLunch 💲🍱
    """
    pass


@splitlunch.command("expenses")
@click.option("--limit", default=None, help="Limit the amount of Results. 0 returns everything.")
def expenses(limit: int):
    """
    Retrieve Splitwise Expenses
    """
    splitlunch = SplitLunch()
    expenses = splitlunch.get_expenses(limit=limit)
    click.echo(json.dumps(expenses, default=pydantic_encoder, indent=2))


@splitlunch.command("make-splitlunch")
@click.option("--tag-transactions", is_flag=True,
              help="Tag the resulting transactions with a `Splitwise` tag.")
def make_splitlunch(tag_transactions) -> List[int]:
    """
    Split all transactions with a `SplitLunch` tag in half
    """
    splitlunch = SplitLunch()
    results = splitlunch.make_splitlunch(tag_transactions=tag_transactions)
    click.echo(json.dumps(results, default=pydantic_encoder))

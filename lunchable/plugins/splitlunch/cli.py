import datetime
import logging
from typing import Optional, Union

import click
from pydantic_core import to_jsonable_python
from rich import print_json

logger = logging.getLogger(__name__)


@click.group
def splitlunch() -> None:
    """
    Splitwise Plugin for lunchable, SplitLunch 💲🍱
    """
    pass


dated_after = click.option(
    "--dated-after",
    default=None,
    help="ISO 8601 Date time. Return expenses later that this date",
)
dated_before = click.option(
    "--dated-before",
    default=None,
    help="ISO 8601 Date time. Return expenses earlier than this date",
)


@splitlunch.command("expenses")
@click.option(
    "--limit", default=None, help="Limit the amount of Results. 0 returns everything."
)
@click.option("--offset", default=None, help="Number of expenses to be skipped")
@click.option("--limit", default=None, help="Number of expenses to be returned")
@click.option("--group-id", default=None, help="GroupID of the expenses")
@click.option("--friendship-id", default=None, help="FriendshipID of the expenses")
@dated_after
@dated_before
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
def splitlunch_expenses(**kwargs: Union[int, str, bool]) -> None:
    """
    Retrieve Splitwise Expenses
    """
    from lunchable.plugins.splitlunch.lunchmoney_splitwise import SplitLunch

    splitlunch = SplitLunch()
    if set(kwargs.values()) == {None}:
        kwargs["limit"] = 5
    expenses = splitlunch.get_expenses(**kwargs)  # type: ignore[arg-type]
    json_data = to_jsonable_python(expenses)
    print_json(data=json_data)


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
def make_splitlunch(**kwargs: Union[int, str, bool]) -> None:
    """
    Split all `SplitLunch` tagged transactions in half.

    One of these new splits will be recategorized to `Reimbursement`.
    """
    from lunchable.plugins.splitlunch.lunchmoney_splitwise import SplitLunch

    splitlunch = SplitLunch()
    results = splitlunch.make_splitlunch(**kwargs)  # type: ignore[arg-type]
    json_data = to_jsonable_python(results)
    print_json(data=json_data)


@splitlunch.command("splitlunch-import")
@tag_transactions
@financial_partner_id
@financial_partner_email
@financial_partner_group_id
def make_splitlunch_import(**kwargs: Union[int, str, bool]) -> None:
    """
    Import `SplitLunchImport` tagged transactions to Splitwise and Split them in Lunch Money

    Send a transaction to Splitwise and then split the original transaction in Lunch Money.
    One of these new splits will be recategorized to `Reimbursement`. Any tags will be
    reapplied.
    """
    from lunchable.plugins.splitlunch.lunchmoney_splitwise import SplitLunch

    financial_partner_id: Optional[int] = kwargs.pop("financial_partner_id")  # type: ignore[assignment]
    financial_partner_email: Optional[str] = kwargs.pop("financial_partner_email")  # type: ignore[assignment]
    financial_partner_group_id: Optional[int] = kwargs.pop("financial_partner_group_id")  # type: ignore[assignment]
    splitlunch = SplitLunch(
        financial_partner_id=financial_partner_id,
        financial_partner_email=financial_partner_email,
        financial_partner_group_id=financial_partner_group_id,
    )
    results = splitlunch.make_splitlunch_import(**kwargs)  # type: ignore[arg-type]
    json_data = to_jsonable_python(results)
    print_json(data=json_data)


@splitlunch.command("splitlunch-direct-import")
@tag_transactions
@financial_partner_id
@financial_partner_email
@financial_partner_group_id
def make_splitlunch_direct_import(**kwargs: Union[int, str, bool]) -> None:
    """
    Import `SplitLunchDirectImport` tagged transactions to Splitwise and Split them in Lunch Money

    Send a transaction to Splitwise and then split the original transaction in Lunch Money.
    One of these new splits will be recategorized to `Reimbursement`. Any tags will be
    reapplied.
    """
    from lunchable.plugins.splitlunch.lunchmoney_splitwise import SplitLunch

    financial_partner_id: Optional[int] = kwargs.pop("financial_partner_id")  # type: ignore[assignment]
    financial_partner_email: Optional[str] = kwargs.pop("financial_partner_email")  # type: ignore[assignment]
    financial_partner_group_id: Optional[int] = kwargs.pop("financial_partner_group_id")  # type: ignore[assignment]
    splitlunch = SplitLunch(
        financial_partner_id=financial_partner_id,
        financial_partner_email=financial_partner_email,
        financial_partner_group_id=financial_partner_group_id,
    )
    results = splitlunch.make_splitlunch_direct_import(**kwargs)  # type: ignore[arg-type]
    json_data = to_jsonable_python(results)
    print_json(data=json_data)


@splitlunch.command("update-balance")
def update_splitwise_balance() -> None:
    """
    Update the Splitwise Asset Balance
    """
    from lunchable.plugins.splitlunch.lunchmoney_splitwise import SplitLunch

    splitlunch = SplitLunch()
    updated_asset = splitlunch.update_splitwise_balance()
    json_data = to_jsonable_python(updated_asset)
    print_json(data=json_data)


@splitlunch.command("refresh")
@dated_after
@dated_before
@click.option(
    "--allow-self-paid/--no-allow-self-paid",
    default=False,
    help="Allow self-paid expenses to be imported (filtered out by default).",
)
@click.option(
    "--allow-payments/--no-allow-payments",
    default=False,
    help="Allow payments to be imported (filtered out by default).",
)
def refresh_splitwise_transactions(
    dated_before: Optional[datetime.datetime],
    dated_after: Optional[datetime.datetime],
    allow_self_paid: bool,
    allow_payments: bool,
) -> None:
    """
    Import New Splitwise Transactions to Lunch Money and

    This function gets all transactions from Splitwise, all transactions from
    your Lunch Money Splitwise account and compares the two. This also updates
    the account balance.
    """
    import lunchable.plugins.splitlunch.lunchmoney_splitwise

    splitlunch = lunchable.plugins.splitlunch.lunchmoney_splitwise.SplitLunch()
    response = splitlunch.refresh_splitwise_transactions(
        dated_before=dated_before,
        dated_after=dated_after,
        allow_self_paid=allow_self_paid,
        allow_payments=allow_payments,
    )
    json_data = to_jsonable_python(response)
    print_json(data=json_data)

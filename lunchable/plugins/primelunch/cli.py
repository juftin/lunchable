import click


@click.group
def primelunch() -> None:
    """
    PrimeLunch CLI - Syncing LunchMoney with Amazon
    """


@primelunch.command("run")
@click.option(
    "-f",
    "--file",
    "csv_file",
    type=click.Path(exists=True, resolve_path=True),
    help="File Path of the Amazon Export",
    required=True,
)
@click.option(
    "-w",
    "--window",
    "window",
    type=click.INT,
    help="Allowable time window between Amazon transaction date and "
    "credit card transaction date",
    default=7,
)
@click.option(
    "-a",
    "--all",
    "update_all",
    is_flag=True,
    type=click.BOOL,
    help="Whether to skip the confirmation step and simply update all matched "
    "transactions",
    default=False,
)
@click.option(
    "-t",
    "--token",
    "access_token",
    type=click.STRING,
    help="LunchMoney Access Token - defaults to the LUNCHMONEY_ACCESS_TOKEN environment variable",
    envvar="LUNCHMONEY_ACCESS_TOKEN",
)
def run_primelunch(
    csv_file: str, window: int, update_all: bool, access_token: str
) -> None:
    """
    Run the PrimeLunch Update Process
    """
    from lunchable.plugins.primelunch.primelunch import PrimeLunch

    primelunch = PrimeLunch(
        file_path=csv_file, time_window=window, access_token=access_token
    )
    primelunch.process_transactions(confirm=not update_all)

import click


@click.group
def pushlunch() -> None:
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
def notify(continuous: bool, interval: int, user_key: str) -> None:
    """
    Send a Notification for each Uncleared Transaction
    """
    from lunchable.plugins.pushlunch.pushover import PushLunch

    push = PushLunch(user_key=user_key)
    if interval is not None:
        interval = int(interval)
    push.notify_uncleared_transactions(continuous=continuous, interval=interval)

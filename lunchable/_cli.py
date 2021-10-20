"""
Lunchmoney CLI
"""

import argparse
from json import dumps
import logging
from typing import List

from pydantic.json import pydantic_encoder

from lunchable import __lunchable__
from lunchable import __version__ as lunchable_version

logger = logging.getLogger(__name__)


def generate_parser() -> argparse.ArgumentParser:
    """
    Generate the Parser

    Returns
    -------
    argparse.ArgumentParser
    """
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument("-v", "--version",
                               action="version",
                               version=f"%(prog)s {lunchable_version}")
    parent_parser.add_argument("--json",
                               action="store_true",
                               help="Disable Logging Output for pure JSON")

    parser = argparse.ArgumentParser(
        prog=__lunchable__,
        description="lunchable interactions with Lunch Money 🍱",
        parents=[parent_parser],
        epilog="bye bye"
    )

    subparsers = parser.add_subparsers(dest="command")

    splitlunch = subparsers.add_parser(
        prog="SplitLunch",
        name="splitlunch",
        parents=[parent_parser],
        help="Interact with the Splitwise Plugin for lunchable, SplitLunch",
        description="Interact with the Splitwise Plugin for lunchable, SplitLunch 💲🍱",
        epilog=parser.epilog)

    return parser


def handle_splitlunch(parser: argparse.ArgumentParser,
                      namespace: argparse.Namespace,
                      args: List[str]) -> None:
    """
    Handle the CLI Arguments

    Parameters
    ----------
    parser: argparse.ArgumentParser
    namespace: argparse.Namespace
    args: List[str]
    """
    from lunchable.plugins.splitlunch import SplitLunch, SplitLunchError
    try:
        splitlunch = SplitLunch()
    except SplitLunchError:
        exit(1)
    expenses = splitlunch.get_expenses(limit=3)
    if namespace.json is False:
        for expense in expenses:
            logger.info("%s\n", expense)
    else:
        print(dumps(expenses, default=pydantic_encoder, indent=2))


def handle_arguments(parser: argparse.ArgumentParser,
                     namespace: argparse.Namespace,
                     args: List[str]) -> None:
    """
    Handle the CLI Arguments

    Parameters
    ----------
    parser: argparse.ArgumentParser
    namespace: argparse.Namespace
    args: List[str]

    Returns
    -------
    None
    """
    if namespace.command == "splitlunch":
        handle_splitlunch(parser=parser,
                          namespace=namespace,
                          args=args)
    elif len(args) == 0 or namespace.command is None:
        parser.print_help()


def main():
    """
    CLI Main
    """
    parser = generate_parser()
    namespace, args = parser.parse_known_args()
    if namespace.json is False:
        logging.basicConfig(level=logging.INFO,
                            format="%(asctime)s [%(levelname)8s]: %(message)s [%(name)s]")
    handle_arguments(parser=parser, namespace=namespace, args=args)
    logger.info((namespace, args))


if __name__ == "__main__":
    main()

"""
PrimeLunch Utils
"""

from __future__ import annotations

import datetime
import logging
import os
import pathlib
from typing import Any, Dict, List, Optional

import click
import numpy as np
import pandas as pd
from numpy import datetime64
from rich import print, table
from rich.prompt import Confirm

from lunchable import LunchMoney, TransactionUpdateObject
from lunchable._config.logging_config import set_up_logging
from lunchable.models import TransactionObject

logger = logging.getLogger(__name__)


class PrimeLunch:
    """
    PrimeLunch: Amazon Notes Updater
    """

    def __init__(self, file_path: str | os.PathLike, time_window: int = 5) -> None:
        """
        Initialize and set internal data
        """
        self.file_path = pathlib.Path(file_path)
        self.time_window = time_window
        self.transaction_map: Dict[int, TransactionObject] = {}
        self.cached = False
        self.lunch = LunchMoney()

    @staticmethod
    def transactions_to_df(transactions: List[TransactionObject]) -> pd.DataFrame:
        """
        Convert Transactions Array to DataFrame

        Parameters
        ----------
        transactions: List[TransactionObject]

        Returns
        -------
        pd.DataFrame
        """
        return pd.DataFrame(
            [item.dict() for item in transactions],
            columns=TransactionObject.__fields__.keys(),
        )

    @staticmethod
    def df_to_transactions(df: pd.DataFrame) -> List[TransactionObject]:
        """
        Convert DataFrame to Transaction Array

        Parameters
        ----------
        df: pd.DataFrame

        Returns
        -------
        List[TransactionObject]
        """
        array_df = df.copy()
        array_df = array_df.fillna(np.nan).replace([np.nan], [None])
        transaction_array = array_df.to_dict(orient="records")
        return [TransactionObject(**item) for item in transaction_array]

    def amazon_to_df(self) -> pd.DataFrame:
        """
        Read an Amazon Data File to a DataFrame

        This is pretty simple, except duplicate header rows need to be cleaned

        Parameters
        ----------
        file_path: os.PathLike

        Returns
        -------
        pd.DataFrame
        """
        dt64: np.dtype[datetime64] = np.dtype("datetime64[ns]")
        string = pd.StringDtype(storage="python")
        expected_columns = {
            "order id": string,
            "items": string,
            "to": string,
            "date": dt64,
            "total": float,
            "shipping": float,
            "shipping_refund": float,
            "gift": float,
            "tax": float,
            "refund": float,
            "payments": string,
        }
        amazon_df = pd.read_csv(
            self.file_path,
            usecols=expected_columns.keys(),
        )
        header_row_eval = pd.concat(
            [amazon_df[item] == item for item in expected_columns.keys()], axis=1
        ).all(axis=1)
        duplicate_header_rows = np.where(header_row_eval)[0]
        amazon_df.drop(duplicate_header_rows, axis=0, inplace=True)
        amazon_df = amazon_df.astype(dtype=expected_columns, copy=True, errors="raise")
        logger.info("Amazon Data File loaded: %s", self.file_path)
        return amazon_df

    @classmethod
    def filter_amazon_transactions(cls, df: pd.DataFrame) -> pd.DataFrame:
        """
        Filter a DataFrame to Amazon Transactions

        Parameters
        ----------
        df: pd.DataFrame

        Returns
        -------
        pd.DataFrame
        """
        amazon_transactions = df.copy()
        amazon_transactions["original_name"] = amazon_transactions[
            "original_name"
        ].fillna("")
        amazon_transactions = amazon_transactions[
            amazon_transactions.payee.str.lower().str.contains("amazon")
            | amazon_transactions.original_name.str.lower().str.contains("amazon")
        ]
        return amazon_transactions

    @classmethod
    def deduplicate_matched(cls, df: pd.DataFrame) -> pd.DataFrame:
        """
        Deduplicate Multiple Connections Made

        Parameters
        ----------
        df: pd.DataFrame

        Returns
        -------
        pd.DataFrame
        """
        deduped = df.copy()
        deduped["duplicated"] = deduped.duplicated(subset=["id"], keep=False)
        deduped = deduped[deduped["duplicated"] == False]  # noqa:E712
        return deduped

    @classmethod
    def merge_transactions(
        cls, amazon: pd.DataFrame, transactions: pd.DataFrame, time_range: int = 5
    ) -> pd.DataFrame:
        """
        Merge Amazon Transactions and LunchMoney Transaction

        Parameters
        ----------
        amazon: pd.DataFrame
        transactions: pd.DataFrame
        time_range: int
            Number of days used to connect credit card transactions with
            Amazon transactions

        Returns
        -------
        pd.DataFrame
        """
        merged_data = transactions.copy()
        merged_data = merged_data.merge(
            amazon,
            how="inner",
            left_on=["amount"],
            right_on=["total"],
            suffixes=(None, "_amazon"),
        )
        merged_data["start_date"] = merged_data["date_amazon"]
        merged_data["end_date"] = merged_data["start_date"] + datetime.timedelta(
            days=time_range
        )
        merged_data.query(
            "start_date <= date <= end_date",
            inplace=True,
        )
        merged_data["notes"] = merged_data["items"]
        deduplicated = cls.deduplicate_matched(df=merged_data)
        logger.info("%s Matching Amazon Transactions Identified", len(deduplicated))
        return deduplicated[TransactionObject.__fields__.keys()]

    def cache_transactions(
        self, start_date: datetime.date, end_date: datetime.date
    ) -> Dict[int, TransactionObject]:
        """
        Cache Transactions to Memory

        Parameters
        ----------
        start_date : datetime.date
        end_date : datetime.date

        Returns
        -------
        Dict[int, TransactionObject]
        """
        end_cache_date = end_date + datetime.timedelta(days=self.time_window)
        logger.info(
            "Fetching LunchMoney transactions between %s and %s",
            start_date,
            end_cache_date,
        )
        transactions = self.lunch.get_transactions(
            start_date=start_date, end_date=end_cache_date
        )
        transaction_map = {item.id: item for item in transactions}
        self.transaction_map = transaction_map
        self.cached = True
        logger.info("%s transactions returned from LunchMoney", len(transactions))
        return transaction_map

    @classmethod
    def print_transaction(
        cls, transaction: TransactionObject, former_transaction: TransactionObject
    ) -> None:
        """
        Print a Transaction for interactive input
        """
        transaction_table = table.Table(show_header=False)
        notes_table = table.Table(show_header=False)
        transaction_table.add_row("🛒 Transaction ID", str(former_transaction.id))
        transaction_table.add_row("🏦 Payee", former_transaction.payee)
        transaction_table.add_row("📅 Date", str(former_transaction.date))
        transaction_table.add_row(
            "💰 Amount", "$" + str(round(former_transaction.amount, 2))
        )
        if (
            former_transaction.original_name is not None
            and former_transaction.original_name != former_transaction.payee
        ):
            transaction_table.add_row(
                "🏦 Original Payee", former_transaction.original_name
            )
        if former_transaction.notes is not None:
            transaction_table.add_row("📝 Notes", former_transaction.notes)
        notes_table.add_row(
            "🗒  Amazon Notes", transaction.notes.strip()  # type: ignore[union-attr]
        )
        print()
        print(transaction_table)
        print(notes_table)

    def update_transaction(
        self, transaction: TransactionObject, confirm: bool = True
    ) -> Optional[Dict[str, Any]]:
        """
        Update a Transaction's Notes if they've changed

        Parameters
        ----------
        transaction: TransactionObject
        confirm: bool

        Returns
        -------
        Optional[Dict[str, Any]]
        """
        former_transaction = self.transaction_map[transaction.id]
        response = None
        if former_transaction.notes != transaction.notes.strip():  # type: ignore[union-attr]
            confirmation = True
            if confirm is True:
                self.print_transaction(
                    transaction=transaction, former_transaction=former_transaction
                )
                confirmation = Confirm.ask(
                    f"\t❓ Should we update transaction #{transaction.id}?"
                )
            if confirmation is True:
                response = self.lunch.update_transaction(
                    transaction_id=transaction.id,
                    transaction=TransactionUpdateObject(
                        notes=transaction.notes.strip()  # type: ignore[union-attr]
                    ),
                )
                if confirm is True:
                    print(f"\t✅ Transaction #{transaction.id} updated")
        return response

    def process_transactions(self, confirm: bool = True):
        """
        Run the End-to-End Process
        """
        logger.info(
            "Beginning search to match Amazon and LunchMoney - using %s day window",
            self.time_window,
        )
        amazon_df = self.amazon_to_df()
        min_date = amazon_df["date"].min().to_pydatetime().date()
        max_date = amazon_df["date"].max().to_pydatetime().date()
        logger.info(
            "%s Amazon transactions loaded ranging from %s to %s",
            len(amazon_df),
            min_date,
            max_date,
        )
        self.cache_transactions(start_date=min_date, end_date=max_date)
        transaction_df = self.transactions_to_df(
            transactions=list(self.transaction_map.values())
        )
        amazon_transaction_df = self.filter_amazon_transactions(df=transaction_df)
        merged_data = self.merge_transactions(
            transactions=amazon_transaction_df, amazon=amazon_df, time_range=5
        )
        updated_transactions = self.df_to_transactions(df=merged_data)
        for item in updated_transactions:
            self.update_transaction(transaction=item, confirm=confirm)


@click.command("run")
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
    default=5,
)
@click.option(
    "-a",
    "--all",
    "update_all",
    type=click.BOOL,
    help="Whether to skip the confirmation step and simply update all matched "
    "transactions",
    default=False,
)
def run_primelunch(csv_file: str, window: int, update_all: bool):
    """
    Run the PrimeLunch Update Process
    """
    primelunch = PrimeLunch(file_path=csv_file, time_window=window)
    primelunch.process_transactions(confirm=not update_all)


if __name__ == "__main__":
    set_up_logging(log_level=logging.INFO)
    run_primelunch()

"""
TermLunch Base Classes
"""

import datetime
from typing import Optional, Any

import numpy as np
import pandas as pd
from textual.app import App
from textual.containers import Container
from textual.reactive import Reactive
from textual.widgets import DataTable

from lunchable.models import AssetsObject, CategoriesObject
from lunchable.plugins.base.pandas_app import LunchablePandasTransactionsApp


class RowDataTable(DataTable):
    """
    Row Highlighted DataTable
    """

    cursor_type: Reactive[str] = Reactive("row")
    header_height: Reactive[int] = Reactive(4)


class TransactionTable(RowDataTable):
    """
    RowDataTable Object: TransactionTable
    """


class TermLunchApp(LunchablePandasTransactionsApp):
    """
    Lunchable App for Textual
    """

    final_columns = {
        "date": "Date",
        "payee": "Payee",
        "amount": "Amount",
        "plaid_account_id": "Account",
        "category_id": "Category",
        "notes": "Notes",
    }

    null_account = AssetsObject(
        id=0,
        name="Unknown",
        type_name="",
        balance=0,
        balance_as_of=datetime.datetime.now(),
        currency="",
        exclude_transactions=False,
        created_at=datetime.datetime.now(),
    )
    null_category = CategoriesObject(
        id=0,
        name=" ",
        is_income=False,
        exclude_from_budget=False,
        exclude_from_totals=False,
        is_group=False,
    )

    def __init__(self, **kwargs: Any) -> None:
        """
        Initialize with DataFrame Attribute
        """
        self.transaction_df = pd.DataFrame(columns=self.final_columns.values())
        super().__init__(**kwargs)

    @classmethod
    def df_to_table(cls, df: pd.DataFrame) -> RowDataTable:
        """
        Convert Pandas DF to Textual RowDataTable

        Parameters
        ----------
        df: pd.DataFrame

        Returns
        -------
        RowDataTable
        """
        table = RowDataTable(show_header=True, zebra_stripes=True, id="transactions")
        for column in df.columns:
            table.add_column(str(column))
        for _, row in df.iterrows():
            value_list = row.to_list()
            row = [str(x) for x in value_list]
            table.add_row(*row)
        return table

    @classmethod
    def format_currency(cls, amount: float) -> str:
        """
        Format currency amounts to be pleasant and human readable

        Parameters
        ----------
        amount: float
            Float Amount to be converted into a string

        Returns
        -------
        str
        """
        if amount < 0:
            float_string = "[bold dark_green]$ ({:,.2f})[/bold dark_green]".format(
                float(abs(amount))
            )
        else:
            float_string = "[bold red]$ {:,.2f}[/bold red]".format(float(amount))
        return float_string

    def prepare_transaction_df(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Prepare a Transaction DF for Visualization

        Parameters
        ----------
        df : pd.DataFrame

        Returns
        -------
        pd.DataFrame
        """
        data = df.copy()
        data.rename(columns=self.final_columns, inplace=True)
        data.sort_values(by="Date", ascending=False, inplace=True)
        data["Category"].fillna(0, inplace=True)
        data["Category"] = data["Category"].astype(int)
        data["Amount"] = data.apply(
            lambda x: self.format_currency(
                amount=x["Amount"],
            ),
            axis=1,
        )
        data["Category"] = data["Category"].apply(
            lambda x: self.lunch_data.categories.get(x, self.null_category).name
        )
        data["Account"] = np.where(
            data["Account"].isnull(), data["asset_id"], data["Account"]
        )
        data["Account"] = data["Account"].apply(
            lambda x: self.lunch_data.asset_map.get(x, self.null_account).name
        )
        data.replace([None], [""], inplace=True)
        data["Payee"] = np.where(
            data["Payee"].str.len() > 60, data["Payee"].str[:49] + " ...", data["Payee"]
        )
        data["Notes"] = np.where(
            data["Notes"].str.len() > 90, data["Notes"].str[:49] + " ...", data["Notes"]
        )
        self.transaction_df = data[list(self.final_columns.values())]
        return self.transaction_df

    def build_transaction_table(self) -> RowDataTable:
        """
        Retrieve the Core Transactions Table
        """
        data_df = self.models_to_df(models=self.lunch_data.transactions.values())
        formatted_data = self.prepare_transaction_df(df=data_df)
        transactions_table = self.df_to_table(df=formatted_data)
        return transactions_table


class LunchMoneyTextualApp(App):
    """
    LunchMoneyTextualApp
    """

    def __init__(self, cache_time: int = 0, access_token: Optional[str] = None):
        """
        Initialize with AppLunch Dependency Injection

        Parameters
        ----------
        cache_time: int
            Amount of time until the cache should be refreshed
            (in seconds). Defaults to 0 which always polls for the latest data
        access_token: Optional[str]
        """
        super().__init__()
        self.cache_time = cache_time
        self._access_token = access_token
        self.input_access_token: Optional[str] = None
        self.lunch_app: Optional[TermLunchApp] = (
            TermLunchApp(access_token=access_token, cache_time=cache_time)
            if access_token is not None
            else None
        )
        self.transaction_table = TransactionTable(id="transactions")
        self.transaction_container = Container(self.transaction_table)

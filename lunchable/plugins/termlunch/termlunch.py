"""
Base App Class
"""

import logging
from os import getenv
from typing import Iterable

from textual.binding import Binding
from textual.widget import Widget
from textual.widgets import Footer, Header, ListView

from lunchable.plugins.termlunch.common import (
    LunchMoneyTextualApp,
    TermLunchApp,
    TransactionTable,
)
from lunchable.plugins.termlunch.widgets import (
    Body,
    DetailBar,
    LoadingPage,
    Sidebar,
    TransactionContainer,
)

logger = logging.getLogger(__name__)


class TermLunch(LunchMoneyTextualApp):
    """
    Textual App for LunchMoney
    """

    TITLE = "TermLunch"
    SUB_TITLE = "LunchMoney on the Terminal"
    CSS_PATH = "termlunch.css"

    BINDINGS = [
        Binding("d", "toggle_dark", "Toggle Dark Mode"),
        Binding(
            "q, ctrl+c, ctrl+q, ctrl+d", "app.quit", "Quit", show=True, key_display="Q"
        ),
        Binding("l", "log_out", "Log Out"),
        Binding("r", "refresh_data", "Refresh Data"),
        Binding("b", "toggle_sidebar", "Sidebar"),
    ]

    def compose(self) -> Iterable[Widget]:
        """
        Create child widgets for the app.
        """
        for column in TermLunchApp.final_columns.values():
            self.transaction_table.add_column(column)
        self.detail_bar = DetailBar()
        self.detail_bar.display = False
        self.transaction_container = TransactionContainer(
            self.transaction_table, self.detail_bar, classes="-sidebar"
        )
        self.transaction_container.display = False
        yield Header()
        yield Body(
            Sidebar(),
            LoadingPage(classes="-sidebar"),
            self.transaction_container,
        )
        yield Footer()

    def action_refresh_data(self) -> None:
        """
        An action to toggle line numbers.
        """
        raise NotImplementedError(self.app.title)

    def action_log_out(self) -> None:
        """
        An action to log out
        """
        datatable_container = self.query_one(TransactionContainer)
        datatable = self.query_one(TransactionTable)
        loading_page = self.query_one(LoadingPage)
        existing_list_view = self.query_one("#info-table", expect_type=ListView)
        existing_list_view.clear()
        datatable_container.display = False
        loading_page.display = True
        datatable.clear()
        if self.lunch_app is not None:
            self.lunch_app.delete_cache()
            self.lunch_app = None

    def action_toggle_sidebar(self) -> None:
        """
        Toggle the Sidebar
        """
        sidebar = self.query_one(Sidebar)
        datatable = self.query_one(TransactionContainer)
        loading_page = self.query_one(LoadingPage)
        self.set_focus(None)
        if sidebar.has_class("-hidden"):
            sidebar.remove_class("-hidden")
            datatable.add_class("-sidebar")
            loading_page.add_class("-sidebar")
        else:
            if sidebar.query("*:focus"):
                self.screen.set_focus(None)
            sidebar.add_class("-hidden")
            datatable.remove_class("-sidebar")
            loading_page.remove_class("-sidebar")


if __name__ == "__main__":
    access_token = getenv("LUNCHMONEY_ACCESS_TOKEN", None)
    app = TermLunch(cache_time=60 * 60 * 60, access_token=access_token)
    app.run()

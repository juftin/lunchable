"""
Textual Widgets for the TermLunch App
"""

from os import getenv
from pathlib import Path
from textwrap import dedent
from typing import Iterable, List

from rich.markdown import Markdown
from rich_pixels import Pixels
from textual.containers import Container, Horizontal, Vertical
from textual.demo import Title
from textual.widget import Widget
from textual.widgets import Button, Input, Label, ListItem, ListView, Static, Switch

from lunchable.plugins.termlunch.common import RowDataTable, TermLunchApp


class Section(Container):
    """
    Container Object: Section
    """


class SectionTitle(Static):
    """
    Static Object: SectionTitle
    """


class Column(Container):
    """
    Container Object: Column
    """


class TextContent(Static):
    """
    Static Object: TextContent
    """


class Body(Container):
    """
    Container Object: Body
    """


class LoadingPage(Container):
    """
    Loading Page
    """

    WELCOME_MD = dedent(
        """

    **Welcome**!

    **LunchTerm** is a TUI app for
    interacting with [LunchMoney](https://lunchmoney.app) on the terminal

    """
    )

    lunch_image_path = Path(__file__).with_name("mascot.png")

    def compose(self) -> Iterable[Widget]:
        """
        Welcome Widgets
        """
        size = 25
        image = Pixels.from_image_path(path=self.lunch_image_path, resize=(size, size))
        yield Column(
            Section(
                SectionTitle(self.app.title),
                TextContent(Markdown(self.WELCOME_MD)),
                LoginContainer(),
                Static(image),
            )
        )


class LoginContainer(Container):
    """
    Welcome Container
    """

    access_token = getenv("LUNCHMONEY_ACCESS_TOKEN", None)

    def compose(self) -> Iterable[Widget]:
        """
        Welcome Widgets
        """
        yield Static("LunchMoney Access Token")
        yield Static()
        self.app.input_access_token = Input(
            placeholder="LunchMoney Access Token",
            password=True,
            value=self.access_token,
        )
        yield self.app.input_access_token
        yield Static()
        yield Button("Login", variant="success")
        yield Static()
        if self.access_token is None:
            yield Static(
                Markdown(
                    "Enter your [LunchMoney Access Token](https://my.lunchmoney.app/developers) "
                    "above or optionally set it as "
                    "the **LUNCHMONEY_ACCESS_TOKEN** environment variable."
                )
            )
        yield Static(id="error-message")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """
        On Enter Key Being Pressed
        """
        self.run_auth_flow()

    def key_enter(self) -> None:
        """
        On Enter Key Being Pressed
        """
        self.run_auth_flow()

    def run_auth_flow(self) -> None:
        """
        Button Pressed Trigger
        """
        access_token_input = self.query_one(Input).value
        self.app.log.error((access_token_input, self.app.lunch_app))
        try:
            self.app.lunch_app = TermLunchApp(
                access_token=access_token_input, cache_time=self.app.cache_time
            )
            self.app.log.error((access_token_input, self.app.lunch_app.__dict__))
            self.app.lunch_app.get_latest_cache()
            self.app.lunch_app.build_transaction_table()
            self.app.log.error((access_token_input, self.app.lunch_app.__dict__))
            info_table = self.app.query_one(InfoTable)
            existing_list_view = self.app.query_one("#info-table", expect_type=ListView)
            list_items = info_table.sync_data()
            existing_list_view.clear()
            for item in list_items:
                existing_list_view.append(item)
            app_table = self.app.query_one(RowDataTable)
            app_table.clear()
            for value_list in self.app.lunch_app.transaction_df.values.tolist():
                row = [str(x) for x in value_list]
                app_table.add_row(*row)
            above_the_fold = self.app.query_one(LoadingPage)
            above_the_fold.display = False
            self.app.transaction_container.display = True
        except EnvironmentError:
            button = self.query_one("#error-message", expect_type=Static)
            error_message = (
                "[bold red]That token wasn't accepted, try again.[/bold red]"
            )
            button.update(error_message)


class TransactionContainer(Horizontal):
    """
    Transaction Container
    """

    def on_mount(self) -> None:
        """
        Handle Sidebar on Mount
        """
        sidebar = self.app.query_one(Sidebar)
        datatable = self.app.query_one(TransactionContainer)
        if not sidebar.has_class("-hidden"):
            datatable.add_class("-sidebar")


class InfoTable(Container):
    """
    User Information Table
    """

    def sync_data(self) -> List[ListItem]:
        """
        Grab the Latest Data
        """
        list_items = []
        if hasattr(self.app.lunch_app, "lunch_data"):
            data = self.app.lunch_app.lunch_data.user
            list_items.append(
                ListItem(Label(Markdown(f"### **Budget**: *{data.budget_name}*")))
            )
            list_items.append(
                ListItem(Label(Markdown(f"### **Email**: *{data.user_email}*")))
            )
            list_items.append(
                ListItem(Label(Markdown(f"### **Username**: *{data.user_name}*")))
            )
            list_items.append(
                ListItem(Label(Markdown(f"### **API Key**: *{data.api_key_label}*")))
            )
        return list_items

    def compose(self) -> Iterable[Widget]:
        """
        Generate Static Table
        """
        yield ListView(id="info-table")


class Sidebar(Container):
    """
    Lunchable SideBar
    """

    def compose(self) -> Iterable[Widget]:
        """
        Yield the Widgets
        """
        yield Title(self.app.title)
        yield InfoTable()
        yield AppButtonContainer(
            DarkSwitch(),
            LogOutButton(),
            QuitButton(),
        )


class DetailBar(Container):
    """
    Lunchable Detail Bar
    """

    def compose(self) -> Iterable[Widget]:
        """
        Yield the Widgets
        """
        yield Title(self.app.title)


class DarkSwitch(Horizontal):
    """
    Dark Mode Toggle Switch
    """

    def compose(self) -> Iterable[Widget]:
        """
        Widget Composure
        """
        yield Switch(value=self.app.dark)
        yield Static("Toggle Dark Mode", classes="label")

    def on_mount(self) -> None:
        """
        Dark Mode Toggle Watcher
        """
        self.watch(self.app, "dark", self.on_dark_change, init=False)

    def on_dark_change(self) -> None:
        """
        Dark Mode Toggle Updater
        """
        self.query_one(Switch).value = self.app.dark

    def on_switch_changed(self, event: Switch.Changed) -> None:
        """
        Dark Mode Toggle Change
        """
        self.app.dark = event.value


class AppButton(Vertical):
    """
    Container Object: AppButton
    """


class AppButtonContainer(AppButton):
    """
    Container Object: AppButtonContainer
    """


class QuitButton(AppButton):
    """
    Dark Mode Toggle Switch
    """

    def compose(self) -> Iterable[Widget]:
        """
        Widget Composure
        """
        yield Button("Quit", variant="error")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """
        On Enter Key Being Pressed
        """
        self.app.exit()


class LogOutButton(AppButton):
    """
    Dark Mode Toggle Switch
    """

    def compose(self) -> Iterable[Widget]:
        """
        Widget Composure
        """
        yield Button("Log Out", variant="warning")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """
        On Enter Key Being Pressed
        """
        self.app.action_log_out()

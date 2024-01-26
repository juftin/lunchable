# Plugins

`lunchable` plugins are Python packages outside of the `lunchable` package that
can be installed into the same environment as `lunchable` to add additional
functionality to the CLI. To install all the known plugins, and their dependencies, install
lunchable with the `plugins` extra:

```shell
pipx install "lunchable[plugins]"
```

lunchable supports CLI plugins with other external packages. See below for what's been built
already. If you can't find what you're looking for, consider building it yourself and
opening a pull-request to add it to the list:

- [PushLunch](https://github.com/juftin/lunchable-pushlunch): Push Notifications via Pushover
- [SplitLunch](https://github.com/juftin/lunchable-splitlunch): Splitwise Integration
- [PrimeLunch](https://github.com/juftin/lunchable-primelunch): Amazon Transaction Updater

## LunchableApp

Lunchable provides a [LunchableApp](#lunchable.plugins.LunchableApp)
class that can be used to easily build plugins, apps,
and more. Notice a few of the main attributes / methods of the `LunchableApp` class:

 attribute / method                                                           | description                                                                    | type
------------------------------------------------------------------------------|--------------------------------------------------------------------------------|-------------------------------------------------------
 **`lunch`**                                                                  | The `LunchMoney` client                                                        | [LunchMoney](interacting.md#lunchmoney)
 **`data`** ¹                                                                 | The `LunchableData` object                                                     | [LunchableData](#lunchable.plugins.app.LunchableData)
 [refresh_data](#lunchable.plugins.LunchableApp.refresh_data)                 | Refresh all data (besides Transactions)                                        | `method`
 [refresh_transactions](#lunchable.plugins.LunchableApp.refresh_transactions) | Refresh transactions, takes same parameters as `LunchMoney.get_transactions()` | `method`
 [refresh](#lunchable.plugins.LunchableApp.refresh) ²                         | Refresh the data for one particular model, takes **kwargs                      | `method`
 [clear_transactions](#lunchable.plugins.LunchableApp.clear_transactions) ³   | Clear all transactions from the internal data                                  | `method`

> ¹ This attribute contains all of the data that is loaded from LunchMoney. It has attributes
> for `assets`, `categories`, `plaid_accounts`, `tags`, `transactions`, `crypto` and `user`.
> These attributes (except for `user`) are `dict[int, LunchableModel]` objects, where the key is
> the ID of the object and the value is the object itself.

> ² This method refreshes all of the data for one particular model. For example,
> `refresh(AssetsObject)` will refresh the assets on the underling `data.assets`
> attribute and return a `dict[int, AssetsObject]` object.

> ³ This the same as running `app.data.transactions.clear()`

### An Example App

```python
from __future__ import annotations

from typing import Any

from lunchable.models import AssetsObject, TransactionUpdateObject
from lunchable.plugins import LunchableApp


class MyCustomApp(LunchableApp):
    """
    My Custom App
    """

    def do_something_with_assets(self) -> None:
        """
        Do something with the assets
        """
        if not self.data.assets:
            # If the data hasn't been loaded yet, load it
            # The following method loads all of the data besides Transactions
            # (Assets, Categories, Plaid Accounts, Tags, Crypto, User)
            self.refresh_data()
        for asset_id, asset in self.data.assets.items():
            # Do something with the asset
            print(asset_id, asset)

    def do_something_with_transactions(self) -> None:
        """
        Do something with the transactions
        """
        if not self.data.transactions:
            # If the transactions haven't been loaded yet, load them
            self.refresh_transactions(start_date="2021-01-01", end_date="2021-01-31")
        # Refresh the latest assets
        latest_assets: dict[int, AssetsObject] = self.refresh(model=AssetsObject)
        for transaction_id, transaction in self.data.transactions.items():
            if transaction.asset_id:
                asset = latest_assets[transaction.asset_id]
                print(transaction_id, transaction, asset)

    def update_transaction(self, transaction_id: int, payee: str) -> dict[str, Any]:
        """
        You can do anything you want with the `self
        """
        update_transaction = TransactionUpdateObject(payee=payee)
        response = self.lunch.update_transaction(transaction_id=transaction_id,
                                                 transaction=update_transaction)
        return response


if __name__ == "__main__":
    app = MyCustomApp(access_token="xxxxxxxx")
    app.do_something_with_assets()
    app.do_something_with_transactions()
    app.update_transaction(transaction_id=12345, payee="New Payee")
```

#### Choose a subset of data to load

If you don't want to load all of the data, you can specify which data you want to load by
specifying the `lunchable_models` attribute of the `LunchableApp` class. The following example
will only sync the `assets` and `plaid_accounts` data when the `refresh_data()` method is called:

```python
from __future__ import annotations

from typing import ClassVar

from lunchable.models import AssetsObject, PlaidAccountObject, LunchableModel

from lunchable.plugins import LunchableApp


class CustomApp(LunchableApp):
    """
    Custom Lunchable App

    This app syncs Plaid Accounts and Assets when its `refresh_data` method
    is called.
    """

    lunchable_models: ClassVar[list[type[LunchableModel]]] = [
        PlaidAccountObject,
        AssetsObject,
    ]

    def do_something_with_assets(self) -> None:
        """
        Do something with the assets
        """
        if not self.data.plaid_accounts:
            self.refresh_data()
        for plaid_account_id, plaid_account in self.data.plaid_accounts.items():
            print(plaid_account_id, plaid_account)
```

## Building a Plugin

Plugins are built separate Python packages and are detected by lunchable via
the `lunchable.cli` entrypoint, these are
[click](https://github.com/pallets/click/) command line applications.
To add your own plugin to lunchable you'll need to add a new entrypoint to
your package. The below example shows how to do this with hatch, a modern,
standards-based Python package manager:

```python
import click


@click.group
def plugin_name():
    """
    Plugin description
    """
    pass


@plugin_name.command
def command():
    """
    Plugin description
    """
    pass
```

```toml
[project.entry-points."lunchable.cli"]
your-package = "your_package.cli:plugin_name"
```

The above example will add a new `command` / `group` to the lunchable `plugins` CLI. When
your package is installed into the same environment as lunchable, your plugin will be
accessible via the `lunchable plugins` command:

```shell
lunchable plugins plugin-name command
```

## API Documentation

::: lunchable.plugins.LunchableApp
    handler: python
    options:
        show_bases: false
        allow_inspection: true
        inherited_members: true
        group_by_category: true
        heading_level: 3
        show_source: false

::: lunchable.plugins.app.LunchableData
    handler: python
    options:
        show_bases: false
        allow_inspection: true
        group_by_category: true
        heading_level: 3
        show_source: false

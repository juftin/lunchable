# Author::    Justin Flannery  (mailto:juftin@juftin.com)

"""
Lunch Money Python SDK - This Module Leverages Class Inheritance to
Distribute API Methods Across a series of files. Ultimately, everything
inherits from the lunchmoney.sdk.core.LunchMoneyCore class which facilitates
interacting with the API.

For example: to see source code on interactions with the "transactions" API endpoint you
will refer to the _LunchMoneyTransactions object.
"""

from .assets import _LunchMoneyAssets
from .budgets import _LunchMoneyBudgets
from .plaid_accounts import _LunchMoneyPlaidAccounts
from .recurring_expenses import _LunchMoneyRecurringExpenses
from .transactions import _LunchMoneyTransactions


class LunchMoney(
    _LunchMoneyAssets,
    _LunchMoneyBudgets,
    _LunchMoneyPlaidAccounts,
    _LunchMoneyRecurringExpenses,
    _LunchMoneyTransactions,
):
    """
    Core Lunch Money SDK.
    """

    pass

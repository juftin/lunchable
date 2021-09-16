"""
Lunch Money Python SDK

This Module Leverages Class Inheritance to
Distribute API Methods Across a series of files. Ultimately, everything
inherits from the lunchmoney.models.core.LunchMoneyAPIClient class which facilitates
interacting with the API.

For example: to see source code on interactions with the "transactions" API endpoint you
will refer to the _LunchMoneyTransactions object.
"""

from .assets import _LunchMoneyAssets
from .budgets import _LunchMoneyBudgets
from .categories import _LunchMoneyCategories
from .plaid_accounts import _LunchMoneyPlaidAccounts
from .recurring_expenses import _LunchMoneyRecurringExpenses
from .tags import _LunchMoneyTags
from .transactions import _LunchMoneyTransactions


class LunchMoney(
    _LunchMoneyAssets,
    _LunchMoneyBudgets,
    _LunchMoneyCategories,
    _LunchMoneyPlaidAccounts,
    _LunchMoneyRecurringExpenses,
    _LunchMoneyTags,
    _LunchMoneyTransactions,
):
    """
    Core Lunch Money SDK.
    """

    pass

# Author::    Justin Flannery  (mailto:juftin@juftin.com)

"""
Lunch Money Python SDK - This Module Leverages Class Inheritance to
Distribute API Methods in an Organized manner
"""

from .assets import AssetsObject, LunchMoneyAssets
from .budgets import BudgetObject, LunchMoneyBudgets
from .plaid_accounts import LunchMoneyPlaidAccounts, PlaidAccountObject
from .recurring_expenses import LunchMoneyRecurringExpenses, RecurringExpensesObject
from .transactions import (
    LunchMoneyTransactions,
    TransactionInsertObject,
    TransactionsObject,
    TransactionUpdateObject,
)


class LunchMoney(
    LunchMoneyTransactions,
    LunchMoneyPlaidAccounts,
    LunchMoneyAssets,
    LunchMoneyRecurringExpenses,
    LunchMoneyBudgets,
):
    """
    Core Lunch Money SDK.
    """

    pass


__all__ = [
    "LunchMoney",
    "RecurringExpensesObject",
    "PlaidAccountObject",
    "TransactionsObject",
    "AssetsObject",
    "TransactionUpdateObject",
    "TransactionInsertObject",
]

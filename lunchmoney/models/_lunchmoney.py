"""
Lunch Money Python SDK

This Module Leverages Class Inheritance to
Distribute API Methods Across a series of files. Ultimately, everything
inherits from the lunchmoney.models.core.LunchMoneyAPIClient class which facilitates
interacting with the API.

For example: to see source code on interactions with the "transactions" API endpoint you
will refer to the _LunchMoneyTransactions object.
"""

from typing import Optional

from .assets import _LunchMoneyAssets
from .budgets import _LunchMoneyBudgets
from .categories import _LunchMoneyCategories
from .crypto import _LunchMoneyCrypto
from .plaid_accounts import _LunchMoneyPlaidAccounts
from .recurring_expenses import _LunchMoneyRecurringExpenses
from .tags import _LunchMoneyTags
from .transactions import _LunchMoneyTransactions


class LunchMoney(
    _LunchMoneyAssets,
    _LunchMoneyBudgets,
    _LunchMoneyCategories,
    _LunchMoneyCrypto,
    _LunchMoneyPlaidAccounts,
    _LunchMoneyRecurringExpenses,
    _LunchMoneyTags,
    _LunchMoneyTransactions,
):
    """
    Core Lunch Money SDK.
    """

    def __init__(self, access_token: Optional[str] = None):
        """
        Initialize a Lunch Money object with an Access Token.

        Tries to inherit from the Environment if one isn't provided

        Parameters
        ----------
        access_token: Optional[str]
            Lunchmoney Developer API Access Token
        """
        super(LunchMoney, self).__init__(access_token=access_token)

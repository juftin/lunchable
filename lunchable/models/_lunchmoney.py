"""
Lunch Money Python Client

This Module Leverages Class Inheritance to
Distribute API Methods Across a series of files. Ultimately, everything
inherits from the lunchable.models.core.LunchMoneyAPIClient class which facilitates
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
    Lunch Money Python Client.

    This class facilitates with connections to
    the `Lunch Money Developer API <https://lunchmoney.dev/>`_. Authenticate
    with an Access Token. If an access token isn't provided one will attempt to
    be inherited from a `LUNCHMONEY_ACCESS_TOKEN` environment variable.

    Examples
    --------
    ::

        from lunchable import LunchMoney

        lunch = LunchMoney(access_token="xxxxxxx")
        transactions = lunch.get_transactions()
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

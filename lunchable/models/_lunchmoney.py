"""
Lunch Money Python Client

This Module Leverages Class Inheritance to distribute API Methods Across a series of
clients. Ultimately, everything inherits from the
lunchable.models.core.LunchMoneyAPIClient class which facilitates interacting with
the API.

For example: to see source code on interactions with the "transactions" API endpoint you
will refer to the TransactionsClient object.
"""

from typing import Optional

from .assets import AssetsClient
from .budgets import BudgetsClient
from .categories import CategoriesClient
from .crypto import CryptoClient
from .plaid_accounts import PlaidAccountsClient
from .recurring_expenses import RecurringExpensesClient
from .tags import TagsClient
from .transactions import TransactionsClient
from .user import UserClient


class LunchMoney(
    AssetsClient,
    BudgetsClient,
    CategoriesClient,
    CryptoClient,
    PlaidAccountsClient,
    RecurringExpensesClient,
    TagsClient,
    TransactionsClient,
    UserClient,
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

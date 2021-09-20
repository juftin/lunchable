"""
API Configuration Helper
"""

import logging
from os import getenv
from typing import Dict, List, Optional, Union
from urllib import parse

from lunchable.exceptions import EnvironmentVariableError, LunchMoneyError

logger = logging.getLogger(__name__)


class APIConfig:
    """
    Configuration Helper Class for Connecting to the Lunchmoney API
    """

    LUNCHMONEY_SCHEME: str = "https"
    LUNCHMONEY_NETLOC: str = "dev.lunchmoney.app"
    LUNCHMONEY_API_PATH: str = "v1"

    LUNCHMONEY_TRANSACTIONS: str = "transactions"
    LUNCHMONEY_TRANSACTION_GROUPS: str = "group"
    LUNCHMONEY_PLAID_ACCOUNTS: str = "plaid_accounts"
    LUNCH_MONEY_RECURRING_EXPENSES: str = "recurring_expenses"
    LUNCHMONEY_BUDGET: str = "budgets"
    LUNCHMONEY_ASSETS: str = "assets"
    LUNCHMONEY_CATEGORIES: str = "categories"
    LUNCHMONEY_TAGS: str = "tags"
    LUNCHMONEY_CRYPTO: str = "crypto"
    LUNCHMONEY_CRYPTO_MANUAL: str = "manual"

    LUNCHMONEY_CONTENT_TYPE_HEADERS: Dict[str, str] = {"Content-Type": "application/json"}

    _access_token_environment_variable = "LUNCHMONEY_ACCESS_TOKEN"

    @staticmethod
    def get_access_token(access_token: Optional[str] = None) -> str:
        """
        Method for Resolving Access Tokens: Hardcoded -> .env File -> Env Var

        Parameters
        ----------
        access_token: Optional[str]
            Lunchmoney Developer API Access Token

        Returns
        -------
        str
        """
        if access_token is None:
            logger.info("Loading Lunch Money Developer API Access token from environment")
            access_token = getenv(APIConfig._access_token_environment_variable, None)
        if access_token is None:
            access_token_error_message = (
                "You must provide a Lunch Money Developer API Access Token directly or set your "
                f"{APIConfig._access_token_environment_variable} environment variable.")
            raise EnvironmentVariableError(access_token_error_message)
        return access_token

    @staticmethod
    def get_header(access_token: Optional[str] = None) -> Dict[str, str]:
        """
        Get the header dict to pass to requests

        Parameters
        ----------
        access_token: Optional[str]
            Lunchmoney Developer API Access Token

        Returns
        -------
        Dict[str, str]
        """
        access_token = APIConfig.get_access_token(access_token=access_token)
        auth_header = {"Authorization": f"Bearer {access_token}"}
        auth_header.update(APIConfig.LUNCHMONEY_CONTENT_TYPE_HEADERS)
        return auth_header

    @staticmethod
    def make_url(url_path: Union[List[Union[str, int]], str, int]):
        """
        Make a Lunch Money API URL using path parts

        Parameters
        ----------
        url_path: Union[List[Union[str, int]], str, int]
            API Components, if a list join these sequentially

        Returns
        -------
        str
        """
        if isinstance(url_path, str):
            url_path = [url_path]
        if not isinstance(url_path, List):
            raise LunchMoneyError("You must provide a string or list of strings to construct a URL")
        path_set = [str(item).lower() for item in url_path if
                    str(item).lower() != APIConfig.LUNCHMONEY_API_PATH]
        url = APIConfig._generate_url(scheme=APIConfig.LUNCHMONEY_SCHEME,
                                      netloc=APIConfig.LUNCHMONEY_NETLOC,
                                      path="/".join([APIConfig.LUNCHMONEY_API_PATH, *path_set]))
        return url

    @classmethod
    def _generate_url(cls, scheme: str, netloc: str,
                      path: str = "", params: str = "",
                      query: str = "", fragment: str = ""):
        """
        Build a URL

        Parameters
        ----------
        scheme: str
            URL scheme specifier
        netloc: str
            Network location part
        path: str
            Hierarchical path
        params: str
            Parameters for last path element
        query: str
            Query component
        fragment: str
            Fragment identifier
        Returns
        -------
        url: str
            Compiled URL
        """
        url_components = dict(scheme=scheme, netloc=netloc, path=path,
                              params=params, query=query, fragment=fragment)
        return parse.urlunparse(components=tuple(url_components.values()))

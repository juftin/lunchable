# Author::    Justin Flannery  (mailto:juftin@juftin.com)

"""
Lunchmoney SDK Core
"""

import datetime
import logging
from typing import Any, List, Optional, Union

import requests

from lunchmoney.config import APIConfig
from lunchmoney.exceptions import LunchMoneyError, LunchMoneyHTTPError

logger = logging.getLogger(__name__)


class LunchMoneyCore:
    """
    Core SDK Class
    """

    def __init__(self, access_token: Optional[str] = None):
        """
        Initialize a Lunch Money object with an Access Token. Try to inherit from the Environment
        if one isn't provided

        Parameters
        ----------
        access_token: Optional[str]
            Lunchmoney Developer API Access Token
        """
        self.access_token = APIConfig.get_access_token(access_token=access_token)
        api_headers = APIConfig.get_header(access_token=self.access_token)
        default_headers = requests.sessions.default_headers()
        updated_headers = dict(**api_headers, **default_headers)
        self.lunch_money_session = requests.Session()
        self.lunch_money_session.headers = updated_headers

    def __repr__(self) -> str:
        """
        String Representation

        Returns
        -------
        str
        """
        return "<LunchMoney: requests.Session>"

    def _make_request(self, method: str, url_path: Union[List[str], str],
                      params: Optional[dict] = None,
                      json: Optional[dict] = None,
                      data: Optional[Any] = None) -> Any:
        """
        Make a Request on the API

        Parameters
        ----------
        method: str
            requests method: ``GET``, ``OPTIONS``, ``HEAD``, ``POST``, ``PUT``,
            ``PATCH``, or ``DELETE``
        url_path: Union[List[str], str]
            API Components, if a list join these sequentially
        params: Optional[dict]
            Params to pass
        json: Optional[dict]
            json to pass
        data: Optional[Any]
            data to pass

        Returns
        -------
        Any
        """
        url = APIConfig.make_url(url_path=url_path)
        try:
            response = self.lunch_money_session.request(method=method, url=url,
                                                        params=params, json=json,
                                                        data=data)
            response.raise_for_status()
        except requests.exceptions.HTTPError as he:
            logger.exception(he)
            # noinspection PyUnboundLocalVariable
            logger.error(response.text)
            raise LunchMoneyHTTPError(he)
        returned_data = response.json()
        if isinstance(returned_data, dict) and any(["error" in returned_data.keys(),
                                                    "errors" in returned_data.keys()]):
            try:
                errors = returned_data["error"]
            except KeyError:
                errors = returned_data["errors"]
            logger.exception(errors)
            raise LunchMoneyHTTPError(errors)
        return response.json()

    @classmethod
    def resolve_date(
            cls, date_obj: Union[datetime.date, datetime.datetime, str]
    ) -> datetime.date:
        """
        If date_obj is a datetime.datetime objects, it will be reduced to dates. If a string is
        provided, it will be attempted to be parsed as YYYY-MM-DD format

        Parameters
        ----------
        date_obj: Union[datetime.date, datetime.datetime, str]:
            date object search

        Returns
        -------
        datetime.date
        """
        if isinstance(date_obj, datetime.date):
            return date_obj
        elif isinstance(date_obj, datetime.datetime):
            return date_obj.date()
        elif isinstance(date_obj, str):
            return datetime.datetime.strptime(date_obj, "%Y-%m-%d").date()
        else:
            raise LunchMoneyError("You must provide a datetime.datetime, datetime.date, "
                                  "or string formatted as YYYY-MM-DD")

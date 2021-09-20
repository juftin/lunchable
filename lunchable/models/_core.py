"""
Lunchmoney SDK Core
"""

import datetime
import json
from json import loads
import logging
from typing import Any, List, Optional, Union

import requests

from lunchable.config import APIConfig
from lunchable.exceptions import LunchMoneyHTTPError

logger = logging.getLogger(__name__)


class _Methods:
    """
    Namespace for Request Methods
    """

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


class LunchMoneyAPIClient:
    """
    Core API Client Class
    """

    methods = _Methods

    def __init__(self, access_token: Optional[str] = None):
        """
        Initialize a Lunch Money object with an Access Token.

        Tries to inherit from the Environment if one isn't provided

        Parameters
        ----------
        access_token: Optional[str]
            Lunchmoney Developer API Access Token
        """
        self.access_token = APIConfig.get_access_token(access_token=access_token)
        api_headers = APIConfig.get_header(access_token=self.access_token)
        default_headers = requests.sessions.default_headers()
        updated_headers = dict(**default_headers, **api_headers)
        typed_headers = requests.models.CaseInsensitiveDict(updated_headers)
        self.lunch_money_session = requests.Session()
        self.lunch_money_session.headers = typed_headers

    def __repr__(self) -> str:
        """
        String Representation

        Returns
        -------
        str
        """
        return "<LunchMoney: requests.Session>"

    @staticmethod
    def _serializer(obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        elif isinstance(obj, datetime.date):
            return obj.isoformat()
        else:
            return obj

    def _make_request(self, method: str, url_path: Union[List[Union[str, int]], str, int],
                      params: Optional[dict] = None,
                      payload: Optional[Any] = None) -> Any:
        """
        Make a Request to the API

        Parameters
        ----------
        method: str
            requests method: ``GET``, ``OPTIONS``, ``HEAD``, ``POST``, ``PUT``,
            ``PATCH``, or ``DELETE``
        url_path: Union[List[Union[str, int]], str, int]
            API Components, if a list join these sequentially
        params: Optional[dict]
            Params to pass
        payload: Optional[Any]
            data to pass

        Returns
        -------
        Any
        """
        url = APIConfig.make_url(url_path=url_path)
        if payload is not None:
            payload = json.dumps(payload, default=LunchMoneyAPIClient._serializer)
        try:
            response = self.lunch_money_session.request(
                method=method, url=url, params=params,
                data=payload)
            response.raise_for_status()
        except requests.exceptions.HTTPError as he:
            logger.exception(he)
            # noinspection PyUnboundLocalVariable
            logger.error(response.text)
            raise LunchMoneyHTTPError(he)
        returned_data = loads(response.content)
        if isinstance(returned_data, dict) and any(["error" in returned_data.keys(),
                                                    "errors" in returned_data.keys()]):
            try:
                errors = returned_data["error"]
            except KeyError:
                errors = returned_data["errors"]
            logger.exception(errors)
            raise LunchMoneyHTTPError(errors)
        return loads(response.content)

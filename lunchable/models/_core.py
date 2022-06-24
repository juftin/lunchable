"""
Lunchmoney SDK Core
"""

import datetime
import json
import logging
from json import loads
from typing import Any, List, Optional, Union

import requests

from lunchable._config import APIConfig
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

    class Methods:
        """
        HTTP Request Method Enumerations: GET, OPTIONS, HEAD, POST, PUT, PATCH, or DELETE
        """

        # This Helper Namespace Organizes and Tracks HTTP Requests by Method
        GET = "GET"
        OPTIONS = "OPTIONS"
        HEAD = "HEAD"
        POST = "POST"
        PUT = "PUT"
        PATCH = "PATCH"
        DELETE = "DELETE"

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

    def _make_request(
        self,
        method: str,
        url_path: Union[List[Union[str, int]], str, int],
        params: Optional[dict] = None,
        payload: Optional[Any] = None,
        **kwargs
    ) -> Any:
        """
        Make a Request to the API

        Parameters
        ----------
        method: str
            requests method: GET, OPTIONS, HEAD, POST, PUT,
            PATCH, or DELETE
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
                method=method, url=url, params=params, data=payload, **kwargs
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError as he:
            logger.exception(he)
            # noinspection PyUnboundLocalVariable
            logger.error(response.text)
            raise LunchMoneyHTTPError(he)
        returned_data = loads(response.content)
        if isinstance(returned_data, dict) and any(
            ["error" in returned_data.keys(), "errors" in returned_data.keys()]
        ):
            try:
                errors = returned_data["error"]
            except KeyError:
                errors = returned_data["errors"]
            logger.exception(errors)
            raise LunchMoneyHTTPError(errors)
        return loads(response.content)

    def make_http_request(
        self,
        method: str,
        url: str,
        params: Optional[Any] = None,
        data: Optional[Any] = None,
        json: Optional[Any] = None,
        **kwargs
    ) -> requests.Response:
        """
        Make a HTTP Request

        This is a simple method :class:`.LunchMoney` exposes to make HTTP requests. It
        has the benefit of using an existing `requests.Session` as well as as out of the box
        auth headers that are used to connect to the Lunch Money Developer API.

        Parameters
        ----------
        method: str
            requests method: GET, OPTIONS, HEAD, POST, PUT,
            PATCH, or DELETE
        url: str
            URL for the new Request object.
        params: Optional[Any]
            Dictionary, list of tuples or bytes to send in the query
            string for the Request.
        data: Optional[Any]
            Dictionary, list of tuples, bytes, or file-like object to send
            in the body of the Request.
        json: Optional[Any]
            A JSON serializable Python object to send in the body of the Request.

        Returns
        -------
        Any

        Examples
        --------
        A recent use of this method was to delete a Tag (which isn't available via the
        Developer API yet) ::

            import lunchable

            lunch = lunchable.LunchMoney()

            # Get All the Tags
            all_tags = lunch.get_tags()
            # Get All The Null Tags (a list of 1 or zero)
            null_tags = [tag for tag in all_tags if tag.name in [None, ""]]

            # Create a Cookie dictionary from a browser session
            cookies = {"cookie_keys": "cookie_values"}

            for null_tag in null_tags:
                # use the requests.session embedded in the class to make a request with cookies
                response = lunch.make_request(
                    method="DELETE",
                    url=f"https://api.lunchmoney.app/tags/{null_tag.id}",
                    cookies=cookies)
                # raise an error for 4XX responses
                response.raise_for_status()
        """
        response = self.lunch_money_session.request(
            method=method, url=url, params=params, data=data, json=json, **kwargs
        )
        return response

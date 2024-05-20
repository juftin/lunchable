"""
Lunchmoney SDK Core
"""

from __future__ import annotations

from functools import cached_property
from typing import (
    Any,
    AsyncIterable,
    Iterable,
    Mapping,
    Optional,
    Union,
)

import httpx
import pydantic_core
from httpx import Client

from lunchable._config import APIConfig
from lunchable.exceptions import LunchMoneyHTTPError


class LunchMoneyClient(Client):
    """
    API HTTP Client
    """

    def __init__(self, access_token: str | None = None) -> None:
        timeout = httpx.Timeout(connect=5, read=30, write=20, pool=5)
        super().__init__(timeout=timeout)
        api_headers = APIConfig.get_header(access_token=access_token)
        self.headers.update(api_headers)


class LunchMoneyAsyncClient(httpx.AsyncClient):
    """
    API Async HTTP Client
    """

    def __init__(self, access_token: str | None = None) -> None:
        timeout = httpx.Timeout(connect=5, read=30, write=20, pool=5)
        super().__init__(timeout=timeout)
        api_headers = APIConfig.get_header(access_token=access_token)
        self.headers.update(api_headers)


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

    def __init__(self, access_token: str | None = None) -> None:
        """
        Initialize a Lunch Money object with an Access Token.

        Tries to inherit from the Environment if one isn't provided

        Parameters
        ----------
        access_token: Optional[str]
            Lunchmoney Developer API Access Token
        """
        self.access_token = APIConfig.get_access_token(access_token=access_token)

    def __repr__(self) -> str:
        """
        String Representation

        Returns
        -------
        str
        """
        return "<LunchMoney: httpx.Client>"

    @cached_property
    def session(self) -> httpx.Client:
        """
        Lunch Money HTTPX Client

        Returns
        -------
        httpx.Client
        """
        return LunchMoneyClient(access_token=self.access_token)

    @cached_property
    def async_session(self) -> httpx.AsyncClient:
        """
        Lunch Money HTTPX Async Client

        Returns
        -------
        httpx.AsyncClient
        """
        return LunchMoneyAsyncClient(access_token=self.access_token)

    def request(
        self,
        method: str,
        url: Union[httpx.URL, str],
        *,
        content: Optional[
            Union[str, bytes, Iterable[bytes], AsyncIterable[bytes]]
        ] = None,
        data: Optional[Mapping[str, Any]] = None,
        json: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        **kwargs: Any,
    ) -> httpx.Response:
        """
        Make an HTTP request

        This is a simple method :class:`.LunchMoney` exposes to make HTTP requests. It
        has the benefit of using an existing `httpx.Client` as well as as out of the box
        auth headers that are used to connect to the Lunch Money Developer API.

        Parameters
        ----------
        method: str
            requests method: GET, OPTIONS, HEAD, POST, PUT,
            PATCH, or DELETE
        url: Union[httpx.URL, str]
            URL for the new Request object.
        content: Optional[Union[str, bytes, Iterable[bytes], AsyncIterable[bytes]]]
            Content to send in the body of the Request.
        data: Optional[Mapping[str, Any]]
            Dictionary, list of tuples, bytes, or file-like object to send
            in the body of the Request.
        json: Optional[Any]
            A JSON serializable Python object to send in the body of the Request.
        params: Optional[Mapping[str, Any]]
            Dictionary, list of tuples or bytes to send in the query
            string for the Request.
        **kwargs: Any
            Additional arguments to send to the request method.

        Returns
        -------
        httpx.Response

        Examples
        --------
        A recent use of this method was to delete a Tag (which isn't available via the
        Developer API yet)

        ```python
        import lunchable

        lunch = lunchable.LunchMoney()

        # Get All the Tags
        all_tags = lunch.get_tags()
        # Get All The Null Tags (a list of 1 or zero)
        null_tags = [tag for tag in all_tags if tag.name in [None, ""]]

        # Create a Cookie dictionary from a browser session
        cookies = {"cookie_keys": "cookie_values"}
        del lunch.session.headers["authorization"]

        for null_tag in null_tags:
            # use the httpx.client embedded in the class to make a request with cookies
            response = lunch.request(
                method=lunch.Methods.DELETE,
                url=f"https://api.lunchmoney.app/tags/{null_tag.id}",
                cookies=cookies
            )
            # raise an error for 4XX responses
            response.raise_for_status()
        ```
        """
        response = self.session.request(
            method=method,
            url=url,
            content=content,
            data=data,
            json=json,
            params=params,
            **kwargs,
        )
        return response

    async def arequest(
        self,
        method: str,
        url: Union[httpx.URL, str],
        *,
        content: Optional[
            Union[str, bytes, Iterable[bytes], AsyncIterable[bytes]]
        ] = None,
        data: Optional[Mapping[str, Any]] = None,
        json: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        **kwargs: Any,
    ) -> httpx.Response:
        """
        Make an async HTTP request

        This is a simple method :class:`.LunchMoney` exposes to make HTTP requests. It
        has the benefit of using an existing `httpx.Client` as well as as out of the box
        auth headers that are used to connect to the Lunch Money Developer API.

        Parameters
        ----------
        method: str
            requests method: GET, OPTIONS, HEAD, POST, PUT,
            PATCH, or DELETE
        url: Union[httpx.URL, str]
            URL for the new Request object.
        content: Optional[Union[str, bytes, Iterable[bytes], AsyncIterable[bytes]]]
            Content to send in the body of the Request.
        data: Optional[Mapping[str, Any]]
            Dictionary, list of tuples, bytes, or file-like object to send
            in the body of the Request.
        json: Optional[Any]
            A JSON serializable Python object to send in the body of the Request.
        params: Optional[Mapping[str, Any]]
            Dictionary, list of tuples or bytes to send in the query
            string for the Request.
        **kwargs: Any
            Additional arguments to send to the request method.

        Returns
        -------
        httpx.Response
        """
        response = self.async_session.request(
            method=method,
            url=url,
            content=content,
            data=data,
            json=json,
            params=params,
            **kwargs,
        )
        return await response

    @classmethod
    def process_response(cls, response: httpx.Response) -> Any:
        """
        Process a Lunch Money response and raise any errors

        This includes 200 responses that are actually errors

        Parameters
        ----------
        response: httpx.Response
            An HTTPX Response Object
        """
        try:
            response.raise_for_status()
        except httpx.HTTPError as he:
            raise LunchMoneyHTTPError(response.text) from he
        if response.content:
            returned_data = response.json()
        else:
            returned_data = None
        if isinstance(returned_data, dict) and any(
            ["error" in returned_data.keys(), "errors" in returned_data.keys()]
        ):
            try:
                errors = returned_data["error"]
            except KeyError:
                errors = returned_data["errors"]
            raise LunchMoneyHTTPError(errors)
        return returned_data

    def make_request(
        self,
        method: str,
        url_path: Union[list[Union[str, int]], str, int],
        params: Optional[Mapping[str, Any]] = None,
        payload: Optional[Any] = None,
        **kwargs: Any,
    ) -> Any:
        """
        Make an HTTP request and `process` its response

        This method is a wrapper around :meth:`.LunchMoney.request` that
        also processes the response and checks for any errors.

        Parameters
        ----------
        method: str
            requests method: GET, OPTIONS, HEAD, POST, PUT,
            PATCH, or DELETE
        url_path: Union[List[Union[str, int]], str, int]
            URL components to make into a URL
        payload: Optional[Mapping[str, Any]]
            Data to send in the body of the Request.
        params: Optional[Mapping[str, Any]]
            Dictionary, list of tuples or bytes to send in the query
            string for the Request.
        **kwargs: Any
            Additional arguments to send to the request method.

        Returns
        -------
        Any
        """
        url = APIConfig.make_url(url_path=url_path)
        json_safe_payload = pydantic_core.to_json(payload) if payload else None
        json_safe_params = pydantic_core.to_jsonable_python(params)
        response = self.request(
            method=method,
            url=url,
            params=json_safe_params,
            content=json_safe_payload,
            **kwargs,
        )
        data = self.process_response(response=response)
        return data

    async def amake_request(
        self,
        method: str,
        url_path: Union[list[Union[str, int]], str, int],
        params: Optional[Mapping[str, Any]] = None,
        payload: Optional[Any] = None,
        **kwargs: Any,
    ) -> Any:
        """
        Make an async HTTP request and `process` its response

        This method is a wrapper around :meth:`.LunchMoney.arequest` that
        also processes the response and checks for any errors.

        Parameters
        ----------
        method: str
            requests method: GET, OPTIONS, HEAD, POST, PUT,
            PATCH, or DELETE
        url_path: Union[List[Union[str, int]], str, int]
            URL components to make into a URL
        payload: Optional[Mapping[str, Any]]
            Data to send in the body of the Request.
        params: Optional[Mapping[str, Any]]
            Dictionary, list of tuples or bytes to send in the query
            string for the Request.
        **kwargs: Any
            Additional arguments to send to the request method.

        Returns
        -------
        Any
        """
        url = APIConfig.make_url(url_path=url_path)
        json_safe_payload = pydantic_core.to_jsonable_python(payload)
        json_safe_params = pydantic_core.to_jsonable_python(params)
        response = await self.arequest(
            method=method,
            url=url,
            params=json_safe_params,
            data=json_safe_payload,
            **kwargs,
        )
        data = self.process_response(response=response)
        return data

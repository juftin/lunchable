# coding: utf-8

"""
Lunch Money API - v2

This is a version of the Lunch Money API described using the the OpenAPI 3.X specification.  The goal of this project is to validate an \"API Design First\" approach for the Lunch Money API, which should allow us to gather developer feedback prior to implementation in order to develop API endpoints more quickly.  This version of the API will differ from the existing v1 beta version. For more information on the changes please see the [v2 API Changelog](https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2/changelog)  Some useful links: - [Current v1 Lunch Money API Documentation](https://lunchmoney.dev) - [v2 API Changelog](https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2/changelog) - [OpenAPI API YAML Specification](https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2/openapi/) - [Awesome Lunch Money Projects](https://lunchmoney.dev/#awesome-projects)

The version of the OpenAPI document: 2.7.4
Contact: devsupport@lunchmoney.app
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import StrictBool
from lunchable.models.transaction_object import TransactionObject

from lunchable.api_client import ApiClient, RequestSerialized
from lunchable.api_response import ApiResponse
from lunchable.rest import RESTResponseType


class TransactionsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def delete_transaction_by_id(
        self,
        id: Annotated[StrictInt, Field(description="ID of the transaction to delete")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Delete a transaction

        Deletes the transaction with the ID specified on the path.<br> If the specified transaction is a split transaction or a split parent, or if it is a grouped transactions or part of a transaction group, the request will fail with a suggestion on how to unsplit or ungroup the transaction(s) prior to deletion.   Otherwise, the specified transaction is deleted. <br> This action is not reversible!

        :param id: ID of the transaction to delete (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._delete_transaction_by_id_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "204": None,
            "401": "ErrorResponseObject",
            "404": "ErrorResponseObject",
            "429": "ErrorResponseObject",
            "500": "ErrorResponseObject",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    @validate_call
    def delete_transaction_by_id_with_http_info(
        self,
        id: Annotated[StrictInt, Field(description="ID of the transaction to delete")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Delete a transaction

        Deletes the transaction with the ID specified on the path.<br> If the specified transaction is a split transaction or a split parent, or if it is a grouped transactions or part of a transaction group, the request will fail with a suggestion on how to unsplit or ungroup the transaction(s) prior to deletion.   Otherwise, the specified transaction is deleted. <br> This action is not reversible!

        :param id: ID of the transaction to delete (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._delete_transaction_by_id_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "204": None,
            "401": "ErrorResponseObject",
            "404": "ErrorResponseObject",
            "429": "ErrorResponseObject",
            "500": "ErrorResponseObject",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    @validate_call
    def delete_transaction_by_id_without_preload_content(
        self,
        id: Annotated[StrictInt, Field(description="ID of the transaction to delete")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Delete a transaction

        Deletes the transaction with the ID specified on the path.<br> If the specified transaction is a split transaction or a split parent, or if it is a grouped transactions or part of a transaction group, the request will fail with a suggestion on how to unsplit or ungroup the transaction(s) prior to deletion.   Otherwise, the specified transaction is deleted. <br> This action is not reversible!

        :param id: ID of the transaction to delete (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._delete_transaction_by_id_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "204": None,
            "401": "ErrorResponseObject",
            "404": "ErrorResponseObject",
            "429": "ErrorResponseObject",
            "500": "ErrorResponseObject",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _delete_transaction_by_id_serialize(
        self,
        id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None

        _collection_formats: Dict[str, str] = {}

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params["id"] = id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json"]
            )

        # authentication setting
        _auth_settings: List[str] = ["cookieAuth", "bearerSecurity"]

        return self.api_client.param_serialize(
            method="DELETE",
            resource_path="/transactions/{id}",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )

    @validate_call
    def get_transaction_by_id(
        self,
        id: Annotated[
            StrictInt, Field(description="ID of the transaction to retrieve")
        ],
        include_metadata: Annotated[
            Optional[StrictBool],
            Field(
                description="Set to true to have the metadata objects associated with this transaction returned as part of the result. A `plaid_metatdata` object will always exist for transactions associated with an account that is synced via plaid. A `custom_metadata` object may exist for transactions that were inserted or updated via the API."
            ),
        ] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> TransactionObject:
        """Get a single transaction

        Retrieve details of a specific transaction by its ID.<br><br>  It the requested transaction is the parent of split transactions, the transaction returned in the response will include a `children` property which will contain a list of the split transactions.<br><br>  Similarly, if the requested transaction is transaction group, the transaction returned in the response will include a `children` property which will contain a list of the original transactions that make up the transaction group.

        :param id: ID of the transaction to retrieve (required)
        :type id: int
        :param include_metadata: Set to true to have the metadata objects associated with this transaction returned as part of the result. A `plaid_metatdata` object will always exist for transactions associated with an account that is synced via plaid. A `custom_metadata` object may exist for transactions that were inserted or updated via the API.
        :type include_metadata: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._get_transaction_by_id_serialize(
            id=id,
            include_metadata=include_metadata,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "TransactionObject",
            "400": "ErrorResponseObject",
            "401": "ErrorResponseObject",
            "404": "ErrorResponseObject",
            "429": "ErrorResponseObject",
            "500": "ErrorResponseObject",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    @validate_call
    def get_transaction_by_id_with_http_info(
        self,
        id: Annotated[
            StrictInt, Field(description="ID of the transaction to retrieve")
        ],
        include_metadata: Annotated[
            Optional[StrictBool],
            Field(
                description="Set to true to have the metadata objects associated with this transaction returned as part of the result. A `plaid_metatdata` object will always exist for transactions associated with an account that is synced via plaid. A `custom_metadata` object may exist for transactions that were inserted or updated via the API."
            ),
        ] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[TransactionObject]:
        """Get a single transaction

        Retrieve details of a specific transaction by its ID.<br><br>  It the requested transaction is the parent of split transactions, the transaction returned in the response will include a `children` property which will contain a list of the split transactions.<br><br>  Similarly, if the requested transaction is transaction group, the transaction returned in the response will include a `children` property which will contain a list of the original transactions that make up the transaction group.

        :param id: ID of the transaction to retrieve (required)
        :type id: int
        :param include_metadata: Set to true to have the metadata objects associated with this transaction returned as part of the result. A `plaid_metatdata` object will always exist for transactions associated with an account that is synced via plaid. A `custom_metadata` object may exist for transactions that were inserted or updated via the API.
        :type include_metadata: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._get_transaction_by_id_serialize(
            id=id,
            include_metadata=include_metadata,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "TransactionObject",
            "400": "ErrorResponseObject",
            "401": "ErrorResponseObject",
            "404": "ErrorResponseObject",
            "429": "ErrorResponseObject",
            "500": "ErrorResponseObject",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    @validate_call
    def get_transaction_by_id_without_preload_content(
        self,
        id: Annotated[
            StrictInt, Field(description="ID of the transaction to retrieve")
        ],
        include_metadata: Annotated[
            Optional[StrictBool],
            Field(
                description="Set to true to have the metadata objects associated with this transaction returned as part of the result. A `plaid_metatdata` object will always exist for transactions associated with an account that is synced via plaid. A `custom_metadata` object may exist for transactions that were inserted or updated via the API."
            ),
        ] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get a single transaction

        Retrieve details of a specific transaction by its ID.<br><br>  It the requested transaction is the parent of split transactions, the transaction returned in the response will include a `children` property which will contain a list of the split transactions.<br><br>  Similarly, if the requested transaction is transaction group, the transaction returned in the response will include a `children` property which will contain a list of the original transactions that make up the transaction group.

        :param id: ID of the transaction to retrieve (required)
        :type id: int
        :param include_metadata: Set to true to have the metadata objects associated with this transaction returned as part of the result. A `plaid_metatdata` object will always exist for transactions associated with an account that is synced via plaid. A `custom_metadata` object may exist for transactions that were inserted or updated via the API.
        :type include_metadata: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._get_transaction_by_id_serialize(
            id=id,
            include_metadata=include_metadata,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "TransactionObject",
            "400": "ErrorResponseObject",
            "401": "ErrorResponseObject",
            "404": "ErrorResponseObject",
            "429": "ErrorResponseObject",
            "500": "ErrorResponseObject",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _get_transaction_by_id_serialize(
        self,
        id,
        include_metadata,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None

        _collection_formats: Dict[str, str] = {}

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params["id"] = id
        # process the query parameters
        if include_metadata is not None:
            _query_params.append(("include_metadata", include_metadata))

        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json"]
            )

        # authentication setting
        _auth_settings: List[str] = ["cookieAuth", "bearerSecurity"]

        return self.api_client.param_serialize(
            method="GET",
            resource_path="/transactions/{id}",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )

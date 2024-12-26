# lunchable.TransactionsApi

All URIs are relative to *https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2*

| Method                                                                      | HTTP request                  | Description              |
| --------------------------------------------------------------------------- | ----------------------------- | ------------------------ |
| [**delete_transaction_by_id**](TransactionsApi.md#delete_transaction_by_id) | **DELETE** /transactions/{id} | Delete a transaction     |
| [**get_transaction_by_id**](TransactionsApi.md#get_transaction_by_id)       | **GET** /transactions/{id}    | Get a single transaction |

# **delete_transaction_by_id**

> delete_transaction_by_id(id)

Delete a transaction

Deletes the transaction with the ID specified on the path.<br> If the specified transaction is a split transaction or a split parent, or if it is a grouped transactions or part of a transaction group, the request will fail with a suggestion on how to unsplit or ungroup the transaction(s) prior to deletion. Otherwise, the specified transaction is deleted. <br> This action is not reversible!

### Example

-   Api Key Authentication (cookieAuth):
-   Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchable
from lunchable.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = lunchable.Configuration(
    host = "https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerSecurity
configuration = lunchable.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with lunchable.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lunchable.TransactionsApi(api_client)
    id = 2112140361 # int | ID of the transaction to delete

    try:
        # Delete a transaction
        api_instance.delete_transaction_by_id(id)
    except Exception as e:
        print("Exception when calling TransactionsApi->delete_transaction_by_id: %s\n" % e)
```

### Parameters

| Name   | Type    | Description                     | Notes |
| ------ | ------- | ------------------------------- | ----- |
| **id** | **int** | ID of the transaction to delete |

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

-   **Content-Type**: Not defined
-   **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                            | Response headers |
| ----------- | ------------------------------------------------------------------------------------------------------ | ---------------- |
| **204**     | No Content                                                                                             | -                |
| **401**     | Unauthorized. This error occurs when an invalid API token is passed to the request.                    | -                |
| **404**     | Not Found                                                                                              | -                |
| **429**     | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. | -                |
| **500**     | Internal Server Error. Contact support.                                                                | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_by_id**

> TransactionObject get_transaction_by_id(id, include_metadata=include_metadata)

Get a single transaction

Retrieve details of a specific transaction by its ID.<br><br> It the requested transaction is the parent of split transactions, the transaction returned in the response will include a `children` property which will contain a list of the split transactions.<br><br> Similarly, if the requested transaction is transaction group, the transaction returned in the response will include a `children` property which will contain a list of the original transactions that make up the transaction group.

### Example

-   Api Key Authentication (cookieAuth):
-   Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchable
from lunchable.models.transaction_object import TransactionObject
from lunchable.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = lunchable.Configuration(
    host = "https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerSecurity
configuration = lunchable.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with lunchable.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lunchable.TransactionsApi(api_client)
    id = 2112140359 # int | ID of the transaction to retrieve
    include_metadata = False # bool | Set to true to have the metadata objects associated with this transaction returned as part of the result. A `plaid_metatdata` object will always exist for transactions associated with an account that is synced via plaid. A `custom_metadata` object may exist for transactions that were inserted or updated via the API. (optional) (default to False)

    try:
        # Get a single transaction
        api_response = api_instance.get_transaction_by_id(id, include_metadata=include_metadata)
        print("The response of TransactionsApi->get_transaction_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->get_transaction_by_id: %s\n" % e)
```

### Parameters

| Name                 | Type     | Description                                                                                                                                                                                                                                                                                                                                       | Notes                         |
| -------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| **id**               | **int**  | ID of the transaction to retrieve                                                                                                                                                                                                                                                                                                                 |
| **include_metadata** | **bool** | Set to true to have the metadata objects associated with this transaction returned as part of the result. A &#x60;plaid_metatdata&#x60; object will always exist for transactions associated with an account that is synced via plaid. A &#x60;custom_metadata&#x60; object may exist for transactions that were inserted or updated via the API. | [optional] [default to False] |

### Return type

[**TransactionObject**](TransactionObject.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

-   **Content-Type**: Not defined
-   **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                            | Response headers |
| ----------- | ------------------------------------------------------------------------------------------------------ | ---------------- |
| **200**     | Transaction Object with the requested transaction.                                                     | -                |
| **400**     | Bad Request                                                                                            | -                |
| **401**     | Unauthorized. This error occurs when an invalid API token is passed to the request.                    | -                |
| **404**     | Not Found                                                                                              | -                |
| **429**     | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. | -                |
| **500**     | Internal Server Error. Contact support.                                                                | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

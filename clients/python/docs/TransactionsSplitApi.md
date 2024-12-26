# lunchable.TransactionsSplitApi

All URIs are relative to *https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2*

| Method                                                                 | HTTP request                        | Description                             |
| ---------------------------------------------------------------------- | ----------------------------------- | --------------------------------------- |
| [**split_transaction**](TransactionsSplitApi.md#split_transaction)     | **POST** /transactions/split/{id}   | Split a transaction                     |
| [**unsplit_transaction**](TransactionsSplitApi.md#unsplit_transaction) | **DELETE** /transactions/split/{id} | Unsplit a previously split transactions |

# **split_transaction**

> GroupTransactions201Response split_transaction(id, split_transaction_request)

Split a transaction

Splits an existing transaction into a set of smaller child transactions.<br><br> After a transaction has been split the original transaction is no longer shown on the transactions page or returned by a `GET /transactions` request. The newly created child transactions are returned instead. To see the details of the original parent transaction after it has been split use the `GET /transactions/{id}` endpoint, passing the value of the `parent_id` of one of the children.

### Example

-   Api Key Authentication (cookieAuth):
-   Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchable
from lunchable.models.group_transactions201_response import GroupTransactions201Response
from lunchable.models.split_transaction_request import SplitTransactionRequest
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
    api_instance = lunchable.TransactionsSplitApi(api_client)
    id = 2112150650 # int | ID of the transaction to spit
    split_transaction_request = {"child_transactions":[{"amount":44.23,"payee":"Food Town - Lenny"},{"amount":44.22,"payee":"Food Town - Penny"}]} # SplitTransactionRequest |

    try:
        # Split a transaction
        api_response = api_instance.split_transaction(id, split_transaction_request)
        print("The response of TransactionsSplitApi->split_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsSplitApi->split_transaction: %s\n" % e)
```

### Parameters

| Name                          | Type                                                      | Description                   | Notes |
| ----------------------------- | --------------------------------------------------------- | ----------------------------- | ----- |
| **id**                        | **int**                                                   | ID of the transaction to spit |
| **split_transaction_request** | [**SplitTransactionRequest**](SplitTransactionRequest.md) |                               |

### Return type

[**GroupTransactions201Response**](GroupTransactions201Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

-   **Content-Type**: application/json
-   **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                            | Response headers |
| ----------- | ------------------------------------------------------------------------------------------------------ | ---------------- |
| **201**     | The new split parent transaction with populated children attribute                                     | -                |
| **400**     | Bad Request                                                                                            | -                |
| **401**     | Unauthorized. This error occurs when an invalid API token is passed to the request.                    | -                |
| **429**     | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. | -                |
| **500**     | Internal Server Error. Contact support.                                                                | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsplit_transaction**

> unsplit_transaction(id)

Unsplit a previously split transactions

Deletes the split children of a previously split transactions and restores the parent transactions to the normal unsplit state.<br><br> Use the value of the `parent_id`property of a split transaction to specify the parent ID.

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
    api_instance = lunchable.TransactionsSplitApi(api_client)
    id = 2112140459 # int | ID of the previously split transaction to delete.

    try:
        # Unsplit a previously split transactions
        api_instance.unsplit_transaction(id)
    except Exception as e:
        print("Exception when calling TransactionsSplitApi->unsplit_transaction: %s\n" % e)
```

### Parameters

| Name   | Type    | Description                                       | Notes |
| ------ | ------- | ------------------------------------------------- | ----- |
| **id** | **int** | ID of the previously split transaction to delete. |

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
| **400**     | Invalid request parameters                                                                             | -                |
| **401**     | Unauthorized. This error occurs when an invalid API token is passed to the request.                    | -                |
| **429**     | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. | -                |
| **500**     | Internal Server Error. Contact support.                                                                | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

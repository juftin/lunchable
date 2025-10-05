# lunchable.TransactionsApi

All URIs are relative to *https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2*

| Method                                                                      | HTTP request                  | Description                    |
| --------------------------------------------------------------------------- | ----------------------------- | ------------------------------ |
| [**delete_transaction_by_id**](TransactionsApi.md#delete_transaction_by_id) | **DELETE** /transactions/{id} | Delete a transaction           |
| [**get_transaction_by_id**](TransactionsApi.md#get_transaction_by_id)       | **GET** /transactions/{id}    | Get a single transaction       |
| [**update_transaction**](TransactionsApi.md#update_transaction)             | **PUT** /transactions/{id}    | Update an existing transaction |

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

> TransactionObject get_transaction_by_id(id)

Get a single transaction

Retrieves the details of a specific transaction by its ID, including the following properties which are not returned by default in the response to a `GET /transactions` request:<br> - `plaid_metadata` will either be `null` or contain the metadata for transactions associated with an account that is synced via plaid. - `custom_metadata` will either be `null` or contain any custom_metadata added to transactions that were inserted or updated via the API. - `files` will be a list of objects that describe any attachments to the transaction. If `is_group` is true in the returned transaction, the object will also include the `children` property which will contain a list of the original transactions that make up the transaction group.<br> If `is_parent` is true in the returned transaction, the object will also include the `children` property which will contain a list of the split transactions.

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
    id = 2112150654 # int | ID of the transaction to retrieve

    try:
        # Get a single transaction
        api_response = api_instance.get_transaction_by_id(id)
        print("The response of TransactionsApi->get_transaction_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->get_transaction_by_id: %s\n" % e)
```

### Parameters

| Name   | Type    | Description                       | Notes |
| ------ | ------- | --------------------------------- | ----- |
| **id** | **int** | ID of the transaction to retrieve |

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

# **update_transaction**

> TransactionObject update_transaction(id, update_transaction_object, update_balance=update_balance)

Update an existing transaction

Modifies the properties of an existing transaction.<br><br> You may submit the response from a `GET /transactions/{id}` as the request body, however only certain properties can be updated using this API. The following system set properties are accepted in the request body but their values will be ignored: `id`, `to_base`, `is_pending`, `created_at`, `updated_at`, `source`, and `plaid_metadata`.<br><br> Transactions that have been previously split or grouped may not be modified by this endpoint. Therefore the `is_parent`, `parent_id`, `is_group`, `group_id`, and `children` properties are also ignored when provided in the request body.<br><br> It is also possible to provide only the properties to be updated in the request body, as long as the request includes at least one of the properties that is not listed above. For example a request body that contains only an `category_id` attribute is valid.

### Example

-   Api Key Authentication (cookieAuth):
-   Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchable
from lunchable.models.transaction_object import TransactionObject
from lunchable.models.update_transaction_object import UpdateTransactionObject
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
    id = 2112140361 # int | ID of the transaction to update
    update_transaction_object = {"category_id":315162} # UpdateTransactionObject |
    update_balance = True # bool | Set this to `false` to skip updating the transaction's associated account balance. Default behavior is to update balances. (optional)

    try:
        # Update an existing transaction
        api_response = api_instance.update_transaction(id, update_transaction_object, update_balance=update_balance)
        print("The response of TransactionsApi->update_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->update_transaction: %s\n" % e)
```

### Parameters

| Name                          | Type                                                      | Description                                                                                                                              | Notes      |
| ----------------------------- | --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **id**                        | **int**                                                   | ID of the transaction to update                                                                                                          |
| **update_transaction_object** | [**UpdateTransactionObject**](UpdateTransactionObject.md) |                                                                                                                                          |
| **update_balance**            | **bool**                                                  | Set this to &#x60;false&#x60; to skip updating the transaction&#39;s associated account balance. Default behavior is to update balances. | [optional] |

### Return type

[**TransactionObject**](TransactionObject.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

-   **Content-Type**: application/json
-   **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                            | Response headers |
| ----------- | ------------------------------------------------------------------------------------------------------ | ---------------- |
| **201**     | Transaction successfully updated                                                                       | -                |
| **400**     | Bad Request                                                                                            | -                |
| **401**     | Unauthorized. This error occurs when an invalid API token is passed to the request.                    | -                |
| **404**     | Not Found                                                                                              | -                |
| **429**     | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. | -                |
| **500**     | Internal Server Error. Contact support.                                                                | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

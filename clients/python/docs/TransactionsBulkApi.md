# lunchable.TransactionsBulkApi

All URIs are relative to *https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2*

| Method                                                                        | HTTP request             | Description                       |
| ----------------------------------------------------------------------------- | ------------------------ | --------------------------------- |
| [**create_new_transactions**](TransactionsBulkApi.md#create_new_transactions) | **POST** /transactions   | Insert one or more transactions.  |
| [**delete_transactions**](TransactionsBulkApi.md#delete_transactions)         | **DELETE** /transactions | Bulk delete existing transactions |
| [**get_all_transactions**](TransactionsBulkApi.md#get_all_transactions)       | **GET** /transactions    | Get all transactions              |

# **create_new_transactions**

> CreateNewTransactions201Response create_new_transactions(create_new_transactions_request)

Insert one or more transactions.

Use this endpoint to add transactions to a budget. The request body for this endpoint must include a list of transactions with at least one transaction and not more than 500 transactions to insert.

### Example

-   Api Key Authentication (cookieAuth):
-   Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchable
from lunchable.models.create_new_transactions201_response import CreateNewTransactions201Response
from lunchable.models.create_new_transactions_request import CreateNewTransactionsRequest
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
    api_instance = lunchable.TransactionsBulkApi(api_client)
    create_new_transactions_request = {"transactions":[{"date":"2024-12-01","amount":"42.89","payee":"Food Town","category_id":315163,"status":"reviewed"}]} # CreateNewTransactionsRequest |

    try:
        # Insert one or more transactions.
        api_response = api_instance.create_new_transactions(create_new_transactions_request)
        print("The response of TransactionsBulkApi->create_new_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsBulkApi->create_new_transactions: %s\n" % e)
```

### Parameters

| Name                                | Type                                                                | Description | Notes |
| ----------------------------------- | ------------------------------------------------------------------- | ----------- | ----- |
| **create_new_transactions_request** | [**CreateNewTransactionsRequest**](CreateNewTransactionsRequest.md) |             |

### Return type

[**CreateNewTransactions201Response**](CreateNewTransactions201Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

-   **Content-Type**: application/json
-   **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                            | Response headers |
| ----------- | ------------------------------------------------------------------------------------------------------ | ---------------- |
| **201**     | Transactions successfully inserted                                                                     | -                |
| **400**     | Bad Request                                                                                            | -                |
| **401**     | Unauthorized. This error occurs when an invalid API token is passed to the request.                    | -                |
| **429**     | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. | -                |
| **500**     | Internal Server Error. Contact support.                                                                | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transactions**

> delete_transactions(delete_transactions_request)

Bulk delete existing transactions

Deletes the transaction with the IDs specified in the request body.<br> If any of the specified transactions are a split transaction or a split parent, or if any are a grouped transactions or part of a transaction group, the request will fail with a suggestion on how to unsplit or ungroup the transaction(s) prior to deletion. This will also fail if any of the specified transaction IDs do not exist.<br> Otherwise, the specified transactions are deleted. This action is not reversible!

### Example

-   Api Key Authentication (cookieAuth):
-   Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchable
from lunchable.models.delete_transactions_request import DeleteTransactionsRequest
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
    api_instance = lunchable.TransactionsBulkApi(api_client)
    delete_transactions_request = {"ids":[2112150653,2112150654,2112150655]} # DeleteTransactionsRequest |

    try:
        # Bulk delete existing transactions
        api_instance.delete_transactions(delete_transactions_request)
    except Exception as e:
        print("Exception when calling TransactionsBulkApi->delete_transactions: %s\n" % e)
```

### Parameters

| Name                            | Type                                                          | Description | Notes |
| ------------------------------- | ------------------------------------------------------------- | ----------- | ----- |
| **delete_transactions_request** | [**DeleteTransactionsRequest**](DeleteTransactionsRequest.md) |             |

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

-   **Content-Type**: application/json
-   **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                            | Response headers |
| ----------- | ------------------------------------------------------------------------------------------------------ | ---------------- |
| **204**     | No Content                                                                                             | -                |
| **400**     | Not Found                                                                                              | -                |
| **401**     | Unauthorized. This error occurs when an invalid API token is passed to the request.                    | -                |
| **404**     | Not Found                                                                                              | -                |
| **429**     | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. | -                |
| **500**     | Internal Server Error. Contact support.                                                                | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_transactions**

> GetAllTransactions200Response get_all_transactions(start_date=start_date, end_date=end_date, manual_account_id=manual_account_id, plaid_account_id=plaid_account_id, recurring_id=recurring_id, category_id=category_id, is_group=is_group, status=status, tag_id=tag_id, include_pending=include_pending, include_custom_metadata=include_custom_metadata, limit=limit, offset=offset)

Get all transactions

Retrieve a list of all transactions associated with a user's account. <br>If called with no parameters this endpoint will return up to 100 of the most recent transactions.

### Example

-   Api Key Authentication (cookieAuth):
-   Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchable
from lunchable.models.get_all_transactions200_response import GetAllTransactions200Response
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
    api_instance = lunchable.TransactionsBulkApi(api_client)
    start_date = '2013-10-20' # date | Denotes the beginning of the time period to fetch transactions for. If omitted, the most recent transactions will be returned.  See `limit`. Required if end_date exists. <br> (optional)
    end_date = '2013-10-20' # date | Denotes the end of the time period you'd like to get transactions for. Required if start_date exists. (optional)
    manual_account_id = 219909 # int | Filter transactions to those associated with specified manual account ID or set this to 0 to omit any transactions from manual accounts. Setting both this and `synched_account_id` to 0 will return transactions with no account. These are listed as \"Cash Transactions\" in the Lunch Money GUI. (optional)
    plaid_account_id = 119807 # int | Filter transactions to those associated with specified plaid account ID or set this to 0 to omit any transactions from plaid accounts. Setting both this and `manual_account_id` to 0 will return transactions with no account. These are listed as \"Cash Transactions\" in the Lunch Money GUI. (optional)
    recurring_id = 994069 # int | Filter transactions to those associated with specified Recurring Item ID  (optional)
    category_id = 83 # int | Filter transactions to those associated with the specified category ID. Will also match category groups. (optional)
    is_group = True # bool | Filter by group (returns only grouped transactions if set to true) (optional)
    status = 'unreviewed' # str | Filter transactions to those with the specified status:<br> - `reviewed`: Only user reviewed transactions or those that were automatically marked as reviewed due to reviewed recurring_item logic<br> - `unreviewed`: Only transactions that need to be reviewed<br> - `delete_pending`: Only transactions that require manual intervention because the plaid account deleted this transaction after it was updated by the user. <br> - `pending`: Only pending transactions from synced accounts.  Must also set `include_pending` to true. (optional)
    tag_id = 56 # int | Filter transactions to those that have a tag with the specified Tag ID (optional)
    include_pending = False # bool | Pass in true if you’d like to include imported transactions with a pending status. (optional) (default to False)
    include_custom_metadata = False # bool | Pass in true if you’d like the returned transactions objects to include any custom metadata that was previously added via the API. (optional) (default to False)
    limit = 100 # int | Sets the maximum number of transactions to return. If more match the filter criteria, the response will include a `has_more` attribute set to `true`.  See [pagination](foo) (optional) (default to 100)
    offset = 56 # int | Sets the offset for the records returned. This is typically set automatically in the header.  See [Pagination](/foo) (optional)

    try:
        # Get all transactions
        api_response = api_instance.get_all_transactions(start_date=start_date, end_date=end_date, manual_account_id=manual_account_id, plaid_account_id=plaid_account_id, recurring_id=recurring_id, category_id=category_id, is_group=is_group, status=status, tag_id=tag_id, include_pending=include_pending, include_custom_metadata=include_custom_metadata, limit=limit, offset=offset)
        print("The response of TransactionsBulkApi->get_all_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsBulkApi->get_all_transactions: %s\n" % e)
```

### Parameters

| Name                        | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Notes                         |
| --------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| **start_date**              | **date** | Denotes the beginning of the time period to fetch transactions for. If omitted, the most recent transactions will be returned. See &#x60;limit&#x60;. Required if end_date exists. &lt;br&gt;                                                                                                                                                                                                                                                                                                                                                                                                                          | [optional]                    |
| **end_date**                | **date** | Denotes the end of the time period you&#39;d like to get transactions for. Required if start_date exists.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [optional]                    |
| **manual_account_id**       | **int**  | Filter transactions to those associated with specified manual account ID or set this to 0 to omit any transactions from manual accounts. Setting both this and &#x60;synched_account_id&#x60; to 0 will return transactions with no account. These are listed as \&quot;Cash Transactions\&quot; in the Lunch Money GUI.                                                                                                                                                                                                                                                                                               | [optional]                    |
| **plaid_account_id**        | **int**  | Filter transactions to those associated with specified plaid account ID or set this to 0 to omit any transactions from plaid accounts. Setting both this and &#x60;manual_account_id&#x60; to 0 will return transactions with no account. These are listed as \&quot;Cash Transactions\&quot; in the Lunch Money GUI.                                                                                                                                                                                                                                                                                                  | [optional]                    |
| **recurring_id**            | **int**  | Filter transactions to those associated with specified Recurring Item ID                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [optional]                    |
| **category_id**             | **int**  | Filter transactions to those associated with the specified category ID. Will also match category groups.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [optional]                    |
| **is_group**                | **bool** | Filter by group (returns only grouped transactions if set to true)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | [optional]                    |
| **status**                  | **str**  | Filter transactions to those with the specified status:&lt;br&gt; - &#x60;reviewed&#x60;: Only user reviewed transactions or those that were automatically marked as reviewed due to reviewed recurring_item logic&lt;br&gt; - &#x60;unreviewed&#x60;: Only transactions that need to be reviewed&lt;br&gt; - &#x60;delete_pending&#x60;: Only transactions that require manual intervention because the plaid account deleted this transaction after it was updated by the user. &lt;br&gt; - &#x60;pending&#x60;: Only pending transactions from synced accounts. Must also set &#x60;include_pending&#x60; to true. | [optional]                    |
| **tag_id**                  | **int**  | Filter transactions to those that have a tag with the specified Tag ID                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | [optional]                    |
| **include_pending**         | **bool** | Pass in true if you’d like to include imported transactions with a pending status.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | [optional] [default to False] |
| **include_custom_metadata** | **bool** | Pass in true if you’d like the returned transactions objects to include any custom metadata that was previously added via the API.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | [optional] [default to False] |
| **limit**                   | **int**  | Sets the maximum number of transactions to return. If more match the filter criteria, the response will include a &#x60;has_more&#x60; attribute set to &#x60;true&#x60;. See [pagination](foo)                                                                                                                                                                                                                                                                                                                                                                                                                        | [optional] [default to 100]   |
| **offset**                  | **int**  | Sets the offset for the records returned. This is typically set automatically in the header. See [Pagination](/foo)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | [optional]                    |

### Return type

[**GetAllTransactions200Response**](GetAllTransactions200Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

-   **Content-Type**: Not defined
-   **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                                                                                                   | Response headers |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **200**     | Returns an array of transactions. &lt;br&gt;&lt;br&gt;The &#x60;has_more&#x60; property is set to &#x60;true&#x60; if more transactions are available. See [Pagination](/foo) | -                |
| **400**     | Invalid request parameters                                                                                                                                                    | -                |
| **401**     | Unauthorized. This error occurs when an invalid API token is passed to the request.                                                                                           | -                |
| **429**     | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header.                                                                        | -                |
| **500**     | Internal Server Error. Contact support.                                                                                                                                       | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

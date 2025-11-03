# lunchable.TransactionsBulkApi

All URIs are relative to *https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2*

| Method                                                                        | HTTP request             | Description                       |
| ----------------------------------------------------------------------------- | ------------------------ | --------------------------------- |
| [**create_new_transactions**](TransactionsBulkApi.md#create_new_transactions) | **POST** /transactions   | Insert one or more transactions.  |
| [**delete_transactions**](TransactionsBulkApi.md#delete_transactions)         | **DELETE** /transactions | Bulk delete existing transactions |
| [**get_all_transactions**](TransactionsBulkApi.md#get_all_transactions)       | **GET** /transactions    | Get all transactions              |
| [**update_transactions**](TransactionsBulkApi.md#update_transactions)         | **PUT** /transactions    | Update multiple transactions      |

# **create_new_transactions**

> InsertTransactionsResponseObject create_new_transactions(create_new_transactions_request)

Insert one or more transactions.

Use this endpoint to add transactions to a budget.

The request body for this endpoint must include a list of transactions with at least one transaction and not more than 500 transactions to insert.

The successful request to this endpoint will return a [response body](v2#model/inserttransactionsresponseobject) will include two arrays:<br> - `transactions`: A list of transactions that were successfully inserted.<br> - `skipped_duplicates`: A list of transactions that were duplicates of existing transactions and were not inserted.

### Example

-   Api Key Authentication (cookieAuth):
-   Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchable
from lunchable.models.create_new_transactions_request import CreateNewTransactionsRequest
from lunchable.models.insert_transactions_response_object import InsertTransactionsResponseObject
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
    create_new_transactions_request = {"transactions":[{"date":"2024-12-01","amount":42.89,"payee":"Food Town","category_id":315163,"status":"reviewed"}]} # CreateNewTransactionsRequest |

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

[**InsertTransactionsResponseObject**](InsertTransactionsResponseObject.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

-   **Content-Type**: application/json
-   **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                            | Response headers |
| ----------- | ------------------------------------------------------------------------------------------------------ | ---------------- |
| **201**     | Created                                                                                                | -                |
| **400**     | Bad Request                                                                                            | -                |
| **401**     | Unauthorized. This error occurs when an invalid API token is passed to the request.                    | -                |
| **429**     | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. | -                |
| **500**     | Internal Server Error. Contact support.                                                                | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transactions**

> delete_transactions(delete_transactions_request)

Bulk delete existing transactions

Deletes the transaction with the IDs specified in the request body.<br>
If any of the specified transactions are a split transaction or a split parent, or if any are a grouped transactions or part of a transaction group, the request will fail with a suggestion on how to unsplit or ungroup the transaction(s) prior to deletion. This will also fail if any of the specified transaction IDs do not exist.<br>
Otherwise, the specified transactions are deleted. This action is not reversible!

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

> GetAllTransactions200Response get_all_transactions(start_date=start_date, end_date=end_date, manual_account_id=manual_account_id, plaid_account_id=plaid_account_id, recurring_id=recurring_id, category_id=category_id, tag_id=tag_id, is_group=is_group, status=status, is_pending=is_pending, include_pending=include_pending, include_metadata=include_metadata, include_split_parents=include_split_parents, include_children=include_children, include_files=include_files, limit=limit, offset=offset)

Get all transactions

Retrieve a list of all transactions associated with a user's account. <br>If called with no parameters this endpoint will return the most recent transactions up to `limit` number of transactions.

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
    start_date = '2013-10-20' # date | Denotes the beginning of the time period to fetch transactions for. If omitted, the most recent transactions will be returned. See `limit`. Required if end_date exists. <br> (optional)
    end_date = '2013-10-20' # date | Denotes the end of the time period you'd like to get transactions for. Required if start_date exists.  (optional)
    manual_account_id = 219909 # int | Filter transactions to those associated with specified manual account ID or set this to 0 to omit any transactions from manual accounts. Setting both this and `synched_account_id` to 0 will return transactions with no account. These are listed as \"Cash Transactions\" in the Lunch Money GUI. (optional)
    plaid_account_id = 119807 # int | Filter transactions to those associated with specified plaid account ID or set this to 0 to omit any transactions from plaid accounts. Setting both this and `manual_account_id` to 0 will return transactions with no account. These are listed as \"Cash Transactions\" in the Lunch Money GUI. (optional)
    recurring_id = 994069 # int | Filter transactions to those associated with specified Recurring  Item ID  (optional)
    category_id = 83 # int | Filter transactions to those associated with the specified category ID. Will also match category groups.  Set this to 0 to return only un-categorized transactions (optional)
    tag_id = 56 # int | Filter transactions to those that have a tag with the specified Tag ID (optional)
    is_group = True # bool | Filter by group (returns only transaction groups if set to true) (optional)
    status = 'unreviewed' # str | Filter transactions to those with the specified status:<br> - `reviewed`: Only user reviewed transactions or those that were automatically marked as reviewed due to reviewed recurring_item logic<br> - `unreviewed`: Only transactions that need to be reviewed<br> - `delete_pending`: Only transactions that require manual intervention because the plaid account deleted this transaction after it was updated by the user. (optional)
    is_pending = true # bool | Filter transactions by pending status. Set to `true` to return only pending transactions, or `false` to return only non-pending transactions. When this parameter is set, it takes precedence over `include_pending`. Note: Pending transactions always have a status of `unreviewed`, so when setting this parameter to `true`, either omit the `status` parameter or set it to `unreviewed`.  (optional)
    include_pending = False # bool | By default, pending transactions are excluded from results. Set to `true` to include imported transactions with a pending status in the results. This query param is ignored if the `is_pending` query param is also set.  (optional) (default to False)
    include_metadata = False # bool | By default, custom and plaid metadata are not included in the response.  Set to true if you'd like the returned transactions objects to include any  metadata associated with the transactions. (optional) (default to False)
    include_split_parents = False # bool | By default, transactions that were split into multiple transactions are not included in the response. Set to true if you'd like the returned transactions objects to include any  transactions that were split into multiple transactions.  Use with caution as this data is normally not exposed after the split transactions are created. (optional) (default to False)
    include_children = False # bool | By default, the `children` property is not included in the response. Set to true if you'd like the children property to be populated with the transactions that  make up a transaction group, or, if the `include_split_parents` query param is also set,  the transactions that were split from a parent transaction. (optional) (default to False)
    include_files = False # bool | By default, the `files` property is not included in the response. Set to true if you'd like the responses to include a list of of  objects that describe any files attached to the transactions. (optional) (default to False)
    limit = 100 # int | Sets the maximum number of transactions to return. If more match the filter criteria, the response will include a `has_more` attribute set to `true`. See [pagination](foo) (optional) (default to 100)
    offset = 56 # int | Sets the offset for the records returned. This is typically set automatically in the header. See [Pagination](/foo) (optional)

    try:
        # Get all transactions
        api_response = api_instance.get_all_transactions(start_date=start_date, end_date=end_date, manual_account_id=manual_account_id, plaid_account_id=plaid_account_id, recurring_id=recurring_id, category_id=category_id, tag_id=tag_id, is_group=is_group, status=status, is_pending=is_pending, include_pending=include_pending, include_metadata=include_metadata, include_split_parents=include_split_parents, include_children=include_children, include_files=include_files, limit=limit, offset=offset)
        print("The response of TransactionsBulkApi->get_all_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsBulkApi->get_all_transactions: %s\n" % e)
```

### Parameters

| Name                      | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Notes                         |
| ------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| **start_date**            | **date** | Denotes the beginning of the time period to fetch transactions for. If omitted, the most recent transactions will be returned. See &#x60;limit&#x60;. Required if end_date exists. &lt;br&gt;                                                                                                                                                                                                                                                                                     | [optional]                    |
| **end_date**              | **date** | Denotes the end of the time period you&#39;d like to get transactions for. Required if start_date exists.                                                                                                                                                                                                                                                                                                                                                                         | [optional]                    |
| **manual_account_id**     | **int**  | Filter transactions to those associated with specified manual account ID or set this to 0 to omit any transactions from manual accounts. Setting both this and &#x60;synched_account_id&#x60; to 0 will return transactions with no account. These are listed as \&quot;Cash Transactions\&quot; in the Lunch Money GUI.                                                                                                                                                          | [optional]                    |
| **plaid_account_id**      | **int**  | Filter transactions to those associated with specified plaid account ID or set this to 0 to omit any transactions from plaid accounts. Setting both this and &#x60;manual_account_id&#x60; to 0 will return transactions with no account. These are listed as \&quot;Cash Transactions\&quot; in the Lunch Money GUI.                                                                                                                                                             | [optional]                    |
| **recurring_id**          | **int**  | Filter transactions to those associated with specified Recurring Item ID                                                                                                                                                                                                                                                                                                                                                                                                          | [optional]                    |
| **category_id**           | **int**  | Filter transactions to those associated with the specified category ID. Will also match category groups. Set this to 0 to return only un-categorized transactions                                                                                                                                                                                                                                                                                                                 | [optional]                    |
| **tag_id**                | **int**  | Filter transactions to those that have a tag with the specified Tag ID                                                                                                                                                                                                                                                                                                                                                                                                            | [optional]                    |
| **is_group**              | **bool** | Filter by group (returns only transaction groups if set to true)                                                                                                                                                                                                                                                                                                                                                                                                                  | [optional]                    |
| **status**                | **str**  | Filter transactions to those with the specified status:&lt;br&gt; - &#x60;reviewed&#x60;: Only user reviewed transactions or those that were automatically marked as reviewed due to reviewed recurring_item logic&lt;br&gt; - &#x60;unreviewed&#x60;: Only transactions that need to be reviewed&lt;br&gt; - &#x60;delete_pending&#x60;: Only transactions that require manual intervention because the plaid account deleted this transaction after it was updated by the user. | [optional]                    |
| **is_pending**            | **bool** | Filter transactions by pending status. Set to &#x60;true&#x60; to return only pending transactions, or &#x60;false&#x60; to return only non-pending transactions. When this parameter is set, it takes precedence over &#x60;include_pending&#x60;. Note: Pending transactions always have a status of &#x60;unreviewed&#x60;, so when setting this parameter to &#x60;true&#x60;, either omit the &#x60;status&#x60; parameter or set it to &#x60;unreviewed&#x60;.              | [optional]                    |
| **include_pending**       | **bool** | By default, pending transactions are excluded from results. Set to &#x60;true&#x60; to include imported transactions with a pending status in the results. This query param is ignored if the &#x60;is_pending&#x60; query param is also set.                                                                                                                                                                                                                                     | [optional] [default to False] |
| **include_metadata**      | **bool** | By default, custom and plaid metadata are not included in the response. Set to true if you&#39;d like the returned transactions objects to include any metadata associated with the transactions.                                                                                                                                                                                                                                                                                 | [optional] [default to False] |
| **include_split_parents** | **bool** | By default, transactions that were split into multiple transactions are not included in the response. Set to true if you&#39;d like the returned transactions objects to include any transactions that were split into multiple transactions. Use with caution as this data is normally not exposed after the split transactions are created.                                                                                                                                     | [optional] [default to False] |
| **include_children**      | **bool** | By default, the &#x60;children&#x60; property is not included in the response. Set to true if you&#39;d like the children property to be populated with the transactions that make up a transaction group, or, if the &#x60;include_split_parents&#x60; query param is also set, the transactions that were split from a parent transaction.                                                                                                                                      | [optional] [default to False] |
| **include_files**         | **bool** | By default, the &#x60;files&#x60; property is not included in the response. Set to true if you&#39;d like the responses to include a list of of objects that describe any files attached to the transactions.                                                                                                                                                                                                                                                                     | [optional] [default to False] |
| **limit**                 | **int**  | Sets the maximum number of transactions to return. If more match the filter criteria, the response will include a &#x60;has_more&#x60; attribute set to &#x60;true&#x60;. See [pagination](foo)                                                                                                                                                                                                                                                                                   | [optional] [default to 100]   |
| **offset**                | **int**  | Sets the offset for the records returned. This is typically set automatically in the header. See [Pagination](/foo)                                                                                                                                                                                                                                                                                                                                                               | [optional]                    |

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

# **update_transactions**

> UpdateTransactions200Response update_transactions(update_transactions_request)

Update multiple transactions

Modifies the properties of multiple existing transactions in a single request.<br><br>
You may submit complete transaction objects from the response returned by a `GET /transactions` in the request body for each transaction, however only certain properties can be updated using this API. The following system set properties are accepted in the request body, but their values will be ignored: `id`, `to_base`, `is_pending`, `created_at`, `updated_at`, `source`, and `plaid_metadata`.<br><br>
Transactions that have been previously split or grouped may not be modified by this endpoint. Therefore the `is_parent`, `parent_id`, `is_group`, `group_id`, and `children` properties are also ignored when provided in the request body.<br><br>
Each transaction in the array **must** include an `id` property to identify which transaction to update, along with at least one other property to be updated. For example, a transaction object that contains only an `id` and `category_id` property is valid.<br><br>
The request can include between 1 and 500 transactions to update in a single call.

### Example

-   Api Key Authentication (cookieAuth):
-   Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchable
from lunchable.models.update_transactions200_response import UpdateTransactions200Response
from lunchable.models.update_transactions_request import UpdateTransactionsRequest
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
    update_transactions_request = {"transactions":[{"id":2112150654,"category_id":315162,"notes":"Treat restaurants the same as groceries"},{"id":2112150649,"category_id":315162,"notes":"Treat restaurants the same as groceries"},{"id":2112140372,"category_id":315162,"notes":"Treat restaurants the same as groceries"}]} # UpdateTransactionsRequest |

    try:
        # Update multiple transactions
        api_response = api_instance.update_transactions(update_transactions_request)
        print("The response of TransactionsBulkApi->update_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsBulkApi->update_transactions: %s\n" % e)
```

### Parameters

| Name                            | Type                                                          | Description | Notes |
| ------------------------------- | ------------------------------------------------------------- | ----------- | ----- |
| **update_transactions_request** | [**UpdateTransactionsRequest**](UpdateTransactionsRequest.md) |             |

### Return type

[**UpdateTransactions200Response**](UpdateTransactions200Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

-   **Content-Type**: application/json
-   **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                            | Response headers |
| ----------- | ------------------------------------------------------------------------------------------------------ | ---------------- |
| **200**     | Transactions successfully updated                                                                      | -                |
| **400**     | Bad Request                                                                                            | -                |
| **401**     | Unauthorized. This error occurs when an invalid API token is passed to the request.                    | -                |
| **429**     | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. | -                |
| **500**     | Internal Server Error. Contact support.                                                                | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

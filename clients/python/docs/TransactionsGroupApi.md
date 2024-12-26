# lunchable.TransactionsGroupApi

All URIs are relative to *https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**group_transactions**](TransactionsGroupApi.md#group_transactions) | **POST** /transactions/group | Create a transaction group
[**ungroup_transactions**](TransactionsGroupApi.md#ungroup_transactions) | **DELETE** /transactions/group/{id} | Delete a transaction group


# **group_transactions**
> GroupTransactions201Response group_transactions(group_transactions_request)

Create a transaction group

Specify a set of existing transaction IDs to group together as a single grouped transaction.   The new transaction will have an amount equal to the sum of the grouped transaction amounts.  If the  grouped transactions have different currencies, the new group transaction will be set in the user's default currency.<br><br>  After a transaction has been grouped the original transactions are no longer shown on the  transactions page or returned by a `GET /transactions` request. The newly created grouped  transaction is returned instead.  To see the details of the original transactions that were used to create a transaction group, use the `GET /transactions/{id}` endpoint, passing the ID of the grouped transaction.  The grouped transactions will be included in the `children` property of the transaction returned in the response 

### Example

* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchable
from lunchable.models.group_transactions201_response import GroupTransactions201Response
from lunchable.models.group_transactions_request import GroupTransactionsRequest
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
    api_instance = lunchable.TransactionsGroupApi(api_client)
    group_transactions_request = {"ids":[2112140365,2112140361],"payee":"Home Entertainment Transactions","date":"2024-12-10"} # GroupTransactionsRequest | 

    try:
        # Create a transaction group
        api_response = api_instance.group_transactions(group_transactions_request)
        print("The response of TransactionsGroupApi->group_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsGroupApi->group_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_transactions_request** | [**GroupTransactionsRequest**](GroupTransactionsRequest.md)|  | 

### Return type

[**GroupTransactions201Response**](GroupTransactions201Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The new grouped parent transaction with populated children attribute |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized.  This error occurs when an invalid API token is passed to the request. |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ungroup_transactions**
> ungroup_transactions(id)

Delete a transaction group

Deletes the transaction group with the ID specified on the path.<br> The transactions within the group are not removed and will subsequently be treated as \"normal\" ungrouped transactions.

### Example

* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (bearerSecurity):

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
    api_instance = lunchable.TransactionsGroupApi(api_client)
    id = 2112140959 # int | ID of the transaction group to delete

    try:
        # Delete a transaction group
        api_instance.ungroup_transactions(id)
    except Exception as e:
        print("Exception when calling TransactionsGroupApi->ungroup_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the transaction group to delete | 

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**401** | Unauthorized.  This error occurs when an invalid API token is passed to the request. |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


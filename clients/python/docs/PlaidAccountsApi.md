# lunchable.PlaidAccountsApi

All URIs are relative to *https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2*

| Method                                                                             | HTTP request                   | Description                                   |
| ---------------------------------------------------------------------------------- | ------------------------------ | --------------------------------------------- |
| [**get_all_plaid_accounts**](PlaidAccountsApi.md#get_all_plaid_accounts)           | **GET** /plaid_accounts        | Get all accounts synced via Plaid             |
| [**get_plaid_account_by_id**](PlaidAccountsApi.md#get_plaid_account_by_id)         | **GET** /plaid_accounts/{id}   | Get a single account that is synced via Plaid |
| [**trigger_plaid_account_fetch**](PlaidAccountsApi.md#trigger_plaid_account_fetch) | **POST** /plaid_accounts/fetch | Trigger Fetch from Plaid                      |

# **get_all_plaid_accounts**

> GetAllPlaidAccounts200Response get_all_plaid_accounts()

Get all accounts synced via Plaid

Retrieve a list of all synced accounts associated with the user's account.

### Example

-   Api Key Authentication (cookieAuth):
-   Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchable
from lunchable.models.get_all_plaid_accounts200_response import GetAllPlaidAccounts200Response
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
    api_instance = lunchable.PlaidAccountsApi(api_client)

    try:
        # Get all accounts synced via Plaid
        api_response = api_instance.get_all_plaid_accounts()
        print("The response of PlaidAccountsApi->get_all_plaid_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaidAccountsApi->get_all_plaid_accounts: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetAllPlaidAccounts200Response**](GetAllPlaidAccounts200Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

-   **Content-Type**: Not defined
-   **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                            | Response headers |
| ----------- | ------------------------------------------------------------------------------------------------------ | ---------------- |
| **200**     | A list of accounts synced via Plaid                                                                    | -                |
| **400**     | Bad Request                                                                                            | -                |
| **401**     | Unauthorized. This error occurs when an invalid API token is passed to the request.                    | -                |
| **429**     | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. | -                |
| **500**     | Internal Server Error. Contact support.                                                                | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plaid_account_by_id**

> PlaidAccountObject get_plaid_account_by_id(id)

Get a single account that is synced via Plaid

Retrieve the details of the plaid account with the specified ID.

### Example

-   Api Key Authentication (cookieAuth):
-   Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchable
from lunchable.models.plaid_account_object import PlaidAccountObject
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
    api_instance = lunchable.PlaidAccountsApi(api_client)
    id = 119805 # int | ID of the plaid account to retrieve

    try:
        # Get a single account that is synced via Plaid
        api_response = api_instance.get_plaid_account_by_id(id)
        print("The response of PlaidAccountsApi->get_plaid_account_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaidAccountsApi->get_plaid_account_by_id: %s\n" % e)
```

### Parameters

| Name   | Type    | Description                         | Notes |
| ------ | ------- | ----------------------------------- | ----- |
| **id** | **int** | ID of the plaid account to retrieve |

### Return type

[**PlaidAccountObject**](PlaidAccountObject.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

-   **Content-Type**: Not defined
-   **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                            | Response headers |
| ----------- | ------------------------------------------------------------------------------------------------------ | ---------------- |
| **200**     | Plaid Account Object with the requested account.                                                       | -                |
| **400**     | Bad Request                                                                                            | -                |
| **401**     | Unauthorized. This error occurs when an invalid API token is passed to the request.                    | -                |
| **404**     | Not Found                                                                                              | -                |
| **429**     | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. | -                |
| **500**     | Internal Server Error. Contact support.                                                                | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_plaid_account_fetch**

> bool trigger_plaid_account_fetch(start_date=start_date, end_date=end_date, plaid_account_id=plaid_account_id)

Trigger Fetch from Plaid

Use this endpoint to trigger a fetch for latest data from Plaid. Eligible accounts are those who last_fetch value is over 1 minute ago. (Although the limit is every minute, please use this endpoint sparingly!) Note that fetching from Plaid is a background job. This endpoint simply queues up the job. You may track the `plaid_last_successful_update`, `last_fetch` and `last_import` properties to verify the results of the fetch. The `last fetch` property is updated when Plaid accepts a request to fetch data. The `plaid_last_successful_update`is updated when it successfully contacts the associated financial institution. The `last_import` field is updated only when new transactions have been imported.

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
    api_instance = lunchable.PlaidAccountsApi(api_client)
    start_date = '2013-10-20' # date | Denotes the beginning of the time period to fetch transactions for. If omitted, the most recent transactions will be returned. <br> Required if end_date exists. <br> (optional)
    end_date = '2013-10-20' # date | Denotes the end of the time period you'd like to get transactions for. Required if start_date exists.  (optional)
    plaid_account_id = 119807 # int | Specific ID of a plaid account to fetch. If not set the endpoint will trigger a fetch for all eligible accounts. (optional)

    try:
        # Trigger Fetch from Plaid
        api_response = api_instance.trigger_plaid_account_fetch(start_date=start_date, end_date=end_date, plaid_account_id=plaid_account_id)
        print("The response of PlaidAccountsApi->trigger_plaid_account_fetch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaidAccountsApi->trigger_plaid_account_fetch: %s\n" % e)
```

### Parameters

| Name                 | Type     | Description                                                                                                                                                                       | Notes      |
| -------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **start_date**       | **date** | Denotes the beginning of the time period to fetch transactions for. If omitted, the most recent transactions will be returned. &lt;br&gt; Required if end_date exists. &lt;br&gt; | [optional] |
| **end_date**         | **date** | Denotes the end of the time period you&#39;d like to get transactions for. Required if start_date exists.                                                                         | [optional] |
| **plaid_account_id** | **int**  | Specific ID of a plaid account to fetch. If not set the endpoint will trigger a fetch for all eligible accounts.                                                                  | [optional] |

### Return type

**bool**

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

-   **Content-Type**: Not defined
-   **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Response headers |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **200**     | A value of true is returned if Plaid acknowledged the fetch request. This indicates that it is possible that query the &#x60;GET /plaid_accounts&#x60; endpoint to determine if the request was successful (&#x60;plaid_last_successful_update&#x60; is more recent than &#x60;last_fetch), or if new transactions were synced (&#x60;last_import&#x60; is more recent than &#x60;last_fetch&#x60;).&lt;br&gt; If false is returned the request failed. This can occur if the requested account does not exist, if there are no Plaid accounts associated with the user, or if a request was already made within the last minute. | -                |
| **400**     | Bad Request                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | -                |
| **401**     | Unauthorized. This error occurs when an invalid API token is passed to the request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | -                |
| **404**     | Not Found                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | -                |
| **429**     | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | -                |
| **500**     | Internal Server Error. Contact support.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

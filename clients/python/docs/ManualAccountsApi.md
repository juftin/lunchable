# lunchable.ManualAccountsApi

All URIs are relative to *https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_manual_account**](ManualAccountsApi.md#create_manual_account) | **POST** /manual_accounts | Create a manual account
[**delete_manual_account**](ManualAccountsApi.md#delete_manual_account) | **DELETE** /manual_accounts/{id} | Delete a manual account
[**get_all_manual_accounts**](ManualAccountsApi.md#get_all_manual_accounts) | **GET** /manual_accounts | Get all manual accounts
[**get_manual_account_by_id**](ManualAccountsApi.md#get_manual_account_by_id) | **GET** /manual_accounts/{id} | Get a single manual account
[**update_manual_account**](ManualAccountsApi.md#update_manual_account) | **PUT** /manual_accounts/{id} | Update an existing manual account


# **create_manual_account**
> ManualAccountObject create_manual_account(create_manual_account_request_object)

Create a manual account

Create a new manually-managed account.

### Example

* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchable
from lunchable.models.create_manual_account_request_object import CreateManualAccountRequestObject
from lunchable.models.manual_account_object import ManualAccountObject
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
    api_instance = lunchable.ManualAccountsApi(api_client)
    create_manual_account_request_object = {"name":"API created Account","type":"cash","balance":"100"} # CreateManualAccountRequestObject | 

    try:
        # Create a manual account
        api_response = api_instance.create_manual_account(create_manual_account_request_object)
        print("The response of ManualAccountsApi->create_manual_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManualAccountsApi->create_manual_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_manual_account_request_object** | [**CreateManualAccountRequestObject**](CreateManualAccountRequestObject.md)|  | 

### Return type

[**ManualAccountObject**](ManualAccountObject.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created manual account |  -  |
**400** | Invalid request body |  -  |
**401** | Unauthorized.  This error occurs when an invalid API token is passed to the request. |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_manual_account**
> delete_manual_account(id)

Delete a manual account

Deletes the single manual account with the ID specified on the path. If any transactions exist with the `manual_account_id` property set to this account's ID they will appear with a warning when displayed in the web view.

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
    api_instance = lunchable.ManualAccountsApi(api_client)
    id = 119807 # int | ID of the manual account to delete

    try:
        # Delete a manual account
        api_instance.delete_manual_account(id)
    except Exception as e:
        print("Exception when calling ManualAccountsApi->delete_manual_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the manual account to delete | 

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

# **get_all_manual_accounts**
> GetAllManualAccounts200Response get_all_manual_accounts()

Get all manual accounts

Retrieve a list of all manually-managed accounts associated with the user's account.

### Example

* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchable
from lunchable.models.get_all_manual_accounts200_response import GetAllManualAccounts200Response
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
    api_instance = lunchable.ManualAccountsApi(api_client)

    try:
        # Get all manual accounts
        api_response = api_instance.get_all_manual_accounts()
        print("The response of ManualAccountsApi->get_all_manual_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManualAccountsApi->get_all_manual_accounts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetAllManualAccounts200Response**](GetAllManualAccounts200Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of manual accounts |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized.  This error occurs when an invalid API token is passed to the request. |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manual_account_by_id**
> ManualAccountObject get_manual_account_by_id(id)

Get a single manual account

Retrieve the details of the manual account with the specified ID.

### Example

* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchable
from lunchable.models.manual_account_object import ManualAccountObject
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
    api_instance = lunchable.ManualAccountsApi(api_client)
    id = 119807 # int | ID of the manual account to retrieve

    try:
        # Get a single manual account
        api_response = api_instance.get_manual_account_by_id(id)
        print("The response of ManualAccountsApi->get_manual_account_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManualAccountsApi->get_manual_account_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the manual account to retrieve | 

### Return type

[**ManualAccountObject**](ManualAccountObject.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Manual Account Object with the requested account. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized.  This error occurs when an invalid API token is passed to the request. |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_manual_account**
> ManualAccountObject update_manual_account(id, update_manual_account_request_object)

Update an existing manual account

Updates an existing manual account.  You may submit the response from a `GET /manual_accounts/{id}` as the request body which includes system created attributes such as `id` or `created_at`, however only the `name`, `type`, `subtype`, `display_name`, `balance`, `balance_as_of`, `closed_on`, `currency`, `institution_name`, `external_id`, and `exclude_from_transactions` can be updated using this API.  It is also possible to provide only the attribute(s) to be updated in the request body, as long as the request includes at least one of the attributes listed above. For example a request body that contains only a `name` attribute is valid.

### Example

* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchable
from lunchable.models.manual_account_object import ManualAccountObject
from lunchable.models.update_manual_account_request_object import UpdateManualAccountRequestObject
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
    api_instance = lunchable.ManualAccountsApi(api_client)
    id = 119807 # int | ID of the manual account to update
    update_manual_account_request_object = {"type":"credit"} # UpdateManualAccountRequestObject | 

    try:
        # Update an existing manual account
        api_response = api_instance.update_manual_account(id, update_manual_account_request_object)
        print("The response of ManualAccountsApi->update_manual_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManualAccountsApi->update_manual_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the manual account to update | 
 **update_manual_account_request_object** | [**UpdateManualAccountRequestObject**](UpdateManualAccountRequestObject.md)|  | 

### Return type

[**ManualAccountObject**](ManualAccountObject.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Manual Account updated successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized.  This error occurs when an invalid API token is passed to the request. |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. |  -  |
**500** | Internal Server Error. Contact support. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


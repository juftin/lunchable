# lunchable.RecurringApi

All URIs are relative to *https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2*

| Method                                                         | HTTP request            | Description                 |
| -------------------------------------------------------------- | ----------------------- | --------------------------- |
| [**get_all_recurring**](RecurringApi.md#get_all_recurring)     | **GET** /recurring      | Get a all recurring items   |
| [**get_recurring_by_id**](RecurringApi.md#get_recurring_by_id) | **GET** /recurring/{id} | Get a single recurring item |

# **get_all_recurring**

> GetAllRecurring200Response get_all_recurring(start_date=start_date, end_date=end_date, include_suggested=include_suggested)

Get a all recurring items

Get info about the recurring items for a specified time frame

### Example

-   Api Key Authentication (cookieAuth):
-   Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchable
from lunchable.models.get_all_recurring200_response import GetAllRecurring200Response
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
    api_instance = lunchable.RecurringApi(api_client)
    start_date = '2013-10-20' # date | Denotes the beginning of the range used to populate the `matching` object in the recurring items. If omitted, the current month will be used as the range.<br> Required if end_date exists. (optional)
    end_date = '2013-10-20' # date | Denotes the end of the the range used to populate the `matching` object in the recurring items.  Required if start_date exists.  (optional)
    include_suggested = True # bool |  (optional)

    try:
        # Get a all recurring items
        api_response = api_instance.get_all_recurring(start_date=start_date, end_date=end_date, include_suggested=include_suggested)
        print("The response of RecurringApi->get_all_recurring:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecurringApi->get_all_recurring: %s\n" % e)
```

### Parameters

| Name                  | Type     | Description                                                                                                                                                                                                 | Notes      |
| --------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **start_date**        | **date** | Denotes the beginning of the range used to populate the &#x60;matching&#x60; object in the recurring items. If omitted, the current month will be used as the range.&lt;br&gt; Required if end_date exists. | [optional] |
| **end_date**          | **date** | Denotes the end of the the range used to populate the &#x60;matching&#x60; object in the recurring items. Required if start_date exists.                                                                    | [optional] |
| **include_suggested** | **bool** |                                                                                                                                                                                                             | [optional] |

### Return type

[**GetAllRecurring200Response**](GetAllRecurring200Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

-   **Content-Type**: Not defined
-   **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                            | Response headers |
| ----------- | ------------------------------------------------------------------------------------------------------ | ---------------- |
| **200**     | A list of recurring items                                                                              | -                |
| **400**     | Bad Request                                                                                            | -                |
| **404**     | Not Found                                                                                              | -                |
| **401**     | Unauthorized. This error occurs when an invalid API token is passed to the request.                    | -                |
| **429**     | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. | -                |
| **500**     | Internal Server Error. Contact support.                                                                | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recurring_by_id**

> RecurringObject get_recurring_by_id(id, start_date=start_date, end_date=end_date)

Get a single recurring item

Retrieve the details of a specific recurring item with the specified ID.

### Example

-   Api Key Authentication (cookieAuth):
-   Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchable
from lunchable.models.recurring_object import RecurringObject
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
    api_instance = lunchable.RecurringApi(api_client)
    id = 994069 # int | ID of the recurring item to retrieve
    start_date = '2013-10-20' # date | Denotes the beginning of the range used to populate the `matching` object in the recurring items. If omitted, the current month will be used as the range.<br> Required if end_date exists. (optional)
    end_date = '2013-10-20' # date | Denotes the end of the the range used to populate the `matching` object in the recurring items.  Required if start_date exists.  (optional)

    try:
        # Get a single recurring item
        api_response = api_instance.get_recurring_by_id(id, start_date=start_date, end_date=end_date)
        print("The response of RecurringApi->get_recurring_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecurringApi->get_recurring_by_id: %s\n" % e)
```

### Parameters

| Name           | Type     | Description                                                                                                                                                                                                 | Notes      |
| -------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **id**         | **int**  | ID of the recurring item to retrieve                                                                                                                                                                        |
| **start_date** | **date** | Denotes the beginning of the range used to populate the &#x60;matching&#x60; object in the recurring items. If omitted, the current month will be used as the range.&lt;br&gt; Required if end_date exists. | [optional] |
| **end_date**   | **date** | Denotes the end of the the range used to populate the &#x60;matching&#x60; object in the recurring items. Required if start_date exists.                                                                    | [optional] |

### Return type

[**RecurringObject**](RecurringObject.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

-   **Content-Type**: Not defined
-   **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                            | Response headers |
| ----------- | ------------------------------------------------------------------------------------------------------ | ---------------- |
| **200**     | Tag Object with the requested Tag ID                                                                   | -                |
| **400**     | Bad Request                                                                                            | -                |
| **404**     | Not Found                                                                                              | -                |
| **401**     | Unauthorized. This error occurs when an invalid API token is passed to the request.                    | -                |
| **429**     | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. | -                |
| **500**     | Internal Server Error. Contact support.                                                                | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

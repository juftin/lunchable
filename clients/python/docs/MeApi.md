# lunchable.MeApi

All URIs are relative to *https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2*

| Method                        | HTTP request | Description      |
| ----------------------------- | ------------ | ---------------- |
| [**get_me**](MeApi.md#get_me) | **GET** /me  | Get current user |

# **get_me**

> UserObject get_me()

Get current user

Get details about the user associated with the supplied authorization token.

### Example

-   Api Key Authentication (cookieAuth):
-   Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchable
from lunchable.models.user_object import UserObject
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
    api_instance = lunchable.MeApi(api_client)

    try:
        # Get current user
        api_response = api_instance.get_me()
        print("The response of MeApi->get_me:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeApi->get_me: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**UserObject**](UserObject.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

-   **Content-Type**: Not defined
-   **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                            | Response headers |
| ----------- | ------------------------------------------------------------------------------------------------------ | ---------------- |
| **200**     | The User Object associated with the authorized token.                                                  | -                |
| **401**     | Unauthorized. This error occurs when an invalid API token is passed to the request.                    | -                |
| **429**     | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. | -                |
| **500**     | Internal Server Error. Contact support.                                                                | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

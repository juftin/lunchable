# lunchable.CategoriesApi

All URIs are relative to *https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2*

| Method                                                        | HTTP request                | Description                                   |
| ------------------------------------------------------------- | --------------------------- | --------------------------------------------- |
| [**create_category**](CategoriesApi.md#create_category)       | **POST** /categories        | Create a new category or category group       |
| [**delete_category**](CategoriesApi.md#delete_category)       | **DELETE** /categories/{id} | Delete a category or category group           |
| [**get_all_categories**](CategoriesApi.md#get_all_categories) | **GET** /categories         | Get all categories                            |
| [**get_category_by_id**](CategoriesApi.md#get_category_by_id) | **GET** /categories/{id}    | Get a single category                         |
| [**update_category**](CategoriesApi.md#update_category)       | **PUT** /categories/{id}    | Update an existing category or category group |

# **create_category**

> CategoryObject create_category(create_category_request_object)

Create a new category or category group

Creates a new category with the given name.<br> If the `is_group` attribute is set to true, a category group is created. In this case the `children` attribute may also be set to an array of existing category IDs to add to the newly created category group.

### Example

-   Api Key Authentication (cookieAuth):
-   Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchable
from lunchable.models.category_object import CategoryObject
from lunchable.models.create_category_request_object import CreateCategoryRequestObject
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
    api_instance = lunchable.CategoriesApi(api_client)
    create_category_request_object = {"name":"API Created Category","description":"Test description of created category","is_income":false,"exclude_from_budget":true,"exclude_from_totals":false,"is_group":false} # CreateCategoryRequestObject |

    try:
        # Create a new category or category group
        api_response = api_instance.create_category(create_category_request_object)
        print("The response of CategoriesApi->create_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->create_category: %s\n" % e)
```

### Parameters

| Name                               | Type                                                              | Description | Notes |
| ---------------------------------- | ----------------------------------------------------------------- | ----------- | ----- |
| **create_category_request_object** | [**CreateCategoryRequestObject**](CreateCategoryRequestObject.md) |             |

### Return type

[**CategoryObject**](CategoryObject.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

-   **Content-Type**: application/json
-   **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                            | Response headers |
| ----------- | ------------------------------------------------------------------------------------------------------ | ---------------- |
| **201**     | Category or Category Group Object with the successfully created category or category group.            | -                |
| **400**     | Bad Request                                                                                            | -                |
| **401**     | Unauthorized. This error occurs when an invalid API token is passed to the request.                    | -                |
| **429**     | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. | -                |
| **500**     | Internal Server Error. Contact support.                                                                | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_category**

> delete_category(id, force=force)

Delete a category or category group

Attempts to delete the single category or category group specified on the path. By default his will only work if there are no dependencies, such as existing budgets for the category, categorized transactions, children categories for a category group, categorized recurring items, etc. If there are dependents, this endpoint will return and object that describes each of the possible dependencies are and how many there are.

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
    api_instance = lunchable.CategoriesApi(api_client)
    id = 83 # int | ID of the category to delete
    force = False # bool | Set to true to force deletion even if there are dependencies (optional) (default to False)

    try:
        # Delete a category or category group
        api_instance.delete_category(id, force=force)
    except Exception as e:
        print("Exception when calling CategoriesApi->delete_category: %s\n" % e)
```

### Parameters

| Name      | Type     | Description                                                  | Notes                         |
| --------- | -------- | ------------------------------------------------------------ | ----------------------------- |
| **id**    | **int**  | ID of the category to delete                                 |
| **force** | **bool** | Set to true to force deletion even if there are dependencies | [optional] [default to False] |

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
| **422**     | Unprocessable Entity                                                                                   | -                |
| **401**     | Unauthorized. This error occurs when an invalid API token is passed to the request.                    | -                |
| **404**     | Not Found                                                                                              | -                |
| **429**     | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. | -                |
| **500**     | Internal Server Error. Contact support.                                                                | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_categories**

> GetAllCategories200Response get_all_categories(format=format, is_group=is_group)

Get all categories

Retrieve a list of all categories associated with the user's account.

### Example

-   Api Key Authentication (cookieAuth):
-   Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchable
from lunchable.models.get_all_categories200_response import GetAllCategories200Response
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
    api_instance = lunchable.CategoriesApi(api_client)
    format = nested # str | If `nested`, returns top-level categories (either category groups or categories not part of a category group) in alphabetical order. Grouped categories are nested within the category group under the property `children`. A `flattened`, response is similar but it also includes grouped categories at the top level of this.<br> Categories are sorted by their `order`.  When `order` is null, they are listed below other categories with an `order` in alphabetical order. (optional) (default to nested)
    is_group = False # bool | If set to `false`, just the list of assignable categories is returned.<br> If set to `true`, only category groups are returned.<br> When set the `format` parameter is ignored. (optional) (default to False)

    try:
        # Get all categories
        api_response = api_instance.get_all_categories(format=format, is_group=is_group)
        print("The response of CategoriesApi->get_all_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->get_all_categories: %s\n" % e)
```

### Parameters

| Name         | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Notes                          |
| ------------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **format**   | **str**  | If &#x60;nested&#x60;, returns top-level categories (either category groups or categories not part of a category group) in alphabetical order. Grouped categories are nested within the category group under the property &#x60;children&#x60;. A &#x60;flattened&#x60;, response is similar but it also includes grouped categories at the top level of this.&lt;br&gt; Categories are sorted by their &#x60;order&#x60;. When &#x60;order&#x60; is null, they are listed below other categories with an &#x60;order&#x60; in alphabetical order. | [optional] [default to nested] |
| **is_group** | **bool** | If set to &#x60;false&#x60;, just the list of assignable categories is returned.&lt;br&gt; If set to &#x60;true&#x60;, only category groups are returned.&lt;br&gt; When set the &#x60;format&#x60; parameter is ignored.                                                                                                                                                                                                                                                                                                                          | [optional] [default to False]  |

### Return type

[**GetAllCategories200Response**](GetAllCategories200Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

-   **Content-Type**: Not defined
-   **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                            | Response headers |
| ----------- | ------------------------------------------------------------------------------------------------------ | ---------------- |
| **200**     | A list of Category Objects                                                                             | -                |
| **400**     | Invalid request parameters                                                                             | -                |
| **401**     | Unauthorized. This error occurs when an invalid API token is passed to the request.                    | -                |
| **429**     | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. | -                |
| **500**     | Internal Server Error. Contact support.                                                                | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category_by_id**

> CategoryObject get_category_by_id(id)

Get a single category

Retrieve details of a specific category or category group by its ID.

### Example

-   Api Key Authentication (cookieAuth):
-   Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchable
from lunchable.models.category_object import CategoryObject
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
    api_instance = lunchable.CategoriesApi(api_client)
    id = 315174 # int | ID of the category to retrieve

    try:
        # Get a single category
        api_response = api_instance.get_category_by_id(id)
        print("The response of CategoriesApi->get_category_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->get_category_by_id: %s\n" % e)
```

### Parameters

| Name   | Type    | Description                    | Notes |
| ------ | ------- | ------------------------------ | ----- |
| **id** | **int** | ID of the category to retrieve |

### Return type

[**CategoryObject**](CategoryObject.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

-   **Content-Type**: Not defined
-   **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                            | Response headers |
| ----------- | ------------------------------------------------------------------------------------------------------ | ---------------- |
| **201**     | Category Object with the requested category or category group.                                         | -                |
| **400**     | Bad Request                                                                                            | -                |
| **401**     | Unauthorized. This error occurs when an invalid API token is passed to the request.                    | -                |
| **404**     | Not Found                                                                                              | -                |
| **429**     | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. | -                |
| **500**     | Internal Server Error. Contact support.                                                                | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_category**

> CategoryObject update_category(id, update_category_request_object)

Update an existing category or category group

Updates an existing category or category group. You may submit the response from a `GET /categories/{id}` as the request body which includes system created attributes such as `id` or `created_at`, however only the `name`, `description`, `is_income`, `exclude_from_budget`, `exclude_from_totals`, `archived`, `group_id`, `order` and `children` can be updated using this API. It is also possible to provide only the attribute(s) to be updated in the request body, as long as the request includes at least one of the attributes listed above. For example a request body that contains only a `name` attribute is valid. It is not possible to use this API to convert a category to a category group, or a vice versa, so while submitting a request body with the `is_group` attribute is tolerated, it will result in an error response if the value is changed. It is possible to modify the children of an existing category group with this API by setting the `children` attribute. If this is set it will replace the existing children with the newly specified children, so if the intention is to add or remove a single category, it is more straightforward to update the child category by specifying the new `group_id` attribute. If the goal is to add multiple new children or remove multiple existing children, it is recommended to first call the `GET /categories/:id` endpoint to get the existing children and then modify the list as desired.

### Example

-   Api Key Authentication (cookieAuth):
-   Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchable
from lunchable.models.category_object import CategoryObject
from lunchable.models.update_category_request_object import UpdateCategoryRequestObject
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
    api_instance = lunchable.CategoriesApi(api_client)
    id = 83 # int | ID of the category to update
    update_category_request_object = {"name":"Updated Category Name","description":"Updated description of the category"} # UpdateCategoryRequestObject |

    try:
        # Update an existing category or category group
        api_response = api_instance.update_category(id, update_category_request_object)
        print("The response of CategoriesApi->update_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->update_category: %s\n" % e)
```

### Parameters

| Name                               | Type                                                              | Description                  | Notes |
| ---------------------------------- | ----------------------------------------------------------------- | ---------------------------- | ----- |
| **id**                             | **int**                                                           | ID of the category to update |
| **update_category_request_object** | [**UpdateCategoryRequestObject**](UpdateCategoryRequestObject.md) |                              |

### Return type

[**CategoryObject**](CategoryObject.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

-   **Content-Type**: application/json
-   **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                            | Response headers |
| ----------- | ------------------------------------------------------------------------------------------------------ | ---------------- |
| **200**     | Category or Category Group updated successfully                                                        | -                |
| **400**     | Bad Request                                                                                            | -                |
| **401**     | Unauthorized. This error occurs when an invalid API token is passed to the request.                    | -                |
| **404**     | Not Found                                                                                              | -                |
| **429**     | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. | -                |
| **500**     | Internal Server Error. Contact support.                                                                | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# lunchable.SummaryApi

All URIs are relative to *https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2*

| Method                                                     | HTTP request     | Description |
| ---------------------------------------------------------- | ---------------- | ----------- |
| [**get_budget_summary**](SummaryApi.md#get_budget_summary) | **GET** /summary | Get summary |

# **get_budget_summary**

> GetBudgetSummary200Response get_budget_summary(start_date, end_date, include_exclude_from_budgets=include_exclude_from_budgets, include_occurrences=include_occurrences, include_totals=include_totals)

Get summary

Returns a summary of the budget activity for the specified date range.

### Example

-   Api Key Authentication (cookieAuth):
-   Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchable
from lunchable.models.get_budget_summary200_response import GetBudgetSummary200Response
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
    api_instance = lunchable.SummaryApi(api_client)
    start_date = '2025-07-01' # date | Start of date range in ISO 8601 date format (YYYY-MM-DD).
    end_date = '2025-08-31' # date | End of date range in ISO 8601 date format (YYYY-MM-DD).
    include_exclude_from_budgets = False # bool | Enable to include categories that have the 'Exclude from Budgets' flag set in the returned `categories` array. (optional) (default to False)
    include_occurrences = False # bool | Enable to include an `occurrences` array for each category in an aligned response. Each array will include an object for each budget period that falls within the specified date range which includes details on the activity for the budget period. (optional) (default to False)
    include_totals = False # bool | Enable to include a top-level `totals` section that summarizes the inflow and outflow across all transactions for the specified date range. (optional) (default to False)

    try:
        # Get summary
        api_response = api_instance.get_budget_summary(start_date, end_date, include_exclude_from_budgets=include_exclude_from_budgets, include_occurrences=include_occurrences, include_totals=include_totals)
        print("The response of SummaryApi->get_budget_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SummaryApi->get_budget_summary: %s\n" % e)
```

### Parameters

| Name                             | Type     | Description                                                                                                                                                                                                                                                    | Notes                         |
| -------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| **start_date**                   | **date** | Start of date range in ISO 8601 date format (YYYY-MM-DD).                                                                                                                                                                                                      |
| **end_date**                     | **date** | End of date range in ISO 8601 date format (YYYY-MM-DD).                                                                                                                                                                                                        |
| **include_exclude_from_budgets** | **bool** | Enable to include categories that have the &#39;Exclude from Budgets&#39; flag set in the returned &#x60;categories&#x60; array.                                                                                                                               | [optional] [default to False] |
| **include_occurrences**          | **bool** | Enable to include an &#x60;occurrences&#x60; array for each category in an aligned response. Each array will include an object for each budget period that falls within the specified date range which includes details on the activity for the budget period. | [optional] [default to False] |
| **include_totals**               | **bool** | Enable to include a top-level &#x60;totals&#x60; section that summarizes the inflow and outflow across all transactions for the specified date range.                                                                                                          | [optional] [default to False] |

### Return type

[**GetBudgetSummary200Response**](GetBudgetSummary200Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

-   **Content-Type**: Not defined
-   **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                            | Response headers |
| ----------- | ------------------------------------------------------------------------------------------------------ | ---------------- |
| **200**     | Budget summary for the requested range.                                                                | -                |
| **401**     | Unauthorized. This error occurs when an invalid API token is passed to the request.                    | -                |
| **429**     | Too Many Requests. Retry your request after the number of seconds specified in the retry-after header. | -                |
| **500**     | Internal Server Error. Contact support.                                                                | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

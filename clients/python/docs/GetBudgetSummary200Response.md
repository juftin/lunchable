# GetBudgetSummary200Response

## Properties

| Name           | Type                                                                            | Description                                                            | Notes      |
| -------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------- |
| **totals**     | [**SummaryTotalsObject**](SummaryTotalsObject.md)                               |                                                                        | [optional] |
| **aligned**    | **bool**                                                                        | true if start_date and end_date are aligned with budget period setting |
| **categories** | [**List[NonAlignedSummaryCategoryObject]**](NonAlignedSummaryCategoryObject.md) |                                                                        |

## Example

```python
from lunchable.models.get_budget_summary200_response import GetBudgetSummary200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetBudgetSummary200Response from a JSON string
get_budget_summary200_response_instance = GetBudgetSummary200Response.from_json(json)
# print the JSON string representation of the object
print(GetBudgetSummary200Response.to_json())

# convert the object into a dict
get_budget_summary200_response_dict = get_budget_summary200_response_instance.to_dict()
# create an instance of GetBudgetSummary200Response from a dict
get_budget_summary200_response_from_dict = GetBudgetSummary200Response.from_dict(get_budget_summary200_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

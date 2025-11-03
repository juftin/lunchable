# SummaryTotalsObject

Total inflow and outflow for the given date range. This object is returned when the query parameter `include_totals` is set to `true`.

## Properties

| Name        | Type                                                                | Description | Notes      |
| ----------- | ------------------------------------------------------------------- | ----------- | ---------- |
| **inflow**  | [**SummaryTotalsBreakdownObject**](SummaryTotalsBreakdownObject.md) |             | [optional] |
| **outflow** | [**SummaryTotalsBreakdownObject**](SummaryTotalsBreakdownObject.md) |             | [optional] |

## Example

```python
from lunchable.models.summary_totals_object import SummaryTotalsObject

# TODO update the JSON string below
json = "{}"
# create an instance of SummaryTotalsObject from a JSON string
summary_totals_object_instance = SummaryTotalsObject.from_json(json)
# print the JSON string representation of the object
print(SummaryTotalsObject.to_json())

# convert the object into a dict
summary_totals_object_dict = summary_totals_object_instance.to_dict()
# create an instance of SummaryTotalsObject from a dict
summary_totals_object_from_dict = SummaryTotalsObject.from_dict(summary_totals_object_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

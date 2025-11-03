# SummaryTotalsBreakdownObject

## Properties

| Name                        | Type      | Description                                                                                                          | Notes      |
| --------------------------- | --------- | -------------------------------------------------------------------------------------------------------------------- | ---------- |
| **other_activity**          | **float** | Total amount, in the user&#39;s default currency, of non recurring activity for the given date range.                | [optional] |
| **recurring_activity**      | **float** | Total amount, in the user&#39;s default currency, of recurring activity that has occurred for the given date range.  | [optional] |
| **recurring_remaining**     | **float** | Total amount, in the user&#39;s default currency, of expected recurring activity that has not yet occurred.          | [optional] |
| **uncategorized**           | **float** | Total amount, in the user&#39;s default currency, of non recurring activity coming from un-categorized transactions. | [optional] |
| **uncategorized_count**     | **int**   | Number of un-categorized transactions for the given date range.                                                      | [optional] |
| **uncategorized_recurring** | **float** | Total amount, in the user&#39;s default currency, of recurring activity coming from un-categorized transactions.     | [optional] |

## Example

```python
from lunchable.models.summary_totals_breakdown_object import SummaryTotalsBreakdownObject

# TODO update the JSON string below
json = "{}"
# create an instance of SummaryTotalsBreakdownObject from a JSON string
summary_totals_breakdown_object_instance = SummaryTotalsBreakdownObject.from_json(json)
# print the JSON string representation of the object
print(SummaryTotalsBreakdownObject.to_json())

# convert the object into a dict
summary_totals_breakdown_object_dict = summary_totals_breakdown_object_instance.to_dict()
# create an instance of SummaryTotalsBreakdownObject from a dict
summary_totals_breakdown_object_from_dict = SummaryTotalsBreakdownObject.from_dict(summary_totals_breakdown_object_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

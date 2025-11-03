# SummaryCategoryOccurrenceObject

Per period budget activity for the each budget period within the given date range.<br> This is only returned if the query parameter `include_occurrences` is set to `true`.

## Properties

| Name                   | Type                                | Description                                                                                                                                                                                        | Notes |
| ---------------------- | ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| **current**            | **bool**                            | true if this occurrence is the current budget period.                                                                                                                                              |
| **start_date**         | **date**                            | The start date of the budget period.                                                                                                                                                               |
| **end_date**           | **date**                            | The end date of the budget period.                                                                                                                                                                 |
| **other_activity**     | **float**                           | Total non recurring activity, in the user&#39;s default currency, for the category within the given date range. The total activity for the category is the sum of this and the recurring_activity. |
| **recurring_activity** | **float**                           | Total recurring activity, in the user&#39;s default currency, for the category within the given date range. The total activity for the category is the sum of this and the other_activity.         |
| **budgeted**           | **float**                           | Total budgeted amount, in the user&#39;s default currency, for the category within the given date range, or null if the category is not budgeted.                                                  |
| **budgeted_amount**    | **str**                             | Total budgeted amount in the budgeted currency for the category within the given date or null if the category is not budgeted.                                                                     |
| **budgeted_currency**  | [**CurrencyEnum**](CurrencyEnum.md) | Currency of the budgeted amount.                                                                                                                                                                   |
| **notes**              | **str**                             | Any notes added in the Web UI for the budget period.                                                                                                                                               |

## Example

```python
from lunchable.models.summary_category_occurrence_object import SummaryCategoryOccurrenceObject

# TODO update the JSON string below
json = "{}"
# create an instance of SummaryCategoryOccurrenceObject from a JSON string
summary_category_occurrence_object_instance = SummaryCategoryOccurrenceObject.from_json(json)
# print the JSON string representation of the object
print(SummaryCategoryOccurrenceObject.to_json())

# convert the object into a dict
summary_category_occurrence_object_dict = summary_category_occurrence_object_instance.to_dict()
# create an instance of SummaryCategoryOccurrenceObject from a dict
summary_category_occurrence_object_from_dict = SummaryCategoryOccurrenceObject.from_dict(summary_category_occurrence_object_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

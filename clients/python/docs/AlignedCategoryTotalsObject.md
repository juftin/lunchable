# AlignedCategoryTotalsObject

Total activity for the given category within the given date range which is aligned with budget period setting.

## Properties

| Name                    | Type      | Description                                                                                                                                                                                                  | Notes |
| ----------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----- |
| **other_activity**      | **float** | Total non recurring activity, in the user&#39;s default currency, for the category within the given date range.&lt;br&gt; The total activity for the category is the sum of this and the recurring_activity. |
| **recurring_activity**  | **float** | Total recurring activity, in the user&#39;s default currency, for the category within the given date range.&lt;br&gt; The total activity for the category is the sum of this and the other_activity.         |
| **budgeted**            | **float** | Total budgeted amount, in the user&#39;s default currency, for the category within the given date range or null if the category is not budgeted.                                                             |
| **available**           | **float** | Total amount of funds available, in the user&#39;s default currency, for the category within the given date range.                                                                                           |
| **recurring_remaining** | **float** | Total expected recurring activity, in the user&#39;s default currency, that has not yet occurred for the category within the given date range.                                                               |
| **recurring_expected**  | **float** | Total expected recurring activity for the category within the given date range.                                                                                                                              |

## Example

```python
from lunchable.models.aligned_category_totals_object import AlignedCategoryTotalsObject

# TODO update the JSON string below
json = "{}"
# create an instance of AlignedCategoryTotalsObject from a JSON string
aligned_category_totals_object_instance = AlignedCategoryTotalsObject.from_json(json)
# print the JSON string representation of the object
print(AlignedCategoryTotalsObject.to_json())

# convert the object into a dict
aligned_category_totals_object_dict = aligned_category_totals_object_instance.to_dict()
# create an instance of AlignedCategoryTotalsObject from a dict
aligned_category_totals_object_from_dict = AlignedCategoryTotalsObject.from_dict(aligned_category_totals_object_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

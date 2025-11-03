# NonAlignedCategoryTotalsObject

Total activity for the given category within the given date range which is not aligned with budget period setting.

## Properties

| Name                    | Type      | Description                                                                                                                                                                                                  | Notes |
| ----------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----- |
| **other_activity**      | **float** | Total non recurring activity, in the user&#39;s default currency, for the category within the given date range.&lt;br&gt; The total activity for the category is the sum of this and the recurring_activity. |
| **recurring_activity**  | **float** | Total recurring activity, in the user&#39;s default currency, for the category within the given date range.&lt;br&gt; The total activity for the category is the sum of this and the other_activity.         |
| **recurring_remaining** | **float** | Total expected recurring activity, in the user&#39;s default currency, that has not yet occurred for the category within the given date range.                                                               |
| **recurring_expected**  | **float** | Total expected recurring activity for the category within the given date range.                                                                                                                              |

## Example

```python
from lunchable.models.non_aligned_category_totals_object import NonAlignedCategoryTotalsObject

# TODO update the JSON string below
json = "{}"
# create an instance of NonAlignedCategoryTotalsObject from a JSON string
non_aligned_category_totals_object_instance = NonAlignedCategoryTotalsObject.from_json(json)
# print the JSON string representation of the object
print(NonAlignedCategoryTotalsObject.to_json())

# convert the object into a dict
non_aligned_category_totals_object_dict = non_aligned_category_totals_object_instance.to_dict()
# create an instance of NonAlignedCategoryTotalsObject from a dict
non_aligned_category_totals_object_from_dict = NonAlignedCategoryTotalsObject.from_dict(non_aligned_category_totals_object_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# NonAlignedSummaryCategoryObject

List of each category's budget configuration and activity for the given date range.<br> Does not include occurrences since the start_date and end_date are not aligned with budget period setting.

## Properties

| Name            | Type                                                                    | Description                                    | Notes |
| --------------- | ----------------------------------------------------------------------- | ---------------------------------------------- | ----- |
| **category_id** | **int**                                                                 | ID of the category associated with the totals. |
| **totals**      | [**NonAlignedCategoryTotalsObject**](NonAlignedCategoryTotalsObject.md) |                                                |

## Example

```python
from lunchable.models.non_aligned_summary_category_object import NonAlignedSummaryCategoryObject

# TODO update the JSON string below
json = "{}"
# create an instance of NonAlignedSummaryCategoryObject from a JSON string
non_aligned_summary_category_object_instance = NonAlignedSummaryCategoryObject.from_json(json)
# print the JSON string representation of the object
print(NonAlignedSummaryCategoryObject.to_json())

# convert the object into a dict
non_aligned_summary_category_object_dict = non_aligned_summary_category_object_instance.to_dict()
# create an instance of NonAlignedSummaryCategoryObject from a dict
non_aligned_summary_category_object_from_dict = NonAlignedSummaryCategoryObject.from_dict(non_aligned_summary_category_object_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

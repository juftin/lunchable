# AlignedSummaryCategoryObject

List of each category's budget configuration and activity for the given date range.

## Properties

| Name            | Type                                                                            | Description                                    | Notes      |
| --------------- | ------------------------------------------------------------------------------- | ---------------------------------------------- | ---------- |
| **category_id** | **int**                                                                         | ID of the category associated with the totals. |
| **totals**      | [**AlignedCategoryTotalsObject**](AlignedCategoryTotalsObject.md)               |                                                |
| **occurrences** | [**List[SummaryCategoryOccurrenceObject]**](SummaryCategoryOccurrenceObject.md) |                                                | [optional] |

## Example

```python
from lunchable.models.aligned_summary_category_object import AlignedSummaryCategoryObject

# TODO update the JSON string below
json = "{}"
# create an instance of AlignedSummaryCategoryObject from a JSON string
aligned_summary_category_object_instance = AlignedSummaryCategoryObject.from_json(json)
# print the JSON string representation of the object
print(AlignedSummaryCategoryObject.to_json())

# convert the object into a dict
aligned_summary_category_object_dict = aligned_summary_category_object_instance.to_dict()
# create an instance of AlignedSummaryCategoryObject from a dict
aligned_summary_category_object_from_dict = AlignedSummaryCategoryObject.from_dict(aligned_summary_category_object_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

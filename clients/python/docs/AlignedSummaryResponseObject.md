# AlignedSummaryResponseObject

## Properties

| Name           | Type                                                                      | Description                                                            | Notes      |
| -------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------- |
| **totals**     | [**SummaryTotalsObject**](SummaryTotalsObject.md)                         |                                                                        | [optional] |
| **aligned**    | **bool**                                                                  | true if start_date and end_date are aligned with budget period setting |
| **categories** | [**List[AlignedSummaryCategoryObject]**](AlignedSummaryCategoryObject.md) |                                                                        |

## Example

```python
from lunchable.models.aligned_summary_response_object import AlignedSummaryResponseObject

# TODO update the JSON string below
json = "{}"
# create an instance of AlignedSummaryResponseObject from a JSON string
aligned_summary_response_object_instance = AlignedSummaryResponseObject.from_json(json)
# print the JSON string representation of the object
print(AlignedSummaryResponseObject.to_json())

# convert the object into a dict
aligned_summary_response_object_dict = aligned_summary_response_object_instance.to_dict()
# create an instance of AlignedSummaryResponseObject from a dict
aligned_summary_response_object_from_dict = AlignedSummaryResponseObject.from_dict(aligned_summary_response_object_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

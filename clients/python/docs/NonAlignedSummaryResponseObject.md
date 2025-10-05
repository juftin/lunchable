# NonAlignedSummaryResponseObject

## Properties

| Name              | Type                                                                            | Description                                                            | Notes      |
| ----------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------- |
| **totals**        | [**SummaryTotalsObject**](SummaryTotalsObject.md)                               |                                                                        | [optional] |
| **aligned**       | **bool**                                                                        | true if start_date and end_date are aligned with budget period setting |
| **rollover_pool** | [**SummaryRolloverPoolObject**](SummaryRolloverPoolObject.md)                   |                                                                        | [optional] |
| **categories**    | [**List[NonAlignedSummaryCategoryObject]**](NonAlignedSummaryCategoryObject.md) |                                                                        |

## Example

```python
from lunchable.models.non_aligned_summary_response_object import NonAlignedSummaryResponseObject

# TODO update the JSON string below
json = "{}"
# create an instance of NonAlignedSummaryResponseObject from a JSON string
non_aligned_summary_response_object_instance = NonAlignedSummaryResponseObject.from_json(json)
# print the JSON string representation of the object
print(NonAlignedSummaryResponseObject.to_json())

# convert the object into a dict
non_aligned_summary_response_object_dict = non_aligned_summary_response_object_instance.to_dict()
# create an instance of NonAlignedSummaryResponseObject from a dict
non_aligned_summary_response_object_from_dict = NonAlignedSummaryResponseObject.from_dict(non_aligned_summary_response_object_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

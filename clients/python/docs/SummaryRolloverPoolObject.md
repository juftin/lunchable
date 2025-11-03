# SummaryRolloverPoolObject

Summary of the current rollover pool balance and all previous adjustments.<br> Only present if the `include_rollover_pool` query parameter is set to `true`.

## Properties

| Name                 | Type                                                                                    | Description                                                                           | Notes |
| -------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ----- |
| **budgeted_to_base** | **float**                                                                               | Amount of funds, in the user&#39;s default currency, currently available to rollover. |
| **all_adjustments**  | [**List[SummaryRolloverPoolAdjustmentObject]**](SummaryRolloverPoolAdjustmentObject.md) | List of previous adjustments to the rollover pool.                                    |

## Example

```python
from lunchable.models.summary_rollover_pool_object import SummaryRolloverPoolObject

# TODO update the JSON string below
json = "{}"
# create an instance of SummaryRolloverPoolObject from a JSON string
summary_rollover_pool_object_instance = SummaryRolloverPoolObject.from_json(json)
# print the JSON string representation of the object
print(SummaryRolloverPoolObject.to_json())

# convert the object into a dict
summary_rollover_pool_object_dict = summary_rollover_pool_object_instance.to_dict()
# create an instance of SummaryRolloverPoolObject from a dict
summary_rollover_pool_object_from_dict = SummaryRolloverPoolObject.from_dict(summary_rollover_pool_object_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

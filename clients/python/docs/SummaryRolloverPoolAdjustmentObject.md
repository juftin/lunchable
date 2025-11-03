# SummaryRolloverPoolAdjustmentObject

The date and adjusted balance of the rollover pool at the time of the adjustment.

## Properties

| Name         | Type                                | Description                                                               | Notes |
| ------------ | ----------------------------------- | ------------------------------------------------------------------------- | ----- |
| **current**  | **bool**                            | true if this is the current rollover pool balance.                        |
| **var_date** | **date**                            |                                                                           |
| **amount**   | **str**                             | Amount of the rollover pool at the time of the adjustment.                |
| **currency** | [**CurrencyEnum**](CurrencyEnum.md) | Currency of the rollover pool at the time of the adjustment.              |
| **to_base**  | **float**                           | Amount of the rollover pool converted to the user&#39;s default currency. |

## Example

```python
from lunchable.models.summary_rollover_pool_adjustment_object import SummaryRolloverPoolAdjustmentObject

# TODO update the JSON string below
json = "{}"
# create an instance of SummaryRolloverPoolAdjustmentObject from a JSON string
summary_rollover_pool_adjustment_object_instance = SummaryRolloverPoolAdjustmentObject.from_json(json)
# print the JSON string representation of the object
print(SummaryRolloverPoolAdjustmentObject.to_json())

# convert the object into a dict
summary_rollover_pool_adjustment_object_dict = summary_rollover_pool_adjustment_object_instance.to_dict()
# create an instance of SummaryRolloverPoolAdjustmentObject from a dict
summary_rollover_pool_adjustment_object_from_dict = SummaryRolloverPoolAdjustmentObject.from_dict(summary_rollover_pool_adjustment_object_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

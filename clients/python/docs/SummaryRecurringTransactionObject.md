# SummaryRecurringTransactionObject

A single transaction associated with a recurring item. I don't think we will expose this in the summary since it's gettable by querying the recurring_id

## Properties

| Name            | Type                                | Description | Notes |
| --------------- | ----------------------------------- | ----------- | ----- |
| **var_date**    | **date**                            |             |
| **category_id** | **int**                             |             |
| **payee**       | **str**                             |             |
| **to_base**     | **float**                           |             |
| **amount**      | **str**                             |             |
| **currency**    | [**CurrencyEnum**](CurrencyEnum.md) |             |

## Example

```python
from lunchable.models.summary_recurring_transaction_object import SummaryRecurringTransactionObject

# TODO update the JSON string below
json = "{}"
# create an instance of SummaryRecurringTransactionObject from a JSON string
summary_recurring_transaction_object_instance = SummaryRecurringTransactionObject.from_json(json)
# print the JSON string representation of the object
print(SummaryRecurringTransactionObject.to_json())

# convert the object into a dict
summary_recurring_transaction_object_dict = summary_recurring_transaction_object_instance.to_dict()
# create an instance of SummaryRecurringTransactionObject from a dict
summary_recurring_transaction_object_from_dict = SummaryRecurringTransactionObject.from_dict(summary_recurring_transaction_object_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

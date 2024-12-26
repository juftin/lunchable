# SplitTransactionObjectAmount

Individual amount of split. Currency will inherit from parent transaction. All amounts must sum up to parent transaction amount.

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |

## Example

```python
from lunchable.models.split_transaction_object_amount import SplitTransactionObjectAmount

# TODO update the JSON string below
json = "{}"
# create an instance of SplitTransactionObjectAmount from a JSON string
split_transaction_object_amount_instance = SplitTransactionObjectAmount.from_json(json)
# print the JSON string representation of the object
print(SplitTransactionObjectAmount.to_json())

# convert the object into a dict
split_transaction_object_amount_dict = split_transaction_object_amount_instance.to_dict()
# create an instance of SplitTransactionObjectAmount from a dict
split_transaction_object_amount_from_dict = SplitTransactionObjectAmount.from_dict(split_transaction_object_amount_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

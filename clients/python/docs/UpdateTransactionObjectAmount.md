# UpdateTransactionObjectAmount

Numeric value of amount without currency symbol. i.e. $4.25 should be denoted as 4.25. May be a string or a number in double format. Regardless of the value of the user's `debits_as_negative` property, transactions with positive amounts are treated as debits. Set the amount to a negative value to insert a credit transaction.<br><br> May not be updated on transactions that belong to a synced account with the \"Allow Modifications to Transactions\" property disabled.

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |

## Example

```python
from lunchable.models.update_transaction_object_amount import UpdateTransactionObjectAmount

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTransactionObjectAmount from a JSON string
update_transaction_object_amount_instance = UpdateTransactionObjectAmount.from_json(json)
# print the JSON string representation of the object
print(UpdateTransactionObjectAmount.to_json())

# convert the object into a dict
update_transaction_object_amount_dict = update_transaction_object_amount_instance.to_dict()
# create an instance of UpdateTransactionObjectAmount from a dict
update_transaction_object_amount_from_dict = UpdateTransactionObjectAmount.from_dict(update_transaction_object_amount_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# SplitTransactionRequest

## Properties

| Name                   | Type                                                          | Description                                                                                                       | Notes |
| ---------------------- | ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----- |
| **child_transactions** | [**List[SplitTransactionObject]**](SplitTransactionObject.md) | List of child transactions to create. The sum of the &#x60;amounts&#x60; must match the split transaction amount. |

## Example

```python
from lunchable.models.split_transaction_request import SplitTransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SplitTransactionRequest from a JSON string
split_transaction_request_instance = SplitTransactionRequest.from_json(json)
# print the JSON string representation of the object
print(SplitTransactionRequest.to_json())

# convert the object into a dict
split_transaction_request_dict = split_transaction_request_instance.to_dict()
# create an instance of SplitTransactionRequest from a dict
split_transaction_request_from_dict = SplitTransactionRequest.from_dict(split_transaction_request_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# UpdateTransactionsRequest

## Properties

| Name             | Type                                                                                                  | Description                                                                                                                      | Notes |
| ---------------- | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ----- |
| **transactions** | [**List[UpdateTransactionsRequestTransactionsInner]**](UpdateTransactionsRequestTransactionsInner.md) | List of transactions to update. Each transaction must have an &#x60;id&#x60; property and at least one other property to update. |

## Example

```python
from lunchable.models.update_transactions_request import UpdateTransactionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTransactionsRequest from a JSON string
update_transactions_request_instance = UpdateTransactionsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTransactionsRequest.to_json())

# convert the object into a dict
update_transactions_request_dict = update_transactions_request_instance.to_dict()
# create an instance of UpdateTransactionsRequest from a dict
update_transactions_request_from_dict = UpdateTransactionsRequest.from_dict(update_transactions_request_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

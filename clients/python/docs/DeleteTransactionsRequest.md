# DeleteTransactionsRequest

## Properties

| Name    | Type            | Description                                 | Notes |
| ------- | --------------- | ------------------------------------------- | ----- |
| **ids** | **List[float]** | Array of existing Transaction IDs to delete |

## Example

```python
from lunchable.models.delete_transactions_request import DeleteTransactionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteTransactionsRequest from a JSON string
delete_transactions_request_instance = DeleteTransactionsRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteTransactionsRequest.to_json())

# convert the object into a dict
delete_transactions_request_dict = delete_transactions_request_instance.to_dict()
# create an instance of DeleteTransactionsRequest from a dict
delete_transactions_request_from_dict = DeleteTransactionsRequest.from_dict(delete_transactions_request_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

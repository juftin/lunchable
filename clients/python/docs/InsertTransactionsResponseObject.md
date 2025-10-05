# InsertTransactionsResponseObject

The object returned from a successful POST /transactions request

## Properties

| Name                   | Type                                                                            | Description                                                                                                 | Notes |
| ---------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----- |
| **transactions**       | [**List[TransactionObject]**](TransactionObject.md)                             | An array of the inserted transactions.                                                                      |
| **skipped_duplicates** | [**List[SkippedExistingExternalIdObject]**](SkippedExistingExternalIdObject.md) | An array of the requested transactions that were duplicates of existing transactions and were not inserted. |

## Example

```python
from lunchable.models.insert_transactions_response_object import InsertTransactionsResponseObject

# TODO update the JSON string below
json = "{}"
# create an instance of InsertTransactionsResponseObject from a JSON string
insert_transactions_response_object_instance = InsertTransactionsResponseObject.from_json(json)
# print the JSON string representation of the object
print(InsertTransactionsResponseObject.to_json())

# convert the object into a dict
insert_transactions_response_object_dict = insert_transactions_response_object_instance.to_dict()
# create an instance of InsertTransactionsResponseObject from a dict
insert_transactions_response_object_from_dict = InsertTransactionsResponseObject.from_dict(insert_transactions_response_object_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

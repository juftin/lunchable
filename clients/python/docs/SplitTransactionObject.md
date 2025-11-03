# SplitTransactionObject

The object representing a split transaction

## Properties

| Name            | Type                                                                | Description                                                                                                                                      | Notes      |
| --------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| **amount**      | [**SplitTransactionObjectAmount**](SplitTransactionObjectAmount.md) |                                                                                                                                                  |
| **payee**       | **str**                                                             | The payee for the child transaction. Will inherit the original payee from the parent if not defined.                                             | [optional] |
| **var_date**    | **date**                                                            | Must be in ISO 8601 format (YYYY-MM-DD). Will inherit from the parent if not defined.                                                            | [optional] |
| **category_id** | **int**                                                             | Unique identifier for associated category_id. Category must already exist for the account. Will inherit category from the parent if not defined. | [optional] |
| **notes**       | **str**                                                             | Will inherit notes from parent if not defined.                                                                                                   | [optional] |

## Example

```python
from lunchable.models.split_transaction_object import SplitTransactionObject

# TODO update the JSON string below
json = "{}"
# create an instance of SplitTransactionObject from a JSON string
split_transaction_object_instance = SplitTransactionObject.from_json(json)
# print the JSON string representation of the object
print(SplitTransactionObject.to_json())

# convert the object into a dict
split_transaction_object_dict = split_transaction_object_instance.to_dict()
# create an instance of SplitTransactionObject from a dict
split_transaction_object_from_dict = SplitTransactionObject.from_dict(split_transaction_object_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# UpdateTransactions200Response

## Properties

| Name             | Type                                                | Description | Notes |
| ---------------- | --------------------------------------------------- | ----------- | ----- |
| **transactions** | [**List[TransactionObject]**](TransactionObject.md) |             |

## Example

```python
from lunchable.models.update_transactions200_response import UpdateTransactions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTransactions200Response from a JSON string
update_transactions200_response_instance = UpdateTransactions200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateTransactions200Response.to_json())

# convert the object into a dict
update_transactions200_response_dict = update_transactions200_response_instance.to_dict()
# create an instance of UpdateTransactions200Response from a dict
update_transactions200_response_from_dict = UpdateTransactions200Response.from_dict(update_transactions200_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

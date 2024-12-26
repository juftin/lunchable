# GroupTransactions201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**List[TransactionObject]**](TransactionObject.md) |  | [optional] 

## Example

```python
from lunchable.models.group_transactions201_response import GroupTransactions201Response

# TODO update the JSON string below
json = "{}"
# create an instance of GroupTransactions201Response from a JSON string
group_transactions201_response_instance = GroupTransactions201Response.from_json(json)
# print the JSON string representation of the object
print(GroupTransactions201Response.to_json())

# convert the object into a dict
group_transactions201_response_dict = group_transactions201_response_instance.to_dict()
# create an instance of GroupTransactions201Response from a dict
group_transactions201_response_from_dict = GroupTransactions201Response.from_dict(group_transactions201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



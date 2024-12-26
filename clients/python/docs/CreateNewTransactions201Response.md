# CreateNewTransactions201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**List[TransactionObject]**](TransactionObject.md) |  | 
**skipped_existing_external_ids** | [**List[SkippedExistingExternalIdObject]**](SkippedExistingExternalIdObject.md) |  | [optional] 

## Example

```python
from lunchable.models.create_new_transactions201_response import CreateNewTransactions201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNewTransactions201Response from a JSON string
create_new_transactions201_response_instance = CreateNewTransactions201Response.from_json(json)
# print the JSON string representation of the object
print(CreateNewTransactions201Response.to_json())

# convert the object into a dict
create_new_transactions201_response_dict = create_new_transactions201_response_instance.to_dict()
# create an instance of CreateNewTransactions201Response from a dict
create_new_transactions201_response_from_dict = CreateNewTransactions201Response.from_dict(create_new_transactions201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GetAllTransactions200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**List[TransactionObject]**](TransactionObject.md) |  | 
**has_more** | **bool** | Set to true if more transactions are available | 
**error** | **str** |  | [optional] 

## Example

```python
from lunchable.models.get_all_transactions200_response import GetAllTransactions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllTransactions200Response from a JSON string
get_all_transactions200_response_instance = GetAllTransactions200Response.from_json(json)
# print the JSON string representation of the object
print(GetAllTransactions200Response.to_json())

# convert the object into a dict
get_all_transactions200_response_dict = get_all_transactions200_response_instance.to_dict()
# create an instance of GetAllTransactions200Response from a dict
get_all_transactions200_response_from_dict = GetAllTransactions200Response.from_dict(get_all_transactions200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GetAllPlaidAccounts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plaid_accounts** | [**List[PlaidAccountObject]**](PlaidAccountObject.md) |  | [optional] 

## Example

```python
from lunchable.models.get_all_plaid_accounts200_response import GetAllPlaidAccounts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllPlaidAccounts200Response from a JSON string
get_all_plaid_accounts200_response_instance = GetAllPlaidAccounts200Response.from_json(json)
# print the JSON string representation of the object
print(GetAllPlaidAccounts200Response.to_json())

# convert the object into a dict
get_all_plaid_accounts200_response_dict = get_all_plaid_accounts200_response_instance.to_dict()
# create an instance of GetAllPlaidAccounts200Response from a dict
get_all_plaid_accounts200_response_from_dict = GetAllPlaidAccounts200Response.from_dict(get_all_plaid_accounts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



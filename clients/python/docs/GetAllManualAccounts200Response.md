# GetAllManualAccounts200Response

## Properties

| Name                | Type                                                    | Description | Notes      |
| ------------------- | ------------------------------------------------------- | ----------- | ---------- |
| **manual_accounts** | [**List[ManualAccountObject]**](ManualAccountObject.md) |             | [optional] |

## Example

```python
from lunchable.models.get_all_manual_accounts200_response import GetAllManualAccounts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllManualAccounts200Response from a JSON string
get_all_manual_accounts200_response_instance = GetAllManualAccounts200Response.from_json(json)
# print the JSON string representation of the object
print(GetAllManualAccounts200Response.to_json())

# convert the object into a dict
get_all_manual_accounts200_response_dict = get_all_manual_accounts200_response_instance.to_dict()
# create an instance of GetAllManualAccounts200Response from a dict
get_all_manual_accounts200_response_from_dict = GetAllManualAccounts200Response.from_dict(get_all_manual_accounts200_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

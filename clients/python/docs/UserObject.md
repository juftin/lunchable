# UserObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | User&#39;s name | 
**email** | **str** | User&#39;s email | 
**id** | **int** | Unique identifier for user | 
**account_id** | **int** | Unique identifier for the associated budgeting account | 
**budget_name** | **str** | Name of the associated budgeting account | 
**primary_currency** | [**CurrencyEnum**](CurrencyEnum.md) | Primary currency from user&#39;s settings | 
**api_key_label** | **str** | User-defined label of the developer API key used. Returns null if nothing has been set. | 

## Example

```python
from lunchable.models.user_object import UserObject

# TODO update the JSON string below
json = "{}"
# create an instance of UserObject from a JSON string
user_object_instance = UserObject.from_json(json)
# print the JSON string representation of the object
print(UserObject.to_json())

# convert the object into a dict
user_object_dict = user_object_instance.to_dict()
# create an instance of UserObject from a dict
user_object_from_dict = UserObject.from_dict(user_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



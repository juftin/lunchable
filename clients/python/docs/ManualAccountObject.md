# ManualAccountObject

An object containing information about a manual account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of this account | [optional] 
**name** | **str** | Name of the account | [optional] 
**type** | [**AccountTypeEnum**](AccountTypeEnum.md) | Primary type of the account | [optional] 
**subtype** | **str** | Optional account subtype. Examples include&lt;br&gt; - retirement - checking - savings - prepaid credit card | [optional] 
**display_name** | **str** | Optional display name for the account set by the user | [optional] 
**balance** | **str** | Current balance of the account in numeric format to 4 decimal places. | [optional] 
**balance_as_of** | **datetime** | Date balance was last updated in ISO 8601 extended format | [optional] 
**closed_on** | **date** | The date this account was closed. Will be null if the account has not been marked as closed | [optional] 
**currency** | **str** | Three-letter lowercase currency code of the account balance | [optional] 
**institution_name** | **str** | Name of institution holding the account | [optional] 
**external_id** | **str** | An optional external_id that may be set or updated via the API | [optional] 
**exclude_from_transactions** | **bool** | If true, this account will not show up as an option for assignment when creating transactions manually | [optional] 
**created_at** | **datetime** | Date/time the account was created in ISO 8601 extended format | [optional] 
**updated_at** | **datetime** | Date/time the account was created in ISO 8601 extended format | [optional] 

## Example

```python
from lunchable.models.manual_account_object import ManualAccountObject

# TODO update the JSON string below
json = "{}"
# create an instance of ManualAccountObject from a JSON string
manual_account_object_instance = ManualAccountObject.from_json(json)
# print the JSON string representation of the object
print(ManualAccountObject.to_json())

# convert the object into a dict
manual_account_object_dict = manual_account_object_instance.to_dict()
# create an instance of ManualAccountObject from a dict
manual_account_object_from_dict = ManualAccountObject.from_dict(manual_account_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



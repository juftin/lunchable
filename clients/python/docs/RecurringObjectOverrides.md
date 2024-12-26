# RecurringObjectOverrides

The values that will be applied to  matching transactions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payee** | **str** | If present, the payee name that will be displayed for any matching transactions. | [optional] 
**notes** | **str** | If present, the notes that will be displayed for any matching transactions. | [optional] 
**category_id** | **int** | If present, the id of the category that matching transactions will be assigned to. | [optional] 

## Example

```python
from lunchable.models.recurring_object_overrides import RecurringObjectOverrides

# TODO update the JSON string below
json = "{}"
# create an instance of RecurringObjectOverrides from a JSON string
recurring_object_overrides_instance = RecurringObjectOverrides.from_json(json)
# print the JSON string representation of the object
print(RecurringObjectOverrides.to_json())

# convert the object into a dict
recurring_object_overrides_dict = recurring_object_overrides_instance.to_dict()
# create an instance of RecurringObjectOverrides from a dict
recurring_object_overrides_from_dict = RecurringObjectOverrides.from_dict(recurring_object_overrides_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



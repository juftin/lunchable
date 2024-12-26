# GetAllRecurring200Response

## Properties

| Name                | Type                                            | Description | Notes      |
| ------------------- | ----------------------------------------------- | ----------- | ---------- |
| **recurring_items** | [**List[RecurringObject]**](RecurringObject.md) |             | [optional] |

## Example

```python
from lunchable.models.get_all_recurring200_response import GetAllRecurring200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllRecurring200Response from a JSON string
get_all_recurring200_response_instance = GetAllRecurring200Response.from_json(json)
# print the JSON string representation of the object
print(GetAllRecurring200Response.to_json())

# convert the object into a dict
get_all_recurring200_response_dict = get_all_recurring200_response_instance.to_dict()
# create an instance of GetAllRecurring200Response from a dict
get_all_recurring200_response_from_dict = GetAllRecurring200Response.from_dict(get_all_recurring200_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

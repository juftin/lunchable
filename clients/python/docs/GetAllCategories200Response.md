# GetAllCategories200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**List[CategoryObject]**](CategoryObject.md) |  | [optional] 

## Example

```python
from lunchable.models.get_all_categories200_response import GetAllCategories200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllCategories200Response from a JSON string
get_all_categories200_response_instance = GetAllCategories200Response.from_json(json)
# print the JSON string representation of the object
print(GetAllCategories200Response.to_json())

# convert the object into a dict
get_all_categories200_response_dict = get_all_categories200_response_instance.to_dict()
# create an instance of GetAllCategories200Response from a dict
get_all_categories200_response_from_dict = GetAllCategories200Response.from_dict(get_all_categories200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



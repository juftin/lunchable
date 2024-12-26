# ErrorResponseObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | overall error message | 
**errors** | **List[object]** |  | 

## Example

```python
from lunchable.models.error_response_object import ErrorResponseObject

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponseObject from a JSON string
error_response_object_instance = ErrorResponseObject.from_json(json)
# print the JSON string representation of the object
print(ErrorResponseObject.to_json())

# convert the object into a dict
error_response_object_dict = error_response_object_instance.to_dict()
# create an instance of ErrorResponseObject from a dict
error_response_object_from_dict = ErrorResponseObject.from_dict(error_response_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



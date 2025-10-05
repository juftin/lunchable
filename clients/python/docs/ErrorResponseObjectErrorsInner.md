# ErrorResponseObjectErrorsInner

## Properties

| Name        | Type    | Description                  | Notes |
| ----------- | ------- | ---------------------------- | ----- |
| **err_msg** | **str** | Human-readable error message |

## Example

```python
from lunchable.models.error_response_object_errors_inner import ErrorResponseObjectErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponseObjectErrorsInner from a JSON string
error_response_object_errors_inner_instance = ErrorResponseObjectErrorsInner.from_json(json)
# print the JSON string representation of the object
print(ErrorResponseObjectErrorsInner.to_json())

# convert the object into a dict
error_response_object_errors_inner_dict = error_response_object_errors_inner_instance.to_dict()
# create an instance of ErrorResponseObjectErrorsInner from a dict
error_response_object_errors_inner_from_dict = ErrorResponseObjectErrorsInner.from_dict(error_response_object_errors_inner_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

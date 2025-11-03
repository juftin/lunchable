# DeleteTagResponseWithDependencies

## Properties

| Name           | Type                                                                                              | Description         | Notes |
| -------------- | ------------------------------------------------------------------------------------------------- | ------------------- | ----- |
| **tag_name**   | **str**                                                                                           | The name of the tag |
| **dependents** | [**DeleteTagResponseWithDependenciesDependents**](DeleteTagResponseWithDependenciesDependents.md) |                     |

## Example

```python
from lunchable.models.delete_tag_response_with_dependencies import DeleteTagResponseWithDependencies

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteTagResponseWithDependencies from a JSON string
delete_tag_response_with_dependencies_instance = DeleteTagResponseWithDependencies.from_json(json)
# print the JSON string representation of the object
print(DeleteTagResponseWithDependencies.to_json())

# convert the object into a dict
delete_tag_response_with_dependencies_dict = delete_tag_response_with_dependencies_instance.to_dict()
# create an instance of DeleteTagResponseWithDependencies from a dict
delete_tag_response_with_dependencies_from_dict = DeleteTagResponseWithDependencies.from_dict(delete_tag_response_with_dependencies_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

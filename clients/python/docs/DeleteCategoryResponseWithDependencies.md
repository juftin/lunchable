# DeleteCategoryResponseWithDependencies

## Properties

| Name              | Type                                                                                                        | Description              | Notes |
| ----------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------ | ----- |
| **category_name** | **str**                                                                                                     | The name of the category |
| **dependents**    | [**DeleteCategoryResponseWithDependenciesDependents**](DeleteCategoryResponseWithDependenciesDependents.md) |                          |

## Example

```python
from lunchable.models.delete_category_response_with_dependencies import DeleteCategoryResponseWithDependencies

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCategoryResponseWithDependencies from a JSON string
delete_category_response_with_dependencies_instance = DeleteCategoryResponseWithDependencies.from_json(json)
# print the JSON string representation of the object
print(DeleteCategoryResponseWithDependencies.to_json())

# convert the object into a dict
delete_category_response_with_dependencies_dict = delete_category_response_with_dependencies_instance.to_dict()
# create an instance of DeleteCategoryResponseWithDependencies from a dict
delete_category_response_with_dependencies_from_dict = DeleteCategoryResponseWithDependencies.from_dict(delete_category_response_with_dependencies_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

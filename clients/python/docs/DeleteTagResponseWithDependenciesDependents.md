# DeleteTagResponseWithDependenciesDependents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_rules** | **float** | The number of rules depending on the tag | 
**transactions** | **float** | The number of transactions with the tag | 

## Example

```python
from lunchable.models.delete_tag_response_with_dependencies_dependents import DeleteTagResponseWithDependenciesDependents

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteTagResponseWithDependenciesDependents from a JSON string
delete_tag_response_with_dependencies_dependents_instance = DeleteTagResponseWithDependenciesDependents.from_json(json)
# print the JSON string representation of the object
print(DeleteTagResponseWithDependenciesDependents.to_json())

# convert the object into a dict
delete_tag_response_with_dependencies_dependents_dict = delete_tag_response_with_dependencies_dependents_instance.to_dict()
# create an instance of DeleteTagResponseWithDependenciesDependents from a dict
delete_tag_response_with_dependencies_dependents_from_dict = DeleteTagResponseWithDependenciesDependents.from_dict(delete_tag_response_with_dependencies_dependents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



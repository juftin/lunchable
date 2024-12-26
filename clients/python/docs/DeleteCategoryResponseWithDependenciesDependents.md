# DeleteCategoryResponseWithDependenciesDependents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget** | **float** | The number of budgets depending on the category | 
**category_rules** | **float** | The number of category rules depending on the category | 
**transactions** | **float** | The number of transactions depending on the category | 
**children** | **float** | The number of child categories in the category group | 
**recurring** | **float** | The number of recurring transactions depending on the category | 
**plaid_cats** | **float** | The number of auto created categories based on Plaid categories | 

## Example

```python
from lunchable.models.delete_category_response_with_dependencies_dependents import DeleteCategoryResponseWithDependenciesDependents

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCategoryResponseWithDependenciesDependents from a JSON string
delete_category_response_with_dependencies_dependents_instance = DeleteCategoryResponseWithDependenciesDependents.from_json(json)
# print the JSON string representation of the object
print(DeleteCategoryResponseWithDependenciesDependents.to_json())

# convert the object into a dict
delete_category_response_with_dependencies_dependents_dict = delete_category_response_with_dependencies_dependents_instance.to_dict()
# create an instance of DeleteCategoryResponseWithDependenciesDependents from a dict
delete_category_response_with_dependencies_dependents_from_dict = DeleteCategoryResponseWithDependenciesDependents.from_dict(delete_category_response_with_dependencies_dependents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



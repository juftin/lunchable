# CreateCategoryRequestObjectChildrenInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A system defined unique identifier for the category. | 
**name** | **str** | The name of the category. | 
**description** | **str** | The description of the category or &#x60;null&#x60; if not set. | 
**updated_at** | **datetime** | The date and time of when the category was last updated (in the ISO 8601 extended format). | 
**created_at** | **datetime** | The date and time of when the category was created (in the ISO 8601 extended format). | 
**group_id** | **int** | The ID of the category group this category belongs to or &#x60;null&#x60; if the category doesn&#39;t belong to a group, or is itself a category group. | 
**is_group** | **bool** | Will always be false for a category that is part of category group. | 
**archived** | **bool** | If true, the category is archived and not displayed in relevant areas of the Lunch Money app. | 
**archived_at** | **datetime** | The date and time of when the category was last archived (in the ISO 8601 extended format). | 
**order** | **float** | An index specifying the position in which the category is displayed on the categories page in the Lunch Money GUI. For categories within a category group the order index is relative to the other categories within the group. | 

## Example

```python
from lunchable.models.create_category_request_object_children_inner import CreateCategoryRequestObjectChildrenInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCategoryRequestObjectChildrenInner from a JSON string
create_category_request_object_children_inner_instance = CreateCategoryRequestObjectChildrenInner.from_json(json)
# print the JSON string representation of the object
print(CreateCategoryRequestObjectChildrenInner.to_json())

# convert the object into a dict
create_category_request_object_children_inner_dict = create_category_request_object_children_inner_instance.to_dict()
# create an instance of CreateCategoryRequestObjectChildrenInner from a dict
create_category_request_object_children_inner_from_dict = CreateCategoryRequestObjectChildrenInner.from_dict(create_category_request_object_children_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CategoryObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A system defined unique identifier for the category. | 
**name** | **str** | The name of the category. | 
**description** | **str** | The description of the category or &#x60;null&#x60; if not set. | 
**is_income** | **bool** | If true, the transactions in this category will be treated as income. | 
**exclude_from_budget** | **bool** | If true, the transactions in this category will be excluded from the budget. | 
**exclude_from_totals** | **bool** | If true, the transactions in this category will be excluded from totals. | 
**updated_at** | **datetime** | The date and time of when the category was last updated (in the ISO 8601 extended format). | 
**created_at** | **datetime** | The date and time of when the category was created (in the ISO 8601 extended format). | 
**group_id** | **int** | The ID of the category group this category belongs to or &#x60;null&#x60; if the category doesn&#39;t belong to a group, or is itself a category group. | 
**is_group** | **bool** | If true, the category is a group that can be a parent to other categories. | 
**children** | [**List[ChildCategoryObject]**](ChildCategoryObject.md) | For category groups, this will populate with details about the categories that belong to this group.  The objects in this array are similar to Category Objects but do not include the &#x60;is_income&#x60;, &#x60;exclude_from_budget&#x60;, and &#x60;exclude_from_totals&#x60; properties as these are inherited from the Category Group.  In addition the &#x60;is_group&#x60; property will always be &#x60;false&#x60;&#x60;, and there will be no &#x60;children&#x60; attribute. | [optional] 
**archived** | **bool** | If true, the category is archived and not displayed in relevant areas of the Lunch Money app. | 
**archived_at** | **datetime** | The date and time of when the category was last archived (in the ISO 8601 extended format). | 
**order** | **float** | An index specifying the position in which the category is displayed on the categories page in the Lunch Money GUI. For categories within a category group the order index is relative to the other categories within the group.&lt;br&gt; This value for this property will be &#x60;null&#x60; for categories created via the API until they are modified on the Categories page in the Lunch Money GUI. | 

## Example

```python
from lunchable.models.category_object import CategoryObject

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryObject from a JSON string
category_object_instance = CategoryObject.from_json(json)
# print the JSON string representation of the object
print(CategoryObject.to_json())

# convert the object into a dict
category_object_dict = category_object_instance.to_dict()
# create an instance of CategoryObject from a dict
category_object_from_dict = CategoryObject.from_dict(category_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



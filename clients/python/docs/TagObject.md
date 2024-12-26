# TagObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the tag. | 
**name** | **str** | Name of the tag. | 
**description** | **str** | Description of the tag. | 
**updated_at** | **datetime** | The date and time of when the tag was last updated (in the ISO 8601 extended format). | 
**created_at** | **datetime** | The date and time of when the tag was created (in the ISO 8601 extended format). | 
**archived** | **bool** | If true, the tag will not show up when creating or updating transactions in the Lunch Money app.  **Can it be assigned via the API** | 
**archived_at** | **datetime** | The date and time of when the tag was last archived or null if not archived | 

## Example

```python
from lunchable.models.tag_object import TagObject

# TODO update the JSON string below
json = "{}"
# create an instance of TagObject from a JSON string
tag_object_instance = TagObject.from_json(json)
# print the JSON string representation of the object
print(TagObject.to_json())

# convert the object into a dict
tag_object_dict = tag_object_instance.to_dict()
# create an instance of TagObject from a dict
tag_object_from_dict = TagObject.from_dict(tag_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



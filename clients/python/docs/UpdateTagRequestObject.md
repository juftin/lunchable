# UpdateTagRequestObject

## Properties

| Name            | Type         | Description                                                                 | Notes      |
| --------------- | ------------ | --------------------------------------------------------------------------- | ---------- |
| **name**        | **str**      | If set the new name of the category. Must be between 1 and 100 characters.  | [optional] |
| **description** | **str**      | If set the new description of the category. Must not exceed 200 characters. | [optional] |
| **archived**    | **bool**     | If set will indicate if this category is archived.                          | [optional] |
| **id**          | **int**      | System defined unique identifier for the category. Ignored if set.          | [optional] |
| **updated_at**  | **datetime** | System set time the tag was last updated. Ignored if set                    | [optional] |
| **created_at**  | **datetime** | System set time the tag was created. Ignored if set.                        | [optional] |
| **archived_at** | **datetime** | System set time the tag was archived. Ignored if set.                       | [optional] |

## Example

```python
from lunchable.models.update_tag_request_object import UpdateTagRequestObject

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTagRequestObject from a JSON string
update_tag_request_object_instance = UpdateTagRequestObject.from_json(json)
# print the JSON string representation of the object
print(UpdateTagRequestObject.to_json())

# convert the object into a dict
update_tag_request_object_dict = update_tag_request_object_instance.to_dict()
# create an instance of UpdateTagRequestObject from a dict
update_tag_request_object_from_dict = UpdateTagRequestObject.from_dict(update_tag_request_object_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

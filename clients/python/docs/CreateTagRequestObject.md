# CreateTagRequestObject

## Properties

| Name            | Type     | Description                                                                                                  | Notes                         |
| --------------- | -------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------- |
| **name**        | **str**  | The name of the new tag. Must be between 1 and 100 characters. Must not match the name of any existing tags. |
| **description** | **str**  | The description of the tag. Must not exceed 200 characters.                                                  | [optional]                    |
| **archived**    | **bool** | If true, the tag is archived and not displayed in relevant areas of the Lunch Money app.                     | [optional] [default to False] |

## Example

```python
from lunchable.models.create_tag_request_object import CreateTagRequestObject

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTagRequestObject from a JSON string
create_tag_request_object_instance = CreateTagRequestObject.from_json(json)
# print the JSON string representation of the object
print(CreateTagRequestObject.to_json())

# convert the object into a dict
create_tag_request_object_dict = create_tag_request_object_instance.to_dict()
# create an instance of CreateTagRequestObject from a dict
create_tag_request_object_from_dict = CreateTagRequestObject.from_dict(create_tag_request_object_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

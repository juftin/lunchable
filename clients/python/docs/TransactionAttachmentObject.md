# TransactionAttachmentObject

## Properties

| Name            | Type         | Description                                                          | Notes      |
| --------------- | ------------ | -------------------------------------------------------------------- | ---------- |
| **id**          | **int**      | The unique identifier of the attachment                              | [optional] |
| **uploaded_by** | **int**      | The id of the user who uploaded the attachment                       | [optional] |
| **name**        | **str**      | The name of the file                                                 | [optional] |
| **type**        | **str**      | The MIME type of the file                                            | [optional] |
| **size**        | **int**      | The size of the file in kilobytes                                    | [optional] |
| **notes**       | **str**      | Optional notes about the attachment                                  | [optional] |
| **created_at**  | **datetime** | The date and time when the attachment was created in ISO 8601 format | [optional] |

## Example

```python
from lunchable.models.transaction_attachment_object import TransactionAttachmentObject

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionAttachmentObject from a JSON string
transaction_attachment_object_instance = TransactionAttachmentObject.from_json(json)
# print the JSON string representation of the object
print(TransactionAttachmentObject.to_json())

# convert the object into a dict
transaction_attachment_object_dict = transaction_attachment_object_instance.to_dict()
# create an instance of TransactionAttachmentObject from a dict
transaction_attachment_object_from_dict = TransactionAttachmentObject.from_dict(transaction_attachment_object_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

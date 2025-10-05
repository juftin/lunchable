# GetTransactionAttachmentUrl200Response

## Properties

| Name           | Type         | Description                                    | Notes |
| -------------- | ------------ | ---------------------------------------------- | ----- |
| **url**        | **str**      | The signed url to download the file attachment |
| **expires_at** | **datetime** | The date and time the signed url will expire   |

## Example

```python
from lunchable.models.get_transaction_attachment_url200_response import GetTransactionAttachmentUrl200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionAttachmentUrl200Response from a JSON string
get_transaction_attachment_url200_response_instance = GetTransactionAttachmentUrl200Response.from_json(json)
# print the JSON string representation of the object
print(GetTransactionAttachmentUrl200Response.to_json())

# convert the object into a dict
get_transaction_attachment_url200_response_dict = get_transaction_attachment_url200_response_instance.to_dict()
# create an instance of GetTransactionAttachmentUrl200Response from a dict
get_transaction_attachment_url200_response_from_dict = GetTransactionAttachmentUrl200Response.from_dict(get_transaction_attachment_url200_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

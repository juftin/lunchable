# SkippedExistingExternalIdObject

The object returned when a new transaction has an external_id that already exists

## Properties

| Name                           | Type                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Notes      |
| ------------------------------ | --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **reason**                     | **str**                                                   | The reason the transaction was skipped, may be one of: - &#x60;duplicate_external_id&#x60;: The transaction has the same &#x60;manual_account_id&#x60; and &#x60;external_id&#x60; as an existing transaction - &#x60;duplicate_payee_amount_date&#x60;: The &#x60;skip_duplicates&#x60; request body property was set to &#x60;true&#x60; and the transaction has the same &#x60;amount&#x60;, &#x60;payee&#x60;, and &#x60;date&#x60; as an existing transaction associated with the same account. | [optional] |
| **request_transactions_index** | **int**                                                   | The index of the transaction in the request body&#39;s transactions array that was skipped.                                                                                                                                                                                                                                                                                                                                                                                                          | [optional] |
| **existing_transaction_id**    | **int**                                                   | The id of the existing transactions that the requested transaction duplicates.                                                                                                                                                                                                                                                                                                                                                                                                                       | [optional] |
| **request_transaction**        | [**InsertTransactionObject**](InsertTransactionObject.md) | The requested transaction that was skipped.                                                                                                                                                                                                                                                                                                                                                                                                                                                          | [optional] |

## Example

```python
from lunchable.models.skipped_existing_external_id_object import SkippedExistingExternalIdObject

# TODO update the JSON string below
json = "{}"
# create an instance of SkippedExistingExternalIdObject from a JSON string
skipped_existing_external_id_object_instance = SkippedExistingExternalIdObject.from_json(json)
# print the JSON string representation of the object
print(SkippedExistingExternalIdObject.to_json())

# convert the object into a dict
skipped_existing_external_id_object_dict = skipped_existing_external_id_object_instance.to_dict()
# create an instance of SkippedExistingExternalIdObject from a dict
skipped_existing_external_id_object_from_dict = SkippedExistingExternalIdObject.from_dict(skipped_existing_external_id_object_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

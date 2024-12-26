# CreateNewTransactionsRequest

## Properties

| Name                    | Type                                                            | Description                                                                                                                                                                                                                                                                                                                              | Notes                         |
| ----------------------- | --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| **transactions**        | [**List[InsertTransactionObject]**](InsertTransactionObject.md) | List of transactions to insert.                                                                                                                                                                                                                                                                                                          |
| **apply_rules**         | **bool**                                                        | If set to true, any rules associated with the account specified by the &#x60;manual_account_id&#x60; property for each transaction will be applied.                                                                                                                                                                                      | [optional] [default to False] |
| **skip_duplicates**     | **bool**                                                        | If set to true, the system will flag new transactions that have the same &#x60;date&#x60;, &#x60;payee&#x60;, &#x60;amount&#x60;, and &#x60;manual_account_id&#x60;, as a duplicate. Not that deduplication based on &#x60;external_id&#x60; and &#x60;manual_account_id&#x60; will always occur regardless of how this property is set. | [optional] [default to False] |
| **skip_balance_update** | **bool**                                                        | If set to true, and new transactions include a &#x60;manual_account_id&#x60;, the balances of these accounts will not be updated, when the transactions are inserted.                                                                                                                                                                    | [optional] [default to False] |

## Example

```python
from lunchable.models.create_new_transactions_request import CreateNewTransactionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNewTransactionsRequest from a JSON string
create_new_transactions_request_instance = CreateNewTransactionsRequest.from_json(json)
# print the JSON string representation of the object
print(CreateNewTransactionsRequest.to_json())

# convert the object into a dict
create_new_transactions_request_dict = create_new_transactions_request_instance.to_dict()
# create an instance of CreateNewTransactionsRequest from a dict
create_new_transactions_request_from_dict = CreateNewTransactionsRequest.from_dict(create_new_transactions_request_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

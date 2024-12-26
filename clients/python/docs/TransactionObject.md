# TransactionObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | System created unique identifier for transaction | 
**var_date** | **date** | Date of transaction in ISO 8601 format | 
**amount** | **str** | Amount of the transaction in numeric format to 4 decimal places | 
**currency** | [**CurrencyEnum**](CurrencyEnum.md) | Three-letter lowercase currency code of the transaction in ISO 4217 format | 
**to_base** | **float** | The amount converted to the user&#39;s primary currency. If the multi-currency feature is not being used, to_base and amount will be the same. | 
**recurring_id** | **int** | The unique identifier of the associated recurring item that this transaction matched.  If the recurring item changed properties of this transaction, an &#x60;overrides&#x60; property with details on what was overridden will be include in the transaction object.  If no &#x60;overrides&#x60; property exists when there is a &#x60;recurring_id&#x60; it means that the recurring_item is still in the suggested state, or that it does not contain any rules to override transaction properties. | 
**overrides** | [**TransactionOverridesObject**](TransactionOverridesObject.md) |  | 
**payee** | **str** | Name of payee set by the user, the financial institution, or by  a matched recurring item. This will match the value  displayed in payee field on the transactions page in the GUI.  | 
**category_id** | **int** | Unique identifier of associated category set by the user or by a matched recurring_item.&lt;br&gt; Category details can be obtained by passing the value of this property to the [Get A Single Category](../operations/getCategoryById) API | 
**notes** | **str** | Any transaction notes set by the user or by  a matched recurring item. This will match the value  displayed in notes field on the transactions page in the GUI.  | 
**status** | **str** | Status of the transaction: - &#x60;reviewed&#x60;: User has reviewed the transaction, or it was automatically marked as reviewed due to reviewed recurring_item logic - &#x60;unreviewed&#x60;: User has not reviewed the transaction and it does not match any reviewed recurring_items. - &#x60;delete_pending&#x60;: The synced account deleted this transaction after it was updated by the user.  Requires manual intervention. - &#x60;pending&#x60;: Transaction is still pending with the synced institution (not posted).  | 
**is_pending** | **bool** | Denotes if the transaction is pending (not posted). Applies only to transactions in synced accounts and will always be false for transactions associated with manual accounts. | 
**created_at** | **datetime** | The date and time of when the transaction was created (in the ISO 8601 extended format). | 
**updated_at** | **datetime** | The date and time of when the transaction was last updated (in the ISO 8601 extended format). | 
**is_parent** | **bool** | If true this transaction has been split into two or more other transactions.  By default parent transactions are not returned in call to &#x60;GET /transactions&#x60; but they can be queried directly by their ID. | [optional] 
**children** | **List[str]** | Exists only for transactions which are the parent of a split transaction, and contains a list of the associated transactions that it was split into. By default parent transactions are not returned in a &#x60;GET /transactions&#x60; API call, but can be examined via a subsequent call to &#x60;GET /transactions{id}&#x60;, where the value of &#x60;parent_id&#x60; field of a split transaction is the requested transaction. | [optional] 
**parent_id** | **List[float]** | A transaction ID if this is a split transaction. Denotes the transaction ID of the original, or parent, transaction.  Is null if this is not a split transaction | 
**is_group** | **bool** | True if this transaction represents a group of transactions. If so, amount and currency represent the totalled amount of transactions bearing this transaction’s id as their group_id. Amount is calculated based on the user’s primary currency. | 
**group_id** | **int** | Is set if this transaction is part of a group. Denotes the ID of the grouped transaction this is now included in. By default the transactions that were grouped are not returned in a call to &#x60;GET /transactions&#x60; but they can be queried directly by calling the &#x60;GET /transactions/group/{id}&#x60;, where the id passed is associated with a transaction where the &#x60;is_group&#x60; attribute is true | 
**manual_account_id** | **int** | The unique identifier of the manual account associated with this transaction.  This will always be null if this transaction is associated with a synced account or if this transaction has no associated account and appears as a \&quot;Cash Transaction\&quot; in the Lunch Money GUI. | 
**plaid_account_id** | **int** | The unique identifier of the plaid account associated with this transaction.  This will always be null if this transaction is associated with a manual account or if this transaction has no associated account and appears as a \&quot;Cash Transaction\&quot; in the Lunch Money GUI. | 
**tag_ids** | **List[int]** | A list of tag_ids for the tags associated with this transaction.  If the transaction has no tags this will be an empty list.&lt;br&gt; Tag details can be obtained by passing the value of this attribute as the &#x60;ids&#x60; query parameter to the [List Tags](../operations/getTags) API | 
**source** | **str** | Source of the transaction: - &#x60;api&#x60;: Transaction was added by a call to the [POST /transactions](../operations/createTransaction) API - &#x60;csv&#x60;: Transaction was added via a CSV Import - &#x60;manual&#x60;: Transaction was created via the \&quot;Add to Cash\&quot; button on the Transactions page - &#x60;merge&#x60;: Transactions were originally in an account that was merged into another account - &#x60;plaid&#x60;: Transaction came from a Financial Institution synced via Plaid - &#x60;recurring&#x60;: Transaction was created from the Recurring page  - &#x60;rule&#x60;: Transaction was created by a rule to split a transaction - &#x60;split&#x60;: This is a transaction created by splitting another transaction - &#x60;user&#x60;: This is a legacy value and is replaced by either csv or manual  | 
**external_id** | **str** | A user-defined external ID for any transaction that was added via csv import, &#x60;POST /transactions&#x60; API call, or manually added via the Lunch Money GUI.  No external ID exists for transactions associated with synced accounts, and they cannot be added. For transactions associated with manual accounts, the external ID must be unique as attempts to add a subsequent transaction with the same external_id and manual_account_id will be flagged as duplicates and fail. | 
**plaid_metadata** | **object** | If requested, the transaction&#39;s plaid_metadata that came when this transaction was obtained. This will be a json object, but the schema is variable. This will only be present for transactions associated with a plaid account. | [optional] 
**custom_metadata** | **object** | If requested, the transaction&#39;s custom_metadata that was included when the transaction was inserted via the API. This will be a json object, but the schema is variable. This will only be present for transactions associated with a manual account. | [optional] 

## Example

```python
from lunchable.models.transaction_object import TransactionObject

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionObject from a JSON string
transaction_object_instance = TransactionObject.from_json(json)
# print the JSON string representation of the object
print(TransactionObject.to_json())

# convert the object into a dict
transaction_object_dict = transaction_object_instance.to_dict()
# create an instance of TransactionObject from a dict
transaction_object_from_dict = TransactionObject.from_dict(transaction_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



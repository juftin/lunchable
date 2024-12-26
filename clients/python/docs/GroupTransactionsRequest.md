# GroupTransactionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** | List of existing transaction IDs to group. Split and recurring transactions may not be grouped. Transactions that are already grouped must be ungrouped before being regrouped. | 
**var_date** | **date** | Date for the new grouped transaction in ISO 8601 format. | 
**payee** | **str** | The payee for the new grouped transaction.  | 
**category_id** | **int** | The ID of an existing category to assign to the grouped transaction. If not set and all the grouped transactions have the same category, the grouped transaction will inherit the category, otherwise the new transaction will have no category. | [optional] 
**notes** | **str** | Notes for the grouped transaction.  | [optional] 
**status** | **str** | If set must be either &#x60;reviewed&#x60; or &#x60;unreviewed&#x60;.  If not set, defaults to &#x60;reviewed&#x60;. | [optional] 
**tag_ids** | **List[int]** | A list of IDs for the tags associated with the grouped transaction.  Each ID must match an existing tag associated with the user&#39;s account. If not set, no tags will be associated with the created transaction. | [optional] 

## Example

```python
from lunchable.models.group_transactions_request import GroupTransactionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupTransactionsRequest from a JSON string
group_transactions_request_instance = GroupTransactionsRequest.from_json(json)
# print the JSON string representation of the object
print(GroupTransactionsRequest.to_json())

# convert the object into a dict
group_transactions_request_dict = group_transactions_request_instance.to_dict()
# create an instance of GroupTransactionsRequest from a dict
group_transactions_request_from_dict = GroupTransactionsRequest.from_dict(group_transactions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



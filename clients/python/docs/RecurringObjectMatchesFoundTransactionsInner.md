# RecurringObjectMatchesFoundTransactionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date for a matching transaction within the specified range. | [optional] 
**transaction_id** | **int** | The ID of a matching transaction within the specified range. | [optional] 

## Example

```python
from lunchable.models.recurring_object_matches_found_transactions_inner import RecurringObjectMatchesFoundTransactionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RecurringObjectMatchesFoundTransactionsInner from a JSON string
recurring_object_matches_found_transactions_inner_instance = RecurringObjectMatchesFoundTransactionsInner.from_json(json)
# print the JSON string representation of the object
print(RecurringObjectMatchesFoundTransactionsInner.to_json())

# convert the object into a dict
recurring_object_matches_found_transactions_inner_dict = recurring_object_matches_found_transactions_inner_instance.to_dict()
# create an instance of RecurringObjectMatchesFoundTransactionsInner from a dict
recurring_object_matches_found_transactions_inner_from_dict = RecurringObjectMatchesFoundTransactionsInner.from_dict(recurring_object_matches_found_transactions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



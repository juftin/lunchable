# RecurringObjectMatches

Details on expected, found and missing transactions for the specified range. This will be `null` for recurring items with a `status` of `suggested`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_start_date** | **date** | The beginning of the date range that this request used to find matching transactions. | [optional] 
**request_end_date** | **date** | The beginning of the date range that this request used to find matching transactions. | [optional] 
**expected_occurrence_dates** | **List[date]** | A list of dates within the specified range where a recurring transactions is expected. | [optional] 
**found_transactions** | [**List[RecurringObjectMatchesFoundTransactionsInner]**](RecurringObjectMatchesFoundTransactionsInner.md) | A list with the dates and IDs of matching transactions. | [optional] 
**missing_transaction_dates** | **List[date]** | A list of dates within the range of where a recurring transaction was expected but none was found. | [optional] 

## Example

```python
from lunchable.models.recurring_object_matches import RecurringObjectMatches

# TODO update the JSON string below
json = "{}"
# create an instance of RecurringObjectMatches from a JSON string
recurring_object_matches_instance = RecurringObjectMatches.from_json(json)
# print the JSON string representation of the object
print(RecurringObjectMatches.to_json())

# convert the object into a dict
recurring_object_matches_dict = recurring_object_matches_instance.to_dict()
# create an instance of RecurringObjectMatches from a dict
recurring_object_matches_from_dict = RecurringObjectMatches.from_dict(recurring_object_matches_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



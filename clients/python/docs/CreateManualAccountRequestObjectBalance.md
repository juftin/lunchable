# CreateManualAccountRequestObjectBalance

Numeric value of the current balance, up to four decimal places, of the account as a number or string. Do not include any special characters aside from a decimal point.

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |

## Example

```python
from lunchable.models.create_manual_account_request_object_balance import CreateManualAccountRequestObjectBalance

# TODO update the JSON string below
json = "{}"
# create an instance of CreateManualAccountRequestObjectBalance from a JSON string
create_manual_account_request_object_balance_instance = CreateManualAccountRequestObjectBalance.from_json(json)
# print the JSON string representation of the object
print(CreateManualAccountRequestObjectBalance.to_json())

# convert the object into a dict
create_manual_account_request_object_balance_dict = create_manual_account_request_object_balance_instance.to_dict()
# create an instance of CreateManualAccountRequestObjectBalance from a dict
create_manual_account_request_object_balance_from_dict = CreateManualAccountRequestObjectBalance.from_dict(create_manual_account_request_object_balance_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

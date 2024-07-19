# LunchMoney

The `LunchMoney` client is the main entrypoint for interacting with the Lunch Money API.
It defaults to inheriting the `LUNCHMONEY_ACCESS_TOKEN` environment variable, but can be
created with an explicit `access_token` parameter.

```python
from lunchable import LunchMoney

lunch = LunchMoney(access_token="xxxxxxxxxxx")
```

## Methods

| HTTP Verb | Name                                                                           | Description                                                              |
|-----------|--------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| GET       | [get_assets](#lunchable.LunchMoney.get_assets)                                 | Get Manually Managed Assets                                              |
| GET       | [get_budgets](#lunchable.LunchMoney.get_budgets)                               | Get Monthly Budgets                                                      |
| GET       | [get_categories](#lunchable.LunchMoney.get_categories)                         | Get Spending categories                                                  |
| GET       | [get_category](#lunchable.LunchMoney.get_category)                             | Get single category                                                      |
| GET       | [get_crypto](#lunchable.LunchMoney.get_crypto)                                 | Get Crypto Assets                                                        |
| GET       | [get_plaid_accounts](#lunchable.LunchMoney.get_plaid_accounts)                 | Get Plaid Synced Assets                                                  |
| GET       | [get_recurring_items](#lunchable.LunchMoney.get_recurring_items)               | Get Recurring Items                                                      |
| GET       | [get_tags](#lunchable.LunchMoney.get_tags)                                     | Get Spending Tags                                                        |
| GET       | [get_transaction](#lunchable.LunchMoney.get_transaction)                       | Get a Transaction by ID                                                  |
| GET       | [get_transactions](#lunchable.LunchMoney.get_transactions)                     | Get Transactions Using Criteria                                          |
| GET       | [get_user](#lunchable.LunchMoney.get_user)                                     | Get Personal User Details                                                |
| POST      | [insert_asset](#lunchable.LunchMoney.insert_asset)                             | Create a single (manually-managed) asset                                 |
| POST      | [insert_category](#lunchable.LunchMoney.insert_category)                       | Create a Spending Category                                               |
| POST      | [insert_category_group](#lunchable.LunchMoney.insert_category_group)           | Create a Spending Category Group                                         |
| POST      | [insert_into_category_group](#lunchable.LunchMoney.insert_into_category_group) | Add to a Category Group                                                  |
| POST      | [insert_transaction_group](#lunchable.LunchMoney.insert_transaction_group)     | Create a Transaction Group of Two or More Transactions                   |
| POST      | [insert_transactions](#lunchable.LunchMoney.insert_transactions)               | Create One or Many Lunch Money Transactions                              |
| POST      | [trigger_fetch_from_plaid](#lunchable.LunchMoney.trigger_fetch_from_plaid)     | Trigger a Plaid Sync                                                     |
| POST      | [unsplit_transactions](#lunchable.LunchMoney.unsplit_transactions)             | Unsplit Transactions                                                     |
| PUT       | [upsert_budget](#lunchable.LunchMoney.upsert_budget)                           | Upsert a Budget for a Category and Date                                  |
| PUT       | [update_asset](#lunchable.LunchMoney.update_asset)                             | Update a Single Asset                                                    |
| PUT       | [update_category](#lunchable.LunchMoney.update_category)                       | Update a single category                                                 |
| PUT       | [update_crypto](#lunchable.LunchMoney.update_crypto)                           | Update a Manual Crypto Asset                                             |
| PUT       | [update_transaction](#lunchable.LunchMoney.update_transaction)                 | Update a Transaction                                                     |
| DELETE    | [remove_budget](#lunchable.LunchMoney.remove_budget)                           | Unset an Existing Budget for a Particular Category in a Particular Month |
| DELETE    | [remove_category](#lunchable.LunchMoney.remove_category)                       | Delete a single category                                                 |
| DELETE    | [remove_category_force](#lunchable.LunchMoney.remove_category_force)           | Forcefully delete a single category                                      |
| DELETE    | [remove_transaction_group](#lunchable.LunchMoney.remove_transaction_group)     | Delete a Transaction Group                                               |

## Low Level Methods

| Name                                                       | Description                                           |
|------------------------------------------------------------|-------------------------------------------------------|
| [request](#lunchable.LunchMoney.request)                   | Make an HTTP request                                  |
| [arequest](#lunchable.LunchMoney.arequest)                 | Make an async HTTP request                            |
| [process_response](#lunchable.LunchMoney.process_response) | Process a Lunch Money response and raise any errors   |
| [make_request](#lunchable.LunchMoney.make_request)         | Make an HTTP request and `process` its response       |
| [amake_request](#lunchable.LunchMoney.amake_request)       | Make an async HTTP request and `process` its response |

## Attributes

| Name                                                 | Description                      |
|------------------------------------------------------|----------------------------------|
| [async_session](#lunchable.LunchMoney.async_session) | Authenticated Async HTTPX Client |
| [session](#lunchable.LunchMoney.session)             | Authenticated HTTPX Client       |

## Class Documentation

::: lunchable.LunchMoney
    handler: python
    options:
        show_bases: false
        allow_inspection: true
        inherited_members: true
        group_by_category: true
        heading_level: 3
        show_source: false

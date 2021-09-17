# lunch-money TODO Checklist

## API Endpoints Roadmap

### Incomplete

#### Budget

- [x] `GET` `v1/budgets`
    - [ ] Tests
- [x] `PUT` `v1/budgets`
    - [x] Tests
- [x] `DELETE` `v1/budgets`
    - [ ] Tests

### Done

#### Assets

- [x] `GET` `v1/assets`
    - [x] Tests
- [x] `PUT` `v1/assets/:id`
    - [x] Tests

#### Categories

- [x] `GET` `v1/categories`
    - [x] Tests
- [x] `POST` `v1/categories`
    - [x] Tests

#### Crypto

- [x] `GET` `v1/crypto`
    - [x] Tests
- [x] `PUT` `v1/crypto/manual/:id`
    - [x] Tests

#### Plaid Accounts

- [x] `GET` `v1/plaid_accounts`
    - [x] Tests

#### Recurring Expenses

- [x] `GET` `v1/recurring_expenses`
    - [x] Tests

#### Tags

- [x] `GET` `v1/tags`
    - [x] Tests

#### Transactions

- [x] `GET` `v1/transactions`
    - [x] Tests
- [x] `GET` `v1/transactions/:transaction_id`
    - [x] Tests
- [x] `POST` `v1/transactions`
    - [x] Tests
- [x] `PUT` `v1/transactions/:transaction_id`
    - [x] Tests


- [x] `POST` `v1/transactions/group`
    - [x] Tests
- [x] `DELETE` `v1/transactions/group/:transaction_id`
    - [x] Tests

## Splitwise Plugin Roadmap

- [ ] Implement Class to interact with Splitwise
- [ ] Tag creates a split transaction
- [ ] Auto Import of non-created transactions
- [ ] Auto Syncing of Account Balance

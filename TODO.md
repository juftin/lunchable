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

#### Crypto

- [ ] `GET` `v1/crypto`
    - [ ] Tests
- [ ] `PUT` `v1/crypto/manual/:id`
    - [ ] Tests

#### Tags

- [ ] `GET` `v1/tags`
    - [ ] Tests

#### Transactions

- [x] `GET` `v1/transactions`
    - [ ] Tests
- [x] `GET` `v1/transactions/:transaction_id`
    - [ ] Tests
- [x] `POST` `v1/transactions`
    - [ ] Tests
- [x] `PUT` `v1/transactions/:transaction_id`
    - [ ] Tests


- [x] `POST` `v1/transactions/group`
    - [ ] Tests
- [x] `DELETE` `v1/transactions/group/:transaction_id`
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

#### Plaid Accounts

- [x] `GET` `v1/plaid_accounts`
    - [x] Tests

#### Recurring Expenses

- [x] `GET` `v1/recurring_expenses`
    - [x] Tests

## Splitwise Plugin Roadmap

- [ ] Implement Class to interact with Splitwise
- [ ] Tag creates a split transaction
- [ ] Auto Import of non-created transactions
- [ ] Auto Syncing of Account Balance

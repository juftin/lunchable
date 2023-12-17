# SplitLunch: Splitwise Integration

<div align="center">
    <p float="center">
        <img src=https://assets.splitwise.com/assets/core/logo-square.svg
            width="35%" alt="lunchable">
        <img src=https://i.imgur.com/FyKDsG3.png
            width="60%" alt="lunchable">
    </p>
</div>

---

## Integrations

This plugin supports different operations, and some of those operations have prerequisites:

### Auto Importer

It supports the auto-importing of Splitwise expenses into Lunch Money transactions. This requires
a manual asset exist in your Lunch Money account with "Splitwise" in the Name. Expenses that
have been deleted or which don't impact you (i.e. are only between other users in your group)
are skipped. By default, payments and expenses for which you are recorded as the payer are
skipped as well, but these can be overridden by the `--allow-payments` and `--allow-self-paid`
CLI flags, respectively.

#### Prerequisites

- Accounts:
    - Splitwise must be in the account name

### LunchMoney -> Splitwise

It supports the creation of Splitwise transactions directly from synced Lunch Money accounts. This syncing requires you create a tag called `SplitLunchImport`. Transactions with this tag will be created in Splitwise with your "financial partner". Once transactions are created in Splitwise they will be split in half in Lunch Money. Half of the split will be marked in the `Reimbursement` category which must be created.

#### Prerequisites

- Financial Partners:
    - If you only have one friend in Splitwise, this is your Financial Partner
    - Financial Partners can be individual users or groups and transactions will be split accordingly
    - Financial Partners must be specified by their Splitwise Group ID, Splitwise User ID, or Email Address
- Tags:
    - `SplitLunchImport`
- Categories:
    - `Reimbursement`

### SplitLunch

It supports a workflow where you mark transactions as split (identical to `Lunch Money -> Splitwise`) without importing them into Splitwise. This syncing requires you create a tag called `SplitLunch` and a category named `Reimbursement`

#### Prerequisites

- Tags:
    - `SplitLunch`
- Categories:
    - `Reimbursement`

### LunchMoney -> Splitwise (without splitting)

It supports the creation of Splitwise transactions directly from synced Lunch Money accounts. This syncing requires you create a tag called `SplitLunchDirectImport`. Transactions with this tag will be created in Splitwise with the total completely owed by your "financial partner". The entire transaction wil then be categorized as `Reimbursement` without being split.

#### Prerequisites

- Financial Partners:
    - If you only have one friend in Splitwise, this is your Financial Partner
    - Financial Partners can be individual users or groups and transactions will be split accordingly
    - Financial Partners must be specified by their Splitwise Group ID, Splitwise User ID, or Email Address
- Tags:
    - `SplitLunchDirectImport`
- Categories:
    - `Reimbursement`

> **Note:** Some of the above scenarios allow for tagging of a `Splitwise` tag on updated transactions. This tag must be created for this functionality to work.

## Installation

```shell
pip install lunchable[splitlunch]
```

## Run the SplitLunch plugin for the Lunchable CLI

```shell
lunchable plugins splitlunch --help
```

## Run the SplitLunch plugin for the Lunchable CLI via Docker

```shell
docker pull juftin/lunchable
```

```shell
docker run \
    --env LUNCHMONEY_ACCESS_TOKEN=${LUNCHMONEY_ACCESS_TOKEN} \
    --env SPLITWISE_CONSUMER_KEY=${SPLITWISE_CONSUMER_KEY} \
    --env SPLITWISE_CONSUMER_SECRET=${SPLITWISE_CONSUMER_SECRET} \
    --env SPLITWISE_API_KEY=${SPLITWISE_API_KEY} \
    juftin/lunchable:latest \
    lunchable plugins splitlunch --help
```

## Run via Python

```python
from lunchable.plugins.splitlunch import SplitLunch
```

::: lunchable.plugins.splitlunch.SplitLunch
    handler: python
    options:
        show_bases: false
        allow_inspection: true
        heading_level: 3

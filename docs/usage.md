# Usage

## Installation

To use lunchable, first install it using pip:

```shell
pip install lunchable
```

## Client

The [LunchMoney](interacting.md#interacting-with-lunch-money) client is the main entrypoint
for interacting with the Lunch Money API. It defaults to inheriting the `LUNCHMONEY_ACCESS_TOKEN`
environment variable, but can be created with an explicit `access_token` parameter.

```python
from lunchable import LunchMoney

lunch = LunchMoney(access_token="xxxxxxx")
```

Read more about [Interacting with Lunch Money](interacting.md#lunchmoney)
to see what else you can do.

# Transactions

## Retrieve a list of [`TransactionObject`][lunchable.models.transactions.TransactionObject]

```python
from typing import List

from lunchable import LunchMoney
from lunchable.models import TransactionObject

lunch = LunchMoney(access_token="xxxxxxx")
transactions: List[TransactionObject] = lunch.get_transactions(
    start_date="2020-01-01",
    end_date="2020-01-31"
)
```

## Retrieve a single transaction ([`TransactionObject`][lunchable.models.transactions.TransactionObject])

```python
from lunchable import LunchMoney
from lunchable.models import TransactionObject

lunch = LunchMoney(access_token="xxxxxxx")
transaction: TransactionObject = lunch.get_transaction(transaction_id=1234)
```

The above code returns a TransactionObject with ID # 1234 (assuming it exists)

## Update a transaction with a [`TransactionUpdateObject`][lunchable.models.transactions.TransactionUpdateObject]

```python
from datetime import datetime
from typing import Any, Dict

from lunchable import LunchMoney
from lunchable.models import TransactionUpdateObject

lunch = LunchMoney(access_token="xxxxxxx")
transaction_note = f"Updated on {datetime.now()}"
notes_update = TransactionUpdateObject(notes=transaction_note)
response: Dict[str, Any] = lunch.update_transaction(
    transaction_id=1234,
    transaction=notes_update
)
```

## Update a [`TransactionObject`][lunchable.models.transactions.TransactionObject] with itself

```python
from datetime import datetime, timedelta

from lunchable import LunchMoney
from lunchable.models import TransactionObject

lunch = LunchMoney(access_token="xxxxxxx")
transaction: TransactionObject = lunch.get_transaction(transaction_id=1234)

transaction.notes = f"Updated on {datetime.now()}"
transaction.date = transaction.date + timedelta(days=1)
response = lunch.update_transaction(
    transaction_id=transaction.id,
    transaction=transaction
)
```

## Create a new transaction with a [`TransactionInsertObject`][lunchable.models.transactions.TransactionInsertObject]

`transactions` can be a single [`TransactionInsertObject`][lunchable.models.transactions.TransactionInsertObject]
or a list of [`TransactionInsertObject`][lunchable.models.transactions.TransactionInsertObject].

```python
from lunchable import LunchMoney
from lunchable.models import TransactionInsertObject

lunch = LunchMoney(access_token="xxxxxxx")

new_transaction = TransactionInsertObject(
    payee="Example Restaurant",
    amount=120.00,
    notes="Saturday Dinner"
)
new_transaction_ids = lunch.insert_transactions(transactions=new_transaction)
```

## Use the Lunchable CLI

```shell
lunchable transactions get --limit 5
```

## Use the Lunchable CLI via Docker

```shell
docker pull juftin/lunchable
```

```shell
docker run \
    --env LUNCHMONEY_ACCESS_TOKEN=${LUNCHMONEY_ACCESS_TOKEN} \
    juftin/lunchable:latest \
    lunchable transactions get --limit 5
```

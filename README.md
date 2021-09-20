# lunch-money

**lunch-money** is a Python client for the Lunch Money Developer API. It's built on top
of [pydantic](https://github.com/samuelcolvin/pydantic>), and it offers a *simple* and *intuitive*
API and Objects.

> ### ⚠️ Note: This project is under active development.

```python
from typing import List

from lunchmoney import LunchMoney
from lunchmoney.models import TransactionObject

lunch = LunchMoney(access_token="xxxxxxxxxxx")
transactions: List[TransactionObject] = lunch.get_transactions()

first_transaction: TransactionObject = transactions[0]
transaction_as_dict: dict = first_transaction.dict()
```

#### Check out the official [**ReadTheDocs**](https://lunch-money.readthedocs.io/en/latest/)
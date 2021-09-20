# lunch-money

[![PyPI](https://img.shields.io/pypi/v/lunch-money?color=blue&label=lunch-money)](https://github.com/juftin/lunch-money)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/lunch-money)](https://pypi.python.org/pypi/lunch-money/)
[![Testing Status](https://github.com/juftin/lunch-money/actions/workflows/tests.yml/badge.svg)](https://github.com/juftin/lunch-money/actions/workflows/tests.yml)
[![GitHub License](https://img.shields.io/github/license/juftin/lunch-money?color=blue&label=License)](https://github.com/juftin/lunch-money/blob/main/LICENSE)

**lunch-money** is a Python client for the Lunch Money Developer API. It's built on top
of [pydantic](https://github.com/samuelcolvin/pydantic>), and it offers a *simple* and *intuitive*
API.

> ### ⚠️ Note: This project is under active development.

### Installation

```shell
pip install lunch-money
```

### Usage

```python
from typing import List

from lunchmoney import LunchMoney
from lunchmoney.models import TransactionObject

lunch = LunchMoney(access_token="xxxxxxxxxxx")
transactions: List[TransactionObject] = lunch.get_transactions()

first_transaction: TransactionObject = transactions[0]
transaction_as_dict: dict = first_transaction.dict()
```

#### Check out the [**ReadTheDocs**](https://lunch-money.readthedocs.io/en/latest/)
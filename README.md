# lunchable

[![Lunchable Version](https://img.shields.io/pypi/v/lunchable?color=blue&label=lunchable)](https://github.com/juftin/lunchable)
[![PyPI](https://img.shields.io/pypi/pyversions/lunchable)](https://pypi.python.org/pypi/lunchable/)
[![Testing Status](https://github.com/juftin/lunchable/actions/workflows/tests.yml/badge.svg)](https://github.com/juftin/lunchable/actions/workflows/tests.yml)
[![GitHub License](https://img.shields.io/github/license/juftin/lunchable?color=blue&label=License)](https://github.com/juftin/lunchable/blob/main/LICENSE)
[![Documentation Status](https://readthedocs.org/projects/lunchable/badge/?version=latest)](https://lunchable.readthedocs.io/en/latest/?badge=latest)

**lunchable** is a Python client for the Lunch Money Developer API. It's built on top
of [pydantic](https://github.com/samuelcolvin/pydantic>), and it offers a *simple* and *intuitive*
API.

### Installation

```shell
pip install lunchable
```

### Usage

```python
from typing import List

from lunchable import LunchMoney
from lunchable.models import TransactionObject

lunch = LunchMoney(access_token="xxxxxxxxxxx")
transactions: List[TransactionObject] = lunch.get_transactions()

first_transaction: TransactionObject = transactions[0]
transaction_as_dict: dict = first_transaction.dict()
```

### Check out the [**ReadTheDocs**](https://lunchable.readthedocs.io/en/latest/)

> ### ⚠️ Note: This project is under active development.

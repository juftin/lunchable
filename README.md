# lunchable

<div align="center">
<a href="https://github.com/juftin/lunchable">
  <img src=https://i.imgur.com/FyKDsG3.png
    width="400" alt="lunchable">
</a>
</div>

[![Lunchable Version](https://img.shields.io/pypi/v/lunchable?color=blue&label=lunchable)](https://github.com/juftin/lunchable)
[![PyPI](https://img.shields.io/pypi/pyversions/lunchable)](https://pypi.python.org/pypi/lunchable/)
[![Docker Image Version](https://img.shields.io/docker/v/juftin/lunchable?color=blue&label=docker&logo=docker)](https://hub.docker.com/r/juftin/lunchable)
[![Testing Status](https://github.com/juftin/lunchable/actions/workflows/tests.yaml/badge.svg?branch=main)](https://github.com/juftin/lunchable/actions/workflows/tests.yaml?query=branch%3Amain)
[![GitHub License](https://img.shields.io/github/license/juftin/lunchable?color=blue&label=License)](https://github.com/juftin/lunchable/blob/main/LICENSE)

**lunchable** is a Python Client for the [Lunch Money Developer API](https://lunchmoney.dev). It's
built on top of [pydantic](https://github.com/samuelcolvin/pydantic), it offers an *intuitive* API,
a *simple* CLI, complete coverage of all endpoints, and *plugins* to other external services.

### Installation

```shell
pip install lunchable
```

### Usage

```python
from typing import Any, Dict, List

from lunchable import LunchMoney
from lunchable.models import TransactionObject

lunch = LunchMoney(access_token="xxxxxxxxxxx")
transactions: List[TransactionObject] = lunch.get_transactions()

first_transaction: TransactionObject = transactions[0]
transaction_as_dict: Dict[str, Any] = first_transaction.dict()
```

```shell
export LUNCHMONEY_ACCESS_TOKEN="xxxxxxxxxxx"
lunchable transactions get --limit 5
lunchable http -X GET https://dev.lunchmoney.app/v1/assets
```

### Check out the [**Docs**](https://juftin.com/lunchable/)
### Looking to contribute? See the [Contributing Guide](docs/source/contributing.md)
### See the [Changelog](https://github.com/juftin/lunchable/releases)


--------------
--------------

<br/>

[<p align="center" ><img src="https://raw.githubusercontent.com/juftin/juftin/main/static/juftin.png" width="60" height="60"  alt="juftin logo"> </p>](https://github.com/juftin)

<h1 align="center">lunchable</h1>

<div align="center">
  <a href="https://github.com/juftin/lunchable">
  <img src=https://i.imgur.com/FyKDsG3.png
    width="400" alt="lunchable">  </a>
</div>

<p align="center">
  <a href="https://github.com/juftin/lunchable"><img src="https://img.shields.io/pypi/v/lunchable?color=blue&label=lunchable" alt="PyPI"></a>
  <a href="https://pypi.python.org/pypi/lunchable/"><img src="https://img.shields.io/pypi/pyversions/lunchable" alt="PyPI - Python Version"></a>
  <a href="https://hub.docker.com/r/juftin/lunchable"><img src="https://img.shields.io/docker/v/juftin/lunchable?color=blue&label=docker&logo=docker" alt="Docker Image Version"></a>
  <a href="https://github.com/conda-forge/lunchable-feedstock"><img src="https://img.shields.io/conda/v/conda-forge/lunchable?label=conda-forge" alt="Conda Version"></a>
  <a href="https://github.com/juftin/lunchable/blob/main/LICENSE"><img src="https://img.shields.io/github/license/juftin/lunchable?color=blue&label=License" alt="GitHub License"></a>
  <a href="https://github.com/juftin/lunchable/actions/workflows/tests.yaml?query=branch%3Amain"><img src="https://github.com/juftin/lunchable/actions/workflows/tests.yaml/badge.svg?branch=main" alt="Testing Status"></a>
  <a href="https://codecov.io/gh/juftin/lunchable"><img src="https://codecov.io/gh/juftin/lunchable/graph/badge.svg?token=2IGD9E5L8K"/></a>
  <a href="https://github.com/pypa/hatch"><img src="https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg" alt="Hatch project"></a>
  <a href="https://github.com/astral-sh/ruff"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="Ruff"></a>
  <a href="https://github.com/pre-commit/pre-commit"><img src="https://img.shields.io/badge/pre--commit-enabled-lightgreen?logo=pre-commit" alt="pre-commit"></a>
  <a href="https://github.com/semantic-release/semantic-release"><img src="https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg" alt="semantic-release"></a>
  <a href="https://gitmoji.dev"><img src="https://img.shields.io/badge/gitmoji-%20😜%20😍-FFDD67.svg" alt="Gitmoji"></a>
</p>

**lunchable** is a Python Client for the [Lunch Money Developer API](https://lunchmoney.dev). It's
built on top of [pydantic](https://github.com/pydantic/pydantic) and [httpx](https://github.com/encode/httpx/),
it offers an _intuitive_ API, a _simple_ CLI, complete coverage of all endpoints,
and a _plugin_ framework for extending the functionality of the library.

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
transaction_as_dict: Dict[str, Any] = first_transaction.model_dump()
```

### CLI

To use the CLI, you'll need to set the `LUNCHMONEY_ACCESS_TOKEN` environment variable.
It's recommended to use [pipx](https://github.com/pypa/pipx) to install the CLI -
use the `lunchable[plugins]` extra to include all the known plugins:

```shell
pipx install "lunchable[plugins]"
```

```shell
export LUNCHMONEY_ACCESS_TOKEN="xxxxxxxxxxx"
lunchable transactions get --limit 5
lunchable http -X GET v1/assets
```

<!--skip-->

### Check out the [**Docs**](https://juftin.com/lunchable/)

### Looking to contribute? See the [Contributing Guide](docs/contributing.md)

### See the [Changelog](https://github.com/juftin/lunchable/releases)

---

---

<br/>

[<p align="center" ><img src="https://raw.githubusercontent.com/juftin/juftin/main/static/juftin.png" width="60" height="60"  alt="juftin logo"> </p>](https://github.com/juftin)

<!--skip-->

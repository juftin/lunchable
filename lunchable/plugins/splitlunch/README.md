# SplitLunch

## A lunchable plugin to Splitwise

<div align="center">
    <p float="center">
        <img src=https://assets.splitwise.com/assets/core/logo-square.svg
            width="195" alt="lunchable">
        <img src=https://i.imgur.com/FyKDsG3.png
            width="300" alt="lunchable">
    </p>
</div>

[![Lunchable Version](https://img.shields.io/pypi/v/lunchable?color=blue&label=lunchable)](https://github.com/juftin/lunchable)
[![PyPI](https://img.shields.io/pypi/pyversions/lunchable)](https://pypi.python.org/pypi/lunchable/)
[![Testing Status](https://github.com/juftin/lunchable/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/juftin/lunchable/actions/workflows/tests.yml?query=branch%3Amain)
[![GitHub License](https://img.shields.io/github/license/juftin/lunchable?color=blue&label=License)](https://github.com/juftin/lunchable/blob/main/LICENSE)
[![Documentation Status](https://readthedocs.org/projects/lunchable/badge/?version=latest)](https://lunchable.readthedocs.io/en/latest/?badge=latest)

```shell
pip install lunchable[splitlunch]
```

```python
from lunchable.plugins.splitlunch import SplitLunch

splitlunch = SplitLunch()
splitlunch.refresh_splitwise_transactions()
```

```shell
lunchable plugins splitlunch expenses --limit 5
lunchable plugins splitlunch refresh
```

The goals of this plugin are to support a few things:

1. Auto-Importing of Splitwise Transactions
2. Creation of Splitwise transactions directly from Lunch Money
3. Syncing of Splitwise Account Balance
4. A simple workflow to split transactions in half and mark half as reimbursed

### More info on the [ReadTheDocs](https://lunchable.readthedocs.io/en/latest/splitlunch.html)

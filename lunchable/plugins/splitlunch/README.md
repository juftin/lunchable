# SplitLunch

lunchable integration with Splitwise.

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

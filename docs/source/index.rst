**lunchable**
===================================

**lunchable** is a Python client for the Lunch Money Developer API.
It's built on top of `pydantic <https://github.com/samuelcolvin/pydantic>`_,
and it offers a *simple* and *intuitive* API and Objects.

.. note::

   This project is under active development.

.. code-block:: python

    from typing import List

    from lunchable import LunchMoney
    from lunchable.models import TransactionObject

    lunch = LunchMoney(access_token="xxxxxxxxxxx")
    transactions: List[TransactionObject] = lunch.get_transactions()

    first_transaction: TransactionObject = transactions[0]
    transaction_as_dict: dict = first_transaction.dict()

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   usage.rst
   lunchable.rst
   models.rst
   plugins.rst
   api.rst

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

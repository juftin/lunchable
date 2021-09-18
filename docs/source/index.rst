Lunch Money Python Client
===================================

**lunch-money** is a Python client for the Lunch Money Developer API.
It's built on top of `pydantic <https://github.com/samuelcolvin/pydantic>`_
and requests and offers a *simple* and *intuitive* API.

.. note::

   This project is under active development.

.. code-block:: python

    from typing import List

    from lunchmoney import LunchMoney
    from lunchmoney.models import TransactionsObject

    lunch = LunchMoney()
    transactions: List[TransactionsObject] = lunch.get_transactions()


.. toctree::
   :maxdepth: 1
   :caption: Contents:

   usage.md
   lunchmoney.rst
   models.rst
   plugins.rst

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

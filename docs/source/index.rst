**lunchable**
===================================

.. image:: https://i.imgur.com/FyKDsG3.png
    :width: 400
    :align: center
    :alt: lunchable
    :target: https://github.com/juftin/lunchable

**lunchable** is a Python Client for the
`Lunch Money Developer API <https://lunchmoney.dev>`_.
It's built on top of `pydantic <https://github.com/samuelcolvin/pydantic>`_,
and it offers a *simple* and *intuitive* API.

.. image:: https://img.shields.io/pypi/v/lunchable?color=blue&label=lunchable
    :target: https://github.com/juftin/lunchable
    :alt: Lunchable Version
.. image:: https://img.shields.io/pypi/pyversions/lunchable
    :target: https://pypi.python.org/pypi/lunchable/
    :alt: PyPI
.. image:: https://github.com/juftin/lunchable/actions/workflows/tests.yml/badge.svg?branch=main
    :target: https://github.com/juftin/lunchable/actions/workflows/tests.yml?query=branch%3Amain
    :alt: Testing Status
.. image:: https://img.shields.io/github/license/juftin/lunchable?color=blue&label=License
    :target: https://github.com/juftin/lunchable/blob/main/LICENSE
    :alt: GitHub License
.. image:: https://readthedocs.org/projects/lunchable/badge/?version=latest
    :target: https://lunchable.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status


.. note::

   This project is under active development.

.. code-block:: console

    pip install lunchable

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
   cli.rst
   models.rst
   plugins.rst
   api/modules.rst

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`



.. image:: https://raw.githubusercontent.com/juftin/juftin/main/static/juftin.png
    :width: 60
    :height: 60
    :align: center
    :alt: juftin
    :target: https://github.com/juftin



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
it offers an *intuitive* API, a *simple* CLI,
complete coverage of all endpoints,
and *plugins* to other external services

.. image:: https://img.shields.io/pypi/v/lunchable?color=blue&label=lunchable
    :target: https://github.com/juftin/lunchable
    :alt: Lunchable Version
.. image:: https://img.shields.io/pypi/pyversions/lunchable
    :target: https://pypi.python.org/pypi/lunchable/
    :alt: PyPI
.. image:: https://img.shields.io/docker/v/juftin/lunchable?color=blue&label=docker&logo=docker
    :target: https://hub.docker.com/r/juftin/lunchable
    :alt: Docker
.. image:: https://github.com/juftin/lunchable/actions/workflows/tests.yml/badge.svg?branch=main
    :target: https://github.com/juftin/lunchable/actions/workflows/tests.yml?query=branch%3Amain
    :alt: Testing Status
.. image:: https://img.shields.io/github/license/juftin/lunchable?color=blue&label=License
    :target: https://github.com/juftin/lunchable/blob/main/LICENSE
    :alt: GitHub License
.. image:: https://readthedocs.org/projects/lunchable/badge/?version=latest
    :target: https://lunchable.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

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

.. code-block:: console

    export LUNCHMONEY_ACCESS_TOKEN="xxxxxxxxxxx"
    lunchable transactions get --limit 5

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   usage.rst
   lunchable.rst
   cli.rst
   plugins.rst
   contributing.md
   API Documentation <api/modules.rst>

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

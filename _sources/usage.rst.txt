##################
Usage
##################

******************
Installation
******************

To use lunchable, first install it using pip:

.. code-block:: console

    pip install lunchable

******************
Examples
******************

Read more about :ref:`interacting-with-lunchable` to see what
else you can do.

Transactions
==================

Retrieve a list of :class:`.TransactionObject`
----------------------------------------------------------------------

.. code-block:: python

    from lunchable import LunchMoney

    lunch = LunchMoney(access_token="xxxxxxx")
    transactions = lunch.get_transactions(start_date="2020-01-01",
                                          end_date="2020-01-31")


Retrieve a single transaction (:class:`.TransactionObject`)
----------------------------------------------------------------------

.. code-block:: python

    from lunchable import LunchMoney

    lunch = LunchMoney(access_token="xxxxxxx")
    transaction = lunch.get_transaction(transaction_id=1234)


The above code returns a :class:`.TransactionObject` with ID # 1234 (assuming it exists)

Update a transaction with a :class:`.TransactionUpdateObject`
----------------------------------------------------------------------

.. code-block:: python

    from datetime import datetime

    from lunchable import LunchMoney, TransactionUpdateObject

    lunch = LunchMoney(access_token="xxxxxxx")
    transaction_note = f"Updated on {datetime.now()}"
    notes_update = TransactionUpdateObject(notes=transaction_note)
    response = lunch.update_transaction(transaction_id=1234,
                                        transaction=notes_update)

Update a :class:`.TransactionObject` with itself
----------------------------------------------------------------------

.. code-block:: python

    from datetime import datetime, timedelta

    from lunchable import LunchMoney

    lunch = LunchMoney(access_token="xxxxxxx")
    transaction = lunch.get_transaction(transaction_id=1234)

    transaction.notes = f"Updated on {datetime.now()}"
    transaction.date = transaction.date + timedelta(days=1)
    response = lunch.update_transaction(transaction_id=transaction.id,
                                        transaction=transaction)

Create a new transaction with a :class:`.TransactionInsertObject`
----------------------------------------------------------------------

.. code-block:: python

    from lunchable import LunchMoney, TransactionInsertObject

    lunch = LunchMoney(access_token="xxxxxxx")

    new_transaction = TransactionInsertObject(payee="Example Restaurant",
                                              amount=120.00,
                                              notes="Saturday Dinner")
    new_transaction_ids = lunch.insert_transactions(transactions=new_transaction)

Use the :ref:`Lunchable CLI`
----------------------------

.. code-block:: console

    lunchable transactions get --limit 5

Use the :ref:`Lunchable CLI` via Docker
---------------------------------------

.. code-block:: console

    docker pull juftin/lunchable

.. code-block:: console

    docker run \
        --env LUNCHMONEY_ACCESS_TOKEN=${LUNCHMONEY_ACCESS_TOKEN} \
        juftin/lunchable:latest \
        lunchable transactions get --limit 5

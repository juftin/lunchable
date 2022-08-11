###########################################
PushLunch: Push Notifications via Pushover
###########################################

|pic1| |pic2|

.. |pic1| image:: https://pushover.net/images/pushover-logo.svg
   :width: 35%
   :alt: pushover
   :target: https://www.splitwise.com/

.. |pic2| image:: https://i.imgur.com/FyKDsG3.png
   :width: 60%
   :alt: lunchable
   :target: https://github.com/juftin/lunchable

--------

`PushLunch` supports Push Notifications via `Pushover <https://pushover.net>`_. Pushover
supports iOS and Android Push notifications. To get started just provide your Pushover
`User Key` directly or via the `PUSHOVER_USER_KEY` environment variable.


Run via the :ref:`Lunchable CLI`
================================

The below command checks for un-reviewed transactions in the current period and
sends them as Push Notifications. The `--continuous` flag tells it to run forever which
will only send you a push notifaction once for each transaction.
By default it will check every 60 minutes, but this can be changed using the `--interval`
argument.

.. code-block:: console

    lunchable plugins pushlunch notify --continuous

Run via Docker
===============

.. code-block:: console

    docker run --rm \
        --env LUNCHMONEY_ACCESS_TOKEN=${LUNCHMONEY_ACCESS_TOKEN} \
        --env PUSHOVER_USER_KEY=${PUSHOVER_USER_KEY} \
        juftin/lunchable:latest \
        lunchable plugins pushlunch notify --continuous

Run via Python
===============

.. currentmodule:: lunchable.plugins.pushlunch

.. autoclass:: PushLunch
    :members:
    :autosummary:
        :toctree: _autosummary

##################
Lunchable CLI
##################

.. code-block:: console

    Usage: lunchable [OPTIONS] COMMAND [ARGS]...

      Interactions with Lunch Money via lunchable 🍱

    Options:
      --version             Show the version and exit.
      --access-token TEXT   LunchMoney Developer API Access Token
      --debug / --no-debug  Enable extra debugging output
      --help                Show this message and exit.

    Commands:
      http          Interact with the LunchMoney API
      plugins       Interact with Lunchable Plugins
      transactions  Interact with Lunch Money transactions

******************
Installation
******************

To use lunchable on the command line, first install it using `pip <https://pypi.org/project/lunchable/>`_ or
`pipx <https://pypa.github.io/pipx/>`_:

.. code-block:: console

    pip install lunchable


or, if you're using the Splitwise plugin on the CLI:

.. code-block:: console

    pip install "lunchable[splitwise]"

Install Shell Completion
=========================


bash
###################

.. code-block:: console

    _LUNCHABLE_COMPLETE=bash_source lunchable > ~/.lunchable-complete.bash
    echo "[[ ! -f ~/.lunchable-complete.bash ]] || source ~/.lunchable-complete.bash" >> ~/.bashrc

zsh
###################

.. code-block:: console

    _LUNCHABLE_COMPLETE=zsh_source lunchable > ~/.lunchable-complete.zsh
    echo "[[ ! -f ~/.lunchable-complete.zsh ]] || source ~/.lunchable-complete.zsh" >> ~/.zshrc

Run via Docker
==============

.. code-block:: console

    docker pull juftin/lunchable

.. code-block:: console

    docker run \
        --env LUNCHMONEY_ACCESS_TOKEN=${LUNCHMONEY_ACCESS_TOKEN} \
        juftin/lunchable:latest \
        lunchable transactions get --limit 5

******************
Examples
******************

.. code-block:: console

    pip install --upgrade lunchable
    export LUNCHMONEY_ACCESS_TOKEN="xxxxxxxxxxx"

.. code-block:: console

    lunchable http /v1/me

.. code-block:: json

    {
      "user_name": "Justin Flannery",
      "user_email": "Justin@example.com",
      "user_id": 99999,
      "account_id": 99999,
      "budget_name": "🤖 Justin",
      "api_key_label": "Testing"
    }

.. code-block:: console

    lunchable http -X GET https://dev.lunchmoney.app/v1/assets

.. code-block:: json

    {
      "assets": [
        {
          "id": 99999,
          "type_name": "cash",
          "subtype_name": "digital wallet (paypal, venmo)",
          "name": "Test Account",
          "display_name": "Test Account",
          "balance": "190.2100",
          "balance_as_of": "2022-04-23T07:23:20.000Z",
          "closed_on": "2022-04-23",
          "currency": "usd",
          "institution_name": "Test",
          "exclude_transactions": true,
          "created_at": "2021-09-20T05:32:29.060Z"
        }
      ]
    }

.. code-block:: console

    lunchable http -X PUT /v1/assets/99999 --data '{"balance": 200.00}'

.. code-block:: json

    {
      "id": 99999,
      "type_name": "cash",
      "subtype_name": "digital wallet (paypal, venmo)",
      "name": "Test Account",
      "display_name": "Test Account",
      "balance": "200.0000",
      "balance_as_of": "2022-10-21T04:22:50.391Z",
      "closed_on": "2022-04-23",
      "currency": "usd",
      "institution_name": "Test",
      "exclude_transactions": true,
      "created_at": "2021-09-20T05:32:29.060Z"
    }

.. code-block:: console

    lunchable transactions get --limit 1 --start-date 2022-09-07 --end-date 2022-09-15 | jq

.. code-block:: json

    [
      {
        "id": 120998527,
        "date": "2022-09-07",
        "payee": "Ally Bank",
        "amount": -87.5,
        "currency": "usd",
        "notes": "ATCO Transfer",
        "category_id": 229148,
        "asset_id": null,
        "plaid_account_id": 41573,
        "status": "cleared",
        "parent_id": null,
        "is_group": false,
        "group_id": null,
        "tags": null,
        "external_id": null,
        "original_name": "Internet transfer from Interest Checking account XXXXXX2045",
        "type": null,
        "subtype": null,
        "fees": null,
        "price": null,
        "quantity": null
      }
    ]

******************
Documentation
******************

.. click:: lunchable._cli:cli
   :prog: lunchable
   :nested: full

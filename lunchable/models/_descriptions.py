"""
Descriptions for LunchMoney Data Models

This file contains descriptions for the data models used in the LunchMoney API.
Descriptions are seperated into a separate module to keep the code clean and
readable.
"""


class _AssetsDescriptions:
    """
    Descriptions for Assets
    """

    type_name = """
    Primary type of the asset. Must be one of: [employee compensation, cash, vehicle, loan,
    cryptocurrency, investment, other, credit, real estate]
    """
    subtype_name = """
    Optional asset subtype. Examples include: [retirement, checking, savings, prepaid credit card]
    """
    balance = """
    Current balance of the asset in numeric format to 4 decimal places"
    """
    balance_as_of = """
    Date/time the balance was last updated in ISO 8601 extended format
    """
    closed_on = """
    The date this asset was closed (optional)
    """
    currency = """
    Three-letter lowercase currency code of the balance in ISO 4217 format
    """
    created_at = """
    Date/time the asset was created in ISO 8601 extended format
    """
    exclude_transactions = """
    If true, this asset will not show up as an option for assignment when
    creating transactions manually
    """


class _BudgetDescriptions:
    """
    Descriptions for Budget
    """

    category_group_name = "Name of the category group, if applicable"
    is_income = """
    If true, this category is an income category (category properties
    are set in the app via the Categories page)
    """
    exclude_from_budget = """
    If true, this category is excluded from budget (category
    properties are set in the app via the Categories page)
    """
    exclude_from_totals = """
    If true, this category is excluded from totals (category
    properties are set in the app via the Categories page)
    """
    data = """
    For each month with budget or category spending data, there is a data object with the key
    set to the month in format YYYY-MM-DD. For properties, see Data object below.
    """
    config = """
    Object representing the category's budget suggestion configuration
    """


class _CategoriesDescriptions:
    """
    Descriptions for Categories
    """

    name = """
    The name of the category. Must be between 1 and 40 characters.
    """
    description = """
    The description of the category. Must not exceed 140 characters.
    """
    is_income = """
    If true, the transactions in this category will be treated as income.
    """
    exclude_from_budget = """
    If true, the transactions in this category will be excluded from the budget.
    """
    exclude_from_totals = """
    If true, the transactions in this category will be excluded from totals.
    """
    updated_at = """
    The date and time of when the category was last updated (in the ISO
    8601 extended format).
    """
    created_at = """
    The date and time of when the category was created (in the ISO 8601
    extended format).
    """
    is_group = """
    If true, the category is a group that can be a parent to other
    categories.
    """
    group_id = """
    The ID of a category group (or null if the category doesn't belong to
    a category group).
    """
    children = """
    For category groups, this will populate with the categories nested
    within and include id, name, description and created_at fields.
    """
    archived = """
    If true, the category is archived and not displayed in relevant
    areas of the Lunch Money app.
    """
    archived_on = """
    The date and time of when the category was last archived
    (in the ISO 8601 extended format).
    """
    order = """
    Numerical ordering of categories
    """


class _CryptoDescriptions:
    """
    Descriptions for Crypto
    """

    id = """
    Unique identifier for a manual crypto account (no ID for synced accounts)
    """
    zabo_account_id = """
    Unique identifier for a synced crypto account (no ID for manual accounts,
    multiple currencies may have the same zabo_account_id)
    """
    source = """
    `synced` (this account is synced via a wallet, exchange, etc.) or `manual` (this account
    balance is managed manually)
    """
    display_name = "Display name of the crypto asset (as set by user)"
    balance_as_of = """
    Date/time the balance was last updated in ISO 8601 extended format
    """
    status = """
    The current status of the crypto account. Either active or in error.
    """
    created_at = """
    Date/time the asset was created in ISO 8601 extended format
    """


class _PlaidAccountDescriptions:
    """
    Descriptions for Plaid Accounts
    """

    date_linked = """
    Date account was first linked in ISO 8601 extended format
    """
    name = """
    Name of the account. Can be overridden by the user. Field is originally set by Plaid
    """
    type = """
    Primary type of account. Typically one of: [credit, depository, brokerage, cash,
    loan, investment]. This field is set by Plaid and cannot be altered.
    """
    subtype = """
    Optional subtype name of account. This field is set by Plaid and cannot be altered
    """
    mask = """
    Mask (last 3 to 4 digits of account) of account. This field is set by
    Plaid and cannot be altered
    """
    institution_name = """
    Name of institution associated with account. This field is set by
    Plaid and cannot be altered
    """
    status = """
    Denotes the current status of the account within Lunch Money. Must be one of:
    active (Account is active and in good state),
    inactive (Account marked inactive from user. No transactions fetched or
    balance update for this account),
    relink (Account needs to be relinked with Plaid),
    syncing (Account is awaiting first import of transactions),
    error (Account is in error with Plaid),
    not found (Account is in error with Plaid),
    not supported (Account is in error with Plaid)
    """
    last_import = """
    Date of last imported transaction in ISO 8601 extended format (not necessarily
    date of last attempted import)
    """
    balance = """
    Current balance of the account in numeric format to 4 decimal places. This field is
    set by Plaid and cannot be altered
    """
    currency = """
    Currency of account balance in ISO 4217 format. This field is set by Plaid
    and cannot be altered
    """
    balance_last_update = """
    Date balance was last updated in ISO 8601 extended format. This field is set
    by Plaid and cannot be altered
    """
    limit = """
    Optional credit limit of the account. This field is set by Plaid and cannot be altered
    """


class _RecurringExpensesDescriptions:
    """
    Descriptions for Recurring Expenses
    """

    id = """
    Unique identifier for recurring expense
    """
    start_date = """
    Denotes when recurring expense starts occurring in ISO 8601 format.
    If null, then this recurring expense will show up for all time
    before end_date
    """
    end_date = """
    Denotes when recurring expense stops occurring in ISO 8601 format.
    If null, then this recurring expense has no set end date and will
    show up for all months after start_date
    """
    cadence = """
    One of: [monthly, twice a month, once a week, every 3 months, every 4 months,
    twice a year, yearly]
    """
    amount = """
    Amount of the recurring expense in numeric format to 4 decimal places
    """
    currency = """
    Three-letter lowercase currency code for the recurring expense in ISO 4217 format
    """
    description = """
    If any, represents the user-entered description of the recurring expense
    """
    billing_date = """
    Expected billing date for this recurring expense for this month in ISO 8601 format
    """
    type = """
    This can be one of two values: cleared (The recurring expense has been reviewed
    by the user), suggested (The recurring expense is suggested by the system;
    the user has yet to review/clear it)
    """
    original_name = """
    If any, represents the original name of the recurring expense as
    denoted by the transaction that triggered its creation
    """
    source = """
    This can be one of three values: manual (User created this recurring expense
    manually from the Recurring Expenses page), transaction (User created this by
    converting a transaction from the Transactions page), system (Recurring expense
    was created by the system on transaction import). Some older recurring expenses
    may not have a source.
    """
    plaid_account_id = """
    If any, denotes the plaid account associated with the creation of this "
    recurring expense (see Plaid Accounts)
    """
    asset_id = """
    If any, denotes the manually-managed account (i.e. asset) associated with the
    creation of this recurring expense (see Assets)
    """
    transaction_id = """
    If any, denotes the unique identifier for the associated transaction matching
    this recurring expense for the current time period
    """
    category_id = """
    If any, denotes the unique identifier for the associated category to this recurring expense
    """


class _TransactionInsertDescriptions:
    """
    Descriptions for TransactionInsertObject
    """

    date = """
    Must be in ISO 8601 format (YYYY-MM-DD).
    """
    amount = """
    Numeric value of amount. i.e. $4.25 should be denoted as 4.25.
    """
    category_id = """
    Unique identifier for associated category_id. Category must be associated with
    the same account and must not be a category group.
    """
    currency = """
    Three-letter lowercase currency code in ISO 4217 format. The code sent must exist
    in our database. Defaults to user account's primary currency.
    """
    asset_id = """
    Unique identifier for associated asset (manually-managed account). Asset must be
    associated with the same account.
    """
    recurring_id = """
    Unique identifier for associated recurring expense. Recurring expense must be associated
    with the same account.
    """
    status = """
    Must be either cleared or uncleared. If recurring_id is provided, the status will
    automatically be set to recurring or recurring_suggested depending on the type of
    recurring_id. Defaults to uncleared.
    """
    external_id = """
    User-defined external ID for transaction. Max 75 characters. External IDs must be
    unique within the same asset_id.
    """
    tags = """
    Passing in a number will attempt to match by ID. If no matching tag ID is found, an error
    will be thrown. Passing in a string will attempt to match by string. If no matching tag
    name is found, a new tag will be created.
    """


class _TransactionUpdateDescriptions:
    """
    Descriptions for TransactionUpdateObject
    """

    date = """
    Must be in ISO 8601 format (YYYY-MM-DD).
    """
    category_id = """
    Unique identifier for associated category_id. Category must be associated
    with the same account and must not be a category group.
    """
    amount = """
    You may only update this if this transaction was not created from an automatic
    import, i.e. if this transaction is not associated with a plaid_account_id
    """
    currency = """
    You may only update this if this transaction was not created from an automatic
    import, i.e. if this transaction is not associated with a plaid_account_id.
    Defaults to user account's primary currency.
    """
    asset_id = """
    Unique identifier for associated asset (manually-managed account). Asset must be
    associated with the same account. You may only update this if this transaction was
    not created from an automatic import, i.e. if this transaction is not associated
    with a plaid_account_id
    """
    recurring_id = """
    Unique identifier for associated recurring expense. Recurring expense must
    be associated with the same account.
    """
    status = """
    Must be either cleared or uncleared. Defaults to uncleared If recurring_id is
    provided, the status will automatically be set to recurring or recurring_suggested
    depending on the type of recurring_id. Defaults to uncleared.
    """
    external_id = """
    User-defined external ID for transaction. Max 75 characters. External IDs must be
    unique within the same asset_id. You may only update this if this transaction was
    not created from an automatic import, i.e. if this transaction is not associated
    with a plaid_account_id
    """
    tags = """
    Passing in a number will attempt to match by ID. If no matching tag ID is found,
    an error will be thrown. Passing in a string will attempt to match by string.
    If no matching tag name is found, a new tag will be created.
    """


class _TransactionSplitDescriptions:
    """
    Descriptions for TransactionSplitObject
    """

    date = "Must be in ISO 8601 format (YYYY-MM-DD)."
    category_id = """
    Unique identifier for associated category_id. Category must be associated
    with the same account.
    """
    notes = "Transaction Split Notes."
    amount = """
    Individual amount of split. Currency will inherit from parent transaction. All
    amounts must sum up to parent transaction amount.
    """


class _TransactionDescriptions:
    """
    Descriptions for TransactionObject
    """

    amount = """
    Amount of the transaction in numeric format to 4 decimal places
    """
    payee = """
    Name of payee If recurring_id is not null, this field will show the payee
    of associated recurring expense instead of the original transaction payee
    """
    currency = """
    Three-letter lowercase currency code of the transaction in ISO 4217 format
    """
    notes = """
    User-entered transaction notes If recurring_id is not null, this field will
    be description of associated recurring expense
    """
    category_id = """
    Unique identifier of associated category (see Categories)
    """
    asset_id = """
    Unique identifier of associated manually-managed account (see Assets)
    Note: plaid_account_id and asset_id cannot both exist for a transaction
    """
    plaid_account_id = """
    Unique identifier of associated Plaid account (see Plaid Accounts) Note:
    plaid_account_id and asset_id cannot both exist for a transaction
    """
    status = """
    One of the following: cleared: User has reviewed the transaction | uncleared:
    User has not yet reviewed the transaction | recurring: Transaction is linked
    to a recurring expense | recurring_suggested: Transaction is listed as a
    suggested transaction for an existing recurring expense | pending: Imported
    transaction is marked as pending. This should be a temporary state. User intervention
    is required to change this to recurring.
    """
    parent_id = """
    Exists if this is a split transaction. Denotes the transaction ID of the original
    transaction. Note that the parent transaction is not returned in this call.
    """
    is_group = """
    True if this transaction represents a group of transactions. If so, amount
    and currency represent the totalled amount of transactions bearing this
    transaction's id as their group_id. Amount is calculated based on the
    user's primary currency.
    """
    group_id = """
    Exists if this transaction is part of a group. Denotes the parent's transaction ID
    """
    external_id = """
    User-defined external ID for any manually-entered or imported transaction.
    External ID cannot be accessed or changed for Plaid-imported transactions.
    External ID must be unique by asset_id. Max 75 characters.
    """
    original_name = """
    The transactions original name before any payee name updates. For synced transactions,
    this is the raw original payee name from your bank.
    """
    type = """
    (for synced investment transactions only) The transaction type as set by
    Plaid for investment transactions. Possible values include: buy, sell, cash,
    transfer and more
    """
    subtype = """
    (for synced investment transactions only) The transaction type as set by Plaid
    for investment transactions. Possible values include: management fee, withdrawal,
    dividend, deposit and more
    """
    fees = """
    (for synced investment transactions only) The fees as set by Plaid for investment
    transactions.
    """
    price = """
    (for synced investment transactions only) The price as set by Plaid for investment
    transactions.
    """
    quantity = """
    (for synced investment transactions only) The quantity as set by Plaid for investment
    transactions.
    """
    to_base = """
    The amount converted to the user's primary currency. If the multicurrency
    feature is not being used, to_base and amount will be the same.
    """

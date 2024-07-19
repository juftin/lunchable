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


class _SummarizedTransactionDescriptions:
    """
    Descriptions for Summarized Transaction
    """

    id = """
    Unique identifier for the transaction that matched this recurring item
    """
    date = """
    Date of transaction in ISO 8601 format
    """
    amount = """
    Amount of the transaction in numeric format to 4 decimal places
    """
    currency = """
    Three-letter lowercase currency code of the transaction in ISO 4217 format
    """
    payee = """
    Payee or payer of the recurring item
    """
    category_id = """
    Unique identifier of associated category
    """
    recurring_id = """
    Unique identifier of associated recurring item
    """
    to_base = """
    The amount converted to the user's primary currency. If the multicurrency
    feature is not being used, to_base and amount will be the same.
    """


class _RecurringItemsDescriptions:
    """
    Descriptions for Recurring Items
    """

    id = """
    Unique identifier for recurring item
    """
    start_date = """
    Denotes when recurring item starts occurring in ISO 8601 format.
    If null, then this recurring item will show up for all time before end_date
    """
    end_date = """
    Denotes when recurring item stops occurring in ISO 8601 format.
    If null, then this recurring item has no set end date and will
    show up for all months after start_date
    """
    payee = """
    Payee or payer of the recurring item
    """
    currency = """
    Three-letter lowercase currency code for the recurring item in ISO 4217 format
    """
    created_by = """
    The id of the user who created this recurring item.
    """
    created_at = """
    The date and time of when the recurring item was created (in the ISO 8601
    extended format).
    """
    updated_at = """
    The date and time of when the recurring item was updated (in the ISO 8601 extended format).
    """
    billing_date = """
    Initial date that a transaction associated with this recurring item occured.
    This date is used in conjunction with values of quantity and granularity to
    determine the expected dates of recurring transactions in the period.
    """
    original_name = """
    If any, represents the original name of the recurring item as denoted by
    the transaction that triggered its creation
    """
    description = """
    If any, represents the user-entered description of the recurring item
    """
    plaid_account_id = """
    If any, denotes the plaid account associated with the creation of this
    recurring item (see Plaid Accounts)
    """
    asset_id = """
    If any, denotes the manually-managed account (i.e. asset) associated
    with the creation of this recurring item (see Assets)
    """
    source = """
    This can be one of four values:
    - manual: User created this recurring item manually from the Recurring Items page
    - transaction: User created this by converting a transaction from the Transactions page
    - system: Recurring item was created by the system on transaction import
    - null: Some older recurring items may not have a source.
    """
    notes = """
    If any, the user-entered notes for the recurring item
    """
    amount = """
    Amount of the recurring item in numeric format to 4 decimal places.
    For recurring items with flexible amounts, this is the average of the
    specified min and max amounts.
    """
    category_id = """
    If any, denotes the unique identifier for the associated category to this recurring item
    """
    category_group_id = """
    If any, denotes the unique identifier of associated category group
    """
    is_income = """
    Based on the associated category's property, denotes if the recurring transaction
    is treated as income
    """
    exclude_from_totals = """
    Based on the associated category's property, denotes if the recurring transaction is excluded from totals
    """
    granularity = """
    The unit of time used to define the cadence of the recurring item.
    One of `weeks`, `months`, `years`
    """
    quantity = """
    The number of granular units between each occurrence
    """
    occurrences = """
    An object which contains dates as keys and lists as values. The dates will
    include all the dates in the month that a recurring item is expected, as well
    as the last date in the previous period and the first date in the next period.
    The value for each key is a list of Summarized Transaction Objects that matched
    the recurring item for that date (if any)
    """
    transactions_within_range = """
    A list of all the Summarized Transaction Objects for transactions that that
    have occurred in the query month for the recurring item (if any)
    """
    missing_dates_within_range = """
    A list of date strings when a recurring transaction is expected but has not (yet) occurred.
    """
    date = """
    Denotes the value of the start_date query parameter, or if none was provided, the date when
    the request was made. This indicates the month used by the system when populating the response.
    """
    to_base = """
    The amount converted to the user's primary currency. If the multicurrency feature is not being
    used, to_base and amount will be the same.
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

    id = """
    Unique identifier for transaction
    """
    date = """
    Date of transaction in ISO 8601 format
    """
    payee = """
    Name of payee. If recurring_id is not null, this field will show the payee
    of associated recurring expense instead of the original transaction payee
    """
    amount = """
    Amount of the transaction in numeric format to 4 decimal places
    """
    currency = """
    Three-letter lowercase currency code of the transaction in ISO 4217 format
    """
    to_base = """
    The amount converted to the user's primary currency. If the multicurrency
    feature is not being used, to_base and amount will be the same.
    """
    category_id = """
    Unique identifier of associated category
    """
    category_name = """
    Name of category associated with transaction
    """
    category_group_id = """
    Unique identifier of associated category group, if any
    """
    category_group_name = """
    Name of category group associated with transaction, if any
    """
    is_income = """
    Based on the associated category's property, denotes if transaction is
    treated as income
    """
    exclude_from_budget = """
    Based on the associated category's property, denotes if transaction is
    excluded from budget
    """
    exclude_from_totals = """
    Based on the associated category's property, denotes if transaction is
    excluded from totals
    """
    created_at = """
    The date and time of when the transaction was created (in the ISO 8601
    extended format).
    """
    updated_at = """
    The date and time of when the transaction was last updated (in the ISO 8601
    extended format).
    """
    status = """
    One of the following: <ul>
        <li>cleared: User has reviewed the transaction</li>
        <li>uncleared: User has not yet reviewed the transaction</li>
        <li>recurring: Transaction is linked to a recurring expense</li>
        <li>recurring_suggested: Transaction is listed as a suggested transaction
            for an existing recurring expense.</li>
        <li>pending: Imported transaction is marked as pending. This should be a
            temporary state.</li>
    </ul>
    User intervention is required to change this to recurring.
    """
    is_pending = """
    Denotes if transaction is pending (not posted)
    """
    notes = """
    User-entered transaction notes If recurring_id is not null, this field will
    be description of associated recurring expense
    """
    original_name = """
    The transactions original name before any payee name updates. For synced
    transactions, this is the raw original payee name from your bank.
    """
    recurring_id = """
    Unique identifier of associated recurring item
    """
    recurring_payee = """
    Payee name of associated recurring item
    """
    recurring_description = """
    Description of associated recurring item
    """
    recurring_cadence = """
    Cadence of associated recurring item (one of `once a week`, `every 2 weeks`,
    `twice a month`, `monthly`, `every 2 months`, `every 3 months`, `every 4 months`,
    `twice a year`, `yearly`)
    """
    recurring_type = """
    Type of associated recurring (one of `cleared`, `suggested`, `dismissed`)
    """
    recurring_amount = """
    Amount of associated recurring item
    """
    recurring_currency = """
    Currency of associated recurring item
    """
    parent_id = """
    Exists if this is a split transaction. Denotes the transaction ID of the
    original transaction. Note that the parent transaction is not returned in
    this call.
    """
    has_children = """
    True if this transaction is a parent transaction and is split into 2 or
    more other transactions
    """
    group_id = """
    Exists if this transaction is part of a group. Denotes the parent’s
    transaction ID
    """
    is_group = """
    True if this transaction represents a group of transactions. If so, amount
    and currency represent the totalled amount of transactions bearing this
    transaction’s id as their group_id. Amount is calculated based on the
    user’s primary currency.
    """
    asset_id = """
    Unique identifier of associated manually-managed account (see Assets)
    Note: plaid_account_id and asset_id cannot both exist for a transaction
    """
    asset_institution_name = """
    Institution name of associated manually-managed account
    """
    asset_name = """
    Name of associated manually-managed account
    """
    asset_display_name = """
    Display name of associated manually-managed account
    """
    asset_status = """
    Status of associated manually-managed account (one of `active`, `closed`)
    """
    plaid_account_id = """
    Unique identifier of associated Plaid account (see Plaid Accounts) Note:
    plaid_account_id and asset_id cannot both exist for a transaction
    """
    plaid_account_name = """
    Name of associated Plaid account
    """
    plaid_account_mask = """
    Mask of associated Plaid account
    """
    institution_name = """
    Institution name of associated Plaid account
    """
    plaid_account_display_name = """
    Display name of associated Plaid account
    """
    plaid_metadata = """
    Metadata associated with imported transaction from Plaid
    """
    source = """
    Source of the transaction (one of `api`, `csv`, `manual`,`merge`,`plaid`,
    `recurring`,`rule`,`user`)
    """
    display_name = """
    Display name for payee for transaction based on whether or not it is
    linked to a recurring item. If linked, returns `recurring_payee` field.
    Otherwise, returns the `payee` field.
    """
    display_notes = """
    Display notes for transaction based on whether or not it is linked to a
    recurring item. If linked, returns `recurring_notes` field. Otherwise,
    returns the `notes` field.
    """
    account_display_name = """
    Display name for associated account (manual or Plaid). If this is a synced
    account, returns `plaid_account_display_name` or `asset_display_name`.
    """
    tags = """
    Array of Tag objects
    """
    external_id = """
    User-defined external ID for any manually-entered or imported transaction.
    External ID cannot be accessed or changed for Plaid-imported transactions.
    External ID must be unique by asset_id. Max 75 characters.
    """
    children = """
    Array of Transaction objects. Only exists if this transaction is a parent
    transaction and is split into 2 or more other transactions. Child transactions
    do not contain all of the same fields as parent transactions.
    """
    formatted_date = """
    Date of transaction in user's preferred format
    """

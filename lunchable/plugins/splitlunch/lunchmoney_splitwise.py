"""
Lunchable Plugin for Splitwise
"""

import datetime
import logging
from math import floor
from os import getenv
from random import shuffle
from textwrap import dedent
from typing import Any, Dict, List, Optional, Tuple, Union

from lunchable import __lunchable__, LunchMoney
from lunchable.exceptions import LunchMoneyImportError
from lunchable.models import (AssetsObject, CategoriesObject,
                              TagsObject, TransactionInsertObject,
                              TransactionObject, TransactionSplitObject,
                              TransactionUpdateObject)
from lunchable.plugins.splitlunch._config import SplitLunchConfig
from lunchable.plugins.splitlunch.exceptions import SplitLunchError
from lunchable.plugins.splitlunch.models import SplitLunchExpense

logger = logging.getLogger(__name__)

try:
    import splitwise  # type: ignore
    from dateutil.tz import tzlocal
except ImportError as ie:
    logger.exception(ie)
    _pip_extra_error = ("Looks like you don't have the Splitwise plugin installed: "
                        f"`pip install {__lunchable__}[splitlunch]`")
    raise LunchMoneyImportError(_pip_extra_error)


class SplitLunch(splitwise.Splitwise):
    """
    Lunchable Plugin For Interacting With Splitwise

    This plugin supports different operations, and some of those operations
    have prerequisites:

    1) It supports the auto-importing of Splitwise expenses into Lunch Money
    transactions. This requires a manual asset exist in your Lunch Money
    account with "Splitwise" in the Name.

        Prerequisites:
           - Accounts:
                - Splitwise must be in the account name

    2) It supports the creation of Splitwise transactions directly from synced Lunch Money
    accounts. This syncing requires you create a tag called `SplitLunchImport`. Transactions
    with this tag will be created in Splitwise with your "financial partner". Once transactions
    are created in Splitwise they will be split in half in Lunch Money. Half of the split will be
    marked in the `Reimbursement` category which must be created.

        Prerequisites:
           - Financial Partners:
                - If you only have one friend in Splitwise, this is your Financial Partner
                - Financial Partners must be specified by their Splitwise ID or Email Address
           - Tags:
                - `SplitLunchImport`
           - Categories:
                - `Reimbursement`

    3) It supports a workflow where you mark transactions as split (identical to scenario #2)
    without importing them into Splitwise. This syncing requires you create a tag
    called `SplitLunch` and a category named `Reimbursement`

        Prerequisites:
           - Tags:
                - `SplitLunch`
           - Categories:
                - `Reimbursement`

    4) It supports a workflow where you mark transactions as `Reimbursed` and import them to
    Splitwise with the total completely owed by your financial partner.

        Prerequisites:
           - Financial Partners:
                - If you only have one friend in Splitwise, this is your Financial Partner
                - Financial Partners must be specified by their Splitwise ID or Email Address
           - Tags:
                - `SplitLunchDirectImport`
           - Categories:
                - `Reimbursement`

    Parameters
    ----------
    financial_partner_id: Optional[int]
        Splitwise User ID of financial partner
    financial_partner_email: Optional[str]
        Splitwise linked email address of financial partner
    consumer_key: Optional[str]
        Consumer Key provided by Splitwise. Defaults to `SPLITWISE_CONSUMER_KEY` environment
        variable
    consumer_secret: Optional[str]
        Consumer Key provided by Splitwise. Defaults to `SPLITWISE_CONSUMER_SECRET`
        environment variable
    api_key: Optional[str]
        Consumer Key provided by Splitwise. Defaults to `SPLITWISE_API_KEY` environment
        variable.
    lunchable_client: LunchMoney
        Instantiated LunchMoney object to use as internal client. One will
        be created using environment variables otherwise.
    """

    def __init__(self,
                 lunch_money_access_token: Optional[str] = None,
                 financial_partner_id: Optional[int] = None,
                 financial_partner_email: Optional[str] = None,
                 consumer_key: Optional[str] = None,
                 consumer_secret: Optional[str] = None,
                 api_key: Optional[str] = None,
                 lunchable_client: Optional[LunchMoney] = None,
                 ):
        """
        Initialize the Parent Class with some additional properties

        Parameters
        ----------
        financial_partner_id: Optional[int]
            Splitwise User ID of financial partner
        financial_partner_email: Optional[str]
            Splitwise linked email address of financial partner
        consumer_key: Optional[str]
            Consumer Key provided by Splitwise. Defaults to `SPLITWISE_CONSUMER_KEY` environment
            variable
        consumer_secret: Optional[str]
            Consumer Key provided by Splitwise. Defaults to `SPLITWISE_CONSUMER_SECRET`
            environment variable
        api_key: Optional[str]
            Consumer Key provided by Splitwise. Defaults to `SPLITWISE_API_KEY` environment
            variable.
        lunch_money_access_token: Optional[str]
            Lunch Money Access Token. Will be inherited from `LUNCHMONEY_ACCESS_TOKEN`
            environment variable if not provided.
        lunchable_client: LunchMoney
            Instantiated LunchMoney object to use as internal client. One will
            be created using environment variables otherwise.
        """
        init_kwargs = self._get_splitwise_init_kwargs(consumer_key=consumer_key,
                                                      consumer_secret=consumer_secret,
                                                      api_key=api_key)
        super(SplitLunch, self).__init__(**init_kwargs)
        self.current_user: splitwise.CurrentUser = self.getCurrentUser()
        self.financial_partner: splitwise.Friend = self.get_friend(
            friend_id=financial_partner_id,
            email_address=financial_partner_email)
        self.last_check: Optional[datetime.datetime] = None
        self.lunchable = LunchMoney(access_token=lunch_money_access_token) if \
            lunchable_client is None else lunchable_client
        self._none_tag = TagsObject(id=0, name="SplitLunchPlaceholder")
        self.splitwise_tag = self._none_tag.copy()
        self.splitlunch_tag = self._none_tag.copy()
        self.splitlunch_import_tag = self._none_tag.copy()
        self.splitlunch_direct_import_tag = self._none_tag.copy()
        self._get_splitwise_tags()
        self.earliest_start_date = datetime.date(1812, 1, 1)
        today = datetime.date.today()
        self.latest_end_date = datetime.date(today.year + 10, 12, 31)
        self.splitwise_asset = self._get_splitwise_asset()
        self.reimbursement_category = self._get_reimbursement_category()

    def __repr__(self):
        """
        String Representation

        Returns
        -------
        str
        """
        return f"<Splitwise: {self.current_user.email}>"

    @classmethod
    def _split_amount(cls, amount: float, splits: int) -> Tuple[float, ...]:
        """
        Split a money amount into fair shares

        Parameters
        ----------
        amount: float
        splits: int

        Returns
        -------
        Tuple[float]
        """
        try:
            assert amount == round(amount, 2)
        except AssertionError:
            raise SplitLunchError(f"{amount} caused an error, you must provide a real "
                                  "spending amount.")
        equal_shares = round(amount, 2) / splits
        remainder_dollars = floor(equal_shares)
        remainder_cents = floor((equal_shares - remainder_dollars) * 100) / 100
        remainder_left = round(
            (equal_shares - remainder_dollars - remainder_cents) * splits * 100, 0)
        owed_amount = remainder_dollars + remainder_cents
        return_amounts = [owed_amount for _ in range(splits)]
        for i in range(int(remainder_left)):
            return_amounts[i] += 0.010
        shuffle(return_amounts)
        return tuple([round(item, 2) for item in return_amounts])

    @classmethod
    def split_a_transaction(cls, amount: Union[float, int]) -> Tuple[float, ...]:
        """
        Split a Transaction into Two

        Split a bill into a tuple of two amounts (and take care
        of the extra penny if needed)

        Parameters
        ----------
        amount: A Currency amount (no more precise than cents)

        Returns
        -------
        tuple
            A tuple is returned with each participant's amount
        """
        amounts_due = cls._split_amount(amount=amount, splits=2)
        return amounts_due

    def create_self_paid_expense(self, amount: float, description: str) -> SplitLunchExpense:
        """
        Create and Submit a Splitwise Expense

        Parameters
        ----------
        amount: float
            Transaction Amount
        description: str
            Transaction Description

        Returns
        -------
        Expense
        """
        # CREATE THE NEW EXPENSE OBJECT
        new_expense = splitwise.Expense()
        new_expense.setDescription(desc=description)
        # GET AND SET AMOUNTS OWED
        primary_user_owes, financial_partner_owes = self.split_a_transaction(amount=amount)
        new_expense.setCost(cost=amount)
        # CONFIGURE PRIMARY USER
        primary_user = splitwise.user.ExpenseUser()
        primary_user.setId(id=self.current_user.id)
        primary_user.setPaidShare(paid_share=amount)
        primary_user.setOwedShare(owed_share=primary_user_owes)
        # CONFIGURE SECONDARY USER
        financial_partner = splitwise.user.ExpenseUser()
        financial_partner.setId(id=self.financial_partner.id)
        financial_partner.setPaidShare(paid_share=0.00)
        financial_partner.setOwedShare(owed_share=financial_partner_owes)
        # ADD USERS AND REPAYMENTS TO EXPENSE
        new_expense.addUser(user=primary_user)
        new_expense.addUser(user=financial_partner)
        # SUBMIT THE EXPENSE AND GET THE RESPONSE
        expense_response: splitwise.Expense
        expense_response, expense_errors = self.createExpense(expense=new_expense)
        try:
            assert expense_errors is None
        except AssertionError:
            raise SplitLunchError(expense_errors["base"][0])
        logger.info("Expense Created: %s", expense_response.id)
        message = f"Created via SplitLunch: {datetime.datetime.now()}"
        self.createComment(expense_id=expense_response.id, content=message)
        pydantic_response = self.splitwise_to_pydantic(expense=expense_response)
        return pydantic_response

    def create_expense_on_behalf_of_partner(self, amount: float,
                                            description: str) -> SplitLunchExpense:
        """
        Create and Submit a Splitwise Expense on behalf of your financial partner.

        This expense will be completely owed by the partner and maked as reimbursed.

        Parameters
        ----------
        amount: float
            Transaction Amount
        description: str
            Transaction Description

        Returns
        -------
        Expense
        """
        # CREATE THE NEW EXPENSE OBJECT
        new_expense = splitwise.Expense()
        new_expense.setDescription(desc=description)
        # GET AND SET AMOUNTS OWED
        new_expense.setCost(cost=amount)
        # CONFIGURE PRIMARY USER
        primary_user = splitwise.user.ExpenseUser()
        primary_user.setId(id=self.current_user.id)
        primary_user.setPaidShare(paid_share=amount)
        primary_user.setOwedShare(owed_share=0.00)
        # CONFIGURE SECONDARY USER
        financial_partner = splitwise.user.ExpenseUser()
        financial_partner.setId(id=self.financial_partner.id)
        financial_partner.setPaidShare(paid_share=0.00)
        financial_partner.setOwedShare(owed_share=amount)
        # ADD USERS AND REPAYMENTS TO EXPENSE
        new_expense.addUser(user=primary_user)
        new_expense.addUser(user=financial_partner)
        # SUBMIT THE EXPENSE AND GET THE RESPONSE
        expense_response: splitwise.Expense
        expense_response, expense_errors = self.createExpense(expense=new_expense)
        try:
            assert expense_errors is None
        except AssertionError:
            raise SplitLunchError(expense_errors["base"][0])
        logger.info("Expense Created: %s", expense_response.id)
        message = f"Created via SplitLunch: {datetime.datetime.now()}"
        self.createComment(expense_id=expense_response.id, content=message)
        pydantic_response = self.splitwise_to_pydantic(expense=expense_response)
        return pydantic_response

    def get_friend(self, email_address: Optional[str] = None,
                   friend_id: Optional[int] = None) -> Optional[splitwise.Friend]:
        """
        Retrieve a Financial Partner by Email Address

        Parameters
        ----------
        email_address: str
            Email Address of Friend's user in Splitwise
        friend_id: Optional[int]
            Splitwise friend ID. Notice the friend ID in the following
            URL: https://secure.splitwise.com/#/friends/12345678

        Returns
        -------
        Optional[splitwise.Friend]
        """
        friend_list: List[splitwise.Friend] = self.getFriends()
        if len(friend_list) == 1:
            return friend_list[0]
        for friend in friend_list:
            if friend_id is not None and friend.id == friend_id:
                return friend
            elif email_address is not None and friend.email.lower() == email_address.lower():
                return friend
        return None

    def get_expenses(self,
                     offset: Optional[int] = None,
                     limit: Optional[int] = None,
                     group_id: Optional[int] = None,
                     friendship_id: Optional[int] = None,
                     dated_after: Optional[datetime.datetime] = None,
                     dated_before: Optional[datetime.datetime] = None,
                     updated_after: Optional[datetime.datetime] = None,
                     updated_before: Optional[datetime.datetime] = None
                     ) -> List[SplitLunchExpense]:
        """
        Get Splitwise Expenses

        Parameters
        ----------
        offset: Optional[int]
            Number of expenses to be skipped
        limit: Optional[int]
            Number of expenses to be returned
        group_id: Optional[int]
            GroupID of the expenses
        friendship_id: Optional[int]
            FriendshipID of the expenses
        dated_after: Optional[datetime.datetime]
            ISO 8601 Date time. Return expenses later that this date
        dated_before: Optional[datetime.datetime]
            ISO 8601 Date time. Return expenses earlier than this date
        updated_after: Optional[datetime.datetime]
            ISO 8601 Date time. Return expenses updated after this date
        updated_before: Optional[datetime.datetime]
            ISO 8601 Date time. Return expenses updated before this date

        Returns
        -------
        List[SplitLunchExpense]
        """
        expenses = self.getExpenses(offset=offset,
                                    limit=limit,
                                    group_id=group_id,
                                    friendship_id=friendship_id,
                                    dated_after=dated_after,
                                    dated_before=dated_before,
                                    updated_after=updated_after,
                                    updated_before=updated_before)
        pydantic_expenses = [self.splitwise_to_pydantic(expense) for expense in expenses]
        return pydantic_expenses

    @classmethod
    def _get_splitwise_init_kwargs(cls,
                                   consumer_key: Optional[str] = None,
                                   consumer_secret: Optional[str] = None,
                                   api_key: Optional[str] = None,
                                   ) -> Dict[str, Any]:
        """
        Get the Splitwise Kwargs

        Parameters
        ----------
        consumer_key: Optional[str]
        consumer_secret: Optional[str]
        api_key: Optional[str]
        """
        if consumer_key is None:
            consumer_key = getenv("SPLITWISE_CONSUMER_KEY")
        if consumer_secret is None:
            consumer_secret = getenv("SPLITWISE_CONSUMER_SECRET")
        if api_key is None:
            api_key = getenv("SPLITWISE_API_KEY", None)
        init_kwargs = dict(consumer_key=consumer_key,
                           consumer_secret=consumer_secret,
                           api_key=api_key)
        if consumer_key is None or consumer_secret is None or api_key is None:
            error_message = dedent("""
            You must set your Splitwise credentials explicitly or by assigning
            the `SPLITWISE_CONSUMER_KEY`, `SPLITWISE_CONSUMER_SECRET`, and the
            `SPLITWISE_API_KEY`environment variables
            """).replace("\n", " ").replace("  ", " ")
            logger.error(error_message)
            raise SplitLunchError(error_message)
        return init_kwargs

    def splitwise_to_pydantic(self, expense: splitwise.Expense) -> SplitLunchExpense:
        """
        Convert Splitwise Object to Pydantic

        Parameters
        ----------
        expense: splitwise.Expense

        Returns
        -------
        SplitLunchExpense
        """
        financial_impact, self_paid = self._get_splitwise_impact(expense=expense)
        if expense.payment is True and financial_impact < 0:
            personal_share = abs(financial_impact)
        elif expense.payment is True and financial_impact > 0:
            personal_share = 0
        elif self_paid is True:
            personal_share = round(float(expense.cost) - financial_impact, 2)
        else:
            personal_share = abs(financial_impact)
        expense = SplitLunchExpense(splitwise_id=expense.id,
                                    original_amount=expense.cost,
                                    financial_impact=financial_impact,
                                    personal_share=personal_share,
                                    self_paid=self_paid,
                                    description=expense.description,
                                    category=expense.category.name,
                                    details=expense.details,
                                    payment=expense.payment,
                                    date=expense.date,
                                    users=[user.id for user in expense.users],
                                    created_at=expense.created_at,
                                    updated_at=expense.updated_at,
                                    deleted_at=expense.deleted_at,
                                    deleted=True if expense.deleted_at is not None else False)
        return expense

    def _get_expense_impact(self, expense: splitwise.Expense) -> Tuple[float, bool]:
        """
        Get the Financial Impact of a Splitwise Expense

        Parameters
        ----------
        expense: splitwise.Expense

        Returns
        -------
        Tuple[float, bool]
        """
        financial_impact = 0.00
        self_paid = True
        if len(expense.repayments) >= 1:
            for debt in expense.repayments:
                if debt.fromUser == self.current_user.id:
                    self_paid = False
                    financial_impact -= float(debt.amount)
                elif debt.toUser == self.current_user.id:
                    financial_impact += float(debt.amount)
        elif len(expense.repayments) == 0:
            assert len(expense.users) == 1
            assert expense.users[0].id == self.current_user.id
        return financial_impact, self_paid

    def _get_payment_impact(self, expense: splitwise.Expense) -> Tuple[float, bool]:
        """
        Get the Financial Impact of a Splitwise Payment

        Parameters
        ----------
        expense: splitwise.Expense

        Returns
        -------
        Tuple[float, bool]
        """
        financial_impact = 0.00
        self_paid = True
        if len(expense.repayments) >= 1:
            for debt in expense.repayments:
                if debt.fromUser == self.current_user.id:
                    self_paid = False
                    financial_impact += float(debt.amount)
                elif debt.toUser == self.current_user.id:
                    financial_impact -= float(debt.amount)
        elif len(expense.repayments) == 0:
            assert expense.users[0].id == self.current_user.id
            financial_impact -= float(expense.cost)
        return financial_impact, self_paid

    def _get_splitwise_asset(self) -> Optional[AssetsObject]:
        """
        Get the Splitwise asset

        Parse a user's Lunch Money accounts and return the manually managed
        Splitwise account asset object

        Returns
        -------
        AssetsObject
        """
        assets = self.lunchable.get_assets()
        splitwise_assets = list()
        for asset in assets:
            if asset.institution_name is not None and \
                    "splitwise" in asset.institution_name.lower():
                splitwise_assets.append(asset)
        if len(splitwise_assets) == 0:
            return None
        elif len(splitwise_assets) > 1:
            raise SplitLunchError("SplitLunch requires an manually managed Splitwise asset. "
                                  "Make sure you have a single account where 'Splitwise' "
                                  "is in the asset's `Institution Name`.")
        else:
            return splitwise_assets[0]

    def _get_reimbursement_category(self) -> Optional[CategoriesObject]:
        """
        Get the Reimbusement Category

        Parse a user's Lunch Money categories and return the Reimbursement
        category

        Returns
        -------
        CategoriesObject
        """
        categories = self.lunchable.get_categories()
        reimbursement_list = list()
        for category in categories:
            if "reimbursement" == category.name.strip().lower():
                reimbursement_list.append(category)
        if len(reimbursement_list) != 1:
            return None
        return reimbursement_list[0]

    def _get_splitwise_impact(self, expense: splitwise.Expense) -> Tuple[float, bool]:
        """
        Get the Financial Impact of a Splitwise Transaction

        Parameters
        ----------
        expense: splitwise.Expense

        Returns
        -------
        Tuple[float, bool]
        """
        if expense.payment is True:
            financial_impact, self_paid = self._get_payment_impact(expense=expense)
        else:
            financial_impact, self_paid = self._get_expense_impact(expense=expense)
        return financial_impact, self_paid

    def _get_splitwise_tags(self) -> None:
        """
        Get Lunch Money Tags to Interact with

        Returns
        -------
        Dict[str, int]
        """
        all_tags = self.lunchable.get_tags()
        for tag in all_tags:
            if tag.name.lower() == SplitLunchConfig.splitlunch_tag.lower():
                self.splitlunch_tag = tag
            elif tag.name.lower() == SplitLunchConfig.splitwise_tag.lower():
                self.splitwise_tag = tag
            elif tag.name.lower() == SplitLunchConfig.splitlunch_import_tag.lower():
                self.splitlunch_import_tag = tag
            elif tag.name.lower() == SplitLunchConfig.splitlunch_direct_import_tag.lower():
                self.splitlunch_direct_import_tag = tag

    def _raise_nonexistent_tag_error(self, tags: List[str]) -> None:
        """
        Raise a warning for specific SplitLunch Tags

        tags: List[str]
            A list of tags to raise the error for
        """
        if self.splitlunch_tag == self._none_tag and SplitLunchConfig.splitlunch_tag in tags:
            error_message = (f"a `{SplitLunchConfig.splitlunch_tag}` tag is required. "
                             f"This tag is used for splitting transactions in half and have half "
                             f"marked as reimbursed.")
            raise SplitLunchError(error_message)
        if self.splitwise_tag == self._none_tag and SplitLunchConfig.splitwise_tag in tags:
            error_message = (f"a `{SplitLunchConfig.splitwise_tag}` tag is required. "
                             f"This tag is used for splitting transactions in half and have half "
                             f"marked as reimbursed.")
            raise SplitLunchError(error_message)
        if self.splitlunch_import_tag == self._none_tag and \
                SplitLunchConfig.splitlunch_import_tag in tags:
            error_message = (f"a `{SplitLunchConfig.splitlunch_import_tag}` tag is required. "
                             f"This tag is used for creating Splitwise transactions directly from "
                             f"Lunch Money transactions. These transactions will be split in half,"
                             f"and have one half marked as reimbursed.")
            raise SplitLunchError(error_message)
        if self.splitlunch_direct_import_tag == self._none_tag and \
                SplitLunchConfig.splitlunch_direct_import_tag in tags:
            error_message = (f"a `{SplitLunchConfig.splitlunch_direct_import_tag}` tag is "
                             "required. This tag is used for creating Splitwise transactions "
                             "directly from Lunch Money transactions. These transactions will "
                             "be completely owed by your financial partner.")
            raise SplitLunchError(error_message)

    def get_splitlunch_tagged_transactions(
            self, start_date: Optional[datetime.date] = None,
            end_date: Optional[datetime.date] = None) -> List[TransactionObject]:
        """
        Retrieve all transactions with the "Splitlunch" Tag

        Parameters
        ----------
        start_date: Optional[datetime.date]
        end_date : Optional[datetime.date]

        Returns
        -------
        List[TransactionObject]
        """
        if start_date is None:
            start_date = self.earliest_start_date
        if end_date is None:
            end_date = self.latest_end_date
        self._raise_nonexistent_tag_error(tags=[SplitLunchConfig.splitlunch_tag])
        transactions = self.lunchable.get_transactions(tag_id=self.splitlunch_tag.id,
                                                       start_date=start_date,
                                                       end_date=end_date)
        return transactions

    def get_splitlunch_import_tagged_transactions(
            self, start_date: Optional[datetime.date] = None,
            end_date: Optional[datetime.date] = None) -> List[TransactionObject]:
        """
        Retrieve all transactions with the "SplitLunchImport" Tag

        Parameters
        ----------
        start_date: Optional[datetime.date]
        end_date : Optional[datetime.date]

        Returns
        -------
        List[TransactionObject]
        """
        if start_date is None:
            start_date = self.earliest_start_date
        if end_date is None:
            end_date = self.latest_end_date
        self._raise_nonexistent_tag_error(tags=[SplitLunchConfig.splitlunch_import_tag])
        transactions = self.lunchable.get_transactions(tag_id=self.splitlunch_import_tag.id,
                                                       start_date=start_date,
                                                       end_date=end_date)
        return transactions

    def get_splitlunch_direct_import_tagged_transactions(
            self, start_date: Optional[datetime.date] = None,
            end_date: Optional[datetime.date] = None) -> List[TransactionObject]:
        """
        Retrieve all transactions with the "SplitLunchDirectImport" Tag

        Parameters
        ----------
        start_date: Optional[datetime.date]
        end_date : Optional[datetime.date]

        Returns
        -------
        List[TransactionObject]
        """
        if start_date is None:
            start_date = self.earliest_start_date
        if end_date is None:
            end_date = self.latest_end_date
        self._raise_nonexistent_tag_error(tags=[SplitLunchConfig.splitlunch_direct_import_tag])
        transactions = self.lunchable.get_transactions(tag_id=self.splitlunch_direct_import_tag.id,
                                                       start_date=start_date,
                                                       end_date=end_date)
        return transactions

    def get_splitwise_tagged_transactions(
            self, start_date: Optional[datetime.date] = None,
            end_date: Optional[datetime.date] = None) -> List[TransactionObject]:
        """
        Retrieve all transactions with the "Splitwise" Tag

        Parameters
        ----------
        start_date: Optional[datetime.date]
        end_date : Optional[datetime.date]

        Returns
        -------
        List[TransactionObject]
        """
        if start_date is None:
            start_date = self.earliest_start_date
        if end_date is None:
            end_date = self.latest_end_date
        self._raise_nonexistent_tag_error(tags=[SplitLunchConfig.splitwise_tag])
        transactions = self.lunchable.get_transactions(tag_id=self.splitwise_tag.id,
                                                       start_date=start_date,
                                                       end_date=end_date)
        return transactions

    def make_splitlunch(self, tag_transactions: bool = False) -> List[Dict[int, Any]]:
        """
        Operate on `SplitLunch` tagged transactions

        Split all transactions with the `SplitLunch` tag in half. One of these
        new splits will be recategorized to `Reimbursement`. Both new splits will receive
        the `Splitwise` tag without any preexisting tags.
        """
        if self.reimbursement_category is None:
            self._raise_category_reimbursement_error()
            raise ValueError("ReimbursementCategory")
        split_transaction_ids = list()
        tagged_objects = self.get_splitlunch_tagged_transactions()
        for transaction in tagged_objects:
            # Split the Original Amount
            amount_1, amount_2 = self.split_a_transaction(amount=transaction.amount)
            # Generate the First Split
            split_object = TransactionSplitObject(
                date=transaction.date,
                category_id=transaction.category_id,
                notes=transaction.notes,
                amount=amount_1
            )
            # Generate the second split as a copy, change some properties
            reimbursement_object = split_object.copy()
            reimbursement_object.amount = amount_2
            reimbursement_object.category_id = self.reimbursement_category.id
            logger.debug("Splitting transaction: %s -> (%s, %s)",
                         transaction.amount, amount_1, amount_2)

            update_response = self.lunchable.update_transaction(transaction_id=transaction.id,
                                                                split=[split_object,
                                                                       reimbursement_object])
            # Tag each of the new transactions generated
            split_transaction_ids.append({transaction.id: update_response["split"]})
            for split_transaction_id in update_response["split"]:
                update_tags = transaction.tags if transaction.tags is not None else []
                tags = [tag.name for tag in update_tags if
                        tag is not None and tag.name.lower() != self.splitlunch_tag.name.lower()]
                if self.splitwise_tag.name not in tags and tag_transactions is True:
                    self._raise_nonexistent_tag_error(tags=[SplitLunchConfig.splitwise_tag])
                    tags.append(self.splitwise_tag.name)
                tag_update = TransactionUpdateObject(tags=tags)
                self.lunchable.update_transaction(transaction_id=split_transaction_id,
                                                  transaction=tag_update)
        return split_transaction_ids

    def make_splitlunch_import(self, tag_transactions: bool = False) -> List[Dict[str, Any]]:
        """
        Operate on `SplitLunchImport` tagged transactions

        Send a transaction to Splitwise and then split the original transaction in Lunch Money.
        One of these new splits will be recategorized to `Reimbursement`. Both new splits
        will receive the `Splitwise` tag without the `SplitLunchImport` tag. Any other tags will be
        reapplied.

        Parameters
        ----------
        tag_transactions : bool
            Whether to tag the transactions with the `Splitwise` tag after splitting them.
            Defaults to False which

        Returns
        -------
        List[Dict[str, Any]]
        """
        self._raise_financial_partner_error()
        if self.reimbursement_category is None:
            self._raise_category_reimbursement_error()
            raise ValueError("ReimbursementCategory")
        tagged_objects = self.get_splitlunch_import_tagged_transactions()
        update_responses = list()
        for transaction in tagged_objects:
            # Split the Original Amount
            description = str(transaction.payee)
            if transaction.notes is not None:
                description = f"{transaction.payee} - {transaction.notes}"
            new_transaction = self.create_self_paid_expense(amount=transaction.amount,
                                                            description=description)
            notes = f"Splitwise ID: {new_transaction.splitwise_id}"
            if transaction.notes is not None:
                notes = f"{transaction.notes} || {notes}"
            split_object = TransactionSplitObject(
                date=transaction.date,
                category_id=transaction.category_id,
                notes=notes,
                amount=new_transaction.personal_share
            )
            reimbursement_object = split_object.copy()
            reimbursement_object.amount = round(transaction.amount - new_transaction.personal_share,
                                                2)
            reimbursement_object.category_id = self.reimbursement_category.id
            logger.debug(f"Transaction split by Splitwise: {transaction.amount} -> "
                         f"({split_object.amount}, {reimbursement_object.amount})")
            update_response = self.lunchable.update_transaction(transaction_id=transaction.id,
                                                                split=[split_object,
                                                                       reimbursement_object])
            update_responses.append(update_response)
            # Tag each of the new transactions generated
            for split_transaction_id in update_response["split"]:
                update_tags = transaction.tags or []
                tags = [tag.name for tag in update_tags if
                        tag.name.lower() != self.splitlunch_import_tag.name.lower()]
                if self.splitwise_tag.name not in tags and tag_transactions is True:
                    self._raise_nonexistent_tag_error(tags=[SplitLunchConfig.splitwise_tag])
                    tags.append(self.splitwise_tag.name)
                tag_update = TransactionUpdateObject(tags=tags)
                self.lunchable.update_transaction(transaction_id=split_transaction_id,
                                                  transaction=tag_update)
        return update_responses

    def make_splitlunch_direct_import(self, tag_transactions: bool = False) -> List[Dict[str, Any]]:
        """
        Operate on `SplitLunchDirectImport` tagged transactions

        Send a transaction to Splitwise and then mark the transaction under the
        `Reimbursement` category. The sum of the transaction will be completely owed
        by the financial partner.

        Parameters
        ----------
        tag_transactions : bool
            Whether to tag the transactions with the `Splitwise` tag after splitting them.
            Defaults to False which
        """
        self._raise_financial_partner_error()
        if self.reimbursement_category is None:
            self._raise_category_reimbursement_error()
            raise ValueError("ReimbursementCategory")
        tagged_objects = self.get_splitlunch_direct_import_tagged_transactions()
        update_responses = list()
        for transaction in tagged_objects:
            # Split the Original Amount
            description = str(transaction.payee)
            if transaction.notes is not None:
                description = f"{transaction.payee} - {transaction.notes}"
            new_transaction = self.create_expense_on_behalf_of_partner(amount=transaction.amount,
                                                                       description=description)
            notes = f"Splitwise ID: {new_transaction.splitwise_id}"
            if transaction.notes is not None:
                notes = f"{transaction.notes} || {notes}"
            existing_tags = transaction.tags or []
            tags = [tag.name for tag in existing_tags if
                    tag.name.lower() != self.splitlunch_import_tag.name.lower()]
            if self.splitwise_tag.name not in tags and tag_transactions is True:
                self._raise_nonexistent_tag_error(tags=[SplitLunchConfig.splitwise_tag])
                tags.append(self.splitwise_tag.name)
            update = TransactionUpdateObject(category_id=self.reimbursement_category.id,
                                             tags=tags,
                                             notes=notes)
            response = self.lunchable.update_transaction(transaction_id=transaction.id,
                                                         transaction=update)
            update_responses.append(response)
        return update_responses

    def splitwise_to_lunchmoney(self, expenses: List[SplitLunchExpense]) -> List[int]:
        """
        Ingest Splitwise Expenses into Lunch Money

        This function inserts splitwise expenses into Lunch Money. If an expense
        is not a payment, not deleted, and not self-paid it qualifies for ingestion. Otherwise
        it will be ignored.

        Parameters
        ----------
        expenses: List[SplitLunchExpense]

        Returns
        -------
        List[int]
            New Lunch Money transaction IDs
        """
        if self.splitwise_asset is None:
            self._raise_splitwise_asset_error()
            raise ValueError("SplitwiseAsset")
        batch = []
        new_transaction_ids = []
        filtered_expenses = self.filter_relevant_splitwise_expenses(expenses=expenses)
        for splitwise_transaction in filtered_expenses:
            new_lunchmoney_transaction = TransactionInsertObject(
                date=splitwise_transaction.date.astimezone(tzlocal()),
                payee=splitwise_transaction.description,
                amount=splitwise_transaction.personal_share,
                asset_id=self.splitwise_asset.id,
                external_id=splitwise_transaction.splitwise_id
            )
            batch.append(new_lunchmoney_transaction)
            if len(batch) == 10:
                new_ids = self.lunchable.insert_transactions(transactions=batch,
                                                             apply_rules=True)
                new_transaction_ids += new_ids
                batch = []
        if len(batch) > 0:
            new_ids = self.lunchable.insert_transactions(transactions=batch,
                                                         apply_rules=True)
            new_transaction_ids += new_ids
        return new_transaction_ids

    @staticmethod
    def filter_relevant_splitwise_expenses(expenses: List[SplitLunchExpense]
                                           ) -> List[SplitLunchExpense]:
        """
        Filter Expenses in Splitwise into relevant expenses.

        This filtering action is important to understand when seeing why not
        all transactions from Splitwise end up flowing into Lunch Money.

        1) It filters out deleted expenses

        2) It filters out `self-paid` expenses. A `self-paid` expense is an expense in Splitwise
        where you originated the payment. This is excluded because it is assumed that these
        transactions will have already been imported via a different account.

        3) It filters out payments. Payments are excluded because it is assumed that these
        transactions will have already been imported via a different account.

        Parameters
        ----------
        expenses: List[SplitLunchExpense]

        Returns
        -------
        List[SplitLunchExpense]
        """
        filtered_expenses = list()
        for splitwise_transaction in expenses:
            if all([
                splitwise_transaction.deleted is False,
                splitwise_transaction.payment is False,
                splitwise_transaction.self_paid is False
            ]):
                filtered_expenses.append(splitwise_transaction)

        return filtered_expenses

    def get_splitwise_balance(self) -> float:
        """
        Get the net balance in Splitwise

        Returns
        -------
        float
        """
        groups = self.getGroups()
        total_balance = 0.00
        for group in groups:
            for debt in group.simplified_debts:
                if debt.fromUser == self.current_user.id:
                    total_balance -= float(debt.amount)
                elif debt.toUser == self.current_user.id:
                    total_balance += float(debt.amount)
        return total_balance

    def update_splitwise_balance(self) -> AssetsObject:
        """
        Get and update the Splitwise Asset in Lunch Money

        Returns
        -------
        AssetsObject
            Updated  balance
        """
        if self.splitwise_asset is None:
            self._raise_splitwise_asset_error()
            raise ValueError("SplitwiseAsset")
        balance = self.get_splitwise_balance()
        if balance != self.splitwise_asset.balance:
            updated_asset = self.lunchable.update_asset(asset_id=self.splitwise_asset.id,
                                                        balance=balance)
            self.splitwise_asset = updated_asset
        return self.splitwise_asset

    _deleted_payee = "[DELETED FROM SPLITWISE]"

    def get_new_transactions(self) -> Tuple[List[SplitLunchExpense], List[TransactionObject]]:
        """
        Get Splitwise Transactions that don't exist in Lunch Money

        Also return deleted transaction from LunchMoney

        Returns
        -------
        Tuple[List[SplitLunchExpense], List[TransactionObject]]
            New and Deleted Transactions
        """
        if self.splitwise_asset is None:
            self._raise_splitwise_asset_error()
            raise ValueError("SplitwiseAsset")
        splitlunch_expenses = self.lunchable.get_transactions(
            asset_id=self.splitwise_asset.id,
            start_date=datetime.datetime(1800, 1, 1),
            end_date=datetime.datetime(2300, 12, 31)
        )
        splitlunch_ids = {int(item.external_id) for item in splitlunch_expenses if
                          item.external_id is not None}
        splitwise_expenses = self.get_expenses(limit=0)
        splitwise_ids = {item.splitwise_id for item in splitwise_expenses}
        new_ids = splitwise_ids.difference(splitlunch_ids)
        filtered_expenses = self.filter_relevant_splitwise_expenses(expenses=splitwise_expenses)
        new_expenses = [expense for expense in filtered_expenses if
                        expense.splitwise_id in new_ids]
        deleted_transactions = self.get_deleted_transactions(
            splitlunch_expenses=splitlunch_expenses,
            splitwise_transactions=splitwise_expenses
        )
        return new_expenses, deleted_transactions

    def get_deleted_transactions(self,
                                 splitlunch_expenses: List[TransactionObject],
                                 splitwise_transactions: List[SplitLunchExpense]
                                 ) -> List[TransactionObject]:
        """
        Get Splitwise Transactions that exist in Lunch Money but have since been deleted

        Set these transactions to $0.00 and Make a Note

        Parameters
        ----------
        splitlunch_expenses: List[TransactionObject]
        splitwise_transactions: List[SplitLunchExpense]

        Returns
        -------
        List[TransactionObject]
        """
        if self.splitwise_asset is None:
            self._raise_splitwise_asset_error()
            raise ValueError("SplitwiseAsset")
        existing_transactions = {int(item.external_id) for item in splitlunch_expenses if
                                 item.external_id is not None}
        deleted_ids = {item.splitwise_id for item in splitwise_transactions if item.deleted is True}
        untethered_transactions = deleted_ids.intersection(existing_transactions)
        transactions_to_delete = [
            tran for tran in splitlunch_expenses if
            tran.external_id is not None and
            int(tran.external_id) in untethered_transactions and
            tran.payee != self._deleted_payee
        ]
        return transactions_to_delete

    def refresh_splitwise_transactions(self) -> Dict[str, Any]:
        """
        Import New Splitwise Transactions to Lunch Money

        This function get's all transactions from Splitwise, all transactions from
        your Lunch Money Splitwise account and compares the two.

        Returns
        -------
        List[SplitLunchExpense]
        """
        new_transactions, deleted_transactions = self.get_new_transactions()
        self.splitwise_to_lunchmoney(expenses=new_transactions)
        splitwise_asset = self.update_splitwise_balance()
        self.handle_deleted_transactions(deleted_transactions=deleted_transactions)
        return dict(balance=splitwise_asset.balance,
                    new=new_transactions,
                    deleted=deleted_transactions)

    def handle_deleted_transactions(self,
                                    deleted_transactions: List[TransactionObject],
                                    ) -> List[Dict[str, Any]]:
        """
        Update Transactions That Exist in Splitwise, but have been deleted in Splitwise

        Parameters
        ----------
        deleted_transactions: List[TransactionObject]

        Returns
        -------
        List[Dict[str, Any]]
        """
        updated_transactions = list()
        for transaction in deleted_transactions:
            update = self.lunchable.update_transaction(
                transaction_id=transaction.id,
                transaction=TransactionUpdateObject(
                    amount=0.00,
                    payee=self._deleted_payee,
                    notes=f"{transaction.payee} || {transaction.amount} || {transaction.notes}"
                )
            )
            updated_transactions.append(update)
        return updated_transactions

    def _raise_financial_partner_error(self) -> None:
        """
        Raise Errors for Financial Partners
        """
        if self.financial_partner is None:
            raise SplitLunchError("You must designate a financial partner in Splitwise. "
                                  "This can be done with the partner's Splitwise User ID # "
                                  "or their email address.")

    def _raise_splitwise_asset_error(self) -> None:
        """
        Raise Errors for Splitwise Asset
        """
        raise SplitLunchError("You must create an asset (aka Account) in Lunch Money with "
                              "`Splitwise` in the name. There should only be one account "
                              "like this.")

    def _raise_category_reimbursement_error(self) -> None:
        """
        Raise Errors for Splitwise Asset
        """
        raise SplitLunchError("SplitLunch requires a reimbursement Category. "
                              "Make sure you have a category entitled `Reimbursement`. "
                              "This category will be excluded from budgeting."
                              "Half of split transactions will be created with "
                              "this category.")

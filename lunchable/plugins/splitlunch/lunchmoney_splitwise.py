"""
Lunchable Plugin for Splitwise
"""

import datetime
import logging
from math import floor
from os import environ, getenv
from random import shuffle
from typing import Any, Dict, List, Optional, Tuple, Union

from lunchable import __lunchable__, LunchMoney
from lunchable.exceptions import LunchMoneyImportError
from lunchable.models import TransactionObject
from lunchable.plugins.splitlunch.config import SplitLunchConfig
from lunchable.plugins.splitlunch.exceptions import SplitLunchError
from lunchable.plugins.splitlunch.models import SplitLunchExpense

logger = logging.getLogger(__name__)

try:
    import splitwise  # type: ignore
except ImportError as ie:
    logger.exception(ie)
    _pip_extra_error = ("Looks like you don't have the Splitwise plugin installed: "
                        f"`pip install {__lunchable__}[splitlunch]`")
    raise LunchMoneyImportError(_pip_extra_error)


class SplitLunch(splitwise.Splitwise):
    """
    Lunchable Plugin For Interacting With Splitwise
    """

    def __init__(self,
                 lunch_money_access_token: Optional[str] = None,
                 financial_partner_id: Optional[int] = None,
                 financial_partner_email: Optional[str] = None,
                 consumer_key: Optional[str] = None,
                 consumer_secret: Optional[str] = None,
                 api_key: Optional[str] = None,
                 access_token: Optional[Dict[str, str]] = None):
        """
        Initialize the Parent Class with some additional properties

        Parameters
        ----------
        financial_partner_id: Optional[int], default = None,
        financial_partner_email: Optional[str], default = None,
        consumer_key: Optional[str], default = None
        consumer_secret: Optional[str], default = None
        access_token: Optional[str], default = None
        """
        init_kwargs = self._get_splitwise_init_kwargs(consumer_key=consumer_key,
                                                      consumer_secret=consumer_secret,
                                                      api_key=api_key,
                                                      access_token=access_token)
        super(SplitLunch, self).__init__(**init_kwargs)

        self.current_user: splitwise.CurrentUser = self.getCurrentUser()
        self.financial_partner: splitwise.Friend = self.get_friend(
            friend_id=financial_partner_id,
            email_address=financial_partner_email)
        self.last_check: Optional[datetime.datetime] = None
        self.lunchable = LunchMoney(access_token=lunch_money_access_token)
        tags = self._get_tag_ids()
        self.splitwise_tag_id = tags[SplitLunchConfig.splitwise_tag]
        self.splitlunch_tag_id = tags[SplitLunchConfig.splitlunch_tag]
        self.earliest_start_date = datetime.date(1812, 1, 1)
        today = datetime.date.today()
        self.latest_end_date = datetime.date(today.year + 10, 12, 31)

    def __repr__(self):
        """
        String Representation

        Returns
        -------
        str
        """
        return f"<Splitwise: {self.current_user.email}>"

    @classmethod
    def split_a_transaction(cls, amount: Union[float, int]) -> Tuple[float, float]:
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
        try:
            assert amount == round(amount, 2)
        except AssertionError:
            raise SplitLunchError(f"{amount} caused an error, you must provide a real "
                                  "spending amount.")
        first_owe = second_owe = amount / 2
        pennies = int((amount - floor(amount)) * 100)
        if (pennies % 2) == 0:
            amounts_due = (round(first_owe, 2), round(second_owe, 2))
        else:
            first_owe += 0.005
            second_owe -= 0.005
            two_amounts = [round(first_owe, 2), round(second_owe, 2)]
            shuffle(two_amounts)
            amounts_due = tuple(two_amounts)  # type: ignore
        return amounts_due

    def create_self_paid_expense(self, amount: float, description: str) -> splitwise.Expense:
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
        primary_user = splitwise.ExpenseUser()
        primary_user.setId(id=self.current_user.id)
        primary_user.setPaidShare(paid_share=amount)
        primary_user.setOwedShare(owed_share=primary_user_owes)
        # CONFIGURE SECONDARY USER
        financial_partner = splitwise.ExpenseUser()
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
        return expense_response

    def get_friend(self, email_address: Optional[str] = None,
                   friend_id: Optional[int] = None) -> splitwise.Friend:
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
        splitwise.Friend
        """
        friend_list: List[splitwise.Friend] = self.getFriends()
        if len(friend_list) == 1:
            return friend_list[0]
        for friend in friend_list:
            if friend.id == friend_id:
                return friend
            elif email_address is not None and friend.email.lower() == email_address.lower():
                return friend
        raise SplitLunchError("Couldn't identify financial partner in Splitwise.")

    @classmethod
    def _get_splitwise_init_kwargs(cls,
                                   consumer_key: Optional[str] = None,
                                   consumer_secret: Optional[str] = None,
                                   api_key: Optional[str] = None,
                                   access_token: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        """
        Get the Splitwise Kwargs

        Parameters
        ----------
        consumer_key: Optional[str], default = None
        consumer_secret: Optional[str], default = None
        api_key: Optional[str], default = None
        access_token: Optional[str], default = None
        """
        if consumer_key is None:
            consumer_key = environ["SPLITWISE_CONSUMER_KEY"]
        if consumer_secret is None:
            consumer_secret = environ["SPLITWISE_CONSUMER_SECRET"]
        init_kwargs = dict(consumer_key=consumer_key,
                           consumer_secret=consumer_secret)
        if api_key is None:
            api_key = getenv("SPLITWISE_API_KEY", None)
        if access_token is None:
            _oauth_token = getenv("SPLITWISE_OAUTH_TOKEN")
            _oauth_token_secret = getenv("SPLITWISE_OAUTH_SECRET")
            if _oauth_token is None or _oauth_token_secret is None:
                access_token = None
            else:
                access_token = dict(oauth_token=_oauth_token,
                                    oauth_token_secret=_oauth_token_secret)
        if api_key is not None and access_token is not None:
            init_kwargs.update(dict(api_key=api_key))
        elif api_key is not None:
            init_kwargs.update(dict(api_key=api_key))
        elif access_token is not None:
            init_kwargs.update(access_token)
        else:
            raise SplitLunchError("No Splitwise API Key or Access Token Identified")
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
        expense = SplitLunchExpense(splitwise_id=expense.id,
                                    original_amount=expense.cost,
                                    financial_impact=financial_impact,
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

    def _get_tag_ids(self) -> Dict[str, Optional[int]]:
        """
        Get Lunch Money Tags to Interact with

        Returns
        -------
        Dict[str, int]
        """
        tag_dict: Dict[str, Optional[int]] = dict()
        tag_dict[SplitLunchConfig.splitlunch_tag] = None
        tag_dict[SplitLunchConfig.splitwise_tag] = None
        if self.lunchable is None:
            return tag_dict
        all_tags = self.lunchable.get_tags()
        for tag in all_tags:
            if tag.name.lower() == SplitLunchConfig.splitlunch_tag.lower():
                tag_dict[SplitLunchConfig.splitlunch_tag] = tag.id
            elif tag.name.lower() == SplitLunchConfig.splitwise_tag.lower():
                tag_dict[SplitLunchConfig.splitwise_tag] = tag.id
        return tag_dict

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
        transactions = self.lunchable.get_transactions(tag_id=self.splitlunch_tag_id,
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
        transactions = self.lunchable.get_transactions(tag_id=self.splitwise_tag_id,
                                                       start_date=start_date,
                                                       end_date=end_date)
        return transactions

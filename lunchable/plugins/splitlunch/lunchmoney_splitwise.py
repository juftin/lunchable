"""
Splitwise Interactions
"""

import datetime
import logging
from math import floor
from os import environ, getenv
from random import shuffle
from typing import Dict, List, Optional, Tuple, Union

from lunchable import __lunchable__
from lunchable.exceptions import LunchMoneyError, LunchMoneyImportError

logger = logging.getLogger(__name__)

try:
    import splitwise  # type: ignore
except ImportError as ie:
    logger.exception(ie)
    _pip_extra_error = ("Looks like you don't have the Splitwise plugin installed: "
                        f"`pip install {__lunchable__}[splitlunch]`")
    raise LunchMoneyImportError(_pip_extra_error)


class SplitLunchError(LunchMoneyError):
    """
    Split Lunch Errors
    """


class SplitLunch(splitwise.Splitwise):
    """
    Python Extension Class for interacting with Splitwise
    """

    def __init__(self,
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
        super().__init__(**init_kwargs)

        self.current_user: splitwise.CurrentUser = self.getCurrentUser()
        self.financial_partner: splitwise.Friend = self.get_friend(
            friend_id=financial_partner_id,
            email_address=financial_partner_email)
        self.last_check: Optional[datetime.datetime] = None

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

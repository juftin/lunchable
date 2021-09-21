"""
Splitwise Interactions
"""

import datetime
import logging
from os import environ
from typing import Dict, Optional

from lunchable import __lunchable__
from lunchable.exceptions import LunchMoneyImportError

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
    Python Extension Class for interacting with Splitwise
    """

    def __init__(self, consumer_key: Optional[str] = None,
                 consumer_secret: Optional[str] = None,
                 access_token: Optional[Dict[str, str]] = None):
        """
        Initialize the Parent Class with some additional properties

        Parameters
        ----------
        consumer_key: Optional[str]
        consumer_secret: Optional[str]
        access_token: Optional[str]
        """
        if consumer_key is None:
            consumer_key = environ["SPLITWISE_CONSUMER_KEY"]
        if consumer_secret is None:
            consumer_secret = environ["SPLITWISE_CONSUMER_SECRET"]
        if access_token is None:
            access_token = dict(oauth_token=environ["SPLITWISE_OAUTH_TOKEN"],
                                oauth_token_secret=environ["SPLITWISE_OAUTH_SECRET"])

        super().__init__(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token=access_token
        )
        self.current_user: splitwise.CurrentUser = self.getCurrentUser()
        self.last_check: Optional[datetime.datetime] = None

    def __repr__(self):
        """
        String Representation

        Returns
        -------
        str
        """
        return f"<Splitwise: {self.current_user.email}>"

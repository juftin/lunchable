"""
SplitLunch Data Models
"""

import datetime
from typing import List, Optional

from lunchable.models._base import LunchableModel


class SplitLunchExpense(LunchableModel):
    """
    SplitLunch Object for Splitwise Expenses
    """

    splitwise_id: int
    original_amount: float
    self_paid: bool
    financial_impact: float
    personal_share: float
    description: str
    category: str
    details: Optional[str]
    payment: bool
    date: datetime.datetime
    users: List[int]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: Optional[datetime.datetime]
    deleted: bool

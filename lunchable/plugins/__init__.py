"""
Optional Plugins for LunchMoney
"""

from .base.base_app import LunchableApp, LunchableModelType, LunchableTransactionsApp

__all__ = [
    "LunchableTransactionsApp",
    "LunchableApp",
    "LunchableModelType",
]

"""
Apps with Pandas Support
"""

from typing import Iterable, List, Type

import numpy as np
import pandas as pd

from lunchable.models import LunchableModel
from lunchable.plugins import LunchableApp, LunchableModelType, LunchableTransactionsApp


class LunchablePandasApp(LunchableApp):
    """
    LunchableApp with Pandas Super Powers
    """

    @staticmethod
    def models_to_df(models: Iterable[LunchableModel]) -> pd.DataFrame:
        """
        Convert Transactions Array to DataFrame

        Parameters
        ----------
        models: List[LunchableModel]

        Returns
        -------
        pd.DataFrame
        """
        if not isinstance(models, list):
            models = list(models)
        return pd.DataFrame(
            [item.dict() for item in models],
            columns=models[0].__fields__.keys(),
        )

    @staticmethod
    def df_to_models(
        df: pd.DataFrame, model_type: Type[LunchableModelType]
    ) -> List[LunchableModelType]:
        """
        Convert DataFrame to Transaction Array

        Parameters
        ----------
        df: pd.DataFrame
        model_type: Type[LunchableModel]

        Returns
        -------
        List[LunchableModel]
        """
        array_df = df.copy()
        array_df = array_df.fillna(np.NaN).replace([np.NaN], [None])
        model_array = array_df.to_dict(orient="records")
        return [model_type(**item) for item in model_array]


class LunchablePandasTransactionsApp(LunchableTransactionsApp, LunchablePandasApp):
    """
    LunchableTransactionsApp with Pandas Super Powers
    """

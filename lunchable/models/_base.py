"""
Base Pydantic Object for Containers
"""

from pydantic import BaseModel, ConfigDict


class LunchableModel(BaseModel):
    """
    Hashable Pydantic Model
    """

    model_config = ConfigDict(extra="allow")

    def __hash__(self) -> int:
        """
        Hash Method for Pydantic BaseModels
        """
        return hash((type(self), *tuple(self.__dict__.values())))

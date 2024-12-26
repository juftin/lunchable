# coding: utf-8

"""
    Lunch Money API - v2

    This is a version of the Lunch Money API described using the the OpenAPI 3.X specification.    The goal of this project is to validate an \"API Design First\" approach for the Lunch Money API, which should allow us to gather developer feedback prior to implementation in order to develop API endpoints more quickly.  This version of the API will differ from the existing v1 beta version. For more information on the changes please see the  [v2 API Changelog](https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2/changelog)  Some useful links: - [Current v1 Lunch Money API Documentation](https://lunchmoney.dev) - [v2 API Changelog](https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2/changelog) - [OpenAPI API YAML Specification](https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2/openapi/) - [Awesome Lunch Money Projects](https://lunchmoney.dev/#awesome-projects)

    The version of the OpenAPI document: 2.7.4
    Contact: devsupport@lunchmoney.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from lunchable.models.account_type_enum import AccountTypeEnum
from typing import Optional, Set
from typing_extensions import Self

class ManualAccountObject(BaseModel):
    """
    An object containing information about a manual account
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The unique identifier of this account")
    name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=45)]] = Field(default=None, description="Name of the account")
    type: Optional[AccountTypeEnum] = Field(default=None, description="Primary type of the account")
    subtype: Optional[StrictStr] = Field(default=None, description="Optional account subtype. Examples include<br> - retirement - checking - savings - prepaid credit card")
    display_name: Optional[StrictStr] = Field(default=None, description="Optional display name for the account set by the user")
    balance: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Current balance of the account in numeric format to 4 decimal places.")
    balance_as_of: Optional[datetime] = Field(default=None, description="Date balance was last updated in ISO 8601 extended format")
    closed_on: Optional[date] = Field(default=None, description="The date this account was closed. Will be null if the account has not been marked as closed")
    currency: Optional[Annotated[str, Field(min_length=3, strict=True, max_length=3)]] = Field(default=None, description="Three-letter lowercase currency code of the account balance")
    institution_name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=50)]] = Field(default=None, description="Name of institution holding the account")
    external_id: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=75)]] = Field(default=None, description="An optional external_id that may be set or updated via the API")
    exclude_from_transactions: Optional[StrictBool] = Field(default=None, description="If true, this account will not show up as an option for assignment when creating transactions manually")
    created_at: Optional[datetime] = Field(default=None, description="Date/time the account was created in ISO 8601 extended format")
    updated_at: Optional[datetime] = Field(default=None, description="Date/time the account was created in ISO 8601 extended format")
    __properties: ClassVar[List[str]] = ["id", "name", "type", "subtype", "display_name", "balance", "balance_as_of", "closed_on", "currency", "institution_name", "external_id", "exclude_from_transactions", "created_at", "updated_at"]

    @field_validator('balance')
    def balance_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^-?\d+(\.\d{0,4})?$", value):
            raise ValueError(r"must validate the regular expression /^-?\d+(\.\d{0,4})?$/")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ManualAccountObject from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if subtype (nullable) is None
        # and model_fields_set contains the field
        if self.subtype is None and "subtype" in self.model_fields_set:
            _dict['subtype'] = None

        # set to None if display_name (nullable) is None
        # and model_fields_set contains the field
        if self.display_name is None and "display_name" in self.model_fields_set:
            _dict['display_name'] = None

        # set to None if closed_on (nullable) is None
        # and model_fields_set contains the field
        if self.closed_on is None and "closed_on" in self.model_fields_set:
            _dict['closed_on'] = None

        # set to None if institution_name (nullable) is None
        # and model_fields_set contains the field
        if self.institution_name is None and "institution_name" in self.model_fields_set:
            _dict['institution_name'] = None

        # set to None if external_id (nullable) is None
        # and model_fields_set contains the field
        if self.external_id is None and "external_id" in self.model_fields_set:
            _dict['external_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ManualAccountObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "type": obj.get("type"),
            "subtype": obj.get("subtype"),
            "display_name": obj.get("display_name"),
            "balance": obj.get("balance"),
            "balance_as_of": obj.get("balance_as_of"),
            "closed_on": obj.get("closed_on"),
            "currency": obj.get("currency"),
            "institution_name": obj.get("institution_name"),
            "external_id": obj.get("external_id"),
            "exclude_from_transactions": obj.get("exclude_from_transactions"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at")
        })
        return _obj



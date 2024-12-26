# coding: utf-8

"""
Lunch Money API - v2

This is a version of the Lunch Money API described using the the OpenAPI 3.X specification.  The goal of this project is to validate an \"API Design First\" approach for the Lunch Money API, which should allow us to gather developer feedback prior to implementation in order to develop API endpoints more quickly.  This version of the API will differ from the existing v1 beta version. For more information on the changes please see the [v2 API Changelog](https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2/changelog)  Some useful links: - [Current v1 Lunch Money API Documentation](https://lunchmoney.dev) - [v2 API Changelog](https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2/changelog) - [OpenAPI API YAML Specification](https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2/openapi/) - [Awesome Lunch Money Projects](https://lunchmoney.dev/#awesome-projects)

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
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictBool,
    StrictFloat,
    StrictInt,
    StrictStr,
    field_validator,
)
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from lunchable.models.currency_enum import CurrencyEnum
from typing import Set
from typing_extensions import Self


class TransactionObject(BaseModel):
    """
    TransactionObject
    """  # noqa: E501

    id: StrictInt = Field(
        description="System created unique identifier for transaction"
    )
    var_date: date = Field(
        description="Date of transaction in ISO 8601 format", alias="date"
    )
    amount: StrictStr = Field(
        description="Amount of the transaction in numeric format to 4 decimal places"
    )
    currency: CurrencyEnum = Field(
        description="Three-letter lowercase currency code of the transaction in ISO 4217 format"
    )
    to_base: Union[StrictFloat, StrictInt] = Field(
        description="The amount converted to the user's primary currency. If the multi-currency feature is not being used, to_base and amount will be the same."
    )
    recurring_id: Optional[StrictInt] = Field(
        description="The unique identifier of the associated recurring item that this transaction matched.  If the recurring item changed properties of this transaction, an `overrides` property with details on what was overridden will be include in the transaction object.  If no `overrides` property exists when there is a `recurring_id` it means that the recurring_item is still in the suggested state, or that it does not contain any rules to override transaction properties."
    )
    overrides: Optional[TransactionOverridesObject]
    payee: Annotated[str, Field(min_length=0, strict=True, max_length=140)] = Field(
        description="Name of payee set by the user, the financial institution, or by a matched recurring item. This will match the value displayed in payee field on the transactions page in the GUI. "
    )
    category_id: Optional[StrictInt] = Field(
        description="Unique identifier of associated category set by the user or by a matched recurring_item.<br> Category details can be obtained by passing the value of this property to the [Get A Single Category](../operations/getCategoryById) API"
    )
    notes: Optional[
        Annotated[str, Field(min_length=0, strict=True, max_length=350)]
    ] = Field(
        description="Any transaction notes set by the user or by a matched recurring item. This will match the value displayed in notes field on the transactions page in the GUI. "
    )
    status: StrictStr = Field(
        description="Status of the transaction: - `reviewed`: User has reviewed the transaction, or it was automatically marked as reviewed due to reviewed recurring_item logic - `unreviewed`: User has not reviewed the transaction and it does not match any reviewed recurring_items. - `delete_pending`: The synced account deleted this transaction after it was updated by the user.  Requires manual intervention. - `pending`: Transaction is still pending with the synced institution (not posted). "
    )
    is_pending: StrictBool = Field(
        description="Denotes if the transaction is pending (not posted). Applies only to transactions in synced accounts and will always be false for transactions associated with manual accounts."
    )
    created_at: datetime = Field(
        description="The date and time of when the transaction was created (in the ISO 8601 extended format)."
    )
    updated_at: datetime = Field(
        description="The date and time of when the transaction was last updated (in the ISO 8601 extended format)."
    )
    is_parent: Optional[StrictBool] = Field(
        default=None,
        description="If true this transaction has been split into two or more other transactions.  By default parent transactions are not returned in call to `GET /transactions` but they can be queried directly by their ID.",
    )
    children: Optional[List[StrictStr]] = Field(
        default=None,
        description="Exists only for transactions which are the parent of a split transaction, and contains a list of the associated transactions that it was split into. By default parent transactions are not returned in a `GET /transactions` API call, but can be examined via a subsequent call to `GET /transactions{id}`, where the value of `parent_id` field of a split transaction is the requested transaction.",
    )
    parent_id: Optional[List[Union[StrictFloat, StrictInt]]] = Field(
        description="A transaction ID if this is a split transaction. Denotes the transaction ID of the original, or parent, transaction.  Is null if this is not a split transaction"
    )
    is_group: StrictBool = Field(
        description="True if this transaction represents a group of transactions. If so, amount and currency represent the totalled amount of transactions bearing this transaction’s id as their group_id. Amount is calculated based on the user’s primary currency."
    )
    group_id: Optional[StrictInt] = Field(
        description="Is set if this transaction is part of a group. Denotes the ID of the grouped transaction this is now included in. By default the transactions that were grouped are not returned in a call to `GET /transactions` but they can be queried directly by calling the `GET /transactions/group/{id}`, where the id passed is associated with a transaction where the `is_group` attribute is true"
    )
    manual_account_id: Optional[StrictInt] = Field(
        description='The unique identifier of the manual account associated with this transaction.  This will always be null if this transaction is associated with a synced account or if this transaction has no associated account and appears as a "Cash Transaction" in the Lunch Money GUI.'
    )
    plaid_account_id: Optional[StrictInt] = Field(
        description='The unique identifier of the plaid account associated with this transaction.  This will always be null if this transaction is associated with a manual account or if this transaction has no associated account and appears as a "Cash Transaction" in the Lunch Money GUI.'
    )
    tag_ids: List[StrictInt] = Field(
        description="A list of tag_ids for the tags associated with this transaction.  If the transaction has no tags this will be an empty list.<br> Tag details can be obtained by passing the value of this attribute as the `ids` query parameter to the [List Tags](../operations/getTags) API"
    )
    source: Optional[StrictStr] = Field(
        description='Source of the transaction: - `api`: Transaction was added by a call to the [POST /transactions](../operations/createTransaction) API - `csv`: Transaction was added via a CSV Import - `manual`: Transaction was created via the "Add to Cash" button on the Transactions page - `merge`: Transactions were originally in an account that was merged into another account - `plaid`: Transaction came from a Financial Institution synced via Plaid - `recurring`: Transaction was created from the Recurring page - `rule`: Transaction was created by a rule to split a transaction - `split`: This is a transaction created by splitting another transaction - `user`: This is a legacy value and is replaced by either csv or manual '
    )
    external_id: Optional[
        Annotated[str, Field(min_length=0, strict=True, max_length=75)]
    ] = Field(
        description="A user-defined external ID for any transaction that was added via csv import, `POST /transactions` API call, or manually added via the Lunch Money GUI.  No external ID exists for transactions associated with synced accounts, and they cannot be added. For transactions associated with manual accounts, the external ID must be unique as attempts to add a subsequent transaction with the same external_id and manual_account_id will be flagged as duplicates and fail."
    )
    plaid_metadata: Optional[Dict[str, Any]] = Field(
        default=None,
        description="If requested, the transaction's plaid_metadata that came when this transaction was obtained. This will be a json object, but the schema is variable. This will only be present for transactions associated with a plaid account.",
    )
    custom_metadata: Optional[Dict[str, Any]] = Field(
        default=None,
        description="If requested, the transaction's custom_metadata that was included when the transaction was inserted via the API. This will be a json object, but the schema is variable. This will only be present for transactions associated with a manual account.",
    )
    __properties: ClassVar[List[str]] = [
        "id",
        "date",
        "amount",
        "currency",
        "to_base",
        "recurring_id",
        "overrides",
        "payee",
        "category_id",
        "notes",
        "status",
        "is_pending",
        "created_at",
        "updated_at",
        "is_parent",
        "children",
        "parent_id",
        "is_group",
        "group_id",
        "manual_account_id",
        "plaid_account_id",
        "tag_ids",
        "source",
        "external_id",
        "plaid_metadata",
        "custom_metadata",
    ]

    @field_validator("status")
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(["reviewed", "unreviewed", "delete_pending", "pending"]):
            raise ValueError(
                "must be one of enum values ('reviewed', 'unreviewed', 'delete_pending', 'pending')"
            )
        return value

    @field_validator("source")
    def source_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(
            [
                "api",
                "csv",
                "manual",
                "merge",
                "plaid",
                "recurring",
                "rule",
                "split",
                "user",
            ]
        ):
            raise ValueError(
                "must be one of enum values ('api', 'csv', 'manual', 'merge', 'plaid', 'recurring', 'rule', 'split', 'user')"
            )
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
        """Create an instance of TransactionObject from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of overrides
        if self.overrides:
            _dict["overrides"] = self.overrides.to_dict()
        # set to None if recurring_id (nullable) is None
        # and model_fields_set contains the field
        if self.recurring_id is None and "recurring_id" in self.model_fields_set:
            _dict["recurring_id"] = None

        # set to None if overrides (nullable) is None
        # and model_fields_set contains the field
        if self.overrides is None and "overrides" in self.model_fields_set:
            _dict["overrides"] = None

        # set to None if category_id (nullable) is None
        # and model_fields_set contains the field
        if self.category_id is None and "category_id" in self.model_fields_set:
            _dict["category_id"] = None

        # set to None if notes (nullable) is None
        # and model_fields_set contains the field
        if self.notes is None and "notes" in self.model_fields_set:
            _dict["notes"] = None

        # set to None if parent_id (nullable) is None
        # and model_fields_set contains the field
        if self.parent_id is None and "parent_id" in self.model_fields_set:
            _dict["parent_id"] = None

        # set to None if group_id (nullable) is None
        # and model_fields_set contains the field
        if self.group_id is None and "group_id" in self.model_fields_set:
            _dict["group_id"] = None

        # set to None if manual_account_id (nullable) is None
        # and model_fields_set contains the field
        if (
            self.manual_account_id is None
            and "manual_account_id" in self.model_fields_set
        ):
            _dict["manual_account_id"] = None

        # set to None if plaid_account_id (nullable) is None
        # and model_fields_set contains the field
        if (
            self.plaid_account_id is None
            and "plaid_account_id" in self.model_fields_set
        ):
            _dict["plaid_account_id"] = None

        # set to None if source (nullable) is None
        # and model_fields_set contains the field
        if self.source is None and "source" in self.model_fields_set:
            _dict["source"] = None

        # set to None if external_id (nullable) is None
        # and model_fields_set contains the field
        if self.external_id is None and "external_id" in self.model_fields_set:
            _dict["external_id"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "date": obj.get("date"),
                "amount": obj.get("amount"),
                "currency": obj.get("currency"),
                "to_base": obj.get("to_base"),
                "recurring_id": obj.get("recurring_id"),
                "overrides": TransactionOverridesObject.from_dict(obj["overrides"])
                if obj.get("overrides") is not None
                else None,
                "payee": obj.get("payee"),
                "category_id": obj.get("category_id"),
                "notes": obj.get("notes"),
                "status": obj.get("status"),
                "is_pending": obj.get("is_pending"),
                "created_at": obj.get("created_at"),
                "updated_at": obj.get("updated_at"),
                "is_parent": obj.get("is_parent"),
                "children": obj.get("children"),
                "parent_id": obj.get("parent_id"),
                "is_group": obj.get("is_group"),
                "group_id": obj.get("group_id"),
                "manual_account_id": obj.get("manual_account_id"),
                "plaid_account_id": obj.get("plaid_account_id"),
                "tag_ids": obj.get("tag_ids"),
                "source": obj.get("source"),
                "external_id": obj.get("external_id"),
                "plaid_metadata": obj.get("plaid_metadata"),
                "custom_metadata": obj.get("custom_metadata"),
            }
        )
        return _obj

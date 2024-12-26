# coding: utf-8

"""
Lunch Money API - v2

This is a version of the Lunch Money API described using the the OpenAPI 3.X specification.  The goal of this project is to validate an \"API Design First\" approach for the Lunch Money API, which should allow us to gather developer feedback prior to implementation in order to develop API endpoints more quickly.  This version of the API will differ from the existing v1 beta version. For more information on the changes please see the [v2 API Changelog](https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2/changelog)  Some useful links: - [Current v1 Lunch Money API Documentation](https://lunchmoney.dev) - [v2 API Changelog](https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2/changelog) - [OpenAPI API YAML Specification](https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2/openapi/) - [Awesome Lunch Money Projects](https://lunchmoney.dev/#awesome-projects)

The version of the OpenAPI document: 2.7.4
Contact: devsupport@lunchmoney.app
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from lunchable.models.create_new_transactions_request import (
    CreateNewTransactionsRequest,
)


class TestCreateNewTransactionsRequest(unittest.TestCase):
    """CreateNewTransactionsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateNewTransactionsRequest:
        """Test CreateNewTransactionsRequest
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `CreateNewTransactionsRequest`
        """
        model = CreateNewTransactionsRequest()
        if include_optional:
            return CreateNewTransactionsRequest(
                transactions = [
                    lunchable.models.insert_transaction_object.insertTransactionObject(
                        date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                        amount = null,
                        currency = null,
                        payee = '',
                        category_id = 56,
                        notes = '',
                        manual_account_id = 56,
                        plaid_account_id = 56,
                        recurring_id = 56,
                        status = 'reviewed',
                        tag_ids = [
                            56
                            ],
                        external_id = '',
                        custom_metadata = { }, )
                    ],
                apply_rules = True,
                skip_duplicates = True,
                skip_balance_update = True
            )
        else:
            return CreateNewTransactionsRequest(
                transactions = [
                    lunchable.models.insert_transaction_object.insertTransactionObject(
                        date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                        amount = null,
                        currency = null,
                        payee = '',
                        category_id = 56,
                        notes = '',
                        manual_account_id = 56,
                        plaid_account_id = 56,
                        recurring_id = 56,
                        status = 'reviewed',
                        tag_ids = [
                            56
                            ],
                        external_id = '',
                        custom_metadata = { }, )
                    ],
        )
        """

    def testCreateNewTransactionsRequest(self):
        """Test CreateNewTransactionsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()

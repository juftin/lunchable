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

from lunchable.models.get_all_recurring200_response import GetAllRecurring200Response


class TestGetAllRecurring200Response(unittest.TestCase):
    """GetAllRecurring200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAllRecurring200Response:
        """Test GetAllRecurring200Response
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `GetAllRecurring200Response`
        """
        model = GetAllRecurring200Response()
        if include_optional:
            return GetAllRecurring200Response(
                recurring_items = [
                    lunchable.models.recurring_object.recurringObject(
                        id = 56,
                        description = '',
                        status = 'suggested',
                        transaction_criteria = lunchable.models.recurring_object_transaction_criteria.recurringObject_transaction_criteria(
                            start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                            end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                            granularity = 'day',
                            quantity = 56,
                            anchor_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                            payee = '',
                            amount = '-80728',
                            currency = '',
                            to_base = 1.337,
                            plaid_account_id = 56,
                            manual_account_id = 56, ),
                        overrides = lunchable.models.recurring_object_overrides.recurringObject_overrides(
                            payee = '',
                            notes = '',
                            category_id = 56, ),
                        matches = lunchable.models.recurring_object_matches.recurringObject_matches(
                            request_start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                            request_end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                            expected_occurrence_dates = [
                                datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date()
                                ],
                            found_transactions = [
                                lunchable.models.recurring_object_matches_found_transactions_inner.recurringObject_matches_found_transactions_inner(
                                    date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                                    transaction_id = 56, )
                                ],
                            missing_transaction_dates = [
                                datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date()
                                ], ),
                        created_by = 56,
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                        source = 'manual', )
                    ]
            )
        else:
            return GetAllRecurring200Response(
        )
        """

    def testGetAllRecurring200Response(self):
        """Test GetAllRecurring200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()

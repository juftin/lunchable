# coding: utf-8

"""
    Lunch Money API - v2

    This is a version of the Lunch Money API described using the the OpenAPI 3.X specification.    The goal of this project is to validate an \"API Design First\" approach for the Lunch Money API, which should allow us to gather developer feedback prior to implementation in order to develop API endpoints more quickly.  This version of the API will differ from the existing v1 beta version. For more information on the changes please see the  [v2 API Changelog](https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2/changelog)  Some useful links: - [Current v1 Lunch Money API Documentation](https://lunchmoney.dev) - [v2 API Changelog](https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2/changelog) - [OpenAPI API YAML Specification](https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2/openapi/) - [Awesome Lunch Money Projects](https://lunchmoney.dev/#awesome-projects)

    The version of the OpenAPI document: 2.7.4
    Contact: devsupport@lunchmoney.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from lunchable.models.get_all_plaid_accounts200_response import GetAllPlaidAccounts200Response

class TestGetAllPlaidAccounts200Response(unittest.TestCase):
    """GetAllPlaidAccounts200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAllPlaidAccounts200Response:
        """Test GetAllPlaidAccounts200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAllPlaidAccounts200Response`
        """
        model = GetAllPlaidAccounts200Response()
        if include_optional:
            return GetAllPlaidAccounts200Response(
                plaid_accounts = [
                    lunchable.models.plaid_account_object.plaidAccountObject(
                        id = 56, 
                        date_linked = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        name = '', 
                        display_name = '', 
                        type = '', 
                        subtype = '', 
                        mask = '', 
                        institution_name = '', 
                        status = 'active', 
                        allow_transaction_modifications = True, 
                        limit = 1.337, 
                        balance = '', 
                        currency = '012', 
                        balance_last_update = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        import_start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        last_import = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_fetch = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        plaid_last_successful_update = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return GetAllPlaidAccounts200Response(
        )
        """

    def testGetAllPlaidAccounts200Response(self):
        """Test GetAllPlaidAccounts200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

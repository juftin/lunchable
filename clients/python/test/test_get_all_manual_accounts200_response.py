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

from lunchable.models.get_all_manual_accounts200_response import GetAllManualAccounts200Response

class TestGetAllManualAccounts200Response(unittest.TestCase):
    """GetAllManualAccounts200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAllManualAccounts200Response:
        """Test GetAllManualAccounts200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAllManualAccounts200Response`
        """
        model = GetAllManualAccounts200Response()
        if include_optional:
            return GetAllManualAccounts200Response(
                manual_accounts = [
                    lunchable.models.manual_account_object.manualAccountObject(
                        id = 56, 
                        name = '0', 
                        type = null, 
                        subtype = '', 
                        display_name = '', 
                        balance = '-80728', 
                        balance_as_of = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        closed_on = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        currency = '012', 
                        institution_name = '0', 
                        external_id = '', 
                        exclude_from_transactions = True, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return GetAllManualAccounts200Response(
        )
        """

    def testGetAllManualAccounts200Response(self):
        """Test GetAllManualAccounts200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

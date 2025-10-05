# lunchable.TransactionsFilesApi

All URIs are relative to *https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2*

| Method                                                                                       | HTTP request                                        | Description                             |
| -------------------------------------------------------------------------------------------- | --------------------------------------------------- | --------------------------------------- |
| [**attach_file_to_transaction**](TransactionsFilesApi.md#attach_file_to_transaction)         | **POST** /transactions/{transaction_id}/attachments | Attach a file to a transaction          |
| [**delete_transaction_attachment**](TransactionsFilesApi.md#delete_transaction_attachment)   | **DELETE** /transactions/attachments/{file_id}      | Delete a file attachment                |
| [**get_transaction_attachment_url**](TransactionsFilesApi.md#get_transaction_attachment_url) | **GET** /transactions/attachments/{file_id}         | Get a url to download a file attachment |

# **attach_file_to_transaction**

> TransactionAttachmentObject attach_file_to_transaction(transaction_id, file, notes=notes)

Attach a file to a transaction

Attaches a file to a transaction. The file must be less than 10MB in size.<br><br> The file will be attached to the transaction and can be downloaded from the link returned by a `GET /transactions/attachments/{file_id}` request.

### Example

-   Api Key Authentication (cookieAuth):
-   Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchable
from lunchable.models.transaction_attachment_object import TransactionAttachmentObject
from lunchable.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = lunchable.Configuration(
    host = "https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerSecurity
configuration = lunchable.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with lunchable.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lunchable.TransactionsFilesApi(api_client)
    transaction_id = 2112150655 # int |
    file = None # bytearray | The file to attach.  Supported file types: - image/jpeg - image/png - application/pdf - image/heic - image/heif  Maximum file size: 10MB
    notes = 'notes_example' # str | Optional notes about the file (optional)

    try:
        # Attach a file to a transaction
        api_response = api_instance.attach_file_to_transaction(transaction_id, file, notes=notes)
        print("The response of TransactionsFilesApi->attach_file_to_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsFilesApi->attach_file_to_transaction: %s\n" % e)
```

### Parameters

| Name               | Type          | Description                                                                                                                            | Notes      |
| ------------------ | ------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **transaction_id** | **int**       |                                                                                                                                        |
| **file**           | **bytearray** | The file to attach. Supported file types: - image/jpeg - image/png - application/pdf - image/heic - image/heif Maximum file size: 10MB |
| **notes**          | **str**       | Optional notes about the file                                                                                                          | [optional] |

### Return type

[**TransactionAttachmentObject**](TransactionAttachmentObject.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

-   **Content-Type**: multipart/form-data
-   **Accept**: application/json

### HTTP response details

| Status code | Description                                                                         | Response headers |
| ----------- | ----------------------------------------------------------------------------------- | ---------------- |
| **200**     | File attached successfully                                                          | -                |
| **400**     | Invalid request                                                                     | -                |
| **401**     | Unauthorized. This error occurs when an invalid API token is passed to the request. | -                |
| **404**     | Transaction not found                                                               | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transaction_attachment**

> delete_transaction_attachment(file_id)

Delete a file attachment

Deletes a file attachment from a transaction.

### Example

-   Api Key Authentication (cookieAuth):
-   Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchable
from lunchable.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = lunchable.Configuration(
    host = "https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerSecurity
configuration = lunchable.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with lunchable.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lunchable.TransactionsFilesApi(api_client)
    file_id = 1234567890 # int |

    try:
        # Delete a file attachment
        api_instance.delete_transaction_attachment(file_id)
    except Exception as e:
        print("Exception when calling TransactionsFilesApi->delete_transaction_attachment: %s\n" % e)
```

### Parameters

| Name        | Type    | Description | Notes |
| ----------- | ------- | ----------- | ----- |
| **file_id** | **int** |             |

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

-   **Content-Type**: Not defined
-   **Accept**: application/json

### HTTP response details

| Status code | Description                                                                         | Response headers |
| ----------- | ----------------------------------------------------------------------------------- | ---------------- |
| **204**     | File attachment successfully deleted                                                | -                |
| **401**     | Unauthorized. This error occurs when an invalid API token is passed to the request. | -                |
| **404**     | File attachment not found                                                           | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_attachment_url**

> GetTransactionAttachmentUrl200Response get_transaction_attachment_url(file_id)

Get a url to download a file attachment

Returns a signed url that can be used to download the file attachment.

### Example

-   Api Key Authentication (cookieAuth):
-   Bearer (JWT) Authentication (bearerSecurity):

```python
import lunchable
from lunchable.models.get_transaction_attachment_url200_response import GetTransactionAttachmentUrl200Response
from lunchable.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = lunchable.Configuration(
    host = "https://lm-v2-api-mock-data-f24357049a1b.herokuapp.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerSecurity
configuration = lunchable.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with lunchable.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lunchable.TransactionsFilesApi(api_client)
    file_id = 1234567890 # int |

    try:
        # Get a url to download a file attachment
        api_response = api_instance.get_transaction_attachment_url(file_id)
        print("The response of TransactionsFilesApi->get_transaction_attachment_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsFilesApi->get_transaction_attachment_url: %s\n" % e)
```

### Parameters

| Name        | Type    | Description | Notes |
| ----------- | ------- | ----------- | ----- |
| **file_id** | **int** |             |

### Return type

[**GetTransactionAttachmentUrl200Response**](GetTransactionAttachmentUrl200Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerSecurity](../README.md#bearerSecurity)

### HTTP request headers

-   **Content-Type**: Not defined
-   **Accept**: application/json

### HTTP response details

| Status code | Description                                                                         | Response headers |
| ----------- | ----------------------------------------------------------------------------------- | ---------------- |
| **200**     | Successfully retrieved the file attachment                                          | -                |
| **401**     | Unauthorized. This error occurs when an invalid API token is passed to the request. | -                |
| **404**     | File attachment not found                                                           | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

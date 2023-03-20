from rest_framework.exceptions import APIException
from rest_framework import status


class AddressCreateException(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "You can only create addresses for yourself."
    default_code = "address_create_exception"


class AddressUpdateException(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "You can only update addresses registered to you."
    default_code = "address_update_exception"


class AddressDeleteException(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "You can only delete addresses registered to you."
    default_code = "address_delete_exception"


class AddressNotFoundException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Address not found."
    default_code = "address_not_Found"


class AddressDeletionFailedException(APIException):
    status_code = 500
    default_detail = "Failed to delete address."
    default_code = "deletion_failed"

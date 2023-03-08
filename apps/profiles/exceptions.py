from rest_framework.exceptions import APIException


class ProfileNotFound(APIException):
    status_code = 404
    default_detail = "Profile not found."


class WrongProfile(APIException):
    status_code = 403
    default_detail = "Attempting to edit Profile not linked to User"

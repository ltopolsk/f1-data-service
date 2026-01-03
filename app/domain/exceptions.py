

class F1AppException(Exception):
    """ Basic class for all exceptions """
    pass


class ExternalApiError(F1AppException):
    """ API does not work or status_code 5xx """
    pass


class ResourceNotFound(F1AppException):
    """ For example Driver does not exist (404) """
    pass

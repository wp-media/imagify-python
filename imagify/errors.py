class ImagifyError(Exception):

    def __init__(self, message=None, context=None):
        super(ImagifyError, self).__init__(message)
        self.message = message
        self.context = context


class AuthenticationError(ImagifyError):
    pass


class BadRequestError(ImagifyError):
    pass


class OverQuotaError(ImagifyError):
    pass


class ServerError(ImagifyError):
    pass


class UnknownError(ImagifyError):
    pass


class UnsupportedMediaType(ImagifyError):
    pass


def raise_errors_on_failure(r):
    if r.status_code == 400:
        detail = r.json().get('detail', False)
        if detail:
            raise BadRequestError(detail)
        raise BadRequestError('Bad Request')
    elif r.status_code == 402:
        raise OverQuotaError("You've consumed all your data")
    elif r.status_code == 415:
        raise UnsupportedMediaType("The file you uploaded is not a valid type")
    elif r.status_code == 500:
        raise ServerError('There is an error on Imagify servers')
    else:
        raise UnknownError('An unknown error occured')

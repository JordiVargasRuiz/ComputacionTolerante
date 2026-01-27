class LoginError(Exception):
    """Error base de autenticación"""
    pass

class EmptyFieldError(LoginError):
    pass

class InvalidCredentialsError(LoginError):
    pass

class AccountLockedError(LoginError):
    pass

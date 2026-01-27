from errors import *
from logger import log_error

USUARIO_CORRECTO = "admin"
PASSWORD_CORRECTA = "1234"

intentos = 0
MAX_INTENTOS = 3

def autenticar(usuario, password):
    global intentos

    try:
        if not usuario or not password:
            raise EmptyFieldError("Campos vacíos")

        assert len(password) >= 4, "Contraseña demasiado corta"

        if usuario != USUARIO_CORRECTO or password != PASSWORD_CORRECTA:
            intentos += 1
            raise InvalidCredentialsError("Credenciales incorrectas")

        intentos = 0
        return True

    except LoginError as e:
        log_error(e)
        if intentos >= MAX_INTENTOS:
            raise AccountLockedError("Cuenta bloqueada")
        raise e

    finally:
        print("Intento de autenticación procesado")

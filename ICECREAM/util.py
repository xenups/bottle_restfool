import secrets

from bottle import request


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


def generate_otp_code():
    return secrets.SystemRandom().randrange(999, 9999)


def strip_path():
    request.environ['PATH_INFO'] = request.environ['PATH_INFO'].rstrip('/')
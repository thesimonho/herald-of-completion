from functools import wraps
from messengers.messenger import Messenger


def informant(notification_method: Messenger):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            notification_method.notify("")
            return result

        return wrapper

    return decorator

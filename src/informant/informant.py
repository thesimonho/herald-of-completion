from functools import wraps
from typing import Union

from informant.messengers import Messenger


def informant(messenger: Union[Messenger, list[Messenger]]):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            if isinstance(messenger, list):
                print(f"Sending notification to {len(messenger)} messengers")
                for method in messenger:
                    method.notify()
            else:
                print(f"Sending notification to {messenger}")
                messenger.notify()

            return result

        return wrapper

    return decorator

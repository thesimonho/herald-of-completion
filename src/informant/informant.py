import traceback
from functools import wraps
from typing import Union

from informant.messengers import Messenger


# NOTE: what should the API look like? message strings to decorator or to messengers?
def informant(messengers: Union[Messenger, list[Messenger]], send_result: bool = False):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                header = f"Task '{func.__name__}' has finished"
                result = func(*args, **kwargs)
                has_errored = False
            except Exception as e:
                header = e
                result = traceback.format_exc()
                has_errored = True

            opts = {"function": func.__name__, "has_errored": has_errored}

            if send_result:
                opts["header"] = str(header)
                # HACK: match for class type desktopmessenger.
                # message needs to be <256 chars, but ONLY for desktop
                opts["message"] = str(result)[:256]
            else:
                status = "successfully." if not has_errored else "with errors."
                opts["header"] = "Task Status"
                opts["message"] = f"Task '{func.__name__}' has finished {status}"

            if isinstance(messengers, list):
                for messenger in messengers:
                    messenger.notify(**opts)
            else:
                messengers.notify(**opts)

            return result

        return wrapper

    return decorator

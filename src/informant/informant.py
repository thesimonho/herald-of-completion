import traceback
from functools import wraps
from typing import Any, Callable, Union

from .messengers import Messenger

# NOTE: should 'messengers' actually be 'targets'?


class Informant:
    def __init__(self, config=None):
        self.config = config

    def __call__(
        self, messengers: Union[Messenger, list[Messenger]], send_result: bool = True
    ) -> Callable:
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args: Any, **kwargs: Any):
                # NOTE: should this be a struct/dataclass?
                vals = {
                    "function": func.__name__,
                    "header": "Task Status",
                    "has_errored": None,
                }

                try:
                    result = func(*args, **kwargs)

                    vals["message"] = f"Task '{func.__name__}' finished successfully."
                    vals["result"] = str(result)
                    vals["has_errored"] = False
                    self._notify_messengers(messengers, vals)

                    return result
                except Exception as e:
                    vals["message"] = f"Task '{func.__name__}' finished with errors."
                    vals["result"] = f"{e}\n\n{traceback.format_exc()}"
                    vals["has_errored"] = True
                    self._notify_messengers(messengers, vals)

                    raise e

            return wrapper

        return decorator

    def _notify_messengers(self, messengers, values) -> None:
        if isinstance(messengers, list):
            for messenger in messengers:
                messenger.notify(**values)
        else:
            messengers.notify(**values)

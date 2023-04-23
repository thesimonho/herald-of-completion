import traceback
from functools import wraps
from typing import Any, Callable, Union

from .types import Messenger, TaskInfo

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
                info = TaskInfo(
                    name=func.__name__,
                    header="Task Status",
                )

                try:
                    result = func(*args, **kwargs)

                    info.message = f"Task '{func.__name__}' finished successfully."
                    info.has_errored = False
                    if send_result:
                        info.result = str(result)
                    self._notify_messengers(messengers, info)

                    return result
                except Exception as e:
                    info.message = f"Task '{func.__name__}' finished with errors."
                    info.has_errored = True
                    if send_result:
                        info.result = f"{e}\n\n{traceback.format_exc()}"
                    self._notify_messengers(messengers, info)

                    raise e

            return wrapper

        return decorator

    def _notify_messengers(self, messengers, info: TaskInfo) -> None:
        if isinstance(messengers, list):
            for messenger in messengers:
                messenger.notify(info)
        else:
            messengers.notify(info)

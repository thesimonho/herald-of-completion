import traceback
from functools import wraps
from typing import Any, Callable, List, Union

from dotenv import dotenv_values

from .types import Messenger, TaskInfo

# NOTE: observer pattern?
# TODO: allow customizable messages for each messenger


class Herald:
    def __init__(self, secrets: str = ".env"):
        self.secrets: dict = dotenv_values(secrets)

    def __call__(
        self, messengers: Union[Messenger, List[Messenger]], send_result: bool = True
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

                    info.message = f"Task `{func.__name__}` has finished successfully."
                    info.has_errored = False
                    if send_result:
                        info.result = str(result)
                    self._notify_messengers(messengers, info)

                    return result
                except Exception as e:
                    info.message = f"Task `{func.__name__}` has finished with errors."
                    info.has_errored = True
                    if send_result:
                        info.result = str(traceback.format_exc())
                    self._notify_messengers(messengers, info)

                    raise e

            return wrapper

        return decorator

    def _notify_messengers(
        self, messengers: Union[Messenger, List[Messenger]], info: TaskInfo
    ) -> None:
        if isinstance(messengers, list):
            for messenger in messengers:
                self._set_messenger_secrets(messenger)
                messenger.notify(info)
        else:
            self._set_messenger_secrets(messengers)
            messengers.notify(info)

    def _set_messenger_secrets(self, messenger: Messenger) -> None:
        messenger.set_secrets(self.secrets)

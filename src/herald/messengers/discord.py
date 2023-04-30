"""Module for the Discord messenger.

This module defines the Discord messenger class, which is used to send
notifications using Discord webhooks to specific servers and channels.

Typical usage example:

.. code-block:: python
    
   from herald.decorators import Herald
   from herald.messengers import DiscordMessenger

   herald = Herald(".env")
   discord = DiscordMessenger()

   @herald(discord)
   def my_function():
       pass
"""

import requests

from ..types import Messenger, TaskInfo
from ..utils import build_arg_string, build_kwarg_string


# TODO: validate url. add test
# TODO: check url exists (and correct) before notifying
class DiscordMessenger(Messenger):
    """A class used to send Discord notifications.

    Args:
        webhook_url: String containing the URL for the Discord webhook.
    """

    def __init__(self):
        """Initializes the DiscordMessenger class."""
        self.webhook_url: str = ""

    def set_secrets(self, secrets: dict) -> None:
        """Sets the secrets for the DiscordMessenger class.

        The only secret required is the webhook URL.

        Args:
            secrets: A dictionary containing the secrets to be used by the messenger.
        """
        self.webhook_url = secrets["WEBHOOK_URL"]

    def notify(self, info: TaskInfo) -> None:
        """Constructs and sends a Discord notification.

        Args:
            info: TaskInfo object containing information about the task that was run. \
            Contents should be used to construct the notification.

        Raises:
            HTTPError: An error occurred while making the HTTP request.
        """
        msg_content = f"**{info.header}**\n"

        if info.send_args:
            args = build_arg_string(info.args)
            kwargs = build_kwarg_string(info.kwargs)
            call = f"{info.name}({args}, {kwargs})"
        else:
            call = f"{info.name}()"

        if info.has_errored:
            msg_content += (
                f"Task has failed with an error.\n\nFunction call:\n```{call}```"
            )
        else:
            msg_content += (
                f"Task has completed successfully.\n\nFunction call:\n```{call}```"
            )

        if info.send_result:
            msg_content += f"\nResult:\n```{info.result}```"

        data = {
            "content": msg_content,
        }

        result = requests.post(self.webhook_url, json=data)

        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise e

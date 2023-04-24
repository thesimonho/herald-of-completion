import requests

from ..types import Messenger, TaskInfo


class DiscordMessenger(Messenger):
    def __init__(self):
        self.webhook_url = ""

    def set_secrets(self, secrets: dict) -> None:
        self.webhook_url = secrets["WEBHOOK_URL"]

    def notify(self, info: TaskInfo) -> None:
        data = {
            "content": f"**{info.header}**\n{info.message}\n```{info.result}```",
        }

        result = requests.post(self.webhook_url, json=data)

        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)

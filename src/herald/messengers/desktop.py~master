from plyer import notification

from ..types import Messenger, TaskInfo


class DesktopMessenger(Messenger):
    def __init__(self):
        pass

    def notify(self, info: TaskInfo) -> None:
        opts = {
            "title": info.header,
            "message": info.message,
            "timeout": 10,
        }
        notification.notify(**opts)

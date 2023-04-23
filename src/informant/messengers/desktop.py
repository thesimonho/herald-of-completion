from plyer import notification

from informant.messengers import Messenger


class DesktopMessenger(Messenger):
    def __init__(self):
        pass

    def notify(self) -> None:
        print("Desktop notification sent")
        kwargs = {
            "title": "title",
            "message": "message",
            "timeout": 5,
        }
        notification.notify(**kwargs)

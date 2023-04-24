from ..types import Messenger, TaskInfo


# TODO: needs to handle both gmail and email more generally
class EmailMessenger(Messenger):
    def __init__(self, recipient, sender, subject, body):
        self.recipient = recipient
        self.sender = sender
        self.subject = subject
        self.body = body

    def set_secrets(self, secrets: dict) -> None:
        pass

    def send_notification(self, info: TaskInfo) -> None:
        pass

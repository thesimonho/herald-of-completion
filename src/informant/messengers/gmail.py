from messenger import Messenger


class EmailNotification(Messenger):
    def __init__(self, recipient, sender, subject, body):
        self.recipient = recipient
        self.sender = sender
        self.subject = subject
        self.body = body

    def send_notification(self):
        pass

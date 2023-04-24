import smtplib
import ssl
from email.message import EmailMessage

from ..types import Messenger, TaskInfo


# TODO: validate email address. probably good to have an email type
class EmailMessenger(Messenger):
    def __init__(self, recipient: str):
        self.recipient = recipient
        self.smtp_server = ""
        self.smtp_port: int = -1
        self.smtp_starttls: bool = False
        self.smtp_user = ""
        self.smtp_password = ""

    def set_secrets(self, secrets: dict) -> None:
        self.smtp_server = secrets["SMTP_SERVER"]
        self.smtp_port = secrets["SMTP_PORT"]
        self.smtp_starttls = secrets["SMTP_STARTTLS"]
        self.smtp_user = secrets["SMTP_USER"]
        self.smtp_password = secrets["SMTP_PASSWORD"]

    def notify(self, info: TaskInfo) -> None:
        msg = EmailMessage()
        msg["Subject"] = f"{info.header}"
        msg.set_content(f"{info.message}\n\n{info.result}")

        context = ssl.create_default_context()
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            try:
                server.ehlo()
                if self.smtp_starttls:
                    server.starttls(context=context)
                server.login(self.smtp_user, self.smtp_password)
                server.send_message(msg, self.smtp_user, self.recipient)
            except Exception as e:
                print(f"Error sending email: {e}")

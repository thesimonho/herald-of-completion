from abc import ABC, abstractmethod


class Messenger(ABC):
    @abstractmethod
    def notify(self, message: str) -> None:
        print(message)

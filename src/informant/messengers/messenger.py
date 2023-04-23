from abc import ABC, abstractmethod


class Messenger(ABC):
    @abstractmethod
    def notify(self) -> None:
        pass

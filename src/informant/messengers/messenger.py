from abc import ABC, abstractmethod


class Messenger(ABC):
    # HACK: **kwargs feels a bit dirty as it becomes hard to type check
    # How to do this since different messengers require different opts?
    @abstractmethod
    def notify(self, **kwargs) -> None:
        pass

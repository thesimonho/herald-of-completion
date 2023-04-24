"""Defines all types, base classes, and dataclasses used in the package."""
from abc import ABC, abstractmethod
from dataclasses import dataclass

# NOTE: dataclass for secrets?


@dataclass
class TaskInfo:
    """Dataclass that holds information about a task."""

    name: str
    header: str
    message: str = ""
    result: str = ""
    has_errored: bool = False


class Messenger(ABC):
    """Abstract base class for all messengers."""

    @abstractmethod
    def set_secrets(self, secrets: dict) -> None:
        pass

    @abstractmethod
    def notify(self, info: TaskInfo) -> None:
        pass

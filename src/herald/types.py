"""Defines all types, base classes, and dataclasses used in the package."""
from abc import ABC, abstractmethod
from dataclasses import dataclass


class Messenger(ABC):
    """Abstract base class for all messengers."""

    @abstractmethod
    def notify(self, info) -> None:
        pass


@dataclass
class TaskInfo:
    """Dataclass that holds information about a task."""

    name: str
    header: str
    message: str = ""
    result: str = ""
    has_errored: bool = False

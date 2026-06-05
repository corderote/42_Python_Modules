from typing import Any
from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> Any:
        pass


class TransformCapability(ABC):
    @abstractmethod
    def transform(self) -> Any:
        pass

    @abstractmethod
    def revert(self) -> Any:
        pass

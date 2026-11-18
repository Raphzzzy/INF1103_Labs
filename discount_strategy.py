from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    """Interchangeable behaviour used by Order (Strategy pattern)."""

    @abstractmethod
    def apply(self, total: float) -> float:
        pass

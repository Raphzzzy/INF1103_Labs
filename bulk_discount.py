from math import isfinite

from discount_strategy import DiscountStrategy


class BulkDiscount(DiscountStrategy):
    def __init__(self, threshold: float, amount: float) -> None:
        if not isfinite(threshold) or threshold <= 0:
            raise ValueError("Bulk threshold must be greater than zero.")
        if not isfinite(amount) or amount < 0:
            raise ValueError("Bulk amount cannot be negative.")
        self.threshold = threshold
        self.amount = amount

    def apply(self, total: float) -> float:
        return max(0.0, total - self.amount) if total >= self.threshold else total

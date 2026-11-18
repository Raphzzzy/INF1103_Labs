from discount_strategy import DiscountStrategy


class StudentDiscount(DiscountStrategy):
    """Fourth discount strategy: five percent off with no changes to Order."""

    def apply(self, total: float) -> float:
        return total * 0.95

from discount_strategy import DiscountStrategy
from no_discount import NoDiscount
from order_line import OrderLine


class Order:
    """Owns its order lines and uses a replaceable discount strategy."""

    def __init__(self, order_id: str, discount: DiscountStrategy | None = None) -> None:
        if not order_id:
            raise ValueError("Order ID must not be empty.")
        self.order_id = order_id
        self.order_lines: list[OrderLine] = []
        self.discount: DiscountStrategy = NoDiscount()
        if discount is not None:
            self.set_discount(discount)

    def add_line(self, line: OrderLine) -> None:
        if not isinstance(line, OrderLine):
            raise TypeError("An order can only contain OrderLine objects.")
        self.order_lines.append(line)

    def set_discount(self, discount: DiscountStrategy) -> None:
        if not isinstance(discount, DiscountStrategy):
            raise TypeError("Discount must be a DiscountStrategy.")
        self.discount = discount

    def calculate_total(self) -> float:
        total = sum(line.calculate_subtotal() for line in self.order_lines)
        return self.discount.apply(total)

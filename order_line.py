from product import Product


class OrderLine:
    """An order line references one product and owns its order quantity."""

    def __init__(self, product: Product, quantity: int) -> None:
        if not isinstance(product, Product):
            raise TypeError("OrderLine requires a Product.")
        self.product = product
        self.quantity = quantity

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, value: int) -> None:
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
            raise ValueError("Quantity must be greater than zero (whole number).")
        self._quantity = value

    def calculate_subtotal(self) -> float:
        return self.product.price * self.quantity

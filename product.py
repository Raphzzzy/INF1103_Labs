from __future__ import annotations

from abc import ABC, abstractmethod
from math import isfinite

from supplier import Supplier


class Product(ABC):
    """Common product API; all product types keep the same validation rules."""

    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock_quantity: int,
        supplier: Supplier,
    ) -> None:
        if not isinstance(product_id, str) or not product_id.strip():
            raise ValueError("Product ID must not be empty.")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Product name must not be empty.")
        if not isinstance(supplier, Supplier):
            raise ValueError("Supplier must be a Supplier object.")
        self.product_id = product_id
        self.name = name
        self.supplier = supplier
        self.price = price
        self.stock_quantity = stock_quantity

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        try:
            price = float(value)
        except (ValueError, TypeError) as exc:
            raise ValueError("Product price must be a number greater than zero.") from exc
        if not isfinite(price) or price <= 0:
            raise ValueError("Product price must be greater than zero.")
        self._price = price

    @property
    def stock_quantity(self) -> int:
        return self._stock_quantity

    @stock_quantity.setter
    def stock_quantity(self, value: int) -> None:
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError("Stock quantity must be a whole number.")
        if value < 0:
            raise ValueError("Stock quantity cannot be negative.")
        self._stock_quantity = value

    @abstractmethod
    def fulfilment_method(self) -> str:
        """Concrete products provide their own fulfilment behaviour."""
        raise NotImplementedError

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}({self.product_id!r}, {self.name!r}, "
            f"price={self.price}, stock_quantity={self.stock_quantity})"
        )

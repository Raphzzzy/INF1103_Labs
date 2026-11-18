from digital_product import DigitalProduct
from physical_product import PhysicalProduct
from product import Product
from supplier import Supplier


class ProductFactory:
    """The only production-code location selecting a concrete Product class."""

    @staticmethod
    def create(
        product_type: str,
        product_id: str,
        name: str,
        price: float,
        stock_quantity: int,
        supplier: Supplier,
    ) -> Product:
        if product_type == "physical":
            return PhysicalProduct(product_id, name, price, stock_quantity, supplier)
        elif product_type == "digital":
            return DigitalProduct(product_id, name, price, stock_quantity, supplier)
        else:
            raise ValueError(f"Unknown product type: {product_type}")

from product import Product


class Inventory:
    """Stores Product references (aggregation, not lifetime ownership)."""

    def __init__(self) -> None:
        self.products: dict[str, Product] = {}

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Inventory only accepts Product objects.")
        if product.product_id in self.products:
            raise ValueError(f"Duplicate product ID: {product.product_id}")
        self.products[product.product_id] = product

    def get_product(self, product_id: str) -> Product:
        return self.products[product_id]

    def list_products(self) -> list[Product]:
        return list(self.products.values())

    def __len__(self) -> int:
        return len(self.products)

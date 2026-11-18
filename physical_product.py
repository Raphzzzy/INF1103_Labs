from product import Product


class PhysicalProduct(Product):
    def fulfilment_method(self) -> str:
        return "Ship the physical item"

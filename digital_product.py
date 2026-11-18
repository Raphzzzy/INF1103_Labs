from product import Product


class DigitalProduct(Product):
    def fulfilment_method(self) -> str:
        return "Provide a digital download"

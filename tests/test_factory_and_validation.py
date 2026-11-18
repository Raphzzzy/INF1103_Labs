import pytest

from digital_product import DigitalProduct
from inventory import Inventory
from order import Order
from order_line import OrderLine
from physical_product import PhysicalProduct
from product import Product
from product_factory import ProductFactory


def create(supplier, kind="physical", price=10.0, stock=2, product_id="P1"):
    return ProductFactory.create(kind, product_id, "Item", price, stock, supplier)


def test_factory_produces_physical_and_digital(supplier):
    a = create(supplier)
    b = create(supplier, kind="digital", product_id="D1")
    assert isinstance(a, PhysicalProduct)
    assert isinstance(b, DigitalProduct)
    assert isinstance(a, Product)
    assert isinstance(b, Product)


def test_product_types_have_polymorphic_fulfilment(supplier):
    a = create(supplier)
    b = create(supplier, kind="digital", product_id="D1")
    assert "Ship" in a.fulfilment_method()
    assert "download" in b.fulfilment_method()


def test_factory_raises_on_unknown_type(supplier):
    with pytest.raises(ValueError, match="Unknown product type: service"):
        create(supplier, kind="service")


@pytest.mark.parametrize("price", [0, -1, float("nan"), float("inf"), "abc"])
def test_prices_must_be_finite_and_positive(supplier, price):
    with pytest.raises(ValueError, match="price"):
        create(supplier, price=price)


@pytest.mark.parametrize("stock", [-1, 2.5, "five", True])
def test_stock_must_be_nonnegative_integer(supplier, stock):
    with pytest.raises(ValueError, match="Stock"):
        create(supplier, stock=stock)


def test_digital_product_cannot_bypass_base_stock_validation(supplier):
    with pytest.raises(ValueError, match="Stock"):
        create(supplier, kind="digital", stock=-1)


def test_product_rejects_invalid_mutations(product):
    with pytest.raises(ValueError):
        product.price = -5
    with pytest.raises(ValueError):
        product.stock_quantity = -1
    assert product.price == 25
    assert product.stock_quantity == 12


@pytest.mark.parametrize("qty", [0, -1, 1.5, "3", True])
def test_orderline_requires_positive_whole_quantity(product, qty):
    with pytest.raises(ValueError, match="Quantity"):
        OrderLine(product, qty)


def test_orderline_mutation_requires_valid_quantity(product):
    line = OrderLine(product, 2)
    with pytest.raises(ValueError):
        line.quantity = 0
    assert line.quantity == 2


def test_orderline_calculates_subtotal(product):
    assert OrderLine(product, 3).calculate_subtotal() == 75


def test_inventory_adds_and_retrieves_product(product):
    inventory = Inventory()
    inventory.add_product(product)
    assert inventory.get_product(product.product_id) is product
    assert len(inventory) == 1


def test_inventory_rejects_duplicate_ids(product):
    inventory = Inventory()
    inventory.add_product(product)
    with pytest.raises(ValueError, match="Duplicate"):
        inventory.add_product(product)


def test_order_composes_orderlines(product):
    order = Order("O1")
    order.add_line(OrderLine(product, 2))
    assert len(order.order_lines) == 1
    assert order.calculate_total() == 50

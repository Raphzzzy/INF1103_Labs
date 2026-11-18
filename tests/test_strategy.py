import pytest

from bulk_discount import BulkDiscount
from discount_strategy import DiscountStrategy
from no_discount import NoDiscount
from order import Order
from order_line import OrderLine
from percentage_discount import PercentageDiscount
from student_discount import StudentDiscount


def test_order_defaults_to_no_discount(product):
    order = Order("O1")
    order.add_line(OrderLine(product, 10))
    assert isinstance(order.discount, NoDiscount)
    assert order.calculate_total() == pytest.approx(250)


def test_bulk_then_percentage_change_same_order(product):
    order = Order("O1", BulkDiscount(200, 20))
    order.add_line(OrderLine(product, 10))
    assert order.calculate_total() == pytest.approx(230)
    order.set_discount(PercentageDiscount(10))
    assert order.calculate_total() == pytest.approx(225)


def test_bulk_below_threshold(product):
    order = Order("O1", BulkDiscount(200, 20))
    order.add_line(OrderLine(product, 1))
    assert order.calculate_total() == pytest.approx(25)


def test_student_discount_adds_new_option_without_editing_order(product):
    order = Order("O1", StudentDiscount())
    order.add_line(OrderLine(product, 10))
    assert order.calculate_total() == pytest.approx(237.5)


def test_same_discount_object_can_be_shared(product):
    strategy = PercentageDiscount(10)
    first = Order("O1", strategy)
    second = Order("O2", strategy)
    first.add_line(OrderLine(product, 2))
    second.add_line(OrderLine(product, 4))
    assert first.discount is second.discount
    assert first.calculate_total() == pytest.approx(45)
    assert second.calculate_total() == pytest.approx(90)


def test_cannot_instantiate_abstract_strategy():
    with pytest.raises(TypeError):
        DiscountStrategy()


def test_invalid_percentage_and_bulk_settings():
    with pytest.raises(ValueError):
        PercentageDiscount(-10)
    with pytest.raises(ValueError):
        PercentageDiscount(101)
    with pytest.raises(ValueError):
        BulkDiscount(0, 10)
    with pytest.raises(ValueError):
        BulkDiscount(200, -1)


def test_bulk_discount_never_negative():
    assert BulkDiscount(200, 999).apply(250) == 0


def test_empty_order_returns_zero():
    assert Order("O1").calculate_total() == 0


def test_wrong_discount_rejected():
    with pytest.raises(TypeError):
        Order("O1").set_discount("ten")

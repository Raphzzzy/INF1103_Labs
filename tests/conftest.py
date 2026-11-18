import pytest

from product_factory import ProductFactory
from supplier import Supplier


@pytest.fixture
def supplier():
    return Supplier("S001", "School Supplier")


@pytest.fixture
def product(supplier):
    return ProductFactory.create("physical", "P100", "Demo", 25.0, 12, supplier)

import io
from contextlib import redirect_stdout
from pathlib import Path

from csv_loader import load_products
from inventory import Inventory
from product_factory import ProductFactory
from supplier import Supplier


ROOT = Path(__file__).resolve().parents[1]


def test_example_csv_loads_three_and_skips_bad_rows(supplier, capsys):
    inventory = Inventory()
    load_products(str(ROOT / "products.csv"), inventory, supplier)
    out = capsys.readouterr().out
    assert len(inventory) == 3
    assert set(inventory.products) == {"P001", "D001", "P003"}
    assert "Skipping row 4: Unknown product type: service" in out
    assert "Skipping row 5:" in out and "abc" in out
    assert out.endswith("3 products loaded.\nLoad attempt finished.\n")


def test_missing_csv_catches_expected_error(supplier, tmp_path, capsys):
    missing = tmp_path / "not-here.csv"
    inventory = Inventory()
    load_products(str(missing), inventory, supplier)
    assert len(inventory) == 0
    out = capsys.readouterr().out
    assert f"Products file not found: {missing}" in out
    assert "3 products loaded." not in out
    assert out.endswith("Load attempt finished.\n")


def test_malformed_csv_row_skipped_and_continues(supplier, tmp_path, capsys):
    file = tmp_path / "temp.csv"
    file.write_text(
        "product_type,product_id,name,price,stock_quantity\n"
        "physical,P1,Wrong,10\n"
        "digital,D1,Good,7.50,0\n",
        encoding="utf-8"
    )
    inventory = Inventory()
    load_products(str(file), inventory, supplier)
    assert len(inventory) == 1
    assert "Skipping row 2: Expected 5 columns, found 4" in capsys.readouterr().out


def test_duplicate_product_row_is_skipped(supplier, tmp_path, capsys):
    file = tmp_path / "dup.csv"
    file.write_text(
        "product_type,product_id,name,price,stock_quantity\n"
        "physical,P1,First,10,1\n"
        "physical,P1,Second,20,2\n",
        encoding="utf-8"
    )
    inventory = Inventory()
    load_products(str(file), inventory, supplier)
    assert len(inventory) == 1
    assert "Duplicate product ID: P1" in capsys.readouterr().out

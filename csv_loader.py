import csv

from inventory import Inventory
from product_factory import ProductFactory
from supplier import Supplier


def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    """Try/except/else/finally + per-row ValueError recovery, per Lab 9."""
    try:
        file = open(path, newline="", encoding="utf-8-sig")
    except FileNotFoundError:
        print(f"Products file not found: {path}")
    else:
        loaded = 0
        with file:
            reader = csv.reader(file)
            next(reader, None)  # Skip the CSV header.
            for line_no, row in enumerate(reader, start=2):
                try:
                    if len(row) != 5:
                        raise ValueError(f"Expected 5 columns, found {len(row)}")
                    product_type, product_id, name, price_text, stock_text = row
                    price = float(price_text)
                    stock_quantity = int(stock_text)
                    product = ProductFactory.create(
                        product_type, product_id, name, price, stock_quantity, supplier
                    )
                    inventory.add_product(product)
                except ValueError as exc:
                    print(f"Skipping row {line_no}: {exc}")
                    continue
                loaded += 1
        print(f"{loaded} products loaded.")
    finally:
        print("Load attempt finished.")

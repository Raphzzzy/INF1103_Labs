"""Lab 9 runnable demonstration. Use --interactive to try input validation."""

import argparse

from bulk_discount import BulkDiscount
from csv_loader import load_products
from input_helpers import get_positive_float
from inventory import Inventory
from order import Order
from order_line import OrderLine
from percentage_discount import PercentageDiscount
from student_discount import StudentDiscount
from supplier import Supplier


def run_demo(csv_path: str) -> None:
    supplier = Supplier("SUP001", "Example Supply Co")
    inventory = Inventory()
    load_products(csv_path, inventory, supplier)

    if "P001" in inventory.products:
        order = Order("ORDER001", BulkDiscount(200, 20))
        order.add_line(OrderLine(inventory.get_product("P001"), 10))
        print(f"Bulk discount total: {order.calculate_total():.2f}")
        order.set_discount(PercentageDiscount(10))
        print(f"10% discount total: {order.calculate_total():.2f}")
        order.set_discount(StudentDiscount())
        print(f"5% student discount total: {order.calculate_total():.2f}")

    for product in inventory.list_products():
        print(f"{product.product_id}: {product.name} - {product.fulfilment_method()}")


def main() -> None:
    parser = argparse.ArgumentParser(description="INF1103 Lab 9 inventory demonstration")
    parser.add_argument("--products", default="products.csv", help="CSV to load")
    parser.add_argument("--interactive", action="store_true", help="Prompt for a positive price")
    args = parser.parse_args()
    run_demo(args.products)
    if args.interactive:
        print(f"Accepted price: {get_positive_float('Enter a positive price: '):.2f}")


if __name__ == "__main__":
    main()

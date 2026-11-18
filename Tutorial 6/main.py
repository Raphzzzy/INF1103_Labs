
import json
from pathlib import Path

from product import product as Product
from inventory import inventory as Inventory

FILE_PATH = Path("inventory.json")


# Load saved inventory from JSON
def load_inventory():
    inventory = Inventory()

    if not FILE_PATH.exists():
        return inventory

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, dict):
            data = data["products"]

        for item in data:
            product = product(
                item.get("id", item.get("product_id")),
                item["name"],
                float(item["price"]),
                int(item["stock"])
            )
            inventory.add_product(product)

        print("Inventory loaded successfully.")

    except (OSError, json.JSONDecodeError,
            KeyError, TypeError, ValueError) as error:
        print(f"Could not load inventory: {error}")

    return inventory


# Save inventory to JSON
def save_inventory(inventory):
    data = [
        product.to_dict()
        for product in inventory.get_all_products()
    ]

    try:
        with open(FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print("Inventory saved successfully.")

    except OSError as error:
        print(f"Could not save inventory: {error}")


# Main program
def main():
    inventory = load_inventory()

    while True:
        print("\n===== Inventory Management System =====")
        print("1. Display all products")
        print("2. Add a product")
        print("3. Update stock")
        print("4. Search for a product")
        print("5. Save inventory")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        # Option 1: Display all products
        if choice == "1":
            if not inventory.get_all_products():
                print("The inventory is empty.")
            else:
                inventory.display_all()

        # Option 2: Add a product
        elif choice == "2":
            product_id = input("Enter Product ID: ").strip()

            if not product_id:
                print("Product ID cannot be empty.")
                continue

            if inventory.search_product(product_id) is not None:
                print("This product ID already exists.")
                continue

            name = input("Enter Product Name: ").strip()

            if not name:
                print("Product name cannot be empty.")
                continue

            try:
                price = float(input("Enter Price: "))
                stock = int(input("Enter Stock: "))
            except ValueError:
                print("Invalid input. Price must be a number and stock must be an integer.")
                continue

            if price < 0 or stock < 0:
                print("Price and stock cannot be negative.")
                continue

            product = Product(product_id, name, price, stock)
            inventory.add_product(product)

            print("Product added successfully.")

        # Option 3: Update stock
        elif choice == "3":
            product_id = input("Enter Product ID to update: ").strip()
            product = inventory.search_product(product_id)

            if product is None:
                print("Product not found.")
                continue

            try:
                quantity = int(input("Enter new stock quantity: "))
            except ValueError:
                print("Stock must be a whole number.")
                continue

            if quantity < 0:
                print("Stock cannot be negative.")
                continue

            product.update_stock(quantity)
            print("Stock updated successfully.")

        # Option 4: Search product
        elif choice == "4":
            product_id = input("Enter Product ID to search: ").strip()
            product = inventory.search_product(product_id)

            if product is None:
                print("Product not found.")
            else:
                product.display_information()

        # Option 5: Save inventory
        elif choice == "5":
            save_inventory(inventory)

        # Option 6: Exit
        elif choice == "6":
            print("Goodbye! Remember to save your inventory before exiting.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()

def get_valid_input(failed_attempts):
    while True:
        user_input = input("Enter stock quantity (or 'quit' to exit): ")

        if user_input.lower() == "quit":
            return "quit", failed_attempts

        elif user_input.isdigit():
            return int(user_input), failed_attempts

        else:
            failed_attempts += 1
            print("ERROR: Invalid input. Please enter a number or 'quit'.")


def process_delivery(current_total, new_value):
    return current_total + new_value


def generate_report(total_units, failed_attempts):
    print("\n--- Audit Summary ---")
    print("Total units:", total_units)
    print("Failed attempts:", failed_attempts)


# Load previous inventory and transaction history
def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()

            inventory = int(lines[0])

            # Load transaction history
            if len(lines) > 1 and lines[1].strip() != "":
                history_line = lines[1].strip()
                history = history_line.split(",")

                converted_history = []

                for item in history:
                    converted_history.append(int(item))

                history = converted_history
            else:
                history = []

            return inventory, history

    except FileNotFoundError:
        return 0, []


# Save inventory and transaction history
def save_inventory(inventory, history):
    with open("inventory.txt", "w") as file:

        # Save inventory on first line
        file.write(str(inventory) + "\n")

        # Convert transaction numbers into strings
        converted_history = []

        for item in history:
            converted_history.append(str(item))

        # Join them together using commas
        history_text = ",".join(converted_history)

        # Save history on second line
        file.write(history_text)


# --------------------
# Main Program
# --------------------

inventory, history = load_inventory()
failed_attempts = 0

print("Current inventory:", inventory)
print("Transaction history:", history)

while True:

    quantity, failed_attempts = get_valid_input(failed_attempts)

    if quantity == "quit":
        save_inventory(inventory, history)
        break

    inventory = process_delivery(inventory, quantity)

    # Store valid transaction
    history.append(quantity)

    print("Current inventory:", inventory)
    print("Transaction history:", history)


generate_report(inventory, failed_attempts)
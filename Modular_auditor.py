# Function 1: Get and validate user input
def get_valid_input():
    failed_attempts = 0

    while True:
        user_input = input("Enter stock quantity (or 'quit' to exit): ").strip()

        if user_input.lower() == "quit":
            return "quit", failed_attempts

        elif user_input.isdigit():
            return int(user_input), failed_attempts

        else:
            failed_attempts += 1
            print("ERROR: Invalid input. Please enter a positive integer.")


# Function 2: Process the delivery
def process_delivery(current_total, new_value):
    return current_total + new_value


# Function 3: Calculate 10% tax
def calculate_tax(amount):
    return amount * 0.1


# Function 4: Generate the final report
def generate_report(total_units, failed_attempts):
    print("\n--- Audit Summary ---")
    print(f"Total Units Processed: {total_units}")
    print(f"Failed/Rejected Entries: {failed_attempts}")


# Main program
inventory = 0
failed_attempts = 0

while True:
    # Get the quantity and failures from the function
    quantity, new_failed_attempts = get_valid_input()

    # Add any new failed attempts to the overall counter
    failed_attempts += new_failed_attempts

    # Check whether user wants to quit
    if quantity == "quit":
        break

    # Process the valid delivery
    inventory = process_delivery(inventory, quantity)

    # Calculate tax for THIS delivery
    tax = calculate_tax(quantity)

    print(f"Accepted: +{quantity} units. Current Inventory: {inventory}")
    print(f"Tax for this delivery: {tax}")

# Print final report after loop ends
generate_report(inventory, failed_attempts)
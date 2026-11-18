# auditor.py

# Step 1: Initialize tracking variables (State Management)
inventory = 0
failed_entries = 0

# Step 2: Continuous input loop
while True:
    user_input = input("Enter stock quantity (or 'quit' to exit): ").strip()

    # Exit condition
    if user_input.lower() == "quit":
        print("Exiting audit system...")
        break

    # Validation: Check if the entry contains only positive digits
    elif user_input.isdigit():
        quantity = int(user_input)
        inventory += quantity
        print(f"Accepted: +{quantity} units. Current Inventory: {inventory}")

        # Business Rule: Trigger overstock alert if threshold exceeded
        if inventory > 500:
            print(f"\nALERT: Overstock threshold exceeded! Total Inventory: {inventory} units.")
            break

    # Error handling: Catch strings, negative signs, or symbols
    else:
        failed_entries += 1
        print("ERROR: Invalid input. Please enter a positive integer.")

# Step 3: Final Reporting
print("\n--- Audit Summary ---")
print(f"Total Units Processed: {inventory}")
print(f"Failed/Rejected Entries: {failed_entries}")

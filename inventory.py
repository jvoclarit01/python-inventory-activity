# Inventory Management System

item_names = []  # List to store item names
item_prices = {}  # Dictionary to store item prices


def display_menu():
    """Display the inventory menu options"""
    print("\n====== INVENTORY MENU ======")
    print("[1] Add Item")
    print("[2] Update Price")
    print("[3] Exit")


def add_item():
    """Add a new item to the inventory"""
    try:
        # Get item name
        name = input("Enter item name: ").strip()

        # Check if item name is empty
        if not name:
            print("Error: Item name cannot be empty!")
            return

        # Check for duplicate
        if name in item_names:
            print(f"Error: '{name}' already exists in the inventory!")
            return

        # Get price
        price_input = input("Enter price: ").strip()
        price = float(price_input)

        # Validate price
        if price < 0:
            print("Error: Price cannot be negative!")
            return

        # Add to data structures
        item_names.append(name)
        item_prices[name] = price

        print("Item added successfully!")

    except ValueError as e:
        print(f"Error: Invalid price format. Please enter a valid number.")
    except Exception as e:
        print(f"Error: {e}")


def update_price():
    """Update the price of an existing item"""
    try:
        # Get item name
        name = input("Enter item name to update: ").strip()

        # Check if item exists
        if name not in item_names:
            print("Item not found in the inventory.")
            return

        # Get new price
        new_price_input = input("Enter new price: ").strip()
        new_price = float(new_price_input)

        # Validate price
        if new_price < 0:
            print("Error: Price cannot be negative!")
            return

        # Update price
        item_prices[name] = new_price

        print("Price updated successfully!")

    except ValueError as e:
        print(f"Error: Invalid price format. Please enter a valid number.")
    except Exception as e:
        print(f"Error: {e}")


def main():
    """Main function to run the inventory system"""
    while True:
        try:
            display_menu()
            choice = input("Choice: ").strip()

            if choice == "1":
                add_item()
            elif choice == "2":
                update_price()
            elif choice == "3":
                print("Exiting system...")
                break
            else:
                print("Invalid choice! Please select 1, 2, or 3.")

        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Exiting...")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()


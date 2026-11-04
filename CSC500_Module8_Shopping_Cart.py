# Student: Richard Aquilo Jr.
# University: Colorado State University Global
# Course: CSC500 - Principles of Programming
# Instructor: Dr. Brian Holbert
# CSC500 Module 8 Final Portfolio Project
# DFW Hospital IT Equipment Shopping Cart
# This program manages a department's equipment requests using a list of
# ItemToPurchase objects. The menu repeats until the user chooses to quit.
# Date: November 03, 2026

# Store the details for one requested piece of hospital IT equipment.
class ItemToPurchase:
    def __init__(self, name="none", price=0.0, quantity=0, description="none"):
        # Default values also support partial updates to existing items.
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
        self.item_description = description

    # Display quantity multiplied by unit price for this item.
    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total:.2f}")

    # Display the name and description of one item.
    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")

# Hold the requesting department's information and its list of items.
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        # These are the exact default values required by the assignment.
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []  # Each list entry is an ItemToPurchase object.

    # Add an ItemToPurchase object to the cart list.
    def add_item(self, item):
        self.cart_items.append(item)

    # Remove the first item whose name matches the requested name.
    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name.strip().lower() == item_name.strip().lower():
                self.cart_items.remove(item)
                return  # Stop searching after a successful removal.
        # Display the assignment's required message if no match exists.
        print("Item not found in cart. Nothing removed.")

    # Update only the supplied fields of an existing item.
    # update_quantity=True distinguishes an intentional zero quantity from
    # the default zero used when the caller does not request a quantity change.
    def modify_item(self, modified_item, update_quantity=False):
        for item in self.cart_items:
            if item.item_name.strip().lower() == modified_item.item_name.strip().lower():
                # Leave the current description and price unchanged when the
                # update object contains their default placeholder values.
                if modified_item.item_description != "none":
                    item.item_description = modified_item.item_description
                if modified_item.item_price != 0:
                    item.item_price = modified_item.item_price
                # The menu can explicitly set a quantity to zero.
                if update_quantity or modified_item.item_quantity != 0:
                    item.item_quantity = modified_item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    # Sum all quantities; this may differ from the number of list entries.
    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    # Add each item's unit price multiplied by its quantity.
    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    # Print the department, date, item count, item costs, and grand total.
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        if self.get_num_items_in_cart() == 0:
            # A cart with only zero-quantity items is empty for output purposes.
            print("SHOPPING CART IS EMPTY")
        else:
            # Display costs only for items with a positive quantity.
            for item in self.cart_items:
                if item.item_quantity > 0:
                    item.print_item_cost()
        print(f"Total: ${self.get_cost_of_cart():.2f}")

    # Display a heading followed by every stored item description.
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()

# Read a valid nonnegative price (float) or quantity (int).
# Repeating this prompt prevents invalid numeric input from crashing the menu.
def read_nonnegative_number(prompt, number_type):
    while True:
        try:
            value = number_type(input(prompt))
            if value < 0:
                print("Enter a nonnegative number.")
            else:
                return value  # Valid number: exit the helper function.
        except ValueError:
            # Letters and other invalid number formats cause this exception.
            print("Invalid number. Please try again.")

# Keep showing the six required menu options until the user selects q.
def print_menu(cart):
    while True:
        print("\nMENU")
        print("a - Add item")
        print("r - Remove item")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        # Remove extra spaces and accept uppercase as well as lowercase input.
        choice = input("Choose an option: ").strip().lower()

        if choice == "q":
            # Only q ends the menu loop.
            break
        elif choice == "a":
            # Gather the four attributes, construct an item, and add it.
            print("\nADD ITEM TO CART")
            name = input("Enter the item name: ")
            description = input("Enter the item description: ")
            price = read_nonnegative_number("Enter the item price: $", float)
            quantity = read_nonnegative_number("Enter the item quantity: ", int)
            cart.add_item(ItemToPurchase(name, price, quantity, description))
        elif choice == "r":
            # The cart method searches by name and handles missing items.
            print("\nREMOVE ITEM FROM CART")
            cart.remove_item(input("Enter name of item to remove: "))
        elif choice == "c":
            # Change only the quantity; preserve the existing price/description.
            print("\nCHANGE ITEM QUANTITY")
            name = input("Enter the item name: ")
            quantity = read_nonnegative_number("Enter the new quantity: ", int)
            updated_item = ItemToPurchase(name=name, quantity=quantity)
            # The flag makes an intentional quantity of zero valid.
            cart.modify_item(updated_item, update_quantity=True)
        elif choice == "i":
            # Output descriptions for all items currently in the cart.
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        elif choice == "o":
            # Output the full cart and its calculated total cost.
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()
        else:
            # An invalid option does not end the loop; ask again.
            print("Invalid option. Please choose a, r, c, i, o, or q.")

# Create a new cart using the department and request date entered by the user.
def main():
    print("DFW HOSPITAL IT EQUIPMENT SHOPPING CART")
    department = input("Enter hospital department (customer name): ")
    request_date = input("Enter request date: ")
    cart = ShoppingCart(department, request_date)
    print_menu(cart)  # Start the interactive menu.

# Run main only when this Python file is launched directly.
if __name__ == "__main__":
    main()

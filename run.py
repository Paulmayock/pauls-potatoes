import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import uuid  # Taken from webdev to generate random order number
import sys  # Allows the user to exit the system

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('pauls_potatoes')

orders = SHEET.worksheet('orders')


class PotatoMenu:
    """
    Potato menu class type
    """
    def __init__(self, name, message):
        self.name = name
        self.message = message

    def print(self):
        """
        Prints a string for the selected baked potato
        """
        return self.message + " " + self.name


class PotatoType:

    """
    Potato type class
    """
    def __init__(self, type, price):
        self.type = type
        self.price = price


potato_toppings = {
    "1": PotatoMenu("All the cheeses", "Cheezy"),
    "2": PotatoMenu("The vegan with all the veggies", "Vegan delight"),
    "3": PotatoMenu("BBQ chicken, peppers, onions, bbq sauce", "cluck cluck"),
    "4": PotatoMenu("Pulled pork, slaw", "oink oink"),
    "5": PotatoMenu("Taco beef, cheese, peppers", "mexican moomoo"),
}

type_price = {
    "F": {"price": 8, "name": "Fries"},
    "B": {"price": 9, "name": "Baked"},
    "R": {"price": 11, "name": "Roastys"},
}


def greeting():
    """
    Function to greet the customer or
    cancel if they decide not to order
    """
    print("Hi, Welcome to Paul's Potatoes!")
    while True:
        print("Would you like to place an order? [Y]es or [N]o\n")
        user_choice = input("Enter: \n")
        user_choice = user_choice.strip()
        if user_choice == "Y" or user_choice == "y":
            print("\nPlease choose from our tasty menu...\n")
            break
        elif user_choice == "N" or user_choice == "n":
            print("Hope to see you again!")
            sys.exit()
        else:
            print("Invalid entry, please try again")
            print("Make sure you entered Y or N\n")
            continue


def select_type():
    """
    Function to select the potato type
    """
    for index, info in type_price.items():
        print(f"{index} - €{info['price']}")
    while True:
        print(
            "\nPlease select what type of potato you wish to order.\n"
            "Enter either F for fries, B for baked or R for roasties.\n"
            "Press E to leave the shop.\n"
        )
        user_type_input = input("Enter type: \n").strip().upper()

        if user_type_input == "E":
            print("We hope to see you soon again!")
            sys.exit()
            break
        elif user_type_input in type_price:
            selected_type = type_price[user_type_input]
            print(
                f"\nYou have chosen a {selected_type['name']}"
                "type potato for €{selected_type['price']}\n"
            )
            return selected_type
        else:
            print("\nSorry, this is invalid.")


def select_potato():
    """
    Function to select the potato topping
    """
    for index, potato in potato_toppings.items():
        print(index, potato.name)
    print(
        "\nPlease pick the corresponding number\n"
        "to the potato topping you wish to order.\n"
        "If you changed your mind,\n"
        "press E to leave.\n"
    )
    while True:
        user_input = input("Enter number: \n")
        user_input = user_input.strip().lower()
        if user_input == "e":
            print("We hope to see you again")
            sys.exit()
            break
        elif user_input in potato_toppings:
            selected_potato = user_input
            print(
                "\nYou have chosen",
                potato_toppings[user_input].print(), "\n"
            )
            return selected_potato
        else:
            print(
                "\nSorry this is invalid\n"
                "Please enter number between 1-5 or E\n"
            )


def number_of_potato_orders():
    """
    Function to select how many orders
    """
    print(
        "How many quantites of your order would you like?\n"
        "You can pick up to a quantity of 10 orders.\n"
        "Press E to cancel your order.\n"
    )
    while True:
        user_quantity_input = input("Enter quantity: \n")

        value = int(user_quantity_input)

        # user_quantity_input = user_quantity_input.strip().lower()
        if user_quantity_input == "e":
            print("We hope to see you soon again!")
            sys.exit()
            break
        elif value >= 1 and value <= 10:
            print("\nYou have selected a quantity of", user_quantity_input)
            break
        else:
            print(
                "\nSorry please choose between 1 and 10\n"
            )
    return user_quantity_input


def confirm_order():
    """
    Function to confirm order
    """
    print(
        "\nTo confirm this order please select\n"
        "[Y]es or [N]o \n(No will restart the order)\n"
    )
    while True:
        user_confirm = input("Enter: \n")
        user_confirm = user_confirm.strip().upper()
        if user_confirm == "Y":
            print("\nYour order is confirmed! ")
            break
        elif user_confirm == "N":
            print("\nPlease order again...\n")
            sys.exit()
            break
        else:
            print("\nYou have entered an incorrect key")
            print("Make sure you either entered Y or N\n")

    return user_confirm


def name():
    """
    Function to get users full name
    """
    print("\nPlease add your details\n")
    while True:
        name = input("Enter your full name: \n").title()
        print(f'name......{name}')
        print(f'type......{type(name)}')
        if name.isalpha():
            break
        else:
            print(
                "\nPlease make sure you entered your "
                "name correctly"
            )
            print("Try again\n")

    return name


def number():
    """
    Function to collect user number
    """
    while True:
        number = input("\nPlease enter your phone number: \n")
        if number.isdigit() and len(number) <= 11:
            print(
                "\nThank you")
            break
        else:
            print(
                "\nPlease make sure you entered your "
                "number correctly"
            )
            print("Try again")

    return number


def receipt():
    """
    Function to generate a recipt
    """
    print(
        "Thank you from Paul's Potatoes\n"
        "Your order has been processed \n"
        "and will be ready for collection within 15 minutes!\n"
    )
    print("RECEIPT")
    print("---------------------------------")
    print("Pauls Potatoes\nBridge Street\nWestport\n")
    identity = str(uuid.uuid4())
    print("Order #")
    print(identity)
    print(orders)
    print("€" + str(select_type))
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    print(time)
    print("---------------------------------\n")

    return {"id": identity, "time": time}


def update_spreadsheet(row):
    """
    Function to update google worksheet with users order info
    """
    orders.append_row(row)


def main():
    """
    Main function which will
    include all the functions
    to run the code
    """
    greeting()

    # Get potato_type variable
    potato_type = select_type()
    price = potato_type['price']

    # Get ....
    selected_potato = select_potato()

    # Get .....
    user_quantity_input = number_of_potato_orders()

    # Get ....
    user_confirm = confirm_order()

    # Get user_name variable
    user_name = name()

    # Get phone_number variable
    phone_number = number()

    receipt_result = receipt()

    # Check all the variables

    receipt()

    row = [
        user_name, phone_number, selected_potato, user_quantity_input, price,
        receipt_result["time"], receipt_result["id"]
    ]
    print(f'row: {row}')
    update_spreadsheet(row)


if __name__ == '__main__':
    main()

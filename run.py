import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
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
    "F": PotatoType("Fries", 8),
    "B": PotatoType("Baked", 9),
    "R": PotatoType("Roastys", 11),
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
            print(
                "\nYou have chosen",
                potato_toppings[user_input].print(), "\n"
            )
            break
        else:
            print(
                "\nSorry this is invalid\n"
                "Please enter number between 1-5 or E\n"
            )
            continue


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
        user_quantity_input = user_quantity_input.strip().lower()
        if user_quantity_input == "e":
            print("We hope to see you soon again!")
            sys.exit()
            break
        elif user_quantity_input >= str(1) and user_quantity_input >= str(10):
            print("\nYou have selected a quantity of", user_quantity_input)
            break
        else:
            print(
                "\nSorry please choose between 1 and 10\n"
            )
    return user_quantity_input


def main():
    """
    Main function which will
    include all the functions
    to run the code
    """
    greeting()
    select_potato()
    number_of_potato_orders()


if __name__ == '__main__':
    main()
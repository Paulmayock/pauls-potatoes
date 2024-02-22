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
    def __init__(self, type, price, label):
        self.type = type
        self.price = price
        self.label = label   


potato_toppings = {
    "1": PotatoMenu("All the cheeses"),
    "2": PotatoMenu("The vegan with all the veggies"),
    "3": PotatoMenu("BBQ chicken, peppers, onions, bbq sauce"),
    "4": PotatoMenu("Pulled pork, slaw"),
    "5": PotatoMenu("Taco beef, cheese, peppers"),
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
    while True:
        print("Hi, Welcome to Paul's Potatoes!")
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
            return greeting()
        
def select_potato():
    """
    Function to select the potato topping
    """
    for index, potato in potato_toppings.items():
        print(index, orders.name)
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
    return potato_toppings[user_input]

def main():
    """
    
    """
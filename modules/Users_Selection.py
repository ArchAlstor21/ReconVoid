import os
from .Ascii_Art import print_ascii_art

def Users_Selection(menu_array):

    # Calculates the valid options range
    max_option = len(menu_array)
    valid_range = list(range(0, max_option + 1))

    while True:  # Keep asking until valid input is received
        try:
            selection = int(input("\nSelect an option: "))
            if selection in valid_range:
                os.system("clear")
                return selection
            else:
                os.system("clear")
                print(f"Invalid input. Please select a valid option (0-{max_option}).\n")
        except ValueError:
            os.system("clear")
            print(f"Invalid input. Please enter a number (0-{max_option}).\n")
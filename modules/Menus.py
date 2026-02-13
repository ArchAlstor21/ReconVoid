import os
from .Ascii_Art import print_ascii_art
from .Users_Selection import Users_Selection

# Define color constants
YELLOW = '\033[33m'
RESET = '\033[0m'

# NOTE: MODULAR MENU FOR ALL MENUS
def Menu(description, ZeroFunction, *options):
    
    print(YELLOW + "OTHER:" +  RESET)
    print("0. " + ZeroFunction)
    print(YELLOW + f"{description}" + RESET)
    
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")


def WebsiteMenu():

    def option_check(selection):

        match selection:
            case 0:
                pass
            case 1:
                from menu_modules.WebApps.Subfinder import Subfinder
                Subfinder()
            case _:
                pass
            # extend later with more tools


    os.system("clear")
    print_ascii_art()

    website_menu_options = [
        "Subfinder"
        # add more as you extend the software
    ]

    Menu("Select an option:", "To leave this menu", "Subfinder")

    selection = Users_Selection(website_menu_options)

    option_check(selection)
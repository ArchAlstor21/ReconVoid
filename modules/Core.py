import os, sys, platform, time


# ANSI escape codes for terminal colors!
GREEN = '\033[92m'
YELLOW = '\033[33m'
RESET = '\033[0m'


def print_ascii_art():
    """Prints ASCII art for ReconVoid"""
    ascii_art = r"""
|--------------------------------------------------------------------------------------------|
|     /$$$$$$$                                          /$$    /$$          /$$       /$$    |
|    | $$__  $$                                        | $$   | $$         |__/      | $$    |
|    | $$  \ $$  /$$$$$$   /$$$$$$$  /$$$$$$  /$$$$$$$ | $$   | $$ /$$$$$$  /$$  /$$$$$$$    |
|    | $$$$$$$/ /$$__  $$ /$$_____/ /$$__  $$| $$__  $$|  $$ / $$//$$__  $$| $$ /$$__  $$    |
|    | $$__  $$| $$$$$$$$| $$      | $$  \ $$| $$  \ $$ \  $$ $$/| $$  \ $$| $$| $$  | $$    |
|    | $$  \ $$| $$_____/| $$      | $$  | $$| $$  | $$  \  $$$/ | $$  | $$| $$| $$  | $$    |
|    | $$  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$/| $$  | $$   \  $/  |  $$$$$$/| $$|  $$$$$$$    |
|    |__/  |__/ \_______/ \_______/ \______/ |__/  |__/    \_/    \______/ |__/ \_______/    |
|--------------------------------------------------------------------------------------------|
    """
    print(GREEN + ascii_art + RESET)


def check_dependencies():

    packages = [
        "subfinder"
        # add more packages as necerssary
    ]

    # NOTE: Linux support only
    if platform.system().lower() == 'linux':
        print("OS is supported!")
    else:
        print("Are you attempting to run this in an unsupported OS? Please make sure you are on Linux!")
        sys.exit(1)

    print("Checking if dependancy packages are installed...")
    time.sleep(0.3)

    # Loops through and checks if all dependencies are installed in a pre-defined array.
    for package in packages:
        if os.path.exists('/usr/bin/' + package):
            print(package + "... ✅")
            time.sleep(0.3)
        else:
            print("Error: " + package + " is not installed or not found at /usr/bin/" + package)
            sys.exit(1)

    print("All dependencies are met! The tool is fully functional!")
    time.sleep(2)


# NOTE: MODULAR MENU FOR ALL MENUS
def Menu(description, ZeroFunction, *options):

    print_ascii_art()
    print(YELLOW + "OTHER:" +  RESET)
    print("0. " + ZeroFunction)
    print(YELLOW + f"{description}" + RESET)

    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    # Gets user option selection and validates it
    menu_array = list(options)
    selection = Users_Selection(menu_array)
    
    if selection != None:
        return selection
    else:
        os.system("clear")
        return None


def Users_Selection(menu_array):

    # Calculates the valid options range
    max_option = len(menu_array)
    valid_range = list(range(0, max_option + 1))

    try:
        selection = int(input("\nSelect an option: "))
        if selection in valid_range:
            os.system("clear")
            return selection
        else:
            return None
    except ValueError:
        return None


def Main_Menu():

    while True:
        menu_options = [
            "WebApps",
            "Option 2",
            "Option 3",
            "Option 4",
            # Add more options here as needed
        ]

        selection = Menu("Select an option:", "To exit the script", *menu_options)

        if selection is not None:
            return selection


def WebAppMenu():

    def webapp_option_check(selection):

        import WebAppCommands

        match selection:
            case 0:
                return False
            case 1:
                WebAppCommands.Subfinder()
                return True
            case _:
                return True

    while True:

        menu_options = [
            "Subfinder"
            # Add more options here as needed
        ]

        selection = Menu("Select an option:", "To leave this menu", *menu_options)
        
        if selection != None:
            result = webapp_option_check(selection)
            if result == False:
                break


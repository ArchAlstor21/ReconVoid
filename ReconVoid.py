import os
from modules.check_dependencies import check_dependencies
import modules.run_commands as run_command # IN DEVELOPMENT

def print_ascii_art():
    """Prints ASCII art for ReconVoid"""
    ascii_art = r"""
|--------------------------------------------------------------------------|
| ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗██╗   ██╗ ██████╗ ██╗██████╗  |
| ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║██║   ██║██╔═══██╗██║██╔══██╗ |
| ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║██║   ██║██║   ██║██║██║  ██║ |
| ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║╚██╗ ██╔╝██║   ██║██║██║  ██║ |
| ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║ ╚████╔╝ ╚██████╔╝██║██████╔╝ |
| ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝  ╚═══╝   ╚═════╝ ╚═╝╚═════╝  |
|--------------------------------------------------------------------------|
    """
    print(ascii_art)


def menu():
    print("\nTo exit the Recon menu:")
    print("0. Leave the Script")
    print("Select a Recon option:")
    print("1. WebApps")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Option 4")

    try:
        selection = int(input("\nSelect an option (1-4, 0 to exit): "))
        if selection in [0, 1, 2, 3, 4]:
            os.system("clear")
            return selection
        else:
            os.system("clear")
            print_ascii_art()
            print("Invalid input. Try Again Please!")
            return menu()
    except ValueError:
        os.system("clear")
        print_ascii_art()
        print("Invalid input. Try Again Please!")
        return menu()


def option_check(selection):
    if selection == 1:
        print(f"You selected option {selection}")
    elif selection in [2, 3, 4]:
        print(f"Option {selection} is currently in development. Use an available option.")
    # Note: selection == 0 is handled in the main while loop to break out
    # DEV NOTE: these print() commands are TEMPERARY, they are to be removed in the future!


if __name__ == "__main__":
    os.system("clear")
    check_dependencies()
    while True:
        print_ascii_art()
        selection = menu()
        option_check(selection)
        if selection == 0:
            break
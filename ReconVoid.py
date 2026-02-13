import os
import modules.check_dependencies as check_dependencies
import modules.Menus as Menus
import modules.Users_Selection as Users_Selection
import modules.Ascii_Art as Ascii_Art


def Main_Menu():

    menu_options = [
        "WebApps",
        "Option 2",
        "Option 3",
        "Option 4",
        # Add more options here as needed
    ]

    Menus.Menu("Select an option:", "To exit the script", *menu_options)

    return Users_Selection.Users_Selection(menu_options)


def option_check(selection):

    match selection:
        case 0:
            pass
        case 1:
            Menus.WebsiteMenu()
        case _:
            pass
        # extend later with more options


if __name__ == "__main__":

    os.system("clear")
    check_dependencies.check_dependencies()
    while True:
        Ascii_Art.print_ascii_art()
        selection = Main_Menu()
        option_check(selection)
        if selection == 0:
            break
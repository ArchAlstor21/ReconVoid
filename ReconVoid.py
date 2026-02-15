import os
import modules.Core as Core


def option_check(selection):

    match selection:
        case 0:
            pass
        case 1:
            Core.WebsiteMenu()
        case _:
            pass
        # extend later with more options


if __name__ == "__main__":

    os.system("clear")
    Core.check_dependencies()
    while True:
        selection = Core.Main_Menu()
        option_check(selection)
        if selection == 0:
            break
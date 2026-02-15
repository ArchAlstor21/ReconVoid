import os
import modules.Core as Core


def option_check(selection):

    match selection:
        case 0:
            return False
        case 1:
            Core.WebAppMenu()
            return True
        case _:
            return True
        # extend later with more options


if __name__ == "__main__":

    os.system("clear")
    Core.check_dependencies()

    while True:

        selection = Core.Main_Menu()
        result = option_check(selection)
        if result == False:
            break
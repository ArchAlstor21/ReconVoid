import os, sys
import modules.Core as Core


def check_root_privileges():
    if os.geteuid() != 0:
        print("Error: This tool requires root privileges to run")
        print("Please run this script as root (use sudo python ./ReconVoid.py)")
        sys.exit(1)


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

    check_root_privileges()
    
    os.system("clear")
    Core.check_dependencies()

    while True:

        selection = Core.Main_Menu()
        result = option_check(selection)
        if result == False:
            break
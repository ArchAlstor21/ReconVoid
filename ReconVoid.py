import os
import sys
import platform
import time


def check_dependencies():
    if platform.system().lower() == 'linux':
        print("OS is supported!")
    else:
        print("Are you attempting to run this in an unsupported OS? Please make sure you are on Linux!")
        sys.exit(1)
    
    if not os.path.exists('/usr/bin/subfinder'):
        print("Subfinder Installed... ✅")
    else:
        print("Error: subfinder is not installed or not found at /usr/bin/subfinder")
        sys.exit(1)
    
    print("All dependencies are met! The tool is fully functional!")
    time.sleep(3)
    

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
    """Display a selection menu and get user input"""
    print("\nSelect an option:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Option 4")
    print("5. Exit")
    
    # Get user input and store it in the selection variable
    try:
        selection = int(input("\nEnter your choice (1-5): "))
        return selection
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None


if __name__ == "__main__":
    check_dependencies()  # Check dependencies before proceeding
    print_ascii_art()
    selection = menu()
    if selection is not None:
        print(f"You selected option {selection}")
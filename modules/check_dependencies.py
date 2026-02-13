import os
import sys
import platform
import time


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
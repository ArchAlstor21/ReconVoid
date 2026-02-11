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

    print("Checking if dependancy packages are installed...")
    time.sleep(0.2)

    if os.path.exists('/usr/bin/subfinder'):
        print("Subfinder... ✅")
        time.sleep(0.2)
    else:
        print("Error: subfinder is not installed or not found at /usr/bin/subfinder")
        sys.exit(1)

    print("All dependencies are met! The tool is fully functional!")
    time.sleep(3)
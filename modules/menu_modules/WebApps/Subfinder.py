### NOTE: MAKE SURE TO REVIEW AND CLEANUP!!! BROKEN CODE!!!

from ...Menus import Menu, Users_Selection
import subprocess

def Subfinder():
    # Import here to avoid circular import
    print("Subfinder Tool Selected")

    # Initialize parameters dictionary
    params = {
        'domain': None,
        'domain_list': None,
        'sources': None,
        'exclude_sources': None,
        'output': None,
        'verbose': False,
        'silent': False,
        'all_sources': False,
        'recursive': False,
        'active': False,
        'ports': None,
        'timeout': None
    }
    
    while True:
        print("\n" + "="*50)
        print("SUBFINDER PARAMETER SELECTION MENU")
        print("="*50)
        
        # Display current parameter values
        print("\nCurrent Parameter Values:")
        for key, value in params.items():
            if value is not None and value is not False:
                print(f"  {key}: {value}")
            elif value is False:
                # Only show boolean flags if they're True
                continue
            else:
                print(f"  {key}: [Not set]")
        
        # Define Subfinder parameter options
        subfinder_options = [
            "Set target domain (-d)",
            "Set domain list (-dL)", 
            "Set sources (-n)",
            "Set excluded sources",
            "Set output file (-o)",
            "Enable verbose mode (-v)",
            "Enable silent mode",
            "Use all sources (-all)",
            "Use recursive sources only",
            "Enable active reconnaissance (-active)",
            "Set ports (-p)",
            "Set timeout",
            "Run Subfinder with current parameters",
            "Return to previous menu"
        ]
        
        # Display menu
        for i, option in enumerate(subfinder_options, 1):
            print(f"{i}. {option}")
        
        try:
            selection = int(input("\nEnter your choice (1-{}): ".format(len(subfinder_options))))
            
            if selection == 1:  # Set target domain
                domain = input("Enter target domain: ").strip()
                if domain:
                    params['domain'] = domain
                    print(f"Domain set to: {domain}")
                else:
                    print("Invalid domain entered.")
                    
            elif selection == 2:  # Set domain list
                domain_list = input("Enter path to domain list file: ").strip()
                if domain_list:
                    params['domain_list'] = domain_list
                    print(f"Domain list file set to: {domain_list}")
                else:
                    print("Invalid file path entered.")
                    
            elif selection == 3:  # Set sources
                sources = input("Enter sources (comma separated): ").strip()
                if sources:
                    params['sources'] = sources
                    print(f"Sources set to: {sources}")
                else:
                    print("No sources entered.")
                    
            elif selection == 4:  # Set excluded sources
                exclude_sources = input("Enter sources to exclude (comma separated): ").strip()
                if exclude_sources:
                    params['exclude_sources'] = exclude_sources
                    print(f"Excluded sources set to: {exclude_sources}")
                else:
                    print("No sources to exclude entered.")
                    
            elif selection == 5:  # Set output file
                output = input("Enter output file path: ").strip()
                if output:
                    params['output'] = output
                    print(f"Output file set to: {output}")
                else:
                    print("Invalid file path entered.")
                    
            elif selection == 6:  # Enable verbose mode
                params['verbose'] = not params['verbose']
                status = "enabled" if params['verbose'] else "disabled"
                print(f"Verbose mode {status}")
                
            elif selection == 7:  # Enable silent mode
                params['silent'] = not params['silent']
                status = "enabled" if params['silent'] else "disabled"
                print(f"Silent mode {status}")
                
            elif selection == 8:  # Use all sources
                params['all_sources'] = not params['all_sources']
                status = "enabled" if params['all_sources'] else "disabled"
                print(f"All sources mode {status}")
                
            elif selection == 9:  # Use recursive sources only
                params['recursive'] = not params['recursive']
                status = "enabled" if params['recursive'] else "disabled"
                print(f"Recursive sources only mode {status}")
                
            elif selection == 10:  # Enable active reconnaissance
                params['active'] = not params['active']
                status = "enabled" if params['active'] else "disabled"
                print(f"Active reconnaissance {status}")
                
            elif selection == 11:  # Set ports
                ports = input("Enter ports (comma separated or range): ").strip()
                if ports:
                    params['ports'] = ports
                    print(f"Ports set to: {ports}")
                else:
                    print("No ports entered.")
                    
            elif selection == 12:  # Set timeout
                timeout = input("Enter timeout value (in seconds): ").strip()
                if timeout.isdigit():
                    params['timeout'] = timeout
                    print(f"Timeout set to: {timeout} seconds")
                else:
                    print("Invalid timeout value entered.")
                    
            elif selection == 13:  # Run Subfinder with current parameters
                run_subfinder(params)
                
            elif selection == 14:  # Return to previous menu
                print("Returning to previous menu...")
                break
                
            else:
                print("Invalid selection. Please enter a number between 1 and {}.".format(len(subfinder_options)))
                
        except ValueError:
            print("Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            break

def run_subfinder(params):
    """Execute the Subfinder command with selected parameters"""
    try:
        # Build the command
        cmd = ["subfinder"]
        
        if params['domain']:
            cmd.extend(["-d", params['domain']])
        if params['domain_list']:
            cmd.extend(["-dL", params['domain_list']])
        if params['sources']:
            cmd.extend(["-n", params['sources']])
        if params['exclude_sources']:
            cmd.extend(["-exclude-sources", params['exclude_sources']])
        if params['output']:
            cmd.extend(["-o", params['output']])
        if params['verbose']:
            cmd.append("-v")
        if params['silent']:
            cmd.append("-silent")
        if params['all_sources']:
            cmd.append("-all")
        if params['recursive']:
            cmd.append("-recursive")
        if params['active']:
            cmd.append("-active")
        if params['ports']:
            cmd.extend(["-p", params['ports']])
        if params['timeout']:
            cmd.extend(["-timeout", params['timeout']])
        
        print(f"\nExecuting command: {' '.join(cmd)}")
        
        # Check if subfinder is installed
        result = subprocess.run(["which", "subfinder"], capture_output=True, text=True)
        if result.returncode != 0:
            print("Error: Subfinder is not installed or not in PATH.")
            print("Please install subfinder using: go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest")
            return
        
        # Execute the command
        print("\nRunning Subfinder...")
        subprocess.run(cmd)
        
    except FileNotFoundError:
        print("Error: Subfinder is not installed or not in PATH.")
        print("Please install subfinder using: go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest")
    except Exception as e:
        print(f"An error occurred while running Subfinder: {e}")

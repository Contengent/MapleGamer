import cliMenu as interface

def main():
    '''
    Main function    
    '''
    menu = interface.cli()

    while(True):
        print("[1] Start")
        print("[2] Select file")
        print("[0] Quit")

        
        option = str(input("> "))
        
        match (option):
            case ("1"): # Start program
                menu.startRoutine()
            
            case ("2"): # Select file
                menu.selectFile()

            case ("0"): # Quit
                menu.quit()
                
            case _: # Invalid option
                print("Ewwow: >.<")
        
        print("...\n")

''' entry point '''
if __name__ == "__main__":
    main()
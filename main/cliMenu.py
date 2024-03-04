import inputManager as inputM
import fileManager as fileM

class cli:
    def __init__(self):
        self.folderPath = "routines/"
        self.fileSelected = ""

    # [1]
    def startRoutine(self):
        '''
        Start rotating through selected file's routine.
        '''

        print(f"'{self.fileSelected}' was selected.")
        print("Note: ./routines/ is the default path, you can change it in 'cliMenu.py'")

        routine = fileM.inputs(self.fileSelected)
        routineManager = inputM.actions(routine)

        loops = int(input("how many loops would you like? "))

        print("Note: You can use 'CTRL+C' to go back to the menu.")


        routineManager.rotation(loops)

    # [2]
    def selectFile(self):
        '''
        Routine/file selection.
        '''

        print("Select a routine file:") # select file
        print(fileM.ALLFILES(self.folderPath))
        self.fileSelected = self.folderPath + input("> ")
        print("File has been selected.")

    def showMinimap(self):
        pass



    # [0]
    def quit(self):
        '''
        Exit gracefully (lol).
        '''
        print("Quitting...")
        exit(0)

if __name__ == "__main__":
    menuu = cli()
    print(menuu.folderPath)
    print(menuu.fileSelected)
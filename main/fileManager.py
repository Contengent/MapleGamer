import csv
import os

class inputs:
    '''
    Type for reading a file of inputs and interacting with it.
    '''

    def __init__(self, inFile):
        self.fileName = inFile                          # Self explanitory
        self.fileOpened = open(self.fileName)           # ''
        self.fileReader = csv.reader(self.fileOpened)   # ''

        self.totalInputs = []                           # All lines in 1 nested array
        self.totalLines = int                           # Total amount of lines

        self.currentInput = []                          # Current line as an array
        self.currentLine = 0                            # Current line number


        # Complex inits
        for row in self.fileReader:
            self.totalInputs.append(row)
        self.totalLines = len(self.totalInputs)

    
    def getNextInput(self):
        '''
        Retrieve next line from file. 
        '''

        self.currentInput = self.totalInputs[self.currentLine]
        self.currentLine += 1
        
        print(self.currentInput) # for debugging, but honestly: It. do. not. matter.

        if (self.currentLine == self.totalLines):
            self.currentLine = 0
            print("End of file reached; Looping.")
        
        return self.currentInput
    
    def __str__(self):
        print(f'''
        self.fileName: {self.fileName}
        self.fileOpened: {self.fileOpened}
        self.fileReader: {self.fileReader}
        self.totalInputs: {self.totalInputs}
        self.totalLines: {self.totalLines}
        self.currentInput: {self.currentInput}
        self.currentLine: {self.currentLine}
''')
        #lol


# Random funcs that don't fit anywhere else :p
def ALLFILES(path=str):
    allFiles = []
    for file_path in os.listdir(path):
        allFiles.append(file_path)
    return allFiles


''' debugging '''
if __name__ == "__main__":
    temp = inputs("routines/cernium-hayato.csv")

    temp.getNextInput()
    temp.getNextInput()
    print(temp.currentInput)
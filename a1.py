# a1.py

# Lauren Cho
# lcho6@uci.edu
# 91059503

from pathlib import Path
import os

def evaluateCommand(theInput):
    """Evaluates if the command is L or Q then evaluates options."""

    if theInput[0] == 'L':
        # Prints the list of files and directories

        checkInputLen(theInput)

        splitChar = theInput[1]
        splitInput = theInput.split(splitChar)
        myPath = Path(splitInput[1])

        listedFiles = []
        listedDirectories = []
        
        if len(splitInput) == 2:
            
            # Not sure if placement is good but will keep here for now
            for currentPath in myPath.iterdir():
                
                # Adds all paths to either the files or directories list
                if os.path.isfile(currentPath) == True:
                    listedFiles.append(currentPath)
                
                elif os.path.isdir(currentPath) == True:
                    listedDirectories.append(currentPath)

            for eachFile in listedFiles:
                print(eachFile)

            for eachDirectory in listedDirectories:
                print(eachDirectory)
            inputs = input()
            evaluateCommand(inputs)
        
        elif len(splitInput) > 2:
            optionList = splitInput[2:]

            options(optionList, myPath)
            
    elif theInput[0] == 'C':
        # Creates a file in the specified directory

        checkInputLen(theInput)
        
        splitChar = theInput[1]
        splitInput = theInput.split(splitChar)
        myPath = Path(splitInput[1])
        fileName = splitInput[-1] + '.dsu'
        combinedPath = Path(myPath) / fileName
        Path.touch(combinedPath)
        print(combinedPath)

        inputs = input()
        evaluateCommand(inputs)

    elif theInput[0] == 'D':
        # Deletes a file
        checkInputLen(theInput)

        splitChar = theInput[1]
        splitInput = theInput.split(splitChar)
        myPath = Path(splitInput[1])
        stringPath = str(myPath)

        if stringPath[-4:] != '.dsu':
            print('ERROR')
            #FIX: be able to ask user for input again

        elif stringPath[-4:] == '.dsu':
            Path.unlink(myPath)
            print(stringPath, 'DELETED')
        inputs = input()
        evaluateCommand(inputs)

    elif theInput[0] == 'R':
        # Prints contents of a DSU file
        checkInputLen(theInput)

        splitChar = theInput[1]
        splitInput = theInput.split(splitChar)
        myPath = Path(splitInput[1])
        stringPath = str(myPath)
        fileName = splitInput[-1]

        if stringPath[-4:] != '.dsu':
            print('ERROR')
            inputs = input()
            evaluateCommand(inputs)

        elif stringPath[-4:] == '.dsu':
            with open(fileName, 'r') as file:
                lines = file.readlines()

                #Check if file is empty
                if len(lines) == 0:
                    print('EMPTY')
                    inputs = input()
                    evaluateCommand(inputs)
                
                elif len(lines) > 0:
                    for line in lines:
                        print(line, end='')
                    inputs = input()
                    evaluateCommand(inputs)

    elif theInput[0] == 'Q':
        exit()

    else:
        print('Please input a valid command.')

def checkInputLen(theInput):
    if len(theInput) == 1:
        print('ERROR')
        inputs = input()
        evaluateCommand(inputs)
    else:
        pass


def options(optionListInput, thePath):
    """Detects the option and performs the option task."""

    if optionListInput[0] == '-r':
        # Outputs directory content recursively

        if len(optionListInput) == 1:
            for currentPath in thePath.iterdir():
                if os.path.isfile(currentPath) == True:
                    print(currentPath)

            for currentPath in thePath.iterdir():
                if os.path.isdir(currentPath) == True:
                    print(currentPath)
                    for smallerPath in currentPath.iterdir():
                        print(smallerPath)
            inputs = input()
            evaluateCommand(inputs)
        
        elif len(optionListInput) > 1:

            if optionListInput[1] == '-f':
                # Recursive search then search for file

                for currentPath in thePath.iterdir():
                    if os.path.isfile(currentPath) == True:
                        print(currentPath)
                for currentPath in thePath.iterdir():
                    if os.path.isdir(currentPath) == True:
                        for aPath in currentPath.iterdir():
                            print(aPath)
                inputs = input()
                evaluateCommand(inputs)


            elif optionListInput[1] == '-s':
                # Recursive search then file name match

                fileName = optionListInput[-1]

                for currentPath in thePath.iterdir():
                    if os.path.isfile(currentPath) == True:
                        stringPath = str(currentPath)
                        splitPath = stringPath.split('/')
                        if splitPath[-1] == fileName: 
                            print(currentPath)
                
                for currentPath in thePath.iterdir():
                    if os.path.isdir(currentPath) == True:
                        for aPath in currentPath.iterdir():
                            stringPath = str(aPath)
                            splitPath = stringPath.split('/')
                            if splitPath[-1] == fileName: 
                                print(aPath)
                inputs = input()
                evaluateCommand(inputs)

            elif optionListInput[1] == '-e':
                # Recursive search then file extension match

                extType = optionListInput[-1]

                for currentPath in thePath.iterdir():
                    if os.path.isfile(currentPath) == True:
                        stringPath = str(currentPath)
                        splitPath = stringPath.split('.')
                        if splitPath[-1] == extType:
                            print(currentPath)  
                for currentPath in thePath.iterdir():
                    if os.path.isdir(currentPath) == True:
                        for aPath in currentPath.iterdir():
                            stringPath = str(aPath)
                            splitPath = stringPath.split('.')
                            if splitPath[-1] == extType: 
                                print(aPath)
                inputs = input()
                evaluateCommand(inputs)          

    elif optionListInput[0] == '-f':
        # Outputs only files

        listedFiles = []

        for currentPath in thePath.iterdir():
                
            # Adds all paths to files list
            if os.path.isfile(currentPath) == True:
                listedFiles.append(currentPath)
                
        for eachFile in listedFiles:
                print(eachFile)
        inputs = input()
        evaluateCommand(inputs)


    elif optionListInput[0] == '-s':
        # Output only files that match the given file name

        fileName = optionListInput[-1]

        for currentPath in thePath.iterdir():
            if os.path.isfile(currentPath) == True:
                stringPath = str(currentPath)
                splitPath = stringPath.split('/')
                if splitPath[-1] == fileName: 
                    print(currentPath)
        inputs = input()
        evaluateCommand(inputs)
  

    elif optionListInput[0] == '-e':
        # Output only files that match a given file extension

        extType = optionListInput[-1]

        for currentPath in thePath.iterdir():
            if os.path.isfile(currentPath) == True:
                stringPath = str(currentPath)
                splitPath = stringPath.split('.')
                if splitPath[-1] == extType:
                    print(currentPath)
        inputs = input()
        evaluateCommand(inputs)


if __name__ == "__main__":
    inputs = input()
    evaluateCommand(inputs)

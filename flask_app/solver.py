from flask_app import app
from copy import deepcopy

DEBUG = False
#set DEBUG to TRUE when you want prints to log

def log( comment, inputValue):
    if DEBUG : 
        return print(comment, inputValue)

def get_row(data, rowIndex):
    # sends in soduku numbers and blanks and row index to iterate through
    # while loop goes through full row pushing numbers and blanks into array
    log("get_row", data)
    oneRow = []
    i=rowIndex
    while(i<=rowIndex):
        log("row I", i)
        j=0
        while(j<=8):
            log("column j", j)
            oneRow.append(data[i][j])
            j+=1
        i+=1
    return oneRow

def get_column(data, columnIndex):
    # does the same as row but by columns
    oneColumn = []
    i=0
    while(i<=8):
        j=columnIndex
        log("column - row i", i)
        while(j<=columnIndex):
            log("column - column j", j)
            oneColumn.append(data[i][j])
            j+=1
        i+=1
    return oneColumn

def get_box(data, rowIndex, columnIndex):
    # collects a box of 3 x 3 row and column (9 inputs) 
    # set up to keep within the 3 by 3 boxes for row
    oneBox = []
    if rowIndex == 0 or rowIndex == 1 or rowIndex == 2:
        i = 0
        x = 0
    elif rowIndex == 3 or rowIndex == 4 or rowIndex == 5:
        i = 3
        x = 3
    elif rowIndex == 6 or rowIndex == 7 or rowIndex == 8:
        i = 6
        x = 6
    # collecting column index in the 3x3 section
    while(i<=x+2):
        log("box i is", i)
        if columnIndex == 0 or columnIndex == 1 or columnIndex == 2:
            j = 0
            y = 0
        elif columnIndex == 3 or columnIndex == 4 or columnIndex == 5:
            j = 3
            y = 3
        elif columnIndex == 6 or columnIndex == 7 or columnIndex == 8:
            j = 6
            y = 6
        # appends the input location of 2d array into 3x3 information
        while(j<=y+2):
            log("box j is", j)
            oneBox.append(data[i][j])
            j+=1
        i+=1
    return oneBox

def nakedSingle (row, column, box):
    # takes in 1 row, column, and box set
    possibleValues = []
    for value in range(1,10):
        # iterates through 1-9 as string 
        log("prelim value", value)
        newValue = str(value)
        log("newValue", newValue)
        if newValue not in row and newValue not in column and newValue not in box:
            possibleValues.append(newValue)
            # if iteration is not in row, column, or box, adds input into array in possible values for those cross points
            log( "possibleValues", possibleValues)
    # if there is only 1 possible value available, return the single value
    if len(possibleValues) == 1:
        log("length", len(possibleValues))
        log("", possibleValues[0])
        return [possibleValues[0], possibleValues]
    # switch from original return to possibly return array or '0' and array
    return ['0', possibleValues]

def take_input (puzzle):
    # creates soduku in 2d array
    log("puzzle", puzzle)
    sudokuData=[[],[],[],[],[],[],[],[],[]]
    i=0
    while (i<=8):
        j=0
        while(j<=8):
            sudokuData[i].append(puzzle[f'{i}-{j}'])
            j+=1
        i+=1
    log("organized sudokuData", sudokuData)
    return sudokuData  


def findFirstEmptyCell(data):
    for i in range(9):
        for j in range(9):
            if data[i][j] == '0':
                row = get_row(data, i)
                log("Onerow", row)
                column = get_column(data,j)
                log("oneColumn", column)
                box = get_box(data, i, j)
                log("oneBox", box)
                possibleValues = nakedSingle(row, column, box)
                return [i, j, possibleValues[1]]
    return None



def guessSolve(data):
    newDataSet = prelimSolve(data)
    if newDataSet == None:
        return None
    firstEmptyCellInfo = findFirstEmptyCell(newDataSet)
    if firstEmptyCellInfo == None:
        return newDataSet
    for value in firstEmptyCellInfo[2]:
        dataSetCopy = deepcopy(newDataSet)
        dataSetCopy[firstEmptyCellInfo[0]][firstEmptyCellInfo[1]] = value
        solvedDataSet = guessSolve(dataSetCopy)
        # sovledDataSet if exits - solution made - if None - no solution found
        if solvedDataSet is not None:
            return solvedDataSet
    return None

def prelimSolve(data):
    # set hasNakedSingles to true to keep the solve process going until marked false.
    hasNakedSingles = True
    while hasNakedSingles:
        edited = False
        for i in range(9):
            for j in range(9):
                log("value = ", data[i][j])
                # if a index location is '0' run through to compare possible inputs in nakedSingle using collected compariative data
                if data[i][j] == '0':
                    #collects row, column, and box data by indexes to input into nakedSingle below
                    row = get_row(data, i)
                    log("Onerow", row)
                    column = get_column(data,j)
                    log("oneColumn", column)
                    box = get_box(data, i, j)
                    log("oneBox", box)
                    print("value =", data[i][j])
                    value = nakedSingle(row, column, box)
                    if len(value[1]) == 0:
                        return None
                    if value[0] != '0':
                        edited = True
                    print("value", value)
                    data[i][j]=value[0]
                    log("new dataSet", data[i])
        if edited == False:
            hasNakedSingles = False
    return data

def solve_one(data):
    dataSet = take_input(data)
    log(dataSet, "dataSet")
    newDataSet = prelimSolve(dataSet)
    print("newDataSet")
    print(newDataSet[0])
    print(newDataSet[1])
    print(newDataSet[2])
    print(newDataSet[3])
    print(newDataSet[4])
    print(newDataSet[5])
    print(newDataSet[6])
    print(newDataSet[7])
    print(newDataSet[8])

    return True


# compare all vertical to horizontal for no repeating numbers
def solve_two(data):
    dataSet = take_input(data)
    newDataSet = guessSolve(dataSet)
    print("newDataSet")
    print(newDataSet[0])
    print(newDataSet[1])
    print(newDataSet[2])
    print(newDataSet[3])
    print(newDataSet[4])
    print(newDataSet[5])
    print(newDataSet[6])
    print(newDataSet[7])
    print(newDataSet[8])
    return True


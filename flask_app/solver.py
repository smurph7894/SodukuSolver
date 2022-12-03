from flask_app import app

DEBUG = False
#set DEBUG to TRUE when you want prints to log

def log(inputValue, comment):
    if DEBUG : 
        return print(inputValue, comment)

def get_row(data, rowIndex):
    log(data, "get_row")
    oneRow = []
    i=rowIndex
    while(i<=rowIndex):
        log(i, "row I")
        j=0
        while(j<=8):
            log(j, "column j")
            oneRow.append(data[i][j])
            j+=1
        i+=1
    return oneRow

def get_column(data, columnIndex):
    oneColumn = []
    i=0
    while(i<=8):
        j=columnIndex
        log(i, "column - row i")
        while(j<=columnIndex):
            log(j, "column - column j")
            oneColumn.append(data[i][j])
            j+=1
        i+=1
    return oneColumn

def get_box(data, rowIndex, columnIndex):
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
    while(i<=x+2):
        log(i, "box i is")
        if columnIndex == 0 or columnIndex == 1 or columnIndex == 2:
            j = 0
            y = 0
        elif columnIndex == 3 or columnIndex == 4 or columnIndex == 5:
            j = 3
            y = 3
        elif columnIndex == 6 or columnIndex == 7 or columnIndex == 8:
            j = 6
            y = 6
        while(j<=y+2):
            log(j, "box j is")
            oneBox.append(data[i][j])
            j+=1
        i+=1
    return oneBox

def nakedSingle (row, column, box):
    possibleValues = []
    for value in range(1,10):
        log(value, "prelim value")
        newValue = str(value)
        log(newValue, "newValue")
        if newValue not in row and newValue not in column and newValue not in box:
            possibleValues.append(newValue)
            log( possibleValues, "possibleValues")
    if len(possibleValues) == 1:
        log(len(possibleValues), "length")
        log(possibleValues[0], "")
        return possibleValues[0]
    return '0'

def take_input (puzzle):
    log(puzzle, "puzzle")
    sudokuData=[[],[],[],[],[],[],[],[],[]]
    i=0
    while (i<=8):
        j=0
        while(j<=8):
            sudokuData[i].append(puzzle[f'{i}-{j}'])
            j+=1
        i+=1
    log(sudokuData, "organized sudokuData")
    return sudokuData  

def prelimSolve(data):
    hasNakedSingles = True
    while hasNakedSingles:
        edited = False
        for i in range(9):
            for j in range(9):
                row = get_row(data, i)
                log(row, "Onerow")
                column = get_column(data,j)
                log(column, "oneColumn")
                box = get_box(data, i, j)
                log(box, "oneBox")
                log(data[i][j], "value = ")
                if data[i][j] == '0':
                    print(data[i][j], "value =")
                    value = nakedSingle(row, column, box)
                    if value != '0':
                        edited = True
                    print(value, "value")
                    data[i][j]=value
                    print("new dataSet", data[i])
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

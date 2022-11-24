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

def prelimSolve (dataPoint, row, column, box):
    possibleValues = []
    for value in range(1,10):
        print("prelim value", value)
        if value not in row and value not in column and value not in box:
            possibleValues.append(value)
            print("possibleValues", possibleValues)
        if len(possibleValues) == 1:
            print("length", len(possibleValues))
            return value 

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
    # log(sudokuData, "organized sudokuData")
    return sudokuData  

def solve_one(data):
    dataSet = take_input(data)
    print(dataSet, "dataSet")
    i=0
    for i in range(9):
        j=0
        for j in range(9):
            row = get_row(dataSet, i)
            print(row, "Onerow", i)
            column = get_column(dataSet,j)
            print(column, "oneColumn", j)
            box = get_box(dataSet, i, j)
            print(box, "oneBox", i , j)
            print("value = ", dataSet[i][j])
            if dataSet[i][j] == '0':
                log(dataSet[i][j], "value =")
                value = prelimSolve(dataSet[i][j], row, column, box)
                log(value, "value")
                dataSet[i][j]=value
            j += 1
        i+= 1
    return True


# compare all vertical to horizontal for no repeating numbers

from flask_app import app

DEBUG = True
#set DEBUG to TRUE when you want prints to log

def log(inputValue):
    if DEBUG : 
        print(inputValue)



def take_input (puzzle):
    log(puzzle)
    log(puzzle["0-1"])
    sudokuData=[[],[],[],[],[],[],[],[],[]]
    i=0
    while (i<=8):
        j=0
        while(j<=8):
            sudokuData[i].append(puzzle[f"{i}-{j}"])
            j+=1
        i+=1
    log(sudokuData)
    return sudokuData  

def get_row(data, rowIndex):
    oneRow = []
    i=rowIndex
    while(i<=rowIndex):
        j=0
        while(j<=8):
            oneRow.append(data[i-j])
        j+=1
    return oneRow

def get_column(data, columnIndex):
    oneColumn = []
    i=0
    while(i<=8):
        j=columnIndex
        while(j<=columnIndex):
            oneColumn.append(data[i-j])
            j+=1
    return oneColumn

def get_box(data, columnIndex, rowIndex):
    oneBox = []
    i=rowIndex
    while(i<=rowIndex+3):
        j=columnIndex
        while(j<=columnIndex+3):
            oneBox.append(data[i-j])
            j+=1
    return oneBox

def solve_one(data):
    dataSet = take_input(data)
    row = get_row(dataSet, 0)
    log(row)
    column = get_column(dataSet,0)
    log(column)
    box = get_box(dataSet, 0, 0)
    log(box)
    return True
# compare all vertical to horizontal for no repeating numbers
# maybe sort
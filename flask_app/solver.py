from flask_app import app

DEBUG = True
#set DEBUG to TRUE when you want prints to log

def log(inputValue):
    if DEBUG : 
        return print(inputValue)

def get_row(data, rowIndex):
    print(data, "get_row")
    oneRow = []
    i=rowIndex
    while(i<=rowIndex):
        print(i, "row I")
        j=0
        while(j<=8):
            print(j, "column j")
            oneRow.append(data[i][j])
            j+=1
        i+=1
    return oneRow

# def get_column(data, columnIndex):
#     oneColumn = []
#     i=0
#     while(i<=8):
#         j=columnIndex
#         while(j<=columnIndex):
#             oneColumn.append(data[i][j])
#             j+=1
    # i+=1
#     return oneColumn

# def get_box(data, columnIndex, rowIndex):
#     oneBox = []
#     i=rowIndex
#     while(i<=rowIndex+3):
#         j=columnIndex
#         while(j<=columnIndex+3):
#             oneBox.append(data[i][j])
#             j+=1
#       i+=1
#     return oneBox

def take_input (puzzle):
    log(puzzle)
    sudokuData=[[],[],[],[],[],[],[],[],[]]
    i=0
    while (i<=8):
        j=0
        while(j<=8):
            sudokuData[i].append(puzzle[f'{i}-{j}'])
            j+=1
        i+=1
    # log(sudokuData)
    return sudokuData  

def solve_one(data):
    dataSet = take_input(data)
    log(dataSet)
    row = get_row(dataSet, 0)
    print(row, "Onerow")
    # column = get_column(dataSet,0)
    # log(column)
    # box = get_box(dataSet, 0, 0)
    # log(box)
    return True
# compare all vertical to horizontal for no repeating numbers
# maybe sort
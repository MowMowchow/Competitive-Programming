import sys
maxrow, maxcolumn = sys.stdin.readline().split()
numberofcatcages = int(sys.stdin.readline())
lab = []
maxrow = int(maxrow) +1
maxcolumn = int(maxcolumn) + 1
for i in range(int(maxrow)): #creates the lab
    column = []
    for x in range(int(maxcolumn)):
        column.append(0)
    column[0] = "/"
    lab.append(column)
for i in range(len(lab[0])):
    lab[0][i] = "/"


for i in range(numberofcatcages):
    row, column = sys.stdin.readline().split()
    lab[int(row)][int(column)] = "c"

lab[-1][-1] = "f"


def findpaths(lab, row, column, maxrow, maxcolumn): #make it actualy DP, you're not saving anything rn
    if row + 1 > maxrow or column + 1 > maxcolumn:  # the problem
        return 0

    elif lab[row][column] == 'f':
        return 1

    elif lab[row][column] != 0:
        if lab[row][column] == "c":
            return 0
        else:
            return lab[row][column]


    else:
        options = findpaths(lab, row+1, column, maxrow, maxcolumn) + findpaths(lab, row, column+1, maxrow, maxcolumn)
        lab[row][column] = options
        return options


print(findpaths(lab, 1, 1, maxrow, maxcolumn))
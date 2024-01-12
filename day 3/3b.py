def containsSymbol(part: str):
    for char in part:
        if char == '*':
            return True
    return False

def getNumbers(matrix: [[]]):
    parts = []
    partNo = ""
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if (str(matrix[row][column]).isdigit()):
                partNo += matrix[row][column]
                continue
            elif ((matrix[row][column] == ".")) and len(partNo) > 0:
                #check surroundings
                bottom = column - len(partNo) - 1 if ((column - len(partNo) - 1) > 0) else 0 
                top = column + 1 if (column < len(matrix[row]) - 1) else column

                if (row > 0) and containsSymbol(str(matrix[row-1][bottom:top])):
                    parts.append(int(partNo))
                    partNo = ""
                    continue
                elif containsSymbol(str(matrix[row][bottom:top])):
                    parts.append(int(partNo))
                    partNo = ""
                    continue
                elif (row < len(matrix) - 1) and containsSymbol(str(matrix[row+1][bottom:top])):
                    parts.append(int(partNo))
                    partNo = ""
                    continue
                partNo = ""
                continue
            elif ('*' == matrix[row][column]) and (len(partNo) > 0):
                parts.append(int(partNo))
                partNo = ""
                continue
        if (len(partNo) > 0):
            #check surroundings
            bottom = column - len(partNo) if ((column - len(partNo)) > 0) else 0 
            top = column + 1 if (column < len(matrix[row]) - 1) else column
            if (row > 0) and containsSymbol(str(matrix[row-1][bottom:top])):
                parts.append(int(partNo))
                partNo = ""
            elif containsSymbol(str(matrix[row][bottom:top])):
                parts.append(int(partNo))
                partNo = ""
            elif (row < len(matrix) - 1) and containsSymbol(str(matrix[row+1][bottom:top])):
                parts.append(int(partNo))
                partNo = ""
        partNo = ""
    return parts

def getSum(matrix: [[]]):
    sum = 0
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if (str(matrix[row][column]) == '*'):
                west = column - 3 if (column - 3 > 0) else 0
                east = column + 3 if (column < len(matrix[row]) - 3) else len(matrix[row])
                north = row - 1 if row > 0 else 0
                south = row + 1 if row < len(matrix) - 1 else len(matrix)

                new = []
                for i in range(north, south + 1):
                    new.append(matrix[i][west:east + 1])

                adjacent = getNumbers(new)
                print(adjacent)

                if len(adjacent) == 2:
                    sum += adjacent[0] * adjacent[1]
    return sum

if __name__ == "__main__":
    file = open("3test2.txt", "r")
    matrix = []
    while True:
        line = file.readline()
        if not line:
            break
        matrix.append(line.removesuffix('\n'))
    result = getSum(matrix)
    print(result)

#74115253 too low
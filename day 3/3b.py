def getNumber(matrix, row, column):
    index = column 
    while index > 0 and str(matrix[row][index]).isdigit() and (str(matrix[row][index-1]).isdigit()):
        index -= 1
    
    part = ""

    while index < len(matrix[row]) and (str(matrix[row][index])).isdigit():
        part += str(matrix[row][index])
        index += 1

    if part == "":
        return -1
    return int(part)

def getNumbers(matrix, row, column):
    parts = []
    if row > 0:
        if not matrix[row - 1][column].isdigit():
            if column > 0:
                parts.append(getNumber(matrix, row - 1, column - 1))
            if column < len(matrix[row-1]):
                parts.append(getNumber(matrix, row - 1, column + 1))
        else:
            parts.append(getNumber(matrix, row - 1, column))
    if column > 0:
        parts.append(getNumber(matrix, row, column -1))
    if column < len(matrix[row]) - 1:
        parts.append(getNumber(matrix, row, column +1))
    if row < len(matrix) - 1: 
        if not matrix[row + 1][column].isdigit():
            if column > 0:
                parts.append(getNumber(matrix, row + 1, column - 1))
            if column < len(matrix[row-1]):
                parts.append(getNumber(matrix, row + 1, column + 1))
        else:
            parts.append(getNumber(matrix, row + 1, column))

    for i in range(parts.count(-1)):
        parts.remove(-1)
    
    return parts


def getSum(matrix: [[]]):
    sum = 0
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if (str(matrix[row][column]) == '*'):
                adjacent = getNumbers(matrix, row, column)
                if len(adjacent) == 2:
                    sum += adjacent[0] * adjacent[1]
    return sum

if __name__ == "__main__":
    file = open("3.txt", "r")
    matrix = []
    while True:
        line = file.readline()
        if not line:
            break
        matrix.append(line.removesuffix('\n'))
    result = getSum(matrix)
    print(result)

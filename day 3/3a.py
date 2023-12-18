def containsSymbol(part: str):
    for char in part:
        if char == '.' or char.isdigit():
            continue
        else:
            return True
    return False

def getSum(matrix: [[]]):
    sum = 0
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
                    print(partNo)
                    sum += int(partNo)
                    partNo = ""
                    continue
                elif containsSymbol(str(matrix[row][bottom:top])):
                    print(partNo)
                    sum += int(partNo)
                    partNo = ""
                    continue
                elif (row < len(matrix) - 1) and containsSymbol(str(matrix[row+1][bottom:top])):
                    print(partNo)
                    sum += int(partNo)
                    partNo = ""
                    continue
                partNo = ""
                continue
            elif (('!', '@', '#', '$', '%', '^', '&', '*', '+', '-', '/', '=').__contains__(matrix[row][column])) and (len(partNo) > 0):
                sum += int(partNo)
                partNo = ""
                continue
        if (len(partNo) > 0):
            #check surroundings
            bottom = column - len(partNo) if ((column - len(partNo)) > 0) else 0 
            top = column + 1 if (column < len(matrix[row]) - 1) else column
            if (row > 0) and containsSymbol(str(matrix[row-1][bottom:top])):
                print(partNo)
                sum += int(partNo)
                partNo = ""
            elif containsSymbol(str(matrix[row][bottom:top])):
                print(partNo)
                sum += int(partNo)
                partNo = ""
            elif (row < len(matrix) - 1) and containsSymbol(str(matrix[row+1][bottom:top])):
                print(partNo)
                sum += int(partNo)
                partNo = ""
        partNo = ""
        print()
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
    print()
    print(result)
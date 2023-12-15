numbersDict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def parseLine(line: str):
    numbers = []
    for i in range(len(line) + 1):
        for j in range(len(line[:i])):
            if line[j:i] in numbersDict.keys():
                numbers.append(int(numbersDict[line[j:i]]))
    return numbers

def getCoordinate(line: str):
    for k, v in numbersDict.items():
        line = line.replace(v, k)
    numbers = parseLine(line)
    if len(numbers) != 1:
        return int(str(numbers[0])+str(numbers[len(numbers)-1]))
    else:
        return int(str(numbers[0])+str(numbers[0]))

if __name__ == "__main__":
    file = open("1.txt", "r")
    out = 0
    while True:
        line = file.readline()
        if not line:
            break
        out += getCoordinate(line)
    print(out)

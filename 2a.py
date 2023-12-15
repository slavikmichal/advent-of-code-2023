constraints = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def checkCorrectHand(hand: str):
    cubes = [h.strip().split(' ') for h in hand.split(',')] 
    for cube in cubes:
        if int(cube[0]) > constraints[cube[1]]:
            return False
    return True


def checkGame(id: int, line: str):
    for hand in line.split('; '):
        if not checkCorrectHand(hand):
            return 0  
    return id 
    
if __name__ == "__main__":
    file = open("2.txt", "r")
    out = 0
    while True:
        line = file.readline().removesuffix('\n')
        if not line:
            break
        game = line.split(": ")
        game[0] = int(game[0].replace("Game ", ""))
        out += checkGame(game[0], game[1])
    print(out)

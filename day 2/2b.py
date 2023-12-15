def checkCorrectHand(hand: str, const: dict):
    cubes = [h.strip().split(' ') for h in hand.split(',')] 
    for cube in cubes:
        if int(cube[0]) > const[cube[1]]:
            const[cube[1]] = int(cube[0])

def checkGame(id: int, line: str):
    constraints = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for hand in line.split('; '):
        checkCorrectHand(hand, constraints)
    power = 1
    for val in list(constraints.values()):
        power *= val
    return power
    
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

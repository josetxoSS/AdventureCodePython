import sys

route = 'InputTwo.txt'
count = 0

import sys

def readfile_line(route):
    try:
        with open(route, 'rb') as f:
            for line in f:
                decoded_line = line.decode('utf-8').strip()
                yield decoded_line
    except OSError:
        print("Could not open/read file:", route)

# Uso de la función
def calculator():
    pointsOptions = {'X': 1, 'Y': 2, 'Z': 3}
    pointResult = {'X': 0, 'Y': 3, 'Z': 6}
    contentGenerator = readfile_line(route)
    total = 0
    for item in contentGenerator:
        listItems = item.split()
        Opponent = listItems[0]
        me = listItems[1]
        defaultPoints = pointResult[me]
        status = switch(Opponent, me)
        total += status + defaultPoints
    return total

def switch(opponent,me):
    if opponent == "A":
        if me == 'X':
            return 3
        elif me == 'Y':
            return 1
        elif me == 'Z':
            return 2
    elif opponent == "B":
        if me == 'X':
            return 1
        elif me == 'Y':
            return 2
        elif me == 'Z':
            return 3
    elif opponent == "C":
        if me == 'X':
            return 2
        elif me == 'Y':
            return 3
        elif me == 'Z':
            return 1

print(calculator())
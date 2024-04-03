route = 'input.txt'
count = 0
from itertools import combinations
import sys
from itertools import product
import sys

def readfile_line(route):
    try:
        with open(route, 'rb') as f:
            for line in f:
                decoded_line = line.decode('utf-8').strip()
                yield decoded_line
    except OSError:
        print("Could not open/read file:", route)

def calculator():
    pointsOptions = {'X': 1, 'Y': 2, 'Z': 3}
    pointResult = {'lost': 0, 'draw': 3, 'win': 6}
    contentGenerator = readfile_line(route)
    total = 0
    for item in contentGenerator:
        listItems = item.split()
        Opponent = listItems[0]
        me = listItems[1]
        defaultPoints = pointsOptions[me]
        status = switch(Opponent,me)
        total += status + defaultPoints
    return total

def switch(opponent,me):
    if opponent == "A":
        if me == 'X':
            return 3
        elif me == 'Y':
            return 6
        elif me == 'Z':
            return 0
    elif opponent == "B":
        if me == 'X':
            return 0
        elif me == 'Y':
            return 3
        elif me == 'Z':
            return 6
    elif opponent == "C":
        if me == 'X':
            return 6
        elif me == 'Y':
            return 0
        elif me == 'Z':
            return 3

print(calculator())
def combin():
    arr = ['A','B','C']
    arrytwo = ['X','Y','Z']
    combinaciones = list(product(arr, arrytwo))
    print(combinaciones)

# Call the function to see the combinations
#combin()
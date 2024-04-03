import string

route = 'input.txt'
def readfile_line(route):
    try:
        with open(route, 'rb') as f:
            for line in f:
                decoded_line = line.decode('utf-8').strip()
                yield decoded_line
    except OSError:
        print("Could not open/read file:", route)

def backpack():
    cont = 0
    contentGenerator = readfile_line(route)
    contentlowercase = {letter: idx + 1 for idx, letter in enumerate(string.ascii_lowercase[:26])}
    contentUppercase = {letter: idx + 27 for idx, letter in enumerate(string.ascii_uppercase[:26])}
    group = []
    for item in contentGenerator:
        # Add the current item to the group
        uniqueWord=''.join(set(item))
        group.append(uniqueWord)
        # If the group contains three items, process it
        #print(group)
        if len(group) == 3:
            # Process the group (e.g., print it)
            comun = list(set(group[0]) & set(group[1]) & set(group[2]))
            letter =comun[0]
            #print(letter)
            if letter.islower():
                cont += contentlowercase[letter]
                #print(cont)
            elif letter.isupper():
                cont += contentUppercase[letter]
            # Clear the group to start a new one
            group.clear()
        #print(cont)
    return cont

print(backpack())
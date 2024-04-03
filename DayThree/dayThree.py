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
    cont=0
    contentGenerator = readfile_line(route)
    contentlowercase = {letter:idx+1 for idx,letter in enumerate (string.ascii_lowercase[:26])}
    contentUppercase = {letter: idx + 27 for idx, letter in enumerate(string.ascii_uppercase[:26])}
    #print(contentlowercase)
    for item in contentGenerator:
        lenFirstItem = int(len(item)/2)
        lensecondaItem = len(item)-lenFirstItem
        firstItem = item[:lensecondaItem]
        secondItem= item[lensecondaItem:]
        #print(item)
        #print(firstItem)
        #print(secondItem)
        for letter in set(firstItem):
            if letter in set(secondItem):
                #print(letter)
                if letter.islower():
                    cont+=contentlowercase[letter]
                    break
                elif letter.isupper():
                    cont+=contentUppercase[letter]
                    break
    return cont

print(backpack())
route = 'test.txt'

def readfile_line(route):
    try:
        with open(route, 'rb') as f:
            for line in f:
                decoded_line = line.decode('utf-8')
                yield decoded_line
    except OSError:
        print("Could not open/read file:", route)

def append_letter(container, letter, index):
    if index < len(letter):
        if letter[index]!=' ':
            container.append(letter[index])
    return container

def content_generator():
    cont = 0
    contentGenerator = readfile_line(route)
    status = False
    containerOne = []
    containerTwo = []
    containerThree = []
    for item in contentGenerator:
        letter = [x for x in item]
        print(letter)
        cont += 1
        if cont < 4:
            containerOne = append_letter(containerOne, letter, 1)
            containerTwo = append_letter(containerTwo, letter, 5)
            containerThree = append_letter(containerThree, letter, 9)
        else:
            break
        # Remove trailing spaces

    containerOne = containerOne[::-1]
    containerTwo = containerTwo[::-1]
    containerThree = containerThree[::-1]
    #print(containerOne)
    #print(containerTwo)
    #print(containerThree)
    return containerOne,containerTwo,containerThree

def calculator():
    cont=0
    contentGenerator = readfile_line(route)
    containerOne, containerTwo, containerThree = content_generator()
    containers=[containerOne,containerTwo,containerThree]
    #print(containers)
    for item in contentGenerator:
        cont += 1
        if cont > 5:

            num_elemets = int(item.strip().split(" ")[1])
            numcontainerSource=int(item.strip().split(" ")[3])
            numcontainerDestiny = int(item.strip().split(" ")[5])
            containerSource = containers[numcontainerSource-1]
            elementstomove=containerSource[-num_elemets:]
            containerDestiny = containers[numcontainerDestiny-1]
            del containerSource[-num_elemets:]
            containerDestiny.extend((elementstomove[::-1]))

            #print(num_elemets)
            print('s')
        print(containers)
            #print(containerSource)
            #print(containerDestiny)
        #print(item.strip().split(" "))
    #print(containers)
    #print(containerThree)




#calculator()
content_generator()
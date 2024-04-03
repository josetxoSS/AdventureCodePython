route = 'input.txt'

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

def content_generator(numContainer,endlineContainer):
    cont = 0

    contentGenerator = readfile_line(route)
    containers = []
    status = False
    for i in range(numContainer):
        container = []
        containers.append(container)
    #containerOne = []
    #containerTwo = []
    #containerThree = []
    for item in contentGenerator:
        contContainer = 0
        letter = [x for x in item]
        #print(letter)
        cont += 1
        if cont < endlineContainer:
            pos = 1
            for container in containers:
                container = append_letter(container, letter, pos)
                contContainer += 1
                #print(container)
                #print(pos)
                pos += 4
                if contContainer > numContainer-1:
                    #print('hi')
                    #print(contContainer)
                    break
                #containerOne = append_letter(containerOne, letter, 1)
                #containerTwo = append_letter(containerTwo, letter, 5)
                #containerThree = append_letter(containerThree, letter, 9)
        else:
            break
        # Remove trailing spaces
    for i in range(len(containers)):
        containers[i] = containers[i][::-1]
        #print(container)
    #containerOne = containerOne[::-1]
    #containerTwo = containerTwo[::-1]
    #containerThree = containerThree[::-1]
    #print(containerOne)
    #print(containerTwo)
    #print(containerThree)
    #return containerOne,containerTwo,containerThree
    #print(containers)
    return containers

def calculator(numContainer,endlineContainer,startInstrucctions):
    cont=0
    contentGenerator = readfile_line(route)
    containers = content_generator(numContainer,endlineContainer)
    #print(containers[0])
    #print(containers)
    for item in contentGenerator:
        cont += 1
        if cont > startInstrucctions:

            num_elemets = int(item.strip().split(" ")[1])
            numcontainerSource=int(item.strip().split(" ")[3])
            numcontainerDestiny = int(item.strip().split(" ")[5])
            containerSource = containers[numcontainerSource-1]
            elementstomove=containerSource[-num_elemets:]
            containerDestiny = containers[numcontainerDestiny-1]
            del containerSource[-num_elemets:]
            containerDestiny.extend((elementstomove[::-1]))

            #print(num_elemets)
            #print('s')
        #print(containers)
    return containers
            #print(containerSource)
            #print(containerDestiny)
        #print(item.strip().split(" "))
    #print(containers)
    #print(containerThree)


def listTopContainer(numContainer,endLine,startInstruc):
    containers = calculator(numContainer, endLine, startInstruc)
    aboveElements = []
    aboveElements=[container[-1] for container in containers]
    print(aboveElements)
    print(''.join(aboveElements))
#print(calculator(3,4,5))
#content_generator(3)
listTopContainer(9,9,10)
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

def pairs(route):
    cont = 0
    contentgenerator = readfile_line(route)
    for content in contentgenerator:
        pairs = content.split(',')
        #print(pairs)
        nums =[int(num) for pair in pairs for num in pair.split('-')]
        if ((nums[2]<=nums[0]<=nums[3] and nums[2]<=nums[1]<=nums[3]) or
        (nums[0]<=nums[2]<=nums[1] and nums[0]<=nums[3]<=nums[1])):
            cont+=1
    return cont



print(pairs(route))
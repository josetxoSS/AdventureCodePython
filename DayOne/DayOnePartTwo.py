route='Data/input.txt'
count = 0
print("Using readlines()")

def readfile_line(route):
    total = 0
    max_sum = 0
    sumList=[]
    with open(route) as fp:
        for line in fp:
            if line.strip():  # Checking if line is not empty
                value = line.strip()
                total += int(value)
            else:
                sumList.append(total)
                if total > max_sum:
                    max_sum = total
                total = 0

        # Check for the maximum sum at the end of file
        sumList.append(total)
        sumList.sort(reverse=True)
        print("Sum top Three",sum(sumList[:3]))
        if total > max_sum:
            max_sum = total

    return max_sum

def top_three(num,top_three,max):
    pass


print(readfile_line(route))

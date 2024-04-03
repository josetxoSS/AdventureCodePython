route='Data/demo.txt'
count = 0
print("Using readlines()")

def readfile_line(route):
    total = 0
    max_sum = 0
    with open(route) as fp:
        for line in fp:
            if line.strip():  # Checking if line is not empty
                value = line.strip()
                total += int(value)
            else:
                if total > max_sum:
                    max_sum = total
                total = 0

        # Check for the maximum sum at the end of file
        if total > max_sum:
            max_sum = total

    return max_sum


print(readfile_line(route))

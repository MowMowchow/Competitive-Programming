import sys
# nested for loop going over all possible lengths
# for each sum (i+j) check to see if there are any boards of those lengths
# (i and j respectively) and add to an array respectively if there are

n = int(sys.stdin.readline())
boards = [int(x) for x in sys.stdin.readline().split()]
arr = [0 for x in range(2001)]
for board in boards:
    arr[board] += 1

# print(arr)
count = [0 for x in range(4001)]
for i in range(2001):
    if arr[i] != 0:
        for j in range(i, 2001):  # something with i + 1
            if arr[j] != 0:
                # print(i, j, arr[i+j])
                if i == j:
                    if arr[i] >= 2:
                        # print("i == j", i, j, "|", count[i+j])
                        count[i+j] += arr[i]//2

                else:
                    # print("i != j", i, j, "|", count[i+j])
                    count[i+j] += min(arr[i], arr[j])


final = 0
finalcount = 0
for i in range(4001):
    if count[i] > final:
        final = count[i]
        finalcount = 1

    elif count[i] == final:
        finalcount += 1

# print(count)
print(final, finalcount)
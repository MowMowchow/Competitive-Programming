import sys


def lowbinsearch(arr, goal):
    first = 0
    last = len(arr)-1
    while last >= first:
        index = first+(last-first+1)//2

        if arr[index] < goal:
            first = index + 1
        else:
            last = index-1
    return first


b = int(sys.stdin.readline())
batches = [[int(x) for x in sys.stdin.readline().split()] for x in range(b)]
f = int(sys.stdin.readline())
failed = [-1]+[int(sys.stdin.readline()) for x in range(f)]
total = 0
failed.sort()
for batch in batches:
    upperf = lowbinsearch(failed, batch[0])  # next highest number

    if upperf > f:
        total += batch[2]

    elif batch[0] <= failed[upperf] <= batch[1]:
        pass

    else:
        total += batch[2]

print(total)
import sys
n, p, m = [int(x) for x in sys.stdin.readline().split()]
tanks = [[int(x) for x in sys.stdin.readline().split()] for x in range(n)]
physicalattacks = [int(x) for x in sys.stdin.readline().split()]
magicalattacks = [int(x) for x in sys.stdin.readline().split()]
physicalattacks.sort()
magicalattacks.sort()
prephysical = [0 for x in range(p+1)]
premagical = [0 for x in range(m+1)]
for i in range(1, p+1):
    prephysical[i] += prephysical[i-1] + physicalattacks[i-1]
for i in range(1, m+1):
    premagical[i] += premagical[i-1] + magicalattacks[i-1]


def binsearch(arr, curr):
    first = 0
    last = len(arr)-1
    while last >= first:
        index = first+(last-first)//2

        if arr[index] <= curr:
            first = index+1
        else:
            last = index-1

    return first


lowest = [float("inf"), 0 ]
counter = 0
for tank in tanks:
    counter += 1
    phys = tank[0]
    magi = tank[1]

    ind1 = binsearch(physicalattacks, phys)
    ind2 = binsearch(magicalattacks, magi)

    x = max((prephysical[-1]-prephysical[ind1]) - (phys*(len(physicalattacks)-ind1)), 0)
    y = max((premagical[-1]-premagical[ind2]) - (magi*(len(magicalattacks)-ind2)), 0)

    if (x+y) < lowest[0]:
        lowest[0] = x + y
        lowest[1] = counter


print(lowest[1])
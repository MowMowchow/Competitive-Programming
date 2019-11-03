import sys

numberofrabbitgirls = int(sys.stdin.readline())
groupsize = int(sys.stdin.readline())

if groupsize > numberofrabbitgirls:
    print(groupsize - numberofrabbitgirls)
elif groupsize == numberofrabbitgirls:
    print(0)
else:
    leftover = numberofrabbitgirls % groupsize

    if leftover > int(groupsize / 2):
        print(groupsize - leftover)

    elif leftover == 0:
        print(0)

    else:
        print(leftover)
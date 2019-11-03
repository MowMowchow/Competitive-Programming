import sys
thing = []

c = int(sys.stdin.readline())

for q in range(c):
    temp = sys.stdin.readline().strip("\n").split()
    ind = int(temp[0])
    if ind != 4:
        cond = temp[1]
    if ind == 1:
        if cond not in thing:
            thing.append(cond)
            print("true")
        else:
            print("false")
    elif ind == 2:
        if cond in thing:
            thing.remove(cond)
            print("true")
        else:
            print("false")
    elif ind == 3:
        if cond in thing:
            print(thing.index(cond))
        else:
            print(-1)
    elif ind == 4:
        thing.sort()
        if thing:
            print(" ".join([x for x in thing]))
        else:
            print()
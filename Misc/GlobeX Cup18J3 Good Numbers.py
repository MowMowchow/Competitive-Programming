import sys, math
numberofqueries = int(sys.stdin.readline())


def checkifgood(x):
    num = int(math.sqrt(x))+1

    for i in range(2, num):
        if x % i == 0:
            return False

    return True


counter = 0
for q in range(numberofqueries):
    query = int(sys.stdin.readline())
    digitnum = sum([int(x) for x in str(query)])
    if query != 1 and query != 0:
        if checkifgood(query) and checkifgood(digitnum):
            counter += 1

print(counter)
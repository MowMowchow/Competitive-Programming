import sys
q = int(sys.stdin.readline().strip('\n'))
n = int(sys.stdin.readline().strip("\n"))

if q == 2: #max
    dmoj = [int(x) for x in sys.stdin.readline().split()]
    peg = [int(x) for x in sys.stdin.readline().split()]

    dmoj.sort(reverse=True)
    peg.sort()

    counter = 0
    for i in range(n):
        counter += max(dmoj[i], peg[i])

    print(counter)


elif q == 1: #min
    dmoj = [int(x) for x in sys.stdin.readline().split()]
    peg = [int(x) for x in sys.stdin.readline().split()]

    dmoj.sort()
    peg.sort()

    counter = 0
    for i in range(n):
        counter += max(dmoj[i], peg[i])

    print(counter)
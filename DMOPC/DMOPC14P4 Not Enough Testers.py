import sys, bisect
t = int(sys.stdin.readline())
factors = [1 for x in range(100001)]
klist = [[0] for x in range(100001)]


def weirdsieve(x):
    p = 2
    while p <= x:
        for i in range(p, x+1, p):
            factors[i] += 1

        p += 1


weirdsieve(100000)

for i in range(1, 100001):
    klist[factors[i]].append(i)

for q in range(t):
    k, a, b = [int(x) for x in sys.stdin.readline().split()]
    if k == 1 and a == 1:
        print(1)
    else:
        result = (bisect.bisect_left(klist[k], b+1))-(bisect.bisect_left(klist[k], a))
        print(result)
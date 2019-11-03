import sys
klist = [0 for x in range(10000001)]


def sieve(x):
    for i in range(2, 10000001):
        if klist[i] == 0:
            for j in range(i, 10000001, i):
                klist[j] += 1


sieve(10000000)


n = int(sys.stdin.readline())
for i in range(n):
    a, b, k = [int(x) for x in sys.stdin.readline().split()]
    total = 0
    for num in klist[a:b+1]:
        if num == k:
            total += 1
    print("Case", "#"+str(i+1)+":", total)
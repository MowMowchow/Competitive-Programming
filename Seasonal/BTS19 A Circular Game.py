import sys
n, m = [int(x) for x in sys.stdin.readline().split()]
spinners = [int(x) for x in sys.stdin.readline().split()]
low = float("inf")
spinners.sort()

for i in range(n):
    temp = 0
    for j in range(n):
        if j != i:
            res1 = ((spinners[j]-spinners[i])+m) % m
            res2 = ((spinners[i]-spinners[j])+m) % m
            if res1 == 0:
                res = m
            if res2 == 0:
                res = m
            temp += min(res1, res2)

    low = min(low, temp)

print(low)
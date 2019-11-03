# problem 3
import sys
n, m = [int(x) for x in sys.stdin.readline().split()]
arr = [int(x) for x in sys.stdin.readline().split()]
bits = [[0 for x in range(n+1)] for y in range(21)]


def sumBIT(g, k):
    total = 0
    while k >= 1:
        total += bits[g][k]
        k -= k& -k
    return total


def updateBIT(g, x, k):
    while k <= n:
        bits[g][k] += x
        k += k & -k

for i in range(n):
    updateBIT(arr[i], 1, i+1)


for qq in range(m):
    q = [int(x) for x in sys.stdin.readline().split()]
    if q[0] == 1:  # update
        a, b = q[1:]
        updateBIT(arr[a-1], -1, a)  # removing old element
        updateBIT(b, 1, a)  # adding new element
        arr[a-1] = b

    elif q[0] == 2:  #loop

        l, r, c = q[1:]
        counter = 0
        for i in range(20, -1, -1):
            result = sumBIT(i, r) - sumBIT(i, l-1)
            counter += result
            if counter >= c:
                print(i)
                break
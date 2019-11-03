# problem 1
import sys
q = int(sys.stdin.readline())


def do(x, a, b, t):
    low = 0
    high = x
    curr = 0

    while low <= high:
        curr = low+(high-low)//2
        amt = a*curr - b*(x-curr)

        if amt >= t and a*(curr-1)-b*(x-curr+1) < t:
            return curr

        elif amt < t:
            low = curr + 1
        else:
            high = curr - 1

    return curr


for qq in range(q):
    n, aa, bb, tt = [int(x) for x in sys.stdin.readline().split()]
    result = do(n, aa, bb, tt)
    if aa*result - bb*(n-result) >= tt:
        print(result)
    else:
        print(-1)
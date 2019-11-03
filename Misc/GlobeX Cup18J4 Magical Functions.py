import sys
a, b, c, d, e, N = [int(x) for x in sys.stdin.readline().split()]
arr = {}


def f(x):

    if x == 0:
        return e

    if x in arr:
        return arr[x]

    final = ((a*f(int(abs(x/b)))) + (c*f(int(abs(x/d))))) % (10**9 + 7)
    arr[x] = final
    return final


print(f(N))
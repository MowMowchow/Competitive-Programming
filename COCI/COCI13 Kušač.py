import sys
n, m = [int(x) for x in sys.stdin.readline().split()]


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)


print(m-gcd(n, m))
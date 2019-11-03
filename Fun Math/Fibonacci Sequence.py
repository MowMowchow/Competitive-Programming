import sys
mod = 1000000007


def fib(n):
    if n == 0:
        return 0, 1
    else:
        a, b = fib(n // 2)
        c = a * (b * 2 - a + mod) % mod
        d = ((a*a)%mod + (b*b)%mod)%mod
        if n % 2 == 0:
            return c, d
        else:
            return d, (c + d) %mod


n = int(sys.stdin.readline())
print(fib(n)[0])
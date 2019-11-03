import sys
n, m = [int(x) for x in sys.stdin.readline().split()]
primes = [True for x in range(n + 1)]
total = 0


def sieve(n):
    x = 2
    while x*x <= n:
        if primes[x]:
            primes.append(x)
            for i in range(x*x, n+1, x):
                primes[i] = False
        x += 1

    return primes


sieve(n)


for i in range(2, n+1):
    if primes[i]:
        if n-i != 0:
            leftover1 = n-i
            leftover2 = n-i-1
            total += (leftover1//m)+1
            total += (leftover2//m)+1
        else:
            total += 1

print(total)
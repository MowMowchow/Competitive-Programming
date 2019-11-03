import sys
primes = [True for x in range(33)]


def sieve(x):
    p = 2
    while p*p <= x:
        if primes[p]:
            for i in range(p*p, x+1, p):
                primes[i] = False

        p += 1


def det(x, og):
    total = 0
    for i in range(2, x+1):
        if x % i == 0 and primes[i] and i != og:
            total += 1
            total += det(x//i, og)
            return total

    return 0


sieve(32)
for q in range(5):
    n = int(sys.stdin.readline())
    print(det(n, n))
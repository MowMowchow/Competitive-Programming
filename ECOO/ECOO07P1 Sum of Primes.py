import sys
from bisect import bisect_right
primes = [True for x in range(10000000)]
onlyprimes = []
primes[0], primes[1] = False, False

def sieve(n):
    for i in range(2, 10000000):
        if primes[i]:
            onlyprimes.append(i)
            for j in range(i << 1, 10000000, i):
                primes[j] = False


def upperbinsearch(arr, goal):
    first = 0
    last = len(arr)-1
    while last >= first:
        index = first+(last-first+1)//2

        if arr[index] <= goal:
            first = index + 1
        else:
            last = index-1
    return first


sieve(10000000)
for q in range(5):
    n = int(sys.stdin.readline())

    if n % 2:
        if primes[n]:
            # print(n, "=", n)
            print '%s = %s' % (n, n)
        else:

            curr = upperbinsearch(onlyprimes, n//3)
            curr -= primes[0]-1
            a, b, c, temp = 1, 0, 0, 0
            while a > b:
                a = onlyprimes[curr]
                temp = n-a
                # a = b, b = c, target = temp
                temp2 = upperbinsearch(onlyprimes, temp//2)
                temp2 -= onlyprimes[0] - 1
                for i in range(temp2, -1, -1):
                    temp3 = temp-onlyprimes[i]
                    if primes[temp3]:
                        b = onlyprimes[i]
                        c = temp3
                        break

                curr -= 1

            # print(n, "=", a, "+", b, "+", c)
            print '%s = %s + %s + %s' % (n, a, b, c)

    else:
        temp = upperbinsearch(onlyprimes, n//2)
        temp -= onlyprimes[0] - 1
        for i in range(temp, -1, -1):
            temp2 = n - onlyprimes[i]
            if primes[temp2]:
                a = onlyprimes[i]
                b = temp2
                break

        # print(n, "=", a, "+", b)
        print '%s = %s + %s' % (n, a, b)
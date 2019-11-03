import sys
from math import sqrt
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b%a, a)
n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split()]
if n == 1:
    print(arr[0])
else:
    largest = float("inf")
    primefactors = [1]

    for i in range(n-1):
        largest = min(largest, gcd(arr[i], arr[i+1]))

    largestt = int(largest)
    root = int(sqrt(largest))+1
    while largestt % 2 == 0:
        primefactors.append(2)
        largestt /= 2

    for number in range(3, root, 2):
        while largestt % number == 0:
            primefactors.append(int(number))
            largestt /= number

    if largestt > 2:
        primefactors.append(int(largestt))

    #print(primefactors)
    if primefactors[-1] == 1:
        print("DNE")
    else:
        print(primefactors[-1])
import sys
from math import sqrt


def uh(a):
    return sqrt((a[0]**2)+(a[1]**2))


def binsearch(arr, goal):
    first = 0
    last = len(arr)-1
    while last >= first:
        index = first+(last-first)//2

        if arr[index] <= goal:
            first = index + 1
        else:
            last = index-1
    return first


n, q = [int(x) for x in sys.stdin.readline().split()]
dists = [uh([int(x) for x in sys.stdin.readline().split()]) for x in range(n)]
dists.sort()

for i in range(q):
    query = int(sys.stdin.readline())
    print(binsearch(dists, query))
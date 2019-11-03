import sys
n, k = [int(x) for x in sys.stdin.readline().split()]
items = [int(x) for x in sys.stdin.readline().split()]
items.sort()

#binary search for closest item
def binsearch(c):
    first = 0
    last = n-1
    while last >= first:
        index = first+(last-first)//2

        if items[index] <= c:
            first = index + 1

        elif items[index] > c:
            last = index-1

    return last

final = 0
for i in range(n):
    final = max(binsearch(items[i]+k)-(i-1), final)

print(final)
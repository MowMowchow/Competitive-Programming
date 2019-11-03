import sys
n, k, q = [int(x) for x in sys.stdin.readline().split()]
seq = [int(x) for x in sys.stdin.readline().split()]
prefix = [0 for x in range(n+1)]

for i in range(1, n+1):
    prefix[i] += prefix[i-1] + seq[i-1]


def binsearch(goal, arr):
    first = 0
    last = len(arr)-1

    while last >= first:
        ind = first+(last-first)//2

        if arr[ind] == goal:
            return True
        elif arr[ind] < goal:
            first = ind + 1
        else:
            last = ind-1

    return False


for _ in range(q):
    a, b, x, y = [int(x) for x in sys.stdin.readline().split()]
    yup = False
    if prefix[y]-prefix[x-1] > k:
        if binsearch(a, seq[x-1:y]) and binsearch(b, seq[x-1:y]):
            yup = True

    if yup:
        print("Yes\n")
    else:
        print("No\n")
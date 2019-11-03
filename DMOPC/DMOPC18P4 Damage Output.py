import sys
n, m = [int(x) for x in sys.stdin.readline().split()]
arr = [int(x) for x in sys.stdin.readline().split()]

last = 0
first = 0
sum = arr[first]
final = float("inf")
while last <= first:
    if sum >= m:
        final = min(first-last, final)
        sum -= arr[last]
        last += 1

    else:
        first += 1
        if first == n:
            break
        sum += arr[first]




if final == float("inf"):
    print(-1)
else:
    print(final+1)
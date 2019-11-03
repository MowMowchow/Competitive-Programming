import sys
n, t = [int(x) for x in sys.stdin.readline().split()]
diff = [0 for x in range(n+2)]
arr = [0 for x in range(n+1)]
for q in range(t):
    a, b, c = [int(x) for x in sys.stdin.readline().split()]
    diff[a] += c
    diff[b+1] -= c
l = int(sys.stdin.readline())


for i in range(1, n+1):
    diff[i] += diff[i-1]

for i in range(1, n+1):
    arr[i] = arr[i-1] + diff[i]

upper = 1
lower = 0
high = 0
curr = 0

while lower <= upper:
    if arr[upper]-arr[lower] <= l:
        high = max(high, upper-lower)
        upper += 1
        if upper == n+1:
            break

    else:
        lower += 1


print(high)
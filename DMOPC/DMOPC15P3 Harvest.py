import sys
# difference array produced from grid
# traverse difference array with sliding window(vertical in terms of grid)
n, m, k = [int(x) for x in sys.stdin.readline().split()]
arr = [0 for x in range(n+2)]
presum = [0 for x in range(n+2)]
for q in range(m):
    a, b = [int(x) for x in sys.stdin.readline().split()]
    arr[a] -= 1
    arr[b+1] += 1

for i in range(1, n+1):
    arr[i] += arr[i-1]

for i in range(1, n+1):
    arr[i] += m
    presum[i] += presum[i-1] + arr[i]

lower = 0
upper = 1
curr = 0
final = float("inf")

while upper <= n:
    if lower <= upper and presum[upper]-presum[lower] >= k:
        final = min(final, upper-lower)
        lower += 1
    else:
        upper += 1


if final != float("inf"):
    print(final)
else:
    print(-1)
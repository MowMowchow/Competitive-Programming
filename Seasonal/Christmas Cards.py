import sys

n = int(sys.stdin.readline())
dp = [float("inf") for x in range(5100)]
dp[0] = 0

for i in range(n):
    c, d = [int(x) for x in sys.stdin.readline().split()]
    for j in range(n-1, i-1, -1):
        ind = min(j+d, n-1)
        dp[ind] = min(dp[ind], dp[j] + c)

print(dp[n-1])
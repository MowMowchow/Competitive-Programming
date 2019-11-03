import sys
n = int(sys.stdin.readline())
stones = [0] + [int(x) for x in sys.stdin.readline().split()]


dp = [float("inf")]*(n+1)
dp[1] = 0
for i in range(1, n+1):
    for j in range(i+1, i+3):
        if j <= n:
            dp[j] = min(dp[i] + abs(stones[i]-stones[j]), dp[j])


print(dp[n])
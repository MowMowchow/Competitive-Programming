import sys
n = int(sys.stdin.readline())
dp = [1 for x in range(n+1)]

for i in range(1, n):
    q = int(sys.stdin.readline())
    dp[q] *= dp[i] + 1

print(dp[n])
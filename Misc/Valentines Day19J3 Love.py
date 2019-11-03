import sys

m = sys.stdin.readline()
n = "love"

dp = [[0 for x in range(len(n)+1)] for x in range(len(m)+1)]

for i in range(len(m)+1):
    dp[i][0] = 1


for i in range(1, len(m)+1):
    for j in range(1, len(n)+1):
        if m[i-1] == n[j-1]:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

        else:
            dp[i][j] = dp[i-1][j]

print(dp[len(m)][len(n)])
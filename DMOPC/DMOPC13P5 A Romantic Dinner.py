import sys
m, u, r = [int(x) for x in sys.stdin.readline().split()]
dp = [[0 for x in range(u+1)] for y in range(m+1)]

for q in range(r):
    v, t, f = [int(x) for x in sys.stdin.readline().split()]
    for i in range(m, t-1, -1):  # time
        for j in range(u, f-1, -1):  # food-cap
            dp[i][j] = max(dp[i][j], dp[i-t][j-f] + v)

print(dp[m][u])
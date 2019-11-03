import sys
n, t = [int(x) for x in sys.stdin.readline().split()]
contests = [[int(x) for x in sys.stdin.readline().split()] for q in range(n)]
dp = [0 for x in range(t+1)]

for i in range(n+1):
    for j in range(t, 0, -1):
        if i != 0 and j != 0:
            poor, average, good = 0, 0, 0
            if contests[i-1][0] <= j:  # poor
                poor = contests[i-1][1] + dp[j-contests[i-1][0]]

            if contests[i-1][2] <= j:  # average
                average = contests[i-1][3] + dp[j-contests[i-1][2]]

            if contests[i-1][4] <= j:  # good
                good = contests[i-1][5] + dp[j-contests[i-1][4]]

            dp[j] = max(poor, average, good, dp[j])


print(dp[t])
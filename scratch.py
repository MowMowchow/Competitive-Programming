N = 4
TW = 6
dp = [[0 for x in range(TW+1)] for y in range(N+1)]
items = [ # weight, value
    [0, 0],
    [5, 7],
    [1, 2],
    [3, 1],
    [6, 4]
]


'''def do(ci, cw, cv):
    if dp[ci][cw] == -1:
        if cw < 0:
            return 0
        elif ci == N or cw == 0:
            return cv
        else:
            case1 = do(ci+1, cw-items[ci][0], cv+items[ci][1])
            case2 = do(ci+1, cw, cv)
            result = max(case1, case2)
            dp[ci][cw] = result

    else:
        print("ALREADY BEEN TO STATE")
    return dp[ci][cw]
'''

# state: d[i][j] = max value for i items and weight j

for i in range(1, N+1):
    for j in range(0, TW+1):
        if j >= items[i][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-items[i][0]] + items[i][1])
        else:
            dp[i][j] = dp[i-1][j]

for i in dp:
    print(i)
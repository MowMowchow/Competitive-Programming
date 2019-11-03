

def do():
    grid = [sys.stdin.readline().strip("\n") for x in range(8)]
    sys.stdin.readline().strip("\n")
    dp = [[0 for x in range(8)] for y in range(8)]
    if grid[7][0] != ".":
        dp[7][0] = int(grid[7][0])

    for i in range(7, -1, -1):
        for j in range(8):
            if i != 7 and j != 0:
                if grid[i][j] != "#":
                    dp[i][j] += max(dp[i+1][j], dp[i][j-1])
                    if grid[i][j] != ".":
                        dp[i][j] += int(grid[i][j])
            elif i == 7 and j != 0:  # bottom row
                if grid[i][j] != "#":
                    if grid[i][j] != ".":
                        dp[i][j] += int(grid[i][j]) + dp[i][j-1]
                    else:
                        dp[i][j] += dp[i][j-1]
            elif i != 7 and j == 0:  # first column
                if grid[i][j] != "#":
                    if grid[i][j] != ".":
                        dp[i][j] += int(grid[i][j]) + dp[i+1][j]
                    else:
                        dp[i][j] += dp[i+1][j]

    return dp[0][7]


for q in range(5):
    print(do())
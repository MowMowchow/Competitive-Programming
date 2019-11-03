import sys
n = int(sys.stdin.readline())
geesewl = sys.stdin.readline()
geesepts = [int(x) for x in sys.stdin.readline().split()]
hawkswl = sys.stdin.readline()
hawkspts = [int(x) for x in sys.stdin.readline().split()]
dp = [[0 for x in range(n+1)] for y in range(n+1)]


def compare(i, j):
    # geesecurr, hawkscurr = geesepts[i], hawkspts[j]

    if geesepts[i-1] < hawkspts[j-1]:
        if geesewl[i-1] == "L" and hawkswl[j-1] == "W":
            return geesepts[i-1] + hawkspts[j-1]

    elif geesepts[i-1] > hawkspts[j-1]:
        if geesewl[i-1] == "W" and hawkswl[j-1] == "L":
            return geesepts[i-1] + hawkspts[j-1]

    return 0


for i in range(1, n+1):
    for j in range(1, n+1):
        curr = max(dp[i][j-1], dp[i-1][j-1] + compare(i, j))
        dp[i][j] = max(dp[i-1][j], curr)

print(dp[n][n])
# problem 2
import sys
n, m = [int(x) for x in sys.stdin.readline().split()]
grid = [[float("inf") for x in range(m+1)]]+[[float("inf")]+[int(x) for x in sys.stdin.readline().split()] for x in range(n)]
grid[0][1], grid[1][0] = 0, 0

for i in range(1, n+1):
    for j in range(1, m+1):
        grid[i][j] += min(grid[i-1][j], grid[i][j-1])

print(grid[n][m])
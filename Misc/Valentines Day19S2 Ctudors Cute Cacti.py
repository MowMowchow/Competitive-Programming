import sys
n, q = [int(x) for x in sys.stdin.readline().split()]
grid = [[True for x in range(n+1)] for x in range(n+1)]

for i in range(q):
    type, x, y = [int(x) for x in sys.stdin.readline().split()]

    if type == 1:
        for i in range(1, n+1):
            grid[i][x] = not grid[i][x]

        # grid[y] = [not grid[z][y] for z in range(1, n+1)]
        for i in range(1, n+1):
            grid[y][i] = not grid[y][i]

        grid[y][x] = not grid[y][x]

    elif type == 2:
        if grid[y][x]:
            print(0)
        elif not grid[y][x]:
            print(1)
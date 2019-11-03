import sys
instruc = sys.stdin.readline()
grid = [1, 2,
        3, 4]

for q in instruc:
    if q == "H":
        new = list(grid)
        new[0] = grid[2]
        new[1] = grid[3]
        new[2] = grid[0]
        new[3] = grid[1]
        grid = list(new)

    if q == "V":
        new = list(grid)
        new[0] = grid[1]
        new[1] = grid[0]
        new[2] = grid[3]
        new[3] = grid[2]
        grid = list(new)

print(grid[0], grid[1], "\n"+str(grid[2]), grid[3])

import sys
sys.setrecursionlimit(100000)
# for each row in the grid + column, if it hasn't been visited and it
# isn't a wall, dfs it. Then come up with the size of the rooms and calculate
# accordingly

n = int(sys.stdin.readline())
r = int(sys.stdin.readline())
c = int(sys.stdin.readline())
grid = [sys.stdin.readline().strip("\n") for x in range(r)]
visited = [[False for x in range(c)] for y in range(r)]
moves = [[0, 1], [0, -1], [-1, 0], [1, 0]]  # U D L R


def dfs(x, y, count):
    global result
    visited[y][x] = True
    result += 1
    # make a global variable and += 1
    for move in moves:
        if 0 <= x+move[0] < c and 0 <= y+move[1] < r:
            if not visited[y+move[1]][x+move[0]] and grid[y+move[1]][x+move[0]] != "I":
                dfs(x+move[0], y+move[1], count+1)

    return


rooms = []
for row in range(r):
    for slot in range(c):
        if grid[row][slot] != "I" and not visited[row][slot]:
            result = 0
            dfs(slot, row, 0)
            rooms.append(result)

rooms.sort()
total = 0
for room in reversed(rooms):
    if n-room >= 0:
        n -= room
        total += 1
    else:
        break

if total != 1:
    print(total, "rooms,", n, "square metre(s) left over")
else:
    print(total, "room,", n, "square metre(s) left over")
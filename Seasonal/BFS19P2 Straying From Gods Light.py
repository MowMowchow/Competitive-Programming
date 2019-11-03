# problem 2
import sys
n = int(sys.stdin.readline())
grid = [sys.stdin.readline().strip("\n") for x in range(n)]
visited = [[float("inf") for x in range(n)] for y in range(n)]
moves = [[0, 1], [-1, 0], [1, 0]]  #D, L, R
visited[0][0] = 0
queue = [[0, 0, 0, 0, 0]] # x, y, d, l, r
while queue:
    cx, cy, d, l, r = queue.pop(0)

    for mx, my in moves:
        if 0 <= cx+mx < n and 0 <= cy+my < n:
            nx, ny, nd, nl, nr = int(cx+mx), int(cy+my), int(d), int(l), int(r)
            if mx == 1: # right
                nr += 1
            elif mx == -1:
                nl += 1
            if my == 1:
                nd += 1


            if grid[ny][nx] != "#" and visited[ny][nx] > ((nd*nd)+(nl*nl)+(nr*nr)):
                visited[ny][nx] = int((nd*nd)+(nl*nl)+(nr*nr))
                new = list([nx, ny, nd, nl, nr])
                queue.append(new)

if visited[n-1][n-1] == float("inf"):
    print(-1)
else:
    print(visited[n-1][n-1])
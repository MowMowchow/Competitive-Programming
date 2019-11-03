import sys
# double for loop i, j going through every spot
#   within second loop have a while loop checking for any cycles
#   ^ done by simulating the path taken from the current spot
#       if curr spot == count:  (is a cycle)
#           total++
#           break
#       also -> if curr spot != initial array val:
#           break  (because then it just become part of something pre-computed
#       after visiting a spot, set it equal to count (showing that it's part of the curr path)
n, m = [int(x) for x in sys.stdin.readline().split()]
grid = [sys.stdin.readline().strip("\n") for x in range(n)]
visited = [[-1 for x in range(m)] for y in range(n)]
count, final = 1, 0

for i in range(n):
    for j in range(m):
        if visited[i][j] == -1:
            x, y = int(j), int(i)

            while True:
                if visited[y][x] == count:
                    final += 1
                    break

                if visited[y][x] != -1:
                    break

                visited[y][x] = count

                if grid[y][x] == "N":
                    y -= 1
                elif grid[y][x] == "S":
                    y += 1
                elif grid[y][x] == "E":
                    x += 1
                elif grid[y][x] == "W":
                    x -= 1

            count += 1

print(final)
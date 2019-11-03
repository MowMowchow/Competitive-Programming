import sys
import math
n = int(sys.stdin.readline())
grid = [[int(x) for x in sys.stdin.readline().split()] for x in range(n)]

counter = 1
sublength = 0
for row in grid:
    for curr in range(n-1):
        if row[curr] != row[curr+1] - 1:
            sublength += 1
            break

            #counter += 1

print(sublength)
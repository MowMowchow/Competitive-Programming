# problem 0
import sys
n, hmin, hmax = [int(x) for x in sys.stdin.readline().split()]
heights = [int(x) for x in sys.stdin.readline().split()]
counter = 0
for i in range(n):
    if hmin <= heights[i] <= hmax:
        counter += 1

print(counter)
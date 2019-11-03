# problem 3
import sys
n = int(sys.stdin.readline().strip("\n"))
m = int(sys.stdin.readline().strip("\n"))
# find the max amt of beakers to solve with k many cups for each t second(s)
# > for each second, k many cups will solve 2^k beakers

for k in range(0, n+1):
    if ((2**k)**m) >= n:
        print(k)
        break
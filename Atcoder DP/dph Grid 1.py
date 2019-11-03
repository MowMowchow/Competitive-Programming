import sys
sys.setrecursionlimit(1000000)
h, w = [int(x) for x in sys.stdin.readline().split()]
grid = [sys.stdin.readline().strip("\n") for x in range(h)]
num = [[0 for z in range(w)] for x in range(h)]
num[0][0] = 1
mod = 1000000007

for i in range(w):
    for j in range(h):
        if grid[j][i] != "#":
            num[j][i] += num[j-1][i] + num[j][i-1]

#for i in num:
#    print(i)
print(num[h-1][w-1]%mod)
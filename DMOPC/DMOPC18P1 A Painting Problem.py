import sys
n, m, k = [int(x) for x in sys.stdin.readline().split()]
blue = 0
purple = 0

for i in range(1, k+1):
    N = "00000000000000000000"+bin(n)
    M = "00000000000000000000"+bin(m)
    if (N[-i] == "1" and  M[-i] == "1") or (N[-i] != "1" and  M[-i] != "1"):
         purple += 1
    else:
        blue += 1

print(blue, purple)
import sys
# prefix sum of the integrity
seq = sys.stdin.readline().strip("\n")
prefix = [0 for x in range(len(seq)+1)]
n = int(sys.stdin.readline())

for i in range(1, len(seq)+1):
    if seq[i-1] == "G":
        prefix[i] += prefix[i-1] + 1
    else:
        prefix[i] += prefix[i-1]


for q in range(n):
    l, r = [int(x) for x in sys.stdin.readline().split()]

    if prefix[r+1] - prefix[l] > 0:
        print(prefix[r+1] - prefix[l])

    else:
        print(0
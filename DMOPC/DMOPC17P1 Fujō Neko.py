import sys
r, c = [int(x) for x in sys.stdin.readline().split()]
column = [False for x in range(r)]  # vertical
row = [False for x in range(c)]  # horizontal
for i in range(r):
    curr = sys.stdin.readline()
    for j in range(c):
        if curr[j] == "X":
            column[i], row[j] = True, True

q = int(sys.stdin.readline())

for qq in range(q):
    x, y = [int(x) for x in sys.stdin.readline().split()]
    if row[x-1] or column[y-1]:
        print("Y")
    else:
        print("N")
import sys
w, h, maxarea = [int(x) for x in sys.stdin.readline().split()]
battlefield = [[0 for x in range(w+1)]] + [[0]+[int(x) for x in sys.stdin.readline().split()] for x in range(h)]
# prefix = [[0 for x in range(w+1)] for x in range(h+1)]
highest = -1

for i in range(h+1):
    for j in range(w+1):
        if i > 0:
            battlefield[i][j] += battlefield[i-1][j]
        if j > 0:
            battlefield[i][j] += battlefield[i][j-1]
        if j > 0 and i > 0:
            battlefield[i][j] -= battlefield[i-1][j-1]


for i in range(h):  # i = h
    for j in range(w):  # j = w
        m = 1
        while m <= maxarea and i+m-1 < h:
            l = min((maxarea//m)+j, w)  # new rect length
            k = i+m  # new rect height
            curr = battlefield[k][l]
            if i > 0:
                curr -= battlefield[i][l]
            if j > 0:
                curr -= battlefield[k][j]
            if i > 0 and j > 0:
                curr += battlefield[i][j]

            highest = max(highest, curr)
            m += 1

print(highest)
# problem 2
import sys
x, y, h, v = [int(x) for x in sys.stdin.readline().split()]
t = int(sys.stdin.readline())
moves = [[1, 2], [2, 1]]  #2u 1r, 1u, 2r
done = False

for i in range(1, t):
    cx = moves[0][0]*i
    cy = moves[0][1]*i
    if cx >= x+h or cy >= y+v:
        continue
        # break
    else:
        movesleft = max(y-cy, (x-cx)//2)
        if movesleft+i < t:
            done = True
            break

if not done:
    print("NO")
else:
    print("YES")
import sys
def do(xx, yy):
    if xx == 1 or xx == 10:
        thing[yy] += 1


low = [float("inf"), 0]


def do2(useless, yy):
    global low
    if low[0] > thing[yy]:
        low[0] = thing[yy]
        low[1] = yy + 1


n, m = [int(x) for x in sys.stdin.readline().split()]
thing = [0 for x in range(n)]
orphanages = [do2([do(int(x), y) for x in sys.stdin.readline().split()], y)for y in range(n)]


print(low[1])
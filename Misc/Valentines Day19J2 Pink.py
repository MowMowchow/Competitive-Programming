import sys
n = int(sys.stdin.readline())

def determine(r, g, b):
    if 240 <= r <= 255 and 0 <= g <= 200 and 95 <= b <= 220:
        return True

    else:
        return False


coutner = 0
for i in range(n):
    r, g, b = [int(x) for x in sys.stdin.readline().split()]
    if determine(r, g, b):
        coutner += 1

print(coutner)
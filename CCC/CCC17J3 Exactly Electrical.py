import sys
a, b = [int(x) for x in sys.stdin.readline().split()]
x, y = [int(x) for x in sys.stdin.readline().split()]
c = int(sys.stdin.readline())


if (abs(a-x) + abs(b-y)) > c or (c-(abs(a-x) + abs(b-y))) % 2:
    print("N")
else:
    print("Y")
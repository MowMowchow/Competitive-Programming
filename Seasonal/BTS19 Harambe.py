# problem 1
import sys
n = int(sys.stdin.readline())
words = [[x]+[len(x)] for x in sys.stdin.readline().strip("\n").split()]
toreplace = sys.stdin.readline().strip("\n")
replen = len(toreplace)

final = [float("inf"), ""]

for word, templen in words:
    if templen <= replen:
        if abs(replen-final[0]) > abs(replen-templen):
            final[0] = templen
            final[1] = word

print(final[1])
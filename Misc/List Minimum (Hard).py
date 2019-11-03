import sys
eh = []
n = int(sys.stdin.readline())
for i in range(n):
    eh.append(int(sys.stdin.readline()))

eh.sort()

for i in eh:
    print(i)
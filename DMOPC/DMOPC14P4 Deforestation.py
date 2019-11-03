import sys
input = sys.stdin.readline

A = int(input())
masses = []
for i in range(A):
    a = int(input())
    masses.append(a)

Q = int(input())
prefix = [0 for x in range(A+1)]

for g in range(1, len(masses)+1):
    prefix[g] = masses[g - 1] + prefix[g - 1]

for f in range(Q):
    a,b = [int(x) for x in input().split()]
    a = int(a)
    b = int(b)
    print(prefix[b+1]-prefix[a])
import sys
n = int(sys.stdin.readline())
seq1 = [int(x) for x in sys.stdin.readline().split()]
seq2 = [int(x) for x in sys.stdin.readline().split()]
onetotal = 0
twototal = 0

last = 0

for i in range(n):
    onetotal += seq1[i]
    twototal += seq2[i]
    if onetotal == twototal:
        last = i+1

print(last)
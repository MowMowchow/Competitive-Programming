import sys

seq = [int(x) for x in sys.stdin.readline().split("x")]
seq.sort()
newstr = ""
total = 1
for i in range(len(seq)):
    newstr += str(seq[i])
    if i+1 < len(seq):
        newstr += "x"
    total *= seq[i]


print(newstr)
print(total)
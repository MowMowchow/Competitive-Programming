import sys
seq = sys.stdin.readline().strip("\n")
n = len(seq)
onepre = [0 for x in range(n+1)]
zeropre = [0 for x in range(n+1)]
oneindex = [-1 for x in range(n+1)]
zeroindex = [-1 for x in range(n+1)]

for i in range(1, n+1):
    if seq[i-1] == "1":
        onepre[i] += 1
    elif seq[i-1] == "0":
        zeropre[i] += 1

    onepre[i] += onepre[i-1]
    zeropre[i] += zeropre[i-1]

    if oneindex[onepre[i]] == -1:
        oneindex[onepre[i]] = i
    if zeroindex[zeropre[i]] == -1:
        zeroindex[zeropre[i]] = i


q = int(sys.stdin.readline().strip("\n"))
for i in range(q):
    x, y, z = [int(x) for x in sys.stdin.readline().split()]
    if z == 0:
        if zeropre[x-1]+y < n+1:
            if zeroindex[zeropre[x-1]+y] != -1:
                print(zeroindex[zeropre[x-1]+y])
            else:
                print(-1)
        else:
            print(-1)

    elif z == 1:
        if onepre[x-1]+y < n+1:
            if oneindex[onepre[x-1]+y] != -1:
                print(oneindex[onepre[x-1]+y])
            else:
                print(-1)
        else:
            print(-1)
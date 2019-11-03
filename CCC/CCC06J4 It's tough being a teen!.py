import sys
adj = [[] for x in range(8)]
ind = [0 for x in range(8)]

while True:
    x = int(sys.stdin.readline())
    y = int(sys.stdin.readline())

    if x == 0 and y == 0:
        break

    else:
        adj[x].append(y)
        ind[y] += 1

adj[1].append(7)
ind[7] += 1
adj[1].append(4)
ind[4] += 1
adj[2].append(1)
ind[1] += 1
adj[3].append(4)
ind[4] += 1
adj[3].append(5)
ind[5] += 1

order = []
done = False
while True:
    for i in range(1, 8):
        if ind[i] == 0:
            ind[i] -= 1

            for node in adj[i]:
                ind[node] -= 1

            order.append(str(i))
            break

    else:
        break


if len(order) == 7:
    print(' '.join(str(e) for e in order))
else:
    print("Cannot complete these tasks. Going to bed.")

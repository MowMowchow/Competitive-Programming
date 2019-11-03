n, m = [int(x) for x in sys.stdin.readline().split()]
rivers = [[] for x in range(n+1)]

for q in range(m):
    query = [int(x) for x in sys.stdin.readline().split()]
    rivers[query[0]].append(query[1])

lakes = [0]*(n+1)
lakes[1] = 1
for lake in range(1, n+1):
    if rivers[lake]:
        probability = float(lakes[lake])/len(rivers[lake])
        for i in rivers[lake]:
            lakes[i] += probability


#print(lakes)
for i in range(1, n+1):
    if not rivers[i]:
        print(lakes[i])
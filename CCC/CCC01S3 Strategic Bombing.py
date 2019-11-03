import sys
edges = []

while True:
    temp = sys.stdin.readline().strip("\n")
    if temp != "**":
        edges.append([ord(temp[0])-ord("A"), ord(temp[1])-ord("A")])
    else:
        break


def find(subsets, node):
    if node != subsets[node][0]:
        subsets[node][0] = find(subsets, subsets[node][0])
    return subsets[node][0]


def union(subsets, u, v):
    if subsets[u][1] > subsets[v][1]:
        subsets[v][0] = u
    elif subsets[u][1] < subsets[v][1]:
        subsets[u][0] = v
    else:
        subsets[v][0] = u
        subsets[u][1] += 1


total = 0
nonoroads = []
for excluded in edges:
    subsets = [[x, 0] for x in range(26)]
    for node in edges:
        if node != excluded:
            x, y = find(subsets, node[0]), find(subsets, node[1])
            union(subsets, x, y)

    if find(subsets, 0) != find(subsets, 1):
        total += 1
        nonoroads.append([chr(excluded[0]+ord("A")), chr(excluded[1]+ord("A"))])


for road in nonoroads:
    print(str(road[0])+str(road[1]))
print("There are", total, "disconnecting roads.")
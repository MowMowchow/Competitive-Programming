import sys
sys.setrecursionlimit(10000000)
n, q = [int(x) for x in sys.stdin.readline().strip("\n").split()]

# index number is also the node
subsets = [[x, 0] for x in range(n+1)]  # parent, rank


def find(subsets, node):
    # Due to indexing, the parent will have itself as the parent
    #  make sure not to misinterpret as a cycle
    if subsets[node][0] != node:
        # path compression (directly connecting node to parent)
        subsets[node][0] = find(subsets, subsets[node][0])
    return subsets[node][0]


def union(subsets, u, v):
    x = find(subsets, u)
    y = find(subsets, v)
    subsets[x][0] = y


for i in range(q):
    query, u, v = sys.stdin.readline().split()

    if query == "A":
        union(subsets, int(u), int(v))

    elif query == "Q":
        if find(subsets, int(u)) == find(subsets, int(v)):
            print("Y")
        else:
            print("N")
import sys
sys.setrecursionlimit(10000000)
# dfs through directed graph made by recipes
# once you get to lowest recipe (no adjacent), sum how many items take to make
# that item (account for how many there are of the base items)
# don't forget to check if item one is given
n, m = [int(x) for x in sys.stdin.readline().split()]
adj = [[] for x in range(n+1)]
required = [0 for x in range(n+1)]
for q in range(m):
    temp = [int(x) for x in sys.stdin.readline().split()]
    adj[temp[0]] += temp[2:]
    required[temp[0]] = temp[1]
items = [0]+[int(x) for x in sys.stdin.readline().split()]


def dfs(curr, prev):
    uh = float("inf")

    if adj[curr]:
        for node in adj[curr]:
            # do something with returning none
            if node != prev:
                uh = min(uh, dfs(node, curr))

        return items[curr] + uh

    else:
        return items[curr]


result = dfs(1, 0)
if result:
    print(result)
else:
    print(0)
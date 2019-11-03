import sys
n, m, a, b = sys.stdin.readline().split()
n,m,a,b = int(n),int(m), int(a), int(b)

adj = [[] for x in range(n+1)]

for i in range(m):
    x, y = [int(x) for x in sys.stdin.readline().split()]
    adj[x].append(y)
    adj[y].append(x)


queue = [a]
visited = [False for k in range(n+1)]
done = False

while queue:
    current = queue.pop(0)
    if not visited[current]:
        visited[current] = True
        for node in adj[current]:
            if node == b:
                done = True
            queue.append(node)

if done == True or a == b:
    print("GO SHAHIR!")
else:
    print("NO SHAHIR!")
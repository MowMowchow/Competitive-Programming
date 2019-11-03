import sys
v = int(sys.stdin.readline())
e = int(sys.stdin.readline())
adj = [[] for x in range(v+1)]
for i in range(e):
    x, y, dist, limit = [int(x) for x in sys.stdin.readline().split()]
    adj[x].append([y, (dist/limit)*60, (dist/(limit*.75))*60])  # node, reg, delay
    adj[y].append([x, (dist/limit)*60, (dist/(limit*.75))*60])
answers = [[float("inf"), 0, 0] for x in range(v+1)]  # time, delayed time, length
visited = [False for x in range(v+1)]

queue = [[1, 1]]  # curr, length, time, delayed time
answers[1][0] = 0

while queue:
    curr, length = queue.pop(0)
    visited[curr] = False

    for node in adj[curr]:
        if answers[node[0]][0] > answers[curr][0] + node[1]:
            answers[node[0]][0] = answers[curr][0] + node[1]
            answers[node[0]][1] = answers[curr][1] + node[2]
            answers[node[0]][2] = length
            if not visited[node[0]]:
                visited[node[0]] = True
                queue.append([node[0], length+1])

        elif answers[node[0]][0] == answers[curr][0] + node[1]:
            if length < answers[node[0]][1]:
                answers[node[0]][0] = answers[curr][0] + node[1]
                answers[node[0]][1] = answers[curr][1] + node[2]
                answers[node[0]][2] = length
                if not visited[node[0]]:
                    visited[node[0]] = True
                    queue.append([node[0], length + 1])


print(answers[v][2])
print(round(answers[v][1]-answers[v][0]))
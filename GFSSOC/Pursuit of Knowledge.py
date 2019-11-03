import sys
numberofrooms, numberofhallways, traversaltime = sys.stdin.readline().split()
numberofrooms = int(numberofrooms)
numberofhallways = int(numberofhallways)
traversaltime = int(traversaltime)
rooms = ["*"]+[[] for x in range(numberofrooms)] #adjacency list (directed)
for i in range(numberofhallways): #creates adjacency lsit
    query = sys.stdin.readline().split()
    rooms[int(query[0])].append(int(query[1]))
numberofqueries = int(sys.stdin.readline())
#visited array for rooms already reached
alreadyreached = ["*"]+[["*"]+[0 for x in range(numberofrooms)] for z in range(numberofrooms)]


def bfs(a):
    visited = []
    queue = [[a, 0]]

    while queue:
        path = queue.pop(0)


        if path[0] not in visited:
            visited.append(path[0])

            for node in rooms[path[0]]:
                newpath = list(path)
                newpath[0] = node
                newpath[1] += 1
                queue.append(newpath)

                if alreadyreached[a][newpath[0]] == 0:
                    alreadyreached[a][newpath[0]] = (newpath[1])*traversaltime


for room in range(1, len(rooms)):
    if rooms[room]:
        bfs(room)

for i in range(numberofqueries):
    query = sys.stdin.readline().split()

    if alreadyreached[int(query[0])][int(query[1])] != 0:
        print(alreadyreached[int(query[0])][int(query[1])])
    else:
        print("Not enough hallways!")
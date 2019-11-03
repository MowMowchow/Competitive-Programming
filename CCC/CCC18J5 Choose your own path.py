#just bfs to find shortest path and check if all a revisted
#to check if all are visited just len(visited)
#we are assuming that you can only access page 2 from page 1
import sys
numberofpages = int(sys.stdin.readline())
book = ["*"]+[[] for x in range(numberofpages+1)]
for i in range(1, numberofpages+1):
    query = sys.stdin.readline().split()
    query = [int(x) for x in query]
    #print(query)
    if query[0] != 0:
        book[i].extend(query[1:])
    else:
       book[i].append(0)


shortestpath = []
#below is just bfs
def pagetraversal(book, currentpage):
    queue = [[currentpage]]
    visited = []

    while queue:
        path = queue.pop(0)

        if path[-1] not in visited:
            visited.append(path[-1])
            for node in book[path[-1]]:
                newpath = list(path)
                newpath.append(node)
                queue.append(newpath)

                if node == 0:
                    shortestpath.append(len(newpath)-1)
                    queue.remove(newpath)

    if len(visited) == numberofpages:
        return True
    else:
        return False

if pagetraversal(book, 1):
    print("Y")
else:
    print("N")

#print(shortestpath)
print(min(shortestpath))

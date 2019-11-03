import sys
n = int(sys.stdin.readline())
countries = [[int(x) for x in sys.stdin.readline().split()] for c in range(n)]
source = int(sys.stdin.readline())-1

# maybe use multiplication instead of power
available = [float("inf")]*n
visited = [False]*n
available[source] = 0


def binsearch(arr, goal):
    first = 0
    last = len(arr)-1
    while last >= first:
        index = first+(last-first)//2

        if arr[index] <= goal:
            first = index + 1

        else:
            last = index-1

    return first


def dijkstra():
    counter = 0
    while True:
        curr = 0

        for city in range(n):
            if available[curr] > available[city] and not visited[city] or visited[curr] and not visited[city]:
                curr = city

        if visited[curr]:
            return

        #print(curr)
        visited[curr] = True

        counter += 1

        for city in range(n):
            available[city] = min(available[curr] + (abs(countries[curr][0]-countries[city][0])**2) + (abs(countries[curr][1]-countries[city][1])**2), available[city])

        #print("City:", curr, available)


dijkstra()
available.sort()
#print(available)

q = int(sys.stdin.readline())
for i in range(q):
    query = int(sys.stdin.readline())
    print(binsearch(available, query))
import sys
stuff = sys.stdin.readline().split()
numberofcities, numberofroads, numberofdestinationcities = int(stuff[0]), int(stuff[1]), int(stuff[2])
roads = ["*"]+[["*"] for x in range(numberofcities)]
weights = ["*"]+[["*"] for x in range(numberofcities)]
destinations = []
for i in range(numberofroads): #adjacency for weights and roads
    newroad = sys.stdin.readline().split()
    if int(newroad[1]) not in roads[int(newroad[0])]:
        roads[int(newroad[0])].append(int(newroad[1]))
        roads[int(newroad[1])].append(int(newroad[0]))
        weights[int(newroad[0])].append(int(newroad[2]))
        weights[int(newroad[1])].append(int(newroad[2]))

for i in range(numberofdestinationcities):
    destinations.append(int(sys.stdin.readline()))


def findpaths():
    visited = []
    potentialnodes = [0 for x in range(numberofcities+1)]
    queue = [x for x in roads[1]]

    while len(queue) > 1:
        #add all new possbile nodes to potential nodes
        currentcity = queue.pop(1)
        for city in range(1, len(roads[currentcity])):
            #if roads[currentcity][city] not in visited:
                #each potential city is assigned the highest weight to travel to that city
            if weights[currentcity][city] > potentialnodes[roads[currentcity][city]]:
                potentialnodes[roads[currentcity][city]] = weights[currentcity][city]
                queue.append(roads[currentcity][city])

        #marks the current city as visited
        #visited.append(currentcity)
        #print(potentialnodes[currentcity])

    return potentialnodes

mindist = 1000000
final = findpaths()
for city in destinations:
    if mindist > final[city]:
        mindist = final[city]
print(mindist)

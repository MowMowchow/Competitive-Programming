import sys
friends = [[] for x in range(51)]
friends[1].extend([6])
friends[2].extend([6])
friends[3].extend([4, 5, 6, 15])
friends[4].extend([3, 5, 6])
friends[5].extend([3, 4, 6])
friends[6].extend([1, 2, 3, 4, 5, 7])
friends[7].extend([6, 8])
friends[8].extend([7, 9])
friends[9].extend([8, 10, 12])
friends[10].extend([9, 11])
friends[11].extend([10, 12])
friends[12].extend([9, 11, 13])
friends[13].extend([12, 14, 15])
friends[14].extend([13])
friends[15].extend([3, 13])
friends[16].extend([17, 18])
friends[17].extend([16, 18])
friends[18].extend([16, 17])
done = False

def bfs(start, finish):
    visited = []
    queue = [[start]]

    while queue:
        path = queue.pop(0)

        if path[-1] not in visited:
            visited.append(path[-1])

            for node in friends[path[-1]]:
                newpath = list(path)
                newpath.append(node)
                queue.append(newpath)

                if finish in newpath:
                    return len(newpath)-1

    return "Not connected"


while not done:
    query = sys.stdin.readline().strip("\n")

    if query == "i":
        x = int(sys.stdin.readline())
        y = int(sys.stdin.readline())
        if x not in friends[y] and y not in friends[x]:
            friends[x].extend([y])
            friends[y].extend([x])

    elif query == "d":
        x = int(sys.stdin.readline())
        y = int(sys.stdin.readline())
        friends[x].remove(y)
        friends[y].remove(x)


    elif query == "n":
        x = int(sys.stdin.readline())
        print(len(friends[x]))

    elif query == "f": #something wrong
        x = int(sys.stdin.readline())
        total = []
        cannotcount = [x]
        cannotcount.append(x)
        for friend in friends[x]:
            cannotcount.append(friend)
            if friend in total:
                total.remove(friend)
            for person in friends[friend]:
                if person not in total and person not in cannotcount:
                    total.append(person)

        print(len(total)) #one less for the first test case

    elif query == "s":
        x = int(sys.stdin.readline())
        y = int(sys.stdin.readline())
        print(bfs(x, y))


    elif query == "q":
        done = True
        break
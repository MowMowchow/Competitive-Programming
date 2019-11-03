import sys
cases = int(sys.stdin.readline())

for case in range(cases):
    connections = []
    numberofconnections = int(sys.stdin.readline())
    for connection in range(numberofconnections):
        connections.append(sys.stdin.readline())
    connections = connections[::-1]
    depth = []
    currentdepth = 0
    maxdepth = 0

    for person in connections:

        if person == connections[0]:
            depth = []
            pass

        elif person in depth:
            del depth[depth.index(person)+1:]

        else:
            depth.append(person)

        currentdepth = len(depth)
        if maxdepth < currentdepth:
            maxdepth = currentdepth


    print((len(connections)*10) - (2*maxdepth*10))
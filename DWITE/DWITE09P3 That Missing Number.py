import sys
for q in range(5):
    m = int(sys.stdin.readline().strip("\n"))
    curr = [int(sys.stdin.readline()) for x in range(m)]
    counter = 1
    currcount = 0
    while counter <= max(curr)+2:
        if currcount >= len(curr):
            print(counter)
            break
        if counter != curr[currcount]:
            print(counter)
            break
        else:
            counter += 1
            currcount += 1
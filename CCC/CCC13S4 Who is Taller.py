import sys
#data manipulation
numberofstudents, numberofconnections = sys.stdin.readline().split()
numberofstudents, numberofconnections = int(numberofstudents), int(numberofconnections)
comparisons1 = [[] for x in range(numberofstudents+1)] #index number is greater than the value stored
visited = [False for x in range(numberofstudents+1)] #kinda a little bit of dp
for i in range(numberofconnections):
    pair = sys.stdin.readline().split()
    comparisons1[int(pair[0])].append(int(pair[1]))
finalpair = sys.stdin.readline().split()
finalpair = [int(finalpair[0]), int(finalpair[1])]


def search(comparisons, currentpoint, finalheight, count, possible, visited):
    #print("checking if student", currentpoint, "is taller than", comparisons[currentpoint])


    if currentpoint == finalheight:
        possible = True
        visited[currentpoint] = True
        #print("yuss")
        return possible

    elif visited[currentpoint]: #this is wrong
        return

    elif count >= numberofstudents:
        possible = False
        #print("thinkg")
        return possible

    else:
        for i in comparisons[currentpoint]:
            #print("next loop")
            possible = search(comparisons, i, finalheight, count+1, possible, visited)
            if possible:
                break

    #print(currentpoint)
    visited[currentpoint] = True #tis is wrong
    return possible


if search(comparisons1, finalpair[0], finalpair[1], 0, False, visited):
    print("yes")
elif search(comparisons1, finalpair[1], finalpair[0], 0, False, visited):
    print("no")
else:
    print("unknown")
#start at first location, recurse all reachable motels (DFS) for that point
#if you reach the end then save how many possibilites there are from that city

import sys
minimumtravellingdistance = int(sys.stdin.readline())
maximumtravellingdistance = int(sys.stdin.readline())
motels = [0, 0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]
numberofmotelsadded = int(sys.stdin.readline())
for i in range(numberofmotelsadded):
    motels.append(int(sys.stdin.readline()))
motels.sort()
dp = [0]*7001

#not that current location is defined by index, not motel value (used for post-difference array)
def dfs(minimumtravellingdistance, maximumtravellingdistance, currentlocation, count):
    if motels[currentlocation] == 7000:
        #print("Found!")
        return 1

    elif dp[currentlocation] != 0:
        return dp[currentlocation]

    for i in range(currentlocation+1, len(motels)):
        if maximumtravellingdistance >= motels[i] - motels[currentlocation] >= minimumtravellingdistance:
            count = dfs(minimumtravellingdistance, maximumtravellingdistance, i, count)
            dp[currentlocation] += count

    return dp[currentlocation]

print(dfs(minimumtravellingdistance, maximumtravellingdistance, 1, 0))
import sys
numberofcages, minutesstaying = [int(x) for x in sys.stdin.readline().split()]
princesses = []
songs = []
dp = [[0 for x in range(minutesstaying+1)] for x in range(numberofcages+1)]
for i in range(numberofcages):
    query = [int(x) for x in sys.stdin.readline().split()]
    princesses.append(query[0])
    songs.append(query[1])


#first for loop is number of cages
#second for loop is number of possible weights
def playsong():
    for cage in range(len(princesses)+1):
        for weight in range(minutesstaying+1):
            if cage == 0 or weight == 0:
                dp[cage][weight] = 0

            elif songs[cage-1] <= weight: #this song weight is valid
                dp[cage][weight] = max(princesses[cage-1] + dp[cage-1][weight-songs[cage-1]], dp[cage-1][weight])

            else:
                dp[cage][weight] = dp[cage-1][weight]

    return dp[numberofcages][minutesstaying]

print(playsong())
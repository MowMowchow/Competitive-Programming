import sys
#manipulating data to make it more manageable
numberofepisodes, numberofqueries = map(int, sys.stdin.readline().split())
episoderatings = sys.stdin.readline().split()
episoderatings = [0]+[int(x) for x in episoderatings]


for i in range(1, numberofepisodes+1):
    episoderatings[i] += episoderatings[i-1]

for i in range(numberofqueries):
    query = sys.stdin.readline().split()
    print(episoderatings[-1] - episoderatings[int(query[1])] + episoderatings[int(query[0])-1])
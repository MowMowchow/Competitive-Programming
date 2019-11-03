import sys
#THANK YOU (ALMOST) BIT PROBLEMS FOR GIVING ME THIS IDEA
n, v = [int(x) for x in sys.stdin.readline().split()]
coins = [int(x) for x in sys.stdin.readline().split()]
queries = []  # query num, cost, first 'l' types
dp = [float("inf") for x in range(10001)]
answers = [0 for x in range(v)]
dp[0] = 0

for q in range(v):
    queries.append([q]+[int(x) for x in sys.stdin.readline().split()])

queries.sort(key=lambda x: x[2])


counter = 0
for i in range(1, n+1):
    for j in range(coins[i-1], 10001):
        dp[j] = min(dp[j], dp[j-coins[i-1]]+1)  # skip vs use

    if counter < v:
        while queries[counter][2] == i:
            qnum, cost, type = queries[counter]
            answers[qnum] = dp[cost]
            counter += 1

            if counter == v:
                break


for i in answers:
    if i != float("inf"):
        print(i)
    else:
        print(-1)
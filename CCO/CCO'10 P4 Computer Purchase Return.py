import sys
t = int(sys.stdin.readline())
n = int(sys.stdin.readline())
parts = [[] for x in range(t)]
for i in range(n):
    q = [int(x) for x in sys.stdin.readline().split()]
    parts[q[2]-1].append([q[0], q[1]])  # cost and value appended to item type
b = int(sys.stdin.readline())
dp = [0 for x in range(b+1)]  # gotta keep track of items kept using an arr, first val s value
counter = 0

for type in range(t):
    flag = False
    for j in range(b, -1, -1):
        for i in range(len(parts[type])):
            if parts[type][i][0] <= j:
                dp[j] = max(dp[j], parts[type][i][1] + dp[j-parts[type][i][0]])
                flag = True

    if flag:
        counter += 1


if counter == t:
    print(dp[b])
else:
    print(-1)
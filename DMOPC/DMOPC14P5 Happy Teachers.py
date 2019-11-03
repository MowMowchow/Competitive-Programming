import sys
n = int(sys.stdin.readline())
teachers = [[int(x) for x in sys.stdin.readline().split()] for x in range(n)]
s = int(sys.stdin.readline())
dp = [[0, 0] for x in range(s+1)]  # val, time

for n in range(1, n + 1):
    h, e, p = teachers[n-1]
    for rawtime in range(s, p-1, -1):
        time = 0
        for i in range(1, (rawtime//p)+1):  # max number of times you can use teacher in curr time
            time += h - e*(i-1)
            if time > 0 and rawtime >= (p*i):
                if time + dp[(rawtime-(p*i))][0] > dp[rawtime][0]:  # val is higher
                        dp[rawtime][0] = time + dp[(rawtime-(p*i))][0]
                        dp[rawtime][1] = i + dp[(rawtime - (p*i))][1]

                elif time + dp[(rawtime-(p*i))][0] == dp[rawtime][0]:  # same val, choose lower time
                    dp[rawtime][1] = min(dp[rawtime][1], i + dp[(rawtime-(p*i))][1])

print(dp[s][0])
print(dp[s][1])
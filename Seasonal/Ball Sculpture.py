import sys
n, balls = [int(x) for x in sys.stdin.readline().split()]
dp = [0]*(n+2)
dp[1] = balls


for i in range(1, n+1):
    switches = [int(x) for x in sys.stdin.readline().split()]
    dp[switches[0]] += (dp[i]+1)//2
    dp[switches[1]] += dp[i]//2

    if dp[i] % 2 == 1:
        dp[i] = 1
    else:
        dp[i] = 0

print(''.join(str(x) for x in dp[1:n+1]))
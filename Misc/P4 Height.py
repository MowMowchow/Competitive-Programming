import sys
n = int(sys.stdin.readline())
seq = [int(sys.stdin.readline()) for x in range(n)]
dp = [x for x in seq]


for i in range(1, n):
    for j in range(i):
        if seq[j] < seq[i] and seq[i] + dp[j] > dp[i]:
            dp[i] = seq[i] + dp[j]

print(max(dp))
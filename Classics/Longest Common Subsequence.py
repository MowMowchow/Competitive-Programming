sys.setrecursionlimit(1000000)
n, m = [int(x) for x in sys.stdin.readline().split()]
seq1 = [int(x) for x in sys.stdin.readline().split()]
seq2 = [int(x) for x in sys.stdin.readline().split()]
#dp = [[-1]*(m+1) for x in range(n+1)]
dp = [[0]*(m+1) for x in range(n+1)]

"""
def f(i, j):
    if i == n or j == m:
        return 0

    if dp[i][j] == -1:
        if seq1[i] == seq2[j]:
            dp[i][j] = f(i+1, j+1) + 1

        else:
            dp[i][j] = max(f(i+1, j), f(i, j+1))

    return dp[i][j]


print(f(0, 0))
"""

for i in range(n+1):
    for j in range(m+1):
        if i == n or j == m:
            dp[i][j] = 0

        elif seq1[i] == seq2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
            # Adding 1 to the longest subsequence made up of sequences length
            # i-1 and j-1.

        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            # choosing between the longest subsequence with n length i-1 and
            # m length j or n length i and m length j-1

print(dp[n-1][m-1])
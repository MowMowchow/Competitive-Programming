import sys


def bowl():
    for i in range(1, numberofballs+1):
        for p in range(numberofpins):
            curr = bowlsum[p]
            if p >= width:
                curr += dp[i-1][p-width]
            dp[i][p] = max(dp[i][p-1], curr)    # choosing between whether last
                                                # throw was most optimal or this one

    return dp[numberofballs][numberofpins-1]


testcases = int(sys.stdin.readline())
for case in range(testcases):

    numberofpins, numberofballs, width = [int(x) for x in sys.stdin.readline().split()]
    pins = [0]*numberofpins
    bowlsum = [0]*numberofpins
    dp = [[0]*numberofpins for x in range(numberofballs+1)]
    for i in range(numberofpins):
        pins[i] = int(sys.stdin.readline())
        for l in range(width):  # prefix sum array
            if l > i:
                break
            else:
                bowlsum[i] += pins[i-l]

    print(bowl())
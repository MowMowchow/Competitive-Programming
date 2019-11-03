import sys

# prefix sums for cuteness and width
# dp holds maxes before the current addition
# when adding a new girl, do arr[curr] = arr[curr-1] + new
# sliding window with prefixes with curr as the upper bound
# dp[curr] = max(dp[curr-1], result of sliding window)
# answer is dp[curr]
# ++ curr at the end of adding (to prep for the next)

n, w = [int(x) for x in sys.stdin.readline().split()]
widthpre = [0 for x in range(500001)]
cutepre = [0 for x in range(500001)]
dp = [0 for x in range(500001)]
curr = 1

for i in range(n):
    q = sys.stdin.readline().split()
    if q[0] == "A":
        p, c = [int(x) for x in q[1:]]
        widthpre[curr] = widthpre[curr-1] + p
        cutepre[curr] = cutepre[curr-1] + c

        upper = curr
        lower = 0
        while lower <= upper:
            index = lower+(upper-lower)//2
            temp = widthpre[curr]-widthpre[index]

            if temp <= w:
                upper = index - 1

            else:
                lower = index + 1

        temp = cutepre[curr]-cutepre[lower]
        dp[curr] = max(dp[curr-1], temp)
        print(dp[curr])

        curr += 1

    elif q[0] == "D":
        curr -= 1
        #decide state!
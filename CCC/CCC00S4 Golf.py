#import sys
#numberofquestions = int(sys.stdin.readline())

distancetoholes = int(input())
numberofclubs = int(input())
clubs = [int(input().strip()) for x in range(numberofclubs)]
dp = [10000 for o in range(distancetoholes + 1)]
dp[0] = 0


for i in range(distancetoholes):
    for clubindex in range(numberofclubs):
        if clubs[clubindex] + i <= distancetoholes:
            dp[i + clubs[clubindex]] = min(dp[i + clubs[clubindex]], dp[i] + 1)


if dp[-1] != 10000:
    print("Roberta wins in", dp[-1], "strokes.")
else:
    print("Roberta acknowledges defeat.")
import sys
numberofsawsandlogs = int(sys.stdin.readline())
saws = [int(x) for x in sys.stdin.readline().split()]
logs = [int(x) for x in sys.stdin.readline().split()]

saws.sort(reverse=True)
logs.sort()
finalcost = 0

for q in range(numberofsawsandlogs):
    finalcost += saws[q]*logs[q]

print(finalcost)
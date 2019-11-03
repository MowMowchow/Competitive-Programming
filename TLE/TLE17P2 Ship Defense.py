import sys
health, d, e = [int(x) for x in sys.stdin.readline().split()]
defensemodes = [[int(x) for x in sys.stdin.readline().split()] for x in range(d)]
time = [0 for x in range(10010)]
for i in range(e):
    t, l, x = [int(x) for x in sys.stdin.readline().split()]
    time[t] += x
    time[t+l] -= x

for i in range(1, 10010):  # doing difference array stuff
    time[i] += time[i-1]

total = 0
for second in range(10010):
    low = time[second]

    for mode in defensemodes:
        temp = max(0, time[second]-mode[1])
        temp *= (100-mode[0])/100
        low = min(low, temp)

    health -= low

if health > 0:
    temp = str(round(health, 2))
    if "." not in temp:
        print(temp+".00")
    else:
        if temp[-2] == ".":
            print(temp+"0")
        elif temp[-1] == ".":
            print(temp+"00")
        else:
            print(temp)
else:
    print("DO A BARREL ROLL!")
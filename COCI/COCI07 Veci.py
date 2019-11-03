import sys
uh = sys.stdin.readline().strip("\n")
ack = int(uh)
digitss = [int(x) for x in uh]
digitss.sort()
n = len(digitss)
lowest = float("inf")


def recurse(num, digits):
    global lowest
    if len(num) == n:
        ug = [str(x) for x in num]
        heh = int("".join(ug))
        if ack < heh < lowest:
            lowest = heh
    for thing in digits:
        tempppp = list(num+[thing])
        if tempppp.count(thing) <= digitss.count(thing):
            recurse(tempppp, digits)



for digit in digitss:
    if digit != 0:
        temp = list(digitss)
        if temp.count(digit) <= digitss.count(digit):
            recurse([digit], temp)

if lowest == float("inf"):
    print(0)
else:
    print(lowest)

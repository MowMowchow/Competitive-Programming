import sys, math

#move in a box based on radius and check if each point is in the circle or not
def calc(radius):
    amt = 0
    xcurr = 1
    for x in range(radius):
        amt += 4*int(math.sqrt((radius**2)-(xcurr**2)))

        xcurr +=1

    return amt+(radius*4)+1


while True:
    curr = int(sys.stdin.readline())
    if curr != 0:
        print(calc(curr))
    else:
        break
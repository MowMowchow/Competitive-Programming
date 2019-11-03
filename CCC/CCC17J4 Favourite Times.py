import sys
clock = [12, 0]  # h, m
total = 0
d = int(sys.stdin.readline())

for i in range(d % 720):
    clock[1] += 1
    if clock[1] == 60:
        clock[0] += 1
        clock[1] = 0

    if clock[0] == 13:
        clock[0] = 1

    if clock[1] > 9:
        temp = str(clock[0]) + str(clock[1])
    else:
        temp = str(clock[0]) + "0" + str(clock[1])

    if len(temp) == 4:
        if int(temp[0])-int(temp[1]) == int(temp[1])-int(temp[2]) == int(temp[2])-int(temp[3]):
            total += 1
    elif len(temp) == 3:
        if int(temp[0])-int(temp[1]) == int(temp[1])-int(temp[2]):
            total += 1

print(total + 31*(d//720))
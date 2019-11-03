import sys
parkingspots = int(sys.stdin.readline())
firstday = sys.stdin.readline()
secondday = sys.stdin.readline()
same = 0

first = []
second = []

for i in firstday:
    first.append(i)

for i in secondday:
    second.append(i)

for i in range(parkingspots):
    if first[i] == 'C':
        if second[i] == 'C':
            same += 1

print(same)
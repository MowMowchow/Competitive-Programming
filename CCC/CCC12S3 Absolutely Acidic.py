import sys
numberofsensors = int(sys.stdin.readline())
sensors = [0]*1001
sensors[0] = 0
#the nnumber is stored at it's equivalent index and the interger is its frequency
for i in range(numberofsensors):
    number = int(sys.stdin.readline())
    sensors[number] += 1

higherfrequncies = []
lowerfrequencies = [0]
highest = max(sensors)
if sensors.count(highest) > 1:
    for frequency in range(len(sensors)):
        if highest == sensors[frequency]:
            higherfrequncies.append(frequency)
    print(max(higherfrequncies) - min(higherfrequncies))


else:
    highestnumber = sensors.index(max(sensors))
    secondhighest = 0
    for i in range(len(sensors)):
        if (sensors[i] < highest) and (sensors[i] > secondhighest):
            secondhighest = sensors[i]
            lowerfrequencies = []
            lowerfrequencies.append(i)
        elif sensors[i] == secondhighest:
            lowerfrequencies.append(i)
    lowerfrequencies.sort()
    if abs(highestnumber-lowerfrequencies[0]) > abs(lowerfrequencies[-1]-highestnumber):
        print(abs(highestnumber-lowerfrequencies[0]))
    else:
        print(abs(highestnumber-lowerfrequencies[-1]))
import sys
gates = ["*"]+[0 for x in range(int(sys.stdin.readline()))]
planes = ["*"]
numberofplanes = int(sys.stdin.readline())
#for i in range(numberofplanes):
#    planes.append(int(sys.stdin.readline()))

total = 0
for i in range(numberofplanes):
    plane = int(sys.stdin.readline())
    docked = False

    #print("Plane:", plane)

    while not docked and plane > 0:
        if gates[plane] == 0:
            gates[plane] += 1
            docked = True
            total += 1
            break
            #print("Docked!")

        elif gates[plane] > 0:
            gates[plane] += 1
            plane -= gates[plane]-1
            #print("Moving plane to gate:", plane)

    if not docked:
        break
        #print("FULL!")

    #print("Gates:", gates)
    #print("Docks:", total)
    #print()

print(total)
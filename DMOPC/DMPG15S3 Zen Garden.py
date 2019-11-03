import sys

numberofflowers = int(sys.stdin.readline())
flowers = sys.stdin.readline().split()
flowers = [0]+[int(x) for x in flowers]
numberofbadpairs = int(sys.stdin.readline())
#bad pair processing is done in main loop
badsum = 0
for x in range(numberofbadpairs):
    badflower, disturbance = sys.stdin.readline().split()
    pair = [int(badflower), int(disturbance)]

    if pair[1] > flowers[pair[0]] or pair[1] > flowers[pair[0]+1]:
        if flowers[pair[0]] > flowers[pair[0]+1]:
            flowers[pair[0]+1] = 0

        elif flowers[pair[0]] < flowers[pair[0]+1]:
            flowers[pair[0]] = 0

        else:
            flowers[pair[0]] = 0

    else:
        badsum += pair[1]

print(sum(flowers)-badsum)
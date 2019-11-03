import sys
numoflines, people = [int(x) for x in sys.stdin.readline().split()]
lines = [int(x) for x in sys.stdin.readline().split()]

for person in range(people):
    curr= [0, float("inf")] #index, val
    for line in range(len(lines)):
        if lines[line] < curr[1]:
            curr[0] = line
            curr[1] = lines[line]

    print(curr[1])
    lines[curr[0]] += 1
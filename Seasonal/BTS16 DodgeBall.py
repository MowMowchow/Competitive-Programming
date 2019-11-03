import sys
numberofpeople = int(sys.stdin.readline())
people = [0]+[x[0] for x in sys.stdin.readline().split()]+[0]

sets = []
current = []
total = numberofpeople
#2^n - n+1
for i in range(1, numberofpeople+2):
    if not current:
        current.append(people[i])

    elif current and current[-1] == people[i]:
        current.append(people[i])

    else:
        if len(current) > 1:
            sets.append(current)
        current = []
        current.append(people[i])

for q in sets:
    #print("adding:", 2**len(q) - len(q) -1)
    total += 2**len(q) - 2*len(q) + 1

#print(sets)
print(total)
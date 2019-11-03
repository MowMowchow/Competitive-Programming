import sys
n, p = [int(x) for x in sys.stdin.readline().split()]
people = [[sys.stdin.readline().strip("\n"), 0] for x in range(n)]

for i in range(p):
    temp = [int(x) for x in sys.stdin.readline().split()]
    for i in range(n):
        people[i][1] += temp[i]


people.sort(key=lambda x: x[1])
counter = 3
for i in reversed(people):
    print(str(counter)+".", i[0])
    counter += 1
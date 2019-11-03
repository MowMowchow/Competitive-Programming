import sys
numberoffloors, numberofapartments = [int(x) for x in sys.stdin.readline().split()]
apartment = [[]] #extra list for indexing
for i in range(numberoffloors):
    floor = [0]+[int(x) for x in sys.stdin.readline().split()]
    #^adding 0 for sum and indexes purposes
    for i in range(1, numberofapartments+1):
        floor[i] = floor[i] + floor[i-1]
    apartment.append(floor)

numberofqueries = int(sys.stdin.readline())

for q in range(numberofqueries):
    a, b, floor = [int(x) for x in sys.stdin.readline().split()]

    print(apartment[floor][b]-apartment[floor][a-1])
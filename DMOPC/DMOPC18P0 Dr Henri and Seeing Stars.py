import sys
import math

telescope = [int(x) for x in sys.stdin.readline().split()]
#radius, x, y
stars = []
for i in range(3):
    #x, y, magnitude
    query = [int(x) for x in sys.stdin.readline().split()]
    stars.append(query)

stars.sort(key=lambda x: x[2])
bigstar = stars[0]

length = math.sqrt(((bigstar[0]-telescope[1])**2) + ((bigstar[1]-telescope[2])**2))

if int(length) < telescope[0]:
    print("What a beauty!")

else:
    print("Time to move my telescope!")
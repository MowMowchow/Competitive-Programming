import sys
import math
number = int(sys.stdin.readline().strip("\n"))
done = False
current = number

while not done:
    haha = True
    for i in range(2, int(math.sqrt(current))):
        if current%i == 0:
            haha = False
            break

    if haha:
        break

    current+=1

if number == 1:
    print(2)
else:
    print(current)
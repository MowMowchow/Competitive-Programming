import sys
numberofcards = int(sys.stdin.readline())
firsthand = []
secondhand = []
for i in range(numberofcards):
    firsthand.append(int(sys.stdin.readline()))
product = 1
negatives = []
zero = [0]

if firsthand.count(0) == len(firsthand):
    product = 0
elif firsthand.count(1) == len(firsthand):
    product = 1

elif len(firsthand) == 1:
    product = firsthand[0]

else:

    for i in range(len(firsthand)):
        if firsthand[i] not in zero:
            secondhand.append(firsthand[i])
            if firsthand[i] < 0:
                negatives.append(firsthand[i])

    if len(negatives) == 1 and firsthand[0] == 1:
        product = 1

    elif len(negatives) % 2 == 1:
        secondhand.remove(max(negatives))

    for i in secondhand:
        product *= i

    if len(secondhand) == 0:
        product = 0


print(product)
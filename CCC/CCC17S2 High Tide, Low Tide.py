import sys
n = int(sys.stdin.readline())
tides = [int(x) for x in sys.stdin.readline().split()]
tides.sort()

if len(tides) % 2 == 0:  # even number of items in list
    lowtides = tides[:(len(tides)//2)]
    hightides = tides[(len(tides)//2):]
elif len(tides) % 2 == 1:  # odd number of items in list
    lowtides = tides[:(len(tides)//2)+1]
    hightides = tides[(len(tides)//2)+1:]



final = ""
lowtideturn = True
while lowtides or hightides:
    if lowtideturn:
        final += str(lowtides.pop(-1))

    elif not lowtideturn:
        final += str(hightides.pop(0))

    lowtideturn = not lowtideturn
    final += " "

print(final)
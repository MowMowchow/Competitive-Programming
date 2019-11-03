import sys
n = int(sys.stdin.readline())
gifts = [[int(x) for x in sys.stdin.readline().split()] for x in range(n)]  # floor, weight
final = float("inf")


def recurse(time, stress, currgifts, curr):
    global final
    if currgifts:
        for gift in currgifts:
            new = list(currgifts)
            new.remove(gift)
            recurse(time, stress + (abs(curr-gift[0])+1)*(sum([x[1] for x in currgifts])), new, gift[0])

    else:
        final = min(final, stress)


recurse(0, 0, gifts, 101)
print(final)
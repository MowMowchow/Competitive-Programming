import sys


def aword(curr):
    if curr == "A":
        return True

    if len(curr) > 0 and curr[0] == "B" and curr[-1] == "S" and monkeyword(curr[1:-1]):
        return True

    return False


def monkeyword(curr):
    if aword(curr):
        return True

    for i in range(len(curr)):
        if curr[i] == "N" and aword(curr[:i]) and monkeyword(curr[i+1:]):
            return True

    return False


while True:
    temp = sys.stdin.readline().strip("\n")
    if temp == "X":
        break

    elif monkeyword(temp):
        print("YES")

    else:
        print("NO")
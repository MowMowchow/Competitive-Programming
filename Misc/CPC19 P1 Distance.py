import sys
n = int(sys.stdin.readline())
final = ""
if n%2 == 0:
    offset = 0
    one = False
    two = False
    for i in range(1, n+1):
        if i%2 == 1:
            final += str(n-offset)
            one = True
        elif i%2 == 0:
            final += str(1+offset)
            two = True

        if one and two:
            one, two = False, False
            offset +=1

        final += " "


elif n%2 == 1:
    offset = 0
    one = False
    two = False
    for i in range(1, n + 1):
        if i % 2 == 0:
            final += str(n - offset)
            one = True
        elif i % 2 == 1:
            final += str(1 + offset)
            two = True

        if one and two:
            one, two = False, False
            offset += 1

        final += " "


print(final)
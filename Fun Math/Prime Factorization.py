import sys, math

n = int(sys.stdin.readline())
for i in range(n):
    currrr = int(sys.stdin.readline())
    curr = int(currrr)
    string = ""
    for i in range(2, int(math.sqrt(curr))+2):
        while curr%i == 0:
            string += str(i) + " "
            curr //= i

    if curr != 1:
        string += str(curr)

    print(string)
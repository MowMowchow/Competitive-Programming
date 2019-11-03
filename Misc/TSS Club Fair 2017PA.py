import sys
n = int(sys.stdin.readline())
for i in range(n):
    done = False
    curr = sys.stdin.readline().split()
    for word in curr:
        if curr.count(word) >= 2:
            print(word)
            done = True
            break

    if not done:
        print("???")
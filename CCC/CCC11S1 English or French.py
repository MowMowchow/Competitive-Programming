import sys
n = int(sys.stdin.readline())
sentences = [sys.stdin.readline().split() for x in range(n)]
s = 0
t = 0

for q in sentences:
    for word in q:
        for letter in word:
            if letter.lower() == "s":
                s += 1
            elif letter.lower() == "t":
                t += 1

if t > s:
    print("English")
else:
    print("French")
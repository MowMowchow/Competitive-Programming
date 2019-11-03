import sys

c = int(input())
p = int(input())

done = False
for i in range(1, 15):
    if c == round((i / 15) * 100) or p == round((i / 15) * 100):
        done = True

if not done:
    if c < p:
        print("PHIL145")

    elif p > c:
        print("CS452")
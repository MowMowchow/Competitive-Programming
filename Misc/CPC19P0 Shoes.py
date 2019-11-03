import sys
shoes = sys.stdin.readline().split()
left = []
right = []
for i in range(1, len(shoes)+1):
    if shoes[i-1] == "L":
        left.append(i)
    elif shoes[i-1] == "R":
        right.append(i)

for i in range(2):
    print(left[i], right[i])
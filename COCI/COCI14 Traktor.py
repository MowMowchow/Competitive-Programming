import sys
n, k = [int(x) for x in sys.stdin.readline().split()]
shrooms = [[int(x) for x in sys.stdin.readline().split()] for y in range(n)]
# find min number of mushrooms on the same line
pointsup = [0 for x in range(200010)]
pointsdown = [0 for x in range(200010)]
x = [0 for x in range(100010)]
y = [0 for x in range(100010)]
done = False
final = 0
counter = 1
for a, b in shrooms:
    valup = (a-b)+100000
    pointsup[valup] += 1
    valdown = a+b
    pointsdown[valdown] += 1
    x[a] += 1
    y[b] += 1
    if pointsup[valup] >= k or x[a] >= k or y[b] >= k or pointsdown[valdown] >= k:
        done = True
        final = counter
        break
    counter += 1

if done:
    print(final)
else:
    print(-1)
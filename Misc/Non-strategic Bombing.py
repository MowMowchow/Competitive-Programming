import sys

numberofcities, numberofplans = [int(x) for x in sys.stdin.readline().split()]
cities = [[int(x) for x in sys.stdin.readline().split()] for x in range(numberofcities)]
plans = []
for q in range(numberofplans):
    query = [int(x) for x in sys.stdin.readline().split()]
    plans.append([[query[0], query[1]], [query[2], query[3]], [query[4], query[5]],])


def inside(x, y, points):

    n = len(points)
    inside = False
    p1x, p1y = points[0]
    for i in range(1, n + 1):
        p2x, p2y = points[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside


for plan in plans:
    counter = 0
    for city in cities:
        if inside(city[0], city[1], plan):
            counter += 1
    print(counter)
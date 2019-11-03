import sys

cities = []
while True:
    curr = sys.stdin.readline().split()
    cities.append(curr)
    if curr[0] == "Waterloo":
        break

cities.sort(key=lambda x: int(x[1]))

print(cities[0][0])
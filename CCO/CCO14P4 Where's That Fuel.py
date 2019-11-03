numberofandstartingplanet = input()
numberofplanets, startingplanet = numberofandstartingplanet.split()
numberofplanets = int(numberofplanets)
startingplanet = int(startingplanet)
planets = []
starfoxfuelcells = 0
planetsvisited = 1

#puts the planets and their data into a manageable format
for i in range(numberofplanets):
    fuelcells, fuelconsumed = map(int, input().split())
    if i != startingplanet-1:
        planets.append([fuelcells, fuelconsumed])

    else:
        starfoxfuelcells += fuelcells

#sorts the planest from lowest fuel consumption (to travel to) to highest
planets.sort()

#calculates the largest number of fuel cells the team can contain within the 'efficient' planets
for i in planets:
    if i[0] > i[1] and i[1] <= starfoxfuelcells:
        starfoxfuelcells += i[0]
        starfoxfuelcells -= i[1]
        planetsvisited += 1

    elif i[0] == i[1] and i[1] <= starfoxfuelcells:
        planetsvisited += 1

#just for testing
print(starfoxfuelcells)
print(planetsvisited)
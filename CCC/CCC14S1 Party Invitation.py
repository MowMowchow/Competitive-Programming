numberofpeople = int(input())
rounds = int(input())
spacing = []
people = []
counter = 1

#the rounds of removal
for i in range(rounds):
    spacing.append(int(input()))

#putting each 'person' into a list
for i in range(numberofpeople):
    i += 1
    people.append(i)

#removes the people
for i in spacing:
    for z in people:
        if counter == i:
            people.remove(z)
            counter = 1

        counter +=1

    counter = 1

#prints the guests
for i in people:
    print(i)
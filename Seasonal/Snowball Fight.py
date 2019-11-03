import sys
person1 = [int(x) for x in sys.stdin.readline().split()]
person2 = [int(x) for x in sys.stdin.readline().split()]

person1[0] -= 1
person2[0] -= 1


p1snowballtimer = 0
p2snowballtimer = 0
#p1turn = True
winner = None
while True:
    if person1[0] == 0 and person2[0] > 0:
        winner = 2
        break

    if person2[0] == 0 and person1[0] > 0:
        winner = 1
        break

    if person1[0] == 0 and person2[0] == 0:
        winner = -1
        break


    if p1snowballtimer == person1[1]:
        p1snowballtimer = 0
        #p1turn = not p1turn
        person2[0] -= 1


    if p2snowballtimer == person2[1]:
        p2snowballtimer = 0
        #p1turn = not p1turn
        person1[0] -= 1


    p1snowballtimer += 1
    p2snowballtimer += 1

print(winner)
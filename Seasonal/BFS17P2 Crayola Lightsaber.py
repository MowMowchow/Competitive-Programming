numberofcrayons = int(input())
crayons = input()
crayons = crayons.split(" ")

red = []
orange = []
yellow = []
green = []
blue = []
black = []

length = 0
sword = []
swordindex = 0
done = False

for crayon in crayons:
    if crayon == "red":
        red.append("red")
    elif crayon == "orange":
        orange.append("orange")
    elif crayon == "yellow":
        yellow.append("yellow")
    elif crayon == "green":
        green.append("green")
    elif crayon == "blue":
        blue.append("blue")
    elif crayon == "black":
        black.append("black")

unsortedcolours = sorted([red, orange, yellow, green, blue, black], key=len)
colours = unsortedcolours[::-1]


while not done:
    colours = [x for x in colours if x != []]
    #the begging of the sword
    if length == 0:
        length += 1
        sword.append(colours[0][0])
        del colours[0][0]
        colours[0] = [x for x in colours[0] if x != []]
        swordindex += 1

    #just incase there aren't enough colours to continue
    elif len(colours) == 0:
        done = True
    elif len(colours) == 1:
        if sword[swordindex-1] == colours[0][0]:
            done = True

        elif sword[swordindex - 1] != colours[0][0]:
            length += 1
            sword.append(colours[0][0])
            del colours[0][0]
            colours[0] = [x for x in colours[0] if x != []]
            swordindex += 1

    elif sword[swordindex-1] != colours[0][0]:
        length += 1
        sword.append(colours[0][0])
        del colours[0][0]
        colours[0] = [x for x in colours[0] if x != []]
        swordindex += 1

    elif sword[swordindex-1] != colours[1][0]:
        length += 1
        sword.append(colours[1][0])
        del colours[1][0]
        colours[1] = [x for x in colours[1] if x != []]
        swordindex += 1

print(length)
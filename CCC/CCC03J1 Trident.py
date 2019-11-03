# height = int(sys.stdin.readline())
# space = int(sys.stdin.readline())
# handle = int(sys.stdin.readline())

height = int(input())
space = int(input())
handle = int(input())

counter = 0
row = ""

# for the prongs of the trident
for i in range(height):

    for z in range(3):

        for x in range(space + 1):

            if counter == 0:
                row += "*"
            else:
                row += " "

            counter += 1

        counter = 0

    print(row)
    row = ""

# for the middle of the trident
for i in range(3 + (space * 2)):
    row += "*"
print(row)
row = ""

# for the handle of the trident
for i in range(handle):

    for z in range(space + 2):

        if counter == (space + 1):
            row += "*"
        else:
            row += " "

        counter += 1

    print(row)
    counter = 0
    row = ""
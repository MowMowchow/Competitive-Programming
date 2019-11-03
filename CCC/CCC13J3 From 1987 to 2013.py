#year = int(sys.stdin.readline())

year = int(input())
newyear = year
case = False
lengthofyear = len(str(year))
tally = 0


while not case:

    newyear += 1

    #checks to see if the year has distinct digits
    for i in str(newyear):
        if str(newyear).count(i) == 1:
            tally += 1

            if tally == lengthofyear:
                case = True
    tally = 0

print(newyear)
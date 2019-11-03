import sys
ages = []
for i in range(5):
    ages.append([int(x) for x in sys.stdin.readline().split()])

for i in ages:
    date, month, year = i
    done = False
    if ((2010-year >= 13) and (month < 10)) or ((month == 10) and (27 >= date)):
        print("old enough")

    else:
        print("too young")
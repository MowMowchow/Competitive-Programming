import sys
n = int(sys.stdin.readline())

def determine(x):
    if x < 1000:
        print("Newbie")

    elif 1000 <= x <= 1199:
        print("Amateur")

    elif 1200 <= x <= 1499:
        print("Expert")

    elif 1500 <= x <= 1799:
        print("Candidate Master")

    elif 1800 <= x <= 2199:
        print("Master")

    elif 2200 <= x <= 2999:
        print("Grandmaster")

    elif 3000 <= x <= 3999:
        print("Target")

    else:
        print("Rainbow Master")


for i in range(n):
    determine(int(sys.stdin.readline()))
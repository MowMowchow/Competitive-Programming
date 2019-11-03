import sys
numberofcases = int(sys.stdin.readline())

for i in range(numberofcases):
    numbers = sys.stdin.readline().split()
    numbers = [int(x) for x in numbers]
    if numbers[0]*numbers[1] == numbers[2]:
        print("POSSIBLE DOUBLE SIGMA")

    else:
        print("16 BIT S/W ONLY")
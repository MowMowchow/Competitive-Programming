import sys
numberofunlucky = int(sys.stdin.readline())
numbers = [int(x) for x in sys.stdin.readline().split()]
hmm = [0 for x in range(1000001)]
for i in numbers:
    hmm[i] += 1
unluckies = [0 for x in range(1000001)]
for i in range(len(unluckies)):
    unluckies[i] = hmm[i]+unluckies[i-1]

numberofapartments = int(sys.stdin.readline())
for q in range(numberofapartments):
    current = int(sys.stdin.readline())
    print(current-unluckies[current])
import sys
numberofstations = int(sys.stdin.readline())
minimumtroops = int(sys.stdin.readline())
numberofwaves = int(sys.stdin.readline())
arr = [0 for x in range(numberofstations+2)]
total = 0

for i in range(numberofwaves):
    a, b, amount = [int(x) for x in sys.stdin.readline().split()]
    arr[a] += amount
    arr[b+1] -= amount

for i in range(1, numberofstations+1):
    #print(arr)
    arr[i] += arr[i-1]
    if arr[i] < minimumtroops:
        total += 1

print(total)

import sys
from collections import deque
n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split()]
answers = [0 for x in range(n)]
answers[0] = 0
for i in range(1, n):
    for j in range(i-1, -1, -1):
        answers[i] += 1
        if arr[j] > arr[i]:
            break
        elif arr[j] == arr[i]:
            answers[i] += answers[j]
            break

print(" ".join([str(x) for x in answers]))
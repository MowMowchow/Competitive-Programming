import sys

n = int(input())
arr = [int(x) for x in sys.stdin.readline().strip("\n").split()]
arr.sort()
final = float('inf')
for i in range(n-1):
  final = min(final, abs(arr[i+1]-arr[i]))
print(final)
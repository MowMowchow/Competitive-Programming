import sys
n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split()]

if max(arr) <= sum(arr)//2:
	print(sum(arr))
else:
	print(2*max(arr))
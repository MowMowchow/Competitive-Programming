# problem 1
import sys
n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split()]
mid = n//2
q1, q2, q3 = float("inf"), float("inf"), float("inf")
arr.sort()
firstside = list(arr[:mid])
secondside = list(arr[-mid:])
# firstside.sort()
# secondside.sort()
minimum = min(arr)
maximum = max(arr)
# arr.sort()
if len(firstside) % 2 == 0:  # size of first half is even
    fmid = len(firstside)//2
    q1 = (firstside[fmid] + firstside[fmid-1])/2

elif len(firstside) % 2 == 1:  # size of first half is odd
    fmid = len(firstside)//2
    q1 = firstside[fmid]

if len(secondside) % 2 == 0:
    smid = len(secondside)//2
    q3 = (secondside[smid]+secondside[smid-1])/2

elif len(secondside) % 2 == 1:
    smid = len(secondside)//2
    q3 = secondside[smid]

if n % 2 == 0:
    q2 = (arr[mid]+arr[mid-1])/2

elif n % 2 == 1:
    q2 = arr[mid]

print(minimum, maximum, q1, q2, q3)
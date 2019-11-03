#diverse arrays
import sys
n, k = [int(x) for x in sys.stdin.readline().split()]
arr = [int(sys.stdin.readline()) for x in range(n)]
nums = [0 for x in range(n+1)]

right = 0
currk = 0
total = 0
for left in range(n):
    while right < n and currk < k:
        nums[arr[right]] += 1

        if nums[arr[right]] == 1:
            currk += 1
        right += 1

    if currk < k:
        break

    total += n-right+1
    nums[arr[left]] -= 1

    if nums[arr[left]] == 0:
        currk -= 1

print(total)
import sys  # p3
n, m = [int(x) for x in sys.stdin.readline().split()]
arr = [int(x) for x in sys.stdin.readline().split()]

currsum = [0, 0]  # value, length
maxsum = [0, 0]
start = 0
end = 0
while end < len(arr):
    if currsum[0] + arr[end] < m:
        currsum[0] += arr[end]
        end += 1

        if end-start > maxsum[1]:
            maxsum[1] = end-start

    else:
        currsum[0] -= arr[start]
        start += 1

print(maxsum[1])
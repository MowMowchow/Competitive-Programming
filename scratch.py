arr = [-5, -3, -1, 0, 1, 5, 7, 8]
n = len(arr)
low = 0
high = n-1

while low < high:
  mid = low + (high-low+1)//2

  if arr[mid] > -1:
    high = mid-1
  else:
    low = mid


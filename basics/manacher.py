import sys
s = sys.stdin.readline().strip("\n")


def manacher(s):
  n = len(s)
  d1 = [0 for x in range(n+1)]
  d2 = [0 for x in range(n+1)]
  l = 0
  r = -1
  for i in range(n):
    if i > r:
      k = 1
    else:
      k = min(d1[l+r-i], r-i+1)
    while 0 <= i-k and i+k < n and s[i-k] == s[i+k]:
      k += 1
    d1[i] = k
    k -= 1
    if i+k > r:
      l = i-k
      r = i+k

  l = 0
  r = -1
  for i in range(n):
    if i > r:
      k = 0
    else:
      k = min(d2[l+r-i+1], r-i+1)
    while 0 <= i-k-1 and i+k < n and s[i-k-1] == s[i+k]:
      k += 1
    d2[i] = k
    k -= 1
    if i+k > r:
      l = i-k-1
      r = i+k

  # longest palindrome centered at index i
  # for d2, the center is the right of the 2
  temp = [0 for x in range(n+1)]
  for i in range(0, n):
    temp[i] = max((d1[i]*2)-1, d2[i]*2)
  
  return temp


ans = manacher(s)
print(ans)
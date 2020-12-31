import sys


def kmp(s, n):
  pi = [0 for x in range(n+1)]
  for i in range(1, n):
    j = pi[i-1]
    while (j > 0 and s[i] != s[j]):
      j = pi[j-1]
    if s[j] == s[i]:
      j += 1
    pi[i] = j

  return pi


# looking for s in t
def kmp_search(s, n, t, m):  
  pi = kmp(s, n)
  s = "#"+s
  j = 0
  for i in range(m):
    if t[i] == s[j+1]:
      j += 1
      if j == n:
        return i-n+1
    else:
      j = pi[j]

  return -1


# occurences of each prefix 
def kmp_oop(s, n):
  pi = kmp(s, n)
  ans = [0 for x in range(n+1)]
  for i in range(n):
    ans[pi[i]] += 1
  for i in range(n-1, 0, -1):
    ans[pi[i-1]] += ans[i]
  for i in range(n):
    ans[i] += 1
  

print(kmp_search("ababd", 5, "ababcabcabababd", 15))
import sys
n = int(sys.stdin.readline())
ns = str(n)
temp = [int(x) for x in ns]
if '0' not in ns:
  print(-1)
else:
  if sum(temp)%3 == 0:
    temp.sort()
    out = reversed(temp)
    print("".join(str(x) for x in out))

  else:
    print(-1)
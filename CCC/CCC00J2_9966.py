import sys

n = int(input())
r = int(input())
rev = {
  '6': '9',
  '9': '6',
  '8': '8',
  '0': '0',
  '1': '1'
}

count = 0
for i in range(n, r+1):
  good = True
  curr = str(i)
  opposite = ""

  for j in range(len(curr)):
    if (curr[j] in rev):
      opposite  += rev[curr[j]]
    else:
      good = False
      opposite += str(curr)

  if good and curr == opposite[::-1]:
    count += 1

print(count)
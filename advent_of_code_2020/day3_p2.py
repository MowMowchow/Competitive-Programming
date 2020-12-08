mount = []

while True:
  q = input()
  if q == '-1':
    break
  mount.append(q)


wide = len(mount[0])  # 31
long = len(mount) # 323

# when i run out of horizontal space reset x index and increment y
def do(sx, sy):
  x = 0
  y = 0
  tree = 0
  while y < 323:
    
    if mount[y][x] == "#":
      tree += 1

    x += sx
    y += sy

    if (x >= 31):
      x %= 31
  return tree

total = 1
total *= do(1, 1)
total *= do(3, 1)
total *= do(5, 1)
total *= do(7, 1)
total *= do(1, 2)
print(total)

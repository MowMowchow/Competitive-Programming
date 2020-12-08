mount = []

while True:
  q = input()
  if q == '-1':
    break
  mount.append(q)


wide = len(mount[0])  # 31
long = len(mount) # 323

# when i run out of horizontal space reset x index and increment y
x = 0
y = 0
tree = 0
while y < 323:
  
  if mount[y][x] == "#":
    tree += 1

  x += 3
  y += 1

  if (x >= 31):
    x %= 31

print(tree)

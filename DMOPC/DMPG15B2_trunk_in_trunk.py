import sys
trunk = [int(x) for x in sys.stdin.readline().strip("\n").split()]
rect = [int(x) for x in sys.stdin.readline().strip("\n").split()]

trunk.sort()
rect.sort()
good = True
for i in range(3):
  for j in range(len(trunk)):
    if rect[i] >= trunk[j]:
      trunk.pop(j)
      break


if not trunk:
  print("Y")
else:
  print('N')
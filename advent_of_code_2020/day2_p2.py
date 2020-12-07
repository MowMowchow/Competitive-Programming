c = 0

while True:
  q = input()

  if q == '-1':
    break
  
  q = q.split(" ")
  q[0] = q[0].split("-")
  low = int(q[0][0])
  high = int(q[0][1])
  good = q[1][0]
  
  if (not (q[2][low-1] == good and q[2][high-1] == good) and (q[2][low-1] == good or q[2][high-1] == good)):
    c += 1

print(c)


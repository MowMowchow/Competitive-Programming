c = 0

while True:
  q = input()

  if q == '-1':
    break
  
  q = q.split(" ")
  q[0] = q[0].split("-")
  low = int(q[0][0])
  high = int(q[0][1])
  bad = q[1][0]
  temptotal = 0
  for let in q[2]:
    if let == bad:
      temptotal += 1

  if (low <= temptotal <= high):
    c += 1

print(c)


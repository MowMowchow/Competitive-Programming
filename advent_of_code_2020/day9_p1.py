
preamble = []
temp = []
k = 0
while True:
  q = input()
  if q == "-1":
    break
  temp.append(int(q))

r = 25

while r < len(temp):
  
  curr = temp[r]

  flag = False
  for i in range(25):
    for j in range(25):
      if i != j and temp[r-i-1] + temp[r-j-1] == curr:
        flag = True
        break
  if not flag:
    print(curr)
    break

  r+=1
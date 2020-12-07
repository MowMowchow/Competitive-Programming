temp = []
while True:
  a = int(input().strip("/n"))
  if a == -1:
    break
  temp.append(a)

n = len(temp)

for i in range(n):
  for j in range(n):
    for k in range(n):
      if i != j != k and temp[i]+temp[j]+temp[k] == 2020:
        print(temp[i]*temp[j]*temp[k])
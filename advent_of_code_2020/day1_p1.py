temp = []
while True:
  a = int(input().strip("/n"))
  if a == -1:
    break
  temp.append(a)
  


print("hi")
for i in temp:
  for j in temp:
    if (i + j == 2020):
      print (i*j)


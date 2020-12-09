
preamble = []
temp = []
k = 0
while True:
  q = input()
  if q == "-1":
    break
  temp.append(int(q))

r = 25
goal = 0
while r < len(temp):
  
  curr = temp[r]

  flag = False
  for i in range(25):
    for j in range(25):
      if i != j and temp[r-i-1] + temp[r-j-1] == curr:
        flag = True
        break
  if not flag:
    goal = curr
    break

  r+=1


l = 0
r = 0
currsum = temp[r]
while l <= r:
  
  if currsum+temp[r+1] == goal:
    print('found goal:', currsum)
    break

  elif currsum + temp[r+1] > goal:
    currsum -= temp[l]
    l += 1
  
  elif currsum + temp[r+1] < goal:
    currsum += temp[r+1]
    r += 1

  
  if r == len(temp)-1:
    break

print('goal:', goal)
print(l, r)
print(min(temp[l:r+1])+max(temp[l:r+1]))
    

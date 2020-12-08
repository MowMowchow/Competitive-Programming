prev = " "
temp = []
total = 0
while True:
  q = input()
  if q == "-1":
    break
  elif q == "":
    flag = True
    prev = " "

    temp2 = [x.split(":")[0] for x in temp]
    print(temp2)

    temp3 = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    for i in temp3:
      if i not in temp2:
        flag = False
    
    if flag:
      total += 1

    temp = []

  else: 
    prev = q
    temp.extend(q.split())


print(total)
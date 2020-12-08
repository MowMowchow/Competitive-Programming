prev = " "
temp = []
total = 0
inputs = 1
while True:
  q = input()
  if q == "-1":
    break
  elif q == "":
    flag = True
    prev = " "

    temp2 = [x.split(":") for x in temp]

    temp3 = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    for i in temp3:
      if i not in [x[0] for x in temp2]:
        flag = False
    

    for i in temp2:
      if i[0] == 'byr':
        if int(i[1]) < 1920 or int(i[1]) > 2002 and len(i[1]) == 4:
          flag = False

      elif i[0] == 'iyr':
        if int(i[1]) < 2010 or int(i[1]) > 2020 and len(i[1]) == 4:
          flag = False

      elif i[0] == 'eyr':
        if int(i[1]) < 2020 or int(i[1]) > 2030 and len(i[1]) == 4:
          flag = False

      elif i[0] == 'hgt':
        if "cm" in i[1] or "in" in i[1]:
          if "cm" in i[1]:
            if int(i[1].strip("cm"))<150 or int(i[1].strip("cm")) > 193:
              flag = False

          elif "in" in i[1]:
            if int(i[1].strip("in"))<59 or int(i[1].strip("in")) > 76:
              flag = False
        else:
          flag = False

      elif i[0] == 'hcl':
        if len(i[1]) != 7 or i[1][0] != "#":
          flag = False
        else:
          for j in i[1][1:]:
            if j not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] and j not in ['a', 'b', 'c', 'd', 'e', 'f']:
              flag = False

      elif i[0] == 'ecl':
        if i[1] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] or len(i[1])>3:
          flag = False

      elif i[0] == 'pid':
        if len(i[1]) != 9:
         flag = False
        else:
          for j in i[1]:
            if j not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
              flag = False

    if flag:
      total += 1

    temp = []
    inputs += 1
  else: 
    prev = q
    temp.extend(q.split())


print(total)
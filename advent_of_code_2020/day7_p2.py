instruc = []
mapp = {}
allcolours = []
visited = {}


while True:  # processing input
  q = input()
  if q == "-1":
    break
  if 'contain no other bags' not in q:
    q = q.replace(' bags contain ', ',')
    q = q.split(',')
    for colour in range(len(q)):
      for i in ["bag", "bag.", "bags", "bags."]:
        if i in q[colour]:
          q[colour] = q[colour].strip(i)
      
      if colour == 1:
        q[colour] = q[colour].split(" ",1)
        q[colour][1] = q[colour][1].strip(" ")
        q[colour][0] = int(q[colour][0])
      elif colour > 1:
        q[colour] = q[colour].split(" ")
        q[colour][2] += " " + q[colour][3]
        q[colour] = list([int(q[colour][1]), q[colour][2]])

    instruc.append(q)


for rule in instruc:
  if rule[0] not in mapp:
    mapp[rule[0]] = []
    allcolours.append(rule[0])

  for colour in rule[1:]:
    mapp[rule[0]].append(colour)
    if colour[1] not in mapp:
      mapp[colour[1]] = []
      allcolours.append(colour[1])


def do(curr):
  result = 0
  for colouramt, colour in mapp[curr]:
    result += colouramt
    result += colouramt*do(colour)

  return result

print(do('shiny gold'))
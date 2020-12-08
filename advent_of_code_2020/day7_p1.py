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
      for charr in q[colour]:
        if charr in [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
          q[colour] = q[colour].strip(charr)

    instruc.append(q)

for rule in instruc:
  for colour in rule[1:]:
    if rule[0] not in mapp:
      mapp[rule[0]] = []
    if colour not in mapp:
      mapp[colour] = [rule[0]]
      allcolours.append(colour)
    else:
      mapp[colour].append(rule[0])


# for i in allcolours:
#   print(i, ":", mapp[i])

def do(curr):
  if curr not in visited:
    visited[curr] = True
    for colour in mapp[curr]:
      do(colour)

do('shiny gold')

print(len(visited)-1)
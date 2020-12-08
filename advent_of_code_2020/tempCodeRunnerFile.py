if rule[0] not in mapp:
    mapp[rule[0]] = []
    allcolours.append(rule[0])

  for colour in rule[1:]:
    mapp[rule[0]].append(colour)
    if colour[1] not in mapp:
      mapp[colour[1]] = []
      allcolours.append(colour[1])

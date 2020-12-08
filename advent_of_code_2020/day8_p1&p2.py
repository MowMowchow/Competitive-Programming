n = 0
instrucs = []
while True:
  q = input()
  if q == "-1":
    break
  instrucs.append(q)

n = len(instrucs)


def do(arr):
  visited = [0 for x in range(n+1)]
  acccumulator = 0
  i = 0
  while True:
    curr, arg = arr[i].split()
    if "+" in arg:
      arg.strip("+")
    arg = int(arg)
    
    if curr == "nop":
      i += 1
    elif curr == "acc":
      acccumulator += arg
      i+=1
    elif curr == "jmp":
      if (i+arg < 0):
        i = (n-1)-(i+arg)
      else:
        i += arg 

    visited[i] += 1
    if visited[i] == 2:
      return 'bad'
    if i == n-1:
      if arr[i].split()[0] == "acc":
        acccumulator += int(arr[i].split()[1])
      return acccumulator

for k in range(len(instrucs)):
  result = 'bad'
  if instrucs[k].split()[0] == "jmp":
    temp = instrucs[:k]
    temp.extend(["nop " +str(instrucs[k].split()[1])])
    temp.extend(instrucs[k+1:])
    result = do(temp)

  elif instrucs[k].split()[0] == "nop":
    temp = instrucs[:k]
    temp.extend(["jmp " + str(instrucs[k].split()[1])])
    temp.extend(instrucs[k+1:])
    result = do(temp)

  if result != 'bad':
    print(result)
    break


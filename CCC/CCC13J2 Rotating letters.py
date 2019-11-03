phrase = input()
new = []
for i in range(len(phrase)):
    new.append(phrase[i])
validletters = ["I", "O", "S", "H", "Z", "X", "N"]
possible = True

for i in new:
    if i not in validletters:
        possible = False

if possible:
    print("YES")

elif not possible:
    print("NO")
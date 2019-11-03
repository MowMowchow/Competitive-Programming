s = input()
p = "pusheen"

counter = 0
for i in range(7):
    if s[i] != p[i]:
        counter += 1

print(counter)
n = int(input())
dbsr = [[0, "Deluxe Tuna Bitz"], [0, "Bonito Bitz"], [0, "Sashimi"], [0, "Ritzy Bitz"]]
for i in range(n):
    q = input()
    if q == "Deluxe Tuna Bitz":
        dbsr[0][0] +=1

    if q == "Bonito Bitz":
        dbsr[1][0] += 1

    if q == "Sashimi":
        dbsr[2][0] += 1

    if q == "Ritzy Bitz":
        dbsr[3][0] += 1

dbsr.sort(key=lambda x: x[0])
order = ["Deluxe Tuna Bitz", "Bonito Bitz", "Sashimi", "Ritzy Bitz"]
final = []

while len(dbsr) > 0:
    if dbsr[-1][0] == 0:
        dbsr.pop(-1)

    else:
        curr = list(dbsr[-1])
        ind = len(dbsr)-1
        for i in range(len(dbsr)-1, -1, -1):
            if curr[0] == dbsr[i][0] and order.index(curr[1]) > order.index(dbsr[i][1]):
                curr = list(dbsr[i])
                ind = i

        final.append(dbsr.pop(ind))

for i in final:
    print(i[1], i[0])
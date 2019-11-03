import sys
n, l = [int(x) for x in sys.stdin.readline().split()]
sets = [[] for x in range(n)]
for i in range(n):
    temp = sys.stdin.readline().split()
    temp[0] = int(temp[0])
    sets[i].extend(temp[1:])

total = []


def recurse(curr, word, prev):

    if len(word) <= l and word != prev:
        total.append(word)
        if len(word) == l:
            return

    if curr == n:
        return

    for letter in sets[curr]:
        recurse(curr+1, word+letter, word)

    recurse(curr+1, word, word)


for uh in sets[0]:
    recurse(1, uh, "0")
total.sort()

for i in total:
    print(i)
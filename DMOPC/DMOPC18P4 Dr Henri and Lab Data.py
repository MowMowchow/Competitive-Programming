n, q = [int(x) for x in sys.stdin.readline().split()]
data = [[int(x)] for x in sys.stdin.readline().split()]  # items, index
queries = [[int(x) for x in sys.stdin.readline().split()]+[y] for y in range(q)]
predata = [0 for x in range(n+1)]
answers = [0 for x in range(q)]
kindarage = [0 for x in range(n+1)]
for i in range(1, n+1):
    predata[i] = predata[i-1] + data[i-1][0]
    data[i-1] += [i-1]

data.sort(key=lambda x: x[0])
queries.sort(key=lambda x: x[2])


def sumBIT(tree, k):
    total = 0
    while k >= 1:
        total += tree[k]
        k -= k & -k

    return total


def updateBIT(tree, x, k):
    nn = len(tree)
    while k < nn:
        tree[k] += x
        k += k & -k

    return tree


prevind = 1
for query in queries:
    if prevind <= n:
        while data[prevind-1][0] < query[2]:
            kindarage = updateBIT(kindarage, data[prevind-1][0], data[prevind-1][1]+1)
            prevind += 1
            if prevind > n:
                break

    currsum = sumBIT(kindarage, query[1])-sumBIT(kindarage, query[0]-1)
    othersum = predata[query[1]]-predata[query[0]-1]
    answers[query[3]] = othersum-(2*currsum)

for i in answers:
    print(i)

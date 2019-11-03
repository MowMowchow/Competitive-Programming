import sys
n = int(sys.stdin.readline())
temp = [int(x) for x in sys.stdin.readline().split()]
arr = [[x, temp[x]] for x in range(n)]  # index, value
arr.sort(key=lambda x: x[1])
q = int(sys.stdin.readline())
queries = [[int(x) for x in sys.stdin.readline().split()]+[x] for x in range(q)]
queries.sort(key=lambda x: x[2])


def sumBIT(tree, k):
    total = 0
    while k >= 1:
        total += tree[k]
        k -= k & -k

    return total


def updateBIT(tree, k, x):  # Adds x to a pre-existing values at index k
    nn = len(tree)
    while k < nn:
        tree[k] += x
        k += k & -k

    return tree


bittree = [0 for x in range(n+1)]
answers = [0 for x in range(q)]
last = 1
for query in reversed(queries):
    if last <= n:
        while arr[-last][1] >= query[2]:  # updating BIT for current query
            bittree = updateBIT(bittree, arr[-last][0]+1, arr[-last][1])
            last += 1
            if last > n:
                break

    answers[query[3]] = sumBIT(bittree, query[1]+1)-sumBIT(bittree, query[0])

for a in answers:
    print(a)
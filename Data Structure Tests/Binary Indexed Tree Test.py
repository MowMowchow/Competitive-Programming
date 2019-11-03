n, m = [int(x) for x in sys.stdin.readline().split()]
array = [int(x) for x in sys.stdin.readline().split()]


def getsum(tree, k):
    total = 0
    while k >= 1:
        total += tree[k]
        k -= k&-k

    return total


def updateBIT(tree, k, x):
    n = len(tree)

    while k <= n:
        tree[k] += x
        k += k&-k

    return tree


def constructBIT(arr, freq):
    n = len(arr)

    if not freq:
        curr = [0 for x in range(n + 1)]
        for i in range(n):
            updateBIT(curr, i+1, arr[i])

    elif freq:
        curr = [0 for x in range(100001)]
        for i in range(n):
            updateBIT(curr, arr[i], 1)

    return curr


bintree = constructBIT(array, False)
freqtree = constructBIT(array, True)

for i in range(m):
    q = sys.stdin.readline().split()

    if q[0] == "C":
        x, v = [int(x) for x in q[1:]]
        new = v - array[x-1]
        freqtree = updateBIT(freqtree, array[x-1], -1)  # getting rid of old
        array[x-1] = v
        bintree = updateBIT(bintree, x, new)  # regular BIT
        freqtree = updateBIT(freqtree, array[x-1], 1)  # adding to freq

    elif q[0] == "S":  # something wrong with this
        l, r = [int(x) for x in q[1:]]
        print(getsum(bintree, r)-getsum(bintree, l-1))

    elif q[0] == "Q":
        v = int(q[1])
        print(getsum(freqtree, v))
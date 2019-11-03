n, q = [int(x) for x in sys.stdin.readline().split()]
arr = [int(x) for x in sys.stdin.readline().split()]
premax = [0 for x in range(n+1)]
sufmax = [0 for x in range(n+1)]
prefreq = [0 for x in range(n+1)]
suffreq = [0 for x in range(n+1)]

for i in range(1, n+1):
    # prefix stuff
    premax[i] = max(premax[i-1], arr[i-1])
    if premax[i-1] == arr[i-1]:  # previous max == curr episode
        prefreq[i] = prefreq[i-1] + 1
    elif arr[i-1] > premax[i-1]:
        prefreq[i] = 1
    elif arr[i-1] < premax[i-1]:
        prefreq[i] = prefreq[i-1]


    # suffix stuff
    sufmax[-i-1] = max(sufmax[-i], arr[-i])
    if sufmax[-i] == arr[-i]:
        suffreq[-i-1] += suffreq[-i] + 1
    elif arr[-i] > sufmax[-i]:
        suffreq[-i-1] = 1
    elif arr[-i] < sufmax[-i]:
        suffreq[-i-1] = suffreq[-i]


for i in range(q):
    a, b = [int(x) for x in sys.stdin.readline().split()]
    rangemax = max(premax[a-1], sufmax[b])

    if premax[a-1] > sufmax[b]:
        freqmax = prefreq[a-1]
    elif premax[a-1] < sufmax[b]:
        freqmax = suffreq[b]
    else:
        freqmax = prefreq[a-1] + suffreq[b]

    print(rangemax, freqmax)
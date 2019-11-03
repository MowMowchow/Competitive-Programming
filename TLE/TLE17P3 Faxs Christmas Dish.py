import sys
n, m, d = [int(x) for x in sys.stdin.readline().split()]
leftover = [1 for x in range(n+1)]  # target at i has x items in its recipe
product = [0 for x in range(n+1)]  # item at i produces t
for q in range(m):
    qq = [int(x) for x in sys.stdin.readline().split()]
    t, r, temp = qq[0], qq[1], qq[2:]
    leftover[t] = r
    for i in range(r):
        product[temp[i]] = t
items = [int(x) for x in sys.stdin.readline().split()]


final = float("inf")
counter = 1
for itemx in items:
    item = int(itemx)
    if final == float("inf") and leftover[item] > 0:
        leftover[item] = 0
        while leftover[item] <= 0:
            if item == 1:
                final = min(counter, final)
                break

            if leftover[product[item]] <= 0:
                break

            leftover[product[item]] -= 1
            item = product[item]

    counter += 1

if final != float("inf"):
    print(final)
else:
    print(-1)
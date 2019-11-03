import sys
n = int(sys.stdin.readline())
ingredients = [[int(x) for x in sys.stdin.readline().split()] for x in range(n)]
final = float("inf")


def choose(curr, sourprod, bittersum, taken):
    result = abs(sourprod-bittersum)

    if curr == -1:
        return choose(curr+1, 1, 0, taken)

    elif curr < n:
        use = choose(curr+1, sourprod*ingredients[curr][0], bittersum+ingredients[curr][1], True)
        skip = choose(curr+1, sourprod, bittersum, taken)

        return min(use, skip)

    elif curr == n and not taken:
        return float("inf")

    return result


# for i in range(n):
    # final = min(final, choose(i, ingredients[i][0], ingredients[i][1], abs(ingredients[i][0]-ingredients[i][1])))

final = choose(-1, 1, 0, False)

print(final)